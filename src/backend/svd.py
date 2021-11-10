from PIL import Image
import numpy as np
from numpy.lib.function_base import append
from numpy.linalg import qr


image = Image.open('src/backend/lena_image.jpg')

array_image = np.asarray(image)
array_image_transpose = array_image.transpose()


def simultaneous_power_iteration(A: np.ndarray, k: int):
    n, m = A.shape
    Q = np.random.rand(n, k)
    Q, _ = np.linalg.qr(Q)
    Q_prev = Q
 
    for i in range(1000):
        Z = A.dot(Q)
        Q, R = np.linalg.qr(Z)

        # can use other stopping criteria as well 
        err = ((Q - Q_prev) ** 2).sum()
        if i % 100 == 0:
            print(i, err) # untuk debug, bisa dihapus

        Q_prev = Q
        if err < 1e-3:
            break

    return np.diag(R), Q
