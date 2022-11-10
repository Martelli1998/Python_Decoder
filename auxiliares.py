# -*- coding: utf-8 -*-
import re

def se_cifra(caracter):
	""" Función que toma un único caracter y devuelve True
	si es lo que en el TP se considera cifrable y false en caso
	contrario, por ejemplo "se_cifra("(")" devuelve False y
	"se_cifra("z")" devuelve True. Debe usarse para identificar qué fue
	cifrado y qué no """
	return bool(re.compile("[a-z]").match(caracter))
