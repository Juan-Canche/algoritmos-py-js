Algoritmo PromedioExamenes
	//Definir las varibles
	Definir nota_examen_uno Como Real
	Definir nota_examen_dos Como Real
	Definir nota_examen_tres Como Real
	Definir promedio_examenes Como Real
	//Datos de entrada las tres notas
	Escribir 'Ingrese la nota del primer examen:'
	Leer nota_examen_uno
	Escribir 'Ingrese ña nota del segundo examen:'
	Leer nota_examen_dos
	Escribir 'Ingrese la nota del tercer examen:'
	Leer nota_examen_tres
	//Calcular el promedion de las notas teniendo en cuenta que los dos primeros valen 25% cada uno y el tercero 50%
	promedio_examenes = (nota_examen_uno*.25) + (nota_examen_dos*.25) + (nota_examen_tres*.50)
	//Mostrar el promedio en pantalla
	Escribir 'El promedio de los examenes es: ', promedio_examenes
FinAlgoritmo
