
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
        if i.get(clave)!=None:
            resp.append(i[clave])

    if resp.len() != 0:
        return resp
    else:
        print("Type Error")
        
               

            
              

