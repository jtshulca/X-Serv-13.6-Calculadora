#!/usr/bin/python3

import sys 
if len(sys.argv) != 4:
	sys.exit("error,no hay 4 elementos")
	
_,operacion, operacion1, operacion2 = sys.argv #si pongo barra baja es que no quiero tenrlo en cuenta

operacion1 = float(operacion1)
operacion2 = float(operacion2)

 
if operacion == "suma":
	print(operacion1 + operacion2)
	
elif operacion == "resta":
	print(operacion1 - operacion2)

elif operacion == "multi":
	print(operacion1 * operacion2)
		
elif operacion == "diviendo":
	
	try:
		print(operacion1/operacion2)
		
	except ZeroDivisionError:
		print("no me dividas entre cero")
