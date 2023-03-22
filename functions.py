
def split(diccionario):
    white = {}
    red = {}
    for i in diccionario:
        if i["type"]==white:
            white.update(diccionario[i])
        if i["type"]==red:
            red.update(diccionario[i])    
    for i in red:
        i.pop("type")
    for i in white:
        i.pop("type")    
    return white,red


def reduce(diccionario,clave):
    resp = []
    for i in diccionario:
        for j in i:
            if j.get(clave)!=None:
                resp.append(j[clave])
            else:
                return    

