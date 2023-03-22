def split(diccionario):
    white = {}
    red = {}
    for i in diccionario:
        if diccionario["type"]==white:
            white.update(diccionario[i])
    

    return