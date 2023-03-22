import functions

diccionario = functions.read_data("winequality.csv")
uno,dos= functions.split(diccionario)
tres = functions.reduce(diccionario,"chlorides")

