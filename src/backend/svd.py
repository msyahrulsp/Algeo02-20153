from PIL import Image
from numpy import asarray

image = Image.open('src/backend/lena_image.jpg')

array_image = asarray(image)
array_image_transpose = array_image.transpose()

#mencari nilai eigen dari singular kiri
aaT = array_image * array_image_transpose


#print(arr)
#print("transpose")
#print(arrT)