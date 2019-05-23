import numpy as np



tiempo =[73,28,59,52,39,137] ##segundos despues de la hora
x = [4,10,12,80,50,40]
y = [100, 5 ,80, 50, 50, 200]



probX = [np.random.random()]
probY = [np.random.random()]
probT = [np.random.random()]

sigma = 0.1 



for i in range(1,10000):

	px = np.random.normal()
	py = np.random.normal()
	pt = np.random.normal()

'''
	a1 = px/x[]
	if(a1>=1):

		probX.append(px)
	else:

		b = np.random.random()
		if(b<= a1):
			probX.append(px)
		else:
			probX.append()

	a2 = py/x[]
	if(a2>=1):

		probY.append(py)
	else:

		b = np.random.random()
		if(b<= a1):
			probY.append(py)
		else:
			probY.append()  

'''










print("coordenada x:" , np.mean(probX) , "+/-")
print("coordenada y:" , np.mean(probY) , "+/-")
print("tiempo de lanzamiento:" , np.mean(probT) , "+/-")
print("velocidad del sonido:" , np.mean(probX) , "+/-")