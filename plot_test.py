import matplotlib.pyplot as plt



def calificaciones():
	""" una funcion para mostrar en graficamente las calificanciones en un grupo de 5 personas. """
	# Info to show
	x = ["Juan", "Camila", "Mama"]
	calificaciones = [5, 7, 9]

	# Estilo de la grafica
	plt.style.use("classic")

	# Creando la fig
	fig, ax = plt.subplots()

	# Agregando los datos, y ajustando el tamano de la linea
	ax.plot(x, calificaciones, linestyle="None")

	# Coloreando los puntos
	ax.scatter(x, calificaciones, c=calificaciones, cmap=plt.cm.Blues, s=10)

	# Agredando etiquetas a cada eje 
	ax.set_title("Calificaciones")
	ax.set_xlabel("Nombres")
	ax.set_ylabel("Calificacion Final")

	# Desplegando
	plt.show()


calificaciones()


""" Plot grafica de una manera inteligente
	En una grafica hay un eje x y un eje y donde se desarrolla la informacion de la grafica

	Matplotlib despliega un resultado sobre una linea x, por lo tanto no te tienen que preocupar por el eje y
	Ya que el mismo Matplot se encarga de desarrollarlo, por lo mismo 

	Para que Matplot funcione necesita que el tu eje x y el resultado a graficar tengan la misma dimension de tamano

	Es decir tu entregas

	--------------
	- x - names  -
	--------------
	- 5 - Juan   -
	--------------
	- 9 - Camila -
	--------------
	- 10 - Mama   -

	A partir de esta informacion automaticamente plot va a desarrollar la informacion en el eje y
	En este caso en particular, la grafica se desarrolla en un rango de 3 datos(names) que seran el eje x
	Y estos van en un rango que va desde 5 hasta 10 (eje y), este dato Matplot lo desarrollara por automaticamente
"""





