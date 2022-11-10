from auxiliares import *
import sys
import pandas as pd

# def leer_mails(filename):
#     df = pd.read_csv(filename, sep='\t',header=None) #abrimos el archivo y lo leemos usando pandas library
#     email_cifrados = list(df[1]) #convertimos nuestro dataset en lista
#     email_cifrados_sin_nan = []
#     '''queremos eleminar aquellos elementos que no estan presentes en el dataset ya que python
#     los intepreta como float y no se pueden iterar (mail 1930 del dataset se encuentra vacio)'''
#     for mail in email_cifrados:
#         if str(mail) != 'nan':
#             email_cifrados_sin_nan.append(mail) #cojemos unicamente los mails que tienen valor aquellos != NAN
#     return email_cifrados_sin_nan



def leer_mails(filename):
    mails = []
    file_archivo = open(filename,encoding='utf-8')
    for line in file_archivo:
        l = line.split('\t')
        mails.append(l[1])
    file_archivo.close()
    return mails


def obtener_frecuencia_caracteres(dataset):
    lista = dataset
    freq_cifrado = dict()
    for i in lista:
        if isinstance(i,str): #funcion is instance devuele true si i es un string, necesario? falta chequiar
            for c in i:
                if isinstance(c,str) == True: #no deberia ser necesario una vez que se controlo por los NAN
                    if se_cifra(c) == True:
                        if c not in freq_cifrado:
                            freq_cifrado[c] = 1 
                        else:
                            freq_cifrado[c]= freq_cifrado[c] + 1
    return freq_cifrado


def ordenar_por_frecuencia(freq_dict):
    dict = freq_dict
    orden_cifrado = []
    for key in dict:
        value = dict[key]
        Tuple = (key, value)
        orden_cifrado.append(Tuple)
    orden_cifrado.sort(key=lambda tup: tup[1], reverse=True) #ordenamos el diccionario en base a los values
    '''utilizamos funcion lambda con tup = tup[1] para agarrar el segundo elemento de la tupla
    si pusieramos tup[0] ordenariamos en base a keys la funcion lambda es una funcion que admite una sola expresion 
    y es anonima'''
    return orden_cifrado

def obtener_frecuencia_estatica():
    ''' Devuelve una lista con las frecuencias de caracteres, ya ordenados en forma decreciente.'''
    return ['e','t','a','o','i','n','s','h','r','d','l','c','u','m','w','f','g','y','p','b','v','k','j','x','q','z']


def inferir_correspondencia(orden_cifrado, orden_sin_cifrar):
    '''agarramos el primer elemento de cada tupla correspondiente de orden cifrado y los coloccamos en una lista
    luego utilizamos la funcion zip para juntar ambas listas en un diccionario'''
    primer_elemento_tuplas = [] 
    for tuplas in orden_cifrado:
        primer_elemento_tuplas.append(tuplas[0])
    correspondencia_inf = dict(zip(primer_elemento_tuplas,orden_sin_cifrar)) 
    '''funcion zip toma dos iterables como argumentos y los devuelve unidos en una lista con tuplas en la forma 
    [(A1,B1),(A2,B2)....(An,Bn)] se le puede pasar como listas, diccionarios o cualquier iterable'''
    return correspondencia_inf


def corregir_correspondencia(diccionario):
    diccionario_corregido = diccionario #correcion manual del diccionario armado por inferencia estadistica
    diccionario_corregido['g'] = 'i'
    diccionario_corregido['l'] = 'n'
    diccionario_corregido['h'] ='f'
    diccionario_corregido['n'] = 'r'
    diccionario_corregido['e'] = 'p'
    diccionario_corregido['j'] = 'b'
    diccionario_corregido['s'] ='c'
    diccionario_corregido['x'] ='l'
    diccionario_corregido['v'] ='h'
    diccionario_corregido['r'] ='y'
    diccionario_corregido['m'] = 'w'
    diccionario_corregido['u'] = 'z'
    return diccionario_corregido


def descifrar_mensaje(mensaje, correspondencia):
    decoder = correspondencia
    email = mensaje
    decoded = []
    for letter in email:
        decoded.append(decoder.get(letter, letter)) #funcion get retorna valor para la clave dada, si no esta devolvemos la letra
    return ''.join(decoded)


#ultimo ejercicio

#modularizamos el problema
#parte(1)
#creamos una lista nueva con nuestro diccionario corregido, agarramos los elementos de la lista con los mensajes codificados y le aplicamos la funcion decifrar mensajes
def creador_lista_mensajes_decodificados(lista_mensajes_codificados,diccionario_a_utilizar):
    mensajeria = []
    for i in range(len(lista_mensajes_codificados)):
        mensajeria.append(descifrar_mensaje(lista_mensajes_codificados[i],diccionario_a_utilizar))
    return mensajeria

#parte 2, creamos funcion para exportar nuestra lista con los mensajes decodificados
def transcribir_mails(filename,lista):
	file = open(filename,'w',encoding='utf-8')
	i = 0
	while i < len(lista):
		file.write(str(i)+"\t"+lista[i]+'\n')
		i = i + 1
	file.close()

def main():
    # Leer el archivo con los mails..
    emails_cifrados = leer_mails('emails_cifrados.csv')
    
    print(' ')
    print(' ')
    
    # Calculamos frecuencia para los mails y ordenamos de forma decreciente por cantidad de apariciones..
    freq_cifrado = obtener_frecuencia_caracteres(emails_cifrados)
    orden_cifrado = ordenar_por_frecuencia(freq_cifrado)
    print()
    print(freq_cifrado)
    print()
    print(orden_cifrado)
    print()
    # Obtenemos lista ordenada de manera estatica, con obtener_frecuencia_estatica.
    orden_sin_cifrar = obtener_frecuencia_estatica()

    # Inferimos la correspondencia de manera automatica, con inferir_correspondencia.
    correspondencia_inf = inferir_correspondencia(orden_cifrado, orden_sin_cifrar)
    print()
    print(correspondencia_inf)
    print()

    # Seguro la correspondencia tenga errores para modifiar. Elegimos un mensaje 
    # y vamos tratando de corregirla de manualmente.
    print('[mensaje deecodificado mediante correspondecia automatica]\n')
    email = descifrar_mensaje(emails_cifrados[1],correspondencia_inf)
    print(email)
    print()
    
    # Aplicamos una funcion para corregir aquellas correspondencias incorrectas.
    # Notar que no devuelve un valor, sino que modifica el parametro (ya que es
    # mutable).

    
    print()
    diccionario_corregido = corregir_correspondencia(correspondencia_inf)
    print()
    
    # Desciframos el mensaje traducido, luego de inferrir (y corregir) la correspondencia.
    
    mensaje_decodificado = descifrar_mensaje(emails_cifrados[1], diccionario_corregido)

    print('[mensaje decodificado con diccionario corregido]\n')
    print(mensaje_decodificado)

    # Finalmente, hacer una funcion que tome un nombre de archivo y guarde, de a uno por linea,
    # los mensajes descifrados.
    
    lista_difinitiva = creador_lista_mensajes_decodificados(emails_cifrados,diccionario_corregido)
    transcribir_mails('lista_mails_decodificados.csv',lista_difinitiva)

    
if __name__ == "__main__":
    main()
