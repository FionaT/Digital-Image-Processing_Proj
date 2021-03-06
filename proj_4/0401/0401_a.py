#the simple 2DFT is for the 2*2 image
#with 4 fourier bases
#and 4 fourier coefficients
from PIL import Image, ImageDraw
import numpy as np 

def f(u, v):
	result = data[u, v]

	result = (-1)**(u + v) * result

	return result
	
image_name = 'sample1'
image_type = '.bmp'
im = Image.open(image_name + image_type)
data = im.load()
M, N = im.size
float_M = round(M, 4)
float_N = round(N, 4)

ans = [[0.0 for i in range(N)] for j in range(M)]

for u in range(M):
	for v in range(N):
		ans[u][v] = f(u, v)
		#print ans[u][v]

resultImage = Image.new('L',(M, N), 'white')
draw = ImageDraw.Draw(resultImage)

for i in range(M):
	for j in range(N):
			draw.point((i, j), ans[i][j])

#save the output files
resultImage.save(image_name+'_result_a.bmp', format='BMP')
