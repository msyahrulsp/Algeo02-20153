from PIL import Image
import numpy as np
from numpy.lib.function_base import append
from numpy.linalg import qr


image = Image.open('src/backend/lena_image.jpg')

array_image = np.asarray(image)
array_image_transpose = array_image.transpose()

def zeros_matrix(rows, cols):
    #fungsi buat bikin matriks yang isi nya nol
    #berfungsi buat nyari nilai eigen nantinya
    M = []
    while len(M) < rows:
        M.append([])
        while len(M[-1]) < cols:
            M[-1].append(0)
    return M

def identity_matrix(n):
    #fungsi buat bikin matriks identitas
    #kepake nanti buat nyari nilai eigen value
    IdM = zeros_matrix(n,n)
    for i in range(n):
        IdM[i][i] = 1
    return IdM



#mencari nilai eigen dari singular kiri
aaT = np.matmul(array_image,array_image_transpose)


#mencari nilai eigen dari singular kanan
aTa = np.matmul(array_image_transpose,array_image)



#print(arr)
#print("transpose")
#print(arrT)