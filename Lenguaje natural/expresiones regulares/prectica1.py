import re


def listToString(lista):
    cadena = ''
    for i in range(len(lista)):
        cadena += lista[i] +'\t'
    return cadena

archivo = open('tweets.txt', 'r', encoding='utf8')

dataset = archivo.read()

#print(dataset)
#outStream = open("busqueda.txt", "w")

cadenaPrueba = "mi cadena!!! de #prueba, aidiconal. \u0144 13:45 2:10 2:01 21/01/2002 1945/17/09 10/02/21 050502/08/12226 :D :d :p :) :v :V xd XD xD :3"

#Los siguientes comentarios corresponden a los imprimibles en consola, primero de la cadena de prueba, y posteriormente la ejecución obteniendo los datos del corpus




#estos son los de las pruebas

#print(re.findall("#+\w{1,30}", cadenaPrueba))
#print(re.findall("\w{1,100}[^\u0144]", cadenaPrueba))
#print(re.findall("\d{1,2}:\d{1,2}", cadenaPrueba))
#print(re.findall("\d{2,4}/\d{1,2}/\d{2,4}", cadenaPrueba))
#print(re.findall("[:,x,X][D,d,p,v,V,)]", cadenaPrueba))
print(re.findall("(?u)\w\w+|\w\w+\n|\.|[\.\,\;\:\¿\?\¡\!]", cadenaPrueba))



#Estos a continuación son los que corresponden a los imprimibles, que posteriormente anexé manualmente a una tabla, están separados de dos en dos, pues el primero de cada uno arroja los elementos, y el segunto, la cantidad de elementos


#print(listToString(re.findall("#+\w{1,30}", dataset)))
#print(len(re.findall("#+\w{1,30}", dataset)))

#print(listToString(re.findall("@+\w{1,30}", dataset)))
#print(len(re.findall("@+\w{1,30}", dataset)))

#print(listToString(re.findall("\d{1,2}:\d{1,2}", dataset)))
#print(len(re.findall("\d{1,2}:\d{1,2}", dataset)))

#print(listToString(re.findall("\d{2,4}/\d{1,2}/\d{2,4}", dataset)))
#print(len(re.findall("\d{2,4}/\d{1,2}/\d{2,4}", dataset)))

#print(listToString(re.findall("[:,x,X][D,d,p,v,V,)]", dataset)))
#print(len(re.findall("[:,;,x,X][D,d,p,v,V,/)]", dataset)))


#outStream.write(listToString(re.findall("#+\w{1,30}[^\u0144,\U0001f4a1,\u2661,\U0001f308,\U0001f62b,\U0001f60c,\U0001f339,\U0001f635,\U0001f499]", dataset)))
#print("\u0144")
#print("\U0001f308")
