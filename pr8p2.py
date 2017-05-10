#!/usr/bin/python

nume=input ("ingrese dia de la semana: ")
dias = {1: "Domingo", 2: "Lunes", 3: "Martes", 4: "Miercoles", 5: "Jueves", 6: "Viernes", 7:"Sabado"}
if (nume) <= 7:
	dia= dias [nume]
	print "El dia es: %s" % (dia)
else:
	print "El numero %s no es valido" % (nume)


