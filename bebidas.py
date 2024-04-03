# Sistema de Gestión de Cafetería 
# Autor: Diego García de los Salmones Ajuria | A01736106

# coding=utf-8

def addBebida(infoBebida):

    iBebida = infoBebida
    
    # Revisar que haya comas
    if (',' in iBebida) == False:
        return False
    
    # Separar el nombre de la bebida de los tamaños
    nombre, tamanos = iBebida.split(",", 1)
    
    # Eliminar espacios al inicio y al final en el nombre de la bebida
    nombre = nombre.lstrip()
    nombre = nombre.rstrip()
    
    # Eliminar espacios en tamanos
    tamanos = tamanos.replace(" ", "")
    
    # Eliminar acentos para evitar cualquier problema para identificar caracteres alfabéticos
    nombre = nombre.replace("á","a")
    nombre = nombre.replace("é","e")
    nombre = nombre.replace("í","i")
    nombre = nombre.replace("ó","o")
    nombre = nombre.replace("ú","u")
    
    # Variable auxiliar del nombre sin espacios
    nombre_aux = nombre.replace(" ","")
    
    # Verificar que el nombre de la bebida sea alfabético
    if nombre_aux.isalpha() == False:
        return False
    
    # Verificar la longitud del nombre
    if len(nombre) < 2 or len(nombre) > 15:
        return False
    
    # Separar los tamaños
    tamanos = tamanos.split(",")
    
    # Verificar la cantidad de tamaños
    if len(tamanos) < 1 or len(tamanos) > 5:
        return False
    
    # Convertir tamaños a enteros y verificar el rango y orden ascendente
    tamanos_enteros = []
    for tam in tamanos:
        try:
            tam_int = int(tam)
            if tam_int < 1 or tam_int > 48:
                return False
            if tamanos_enteros and tam_int <= tamanos_enteros[-1]:
                return False
            tamanos_enteros.append(tam_int)
        except ValueError:
            return False
    
    return True
