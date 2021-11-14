from PIL import Image
import numpy as np
from numpy.core.fromnumeric import shape

def simultaneous_iteration(A, k=None, max_iter=1000, epsilon=1e-2):
    """Simultaneous power iteration to calculate the eigenvalues and eigenvectors of A

    Parameters:
        A: Matrix A
        k: Number of eigenvalues to calculate
        max_iter: Maximum number of iterations
        epsilon: Tolerance for convergence
    Returns:
        tuple: (eigenvalues, eigenvectors)
    """

    if k is None:
        k = A.shape[0]

    n, m = A.shape
    Q = np.random.rand(n, k)
    Q, _ = np.linalg.qr(Q)
    Q_prev = Q
 
    for i in range(max_iter):
        Z = A.dot(Q)
        Q, R = np.linalg.qr(Z)

        # Error
        err = ((Q - Q_prev) ** 2).sum()
        if i % 100 == 0:
            # for progress
            print(i, err)
        Q_prev = Q
        if err < epsilon:
            break

    return np.diag(R), Q


def qr_method(A, k=None, max_iter=100, epsilon=1e-2):
    """QR decomposition to calculate the eigenvalues and eigenvectors of A

    Parameters:
        A: Matrix A
        k: Number of eigenvalues to calculate
        max_iter: Maximum number of iterations
        epsilon: Tolerance for convergence
    Returns:
        tuple: (eigenvalues, eigenvectors)
    """

    if k is None:
        k = A.shape[0]

    n = A.shape[0]
    pQ = np.eye(n)
    X = A.copy()
    Q_prev = pQ
    for i in range(1, max_iter+1):
        Q,R = np.linalg.qr(X)
        pQ = pQ @ Q
        X = (R @ Q)
        err = ((Q - Q_prev) ** 2).sum()
        if (i) % 10 == 0:
            # print(i, err)
            pass
        if err < epsilon:
            break
        Q_prev = Q

    return np.diag(X), pQ


def singular_value_decomposition(I: Image, p=None, max_iter=200, epsilon=1e-2):
    """Compression of image I, which reduces the quality of the image by using SVD 

    Parameters:
        I: image object
        p: fraction of eigenvalues to calculate (0 <= p <= 1), default is 1.0
        max_iter: Maximum number of iterations
        epsilon: Tolerance for convergence
    Returns:
        rgb: Image object, reduced result of I
    """
    if p is None:
        p = 100.0
    else:
        p = 100.0 - p

    # If the image is not RGB, use a slightly different approach
    if I.mode == 'P' or I.mode == 'L':
        # The image is using palette mode
        I = I.convert('RGBA')
        num_channel = 4
    elif I.mode == 'RGBA': 
        # For transparent image e.g. PNG
        num_channel = 4
    elif I.mode == 'RGB':
        # Regular image e.g. JPG or JPEG
        num_channel = 3
    else:
        num_channel = 0
        raise ValueError('Unsupported image mode')

    mode = I.mode
    print("MODE:", mode)
    A = np.asarray(I, dtype=np.float64)

    # Convert p to matrix rank used
    # The fomula is: p = (mk + k + kn) / (mn) * 100%
    # Then we solve for k: k = mn / (m + 1 + k) * p/100%
    m = A.shape[0]
    n = A.shape[1]
    k = (m * n) / (m + 1 + n) * (p) / 100.0
    k = int(k)
    
    result = [] 
    for i in range(num_channel):
        if i == 3:
            # channel alpha
            result.append(A[:,:,3])
            break

        if num_channel == 1:
            sub_array = A
        else:
            sub_array = A[:, :, i]
        U_eigval, U_eigvector = simultaneous_iteration(sub_array@sub_array.T, k, max_iter, epsilon)

        # calculate S from the corresponding eigenvalues in U_eigval
        S = U_eigval
        S = np.sqrt(np.abs(S))
        diff = len(U_eigval)-len(S)
        S = np.pad(np.diag(S), pad_width=[(0, diff), (0, diff)])

        # calculate VT from the inverse of U_eigvector and S
        VT = np.linalg.inv(S) @ U_eigvector.T @ sub_array

        # calculate the result
        res = U_eigvector[:,:k] @ S[:k,:k] @ VT[:k,:]
        res = np.clip(res, 0, 255).astype(np.uint8)
        result.append(res)

    if num_channel != 1:
        image = np.dstack(result).astype(np.uint8)
    else:
        image = result[0]

    result = Image.fromarray(image).convert(mode)
    return result