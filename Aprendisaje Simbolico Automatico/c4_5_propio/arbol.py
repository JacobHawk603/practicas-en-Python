class rama:
    def __init__(self, nodo:str = '', is_hoja:bool = False):
        self.nodo = nodo
        self.subramas = []
        self.is_hoja = is_hoja
    
    def ramificar(self, subramas):
        
        self.subramas.append(subramas)

    def recorrerRama(self):
        '''retorna el objeto de tipo rama si es que no tiene subramas, en caso de que se trate de un nodo hoja, no retornará nada'''

        if len(self.subramas > 1):
            for subrama in self.subramas:
                sub_rama = subrama.recorrerRama()

                if(not sub_rama.is_hoja):
                    return sub_rama

        elif(len(self.subramas == 0) and not self.is_hoja):
            # es_hoja = True
            return self
            # return es_hoja, self.subramas
        # else:
        #     es_hoja = False

        #     return es_hoja, self.subramas


        #         # if (nodo_hoja):
        #         #     return False
        #         # else:
        #         #     return self

        



class arbol:
    def __init__(self, nodo_inicial:str):
        self.arbol = [nodo_inicial, []]
    

    def ramificar(self, rama:rama, nombre_nodo:str, is_hoja:bool, sub_ramas:list[rama]=None):
        '''ramas -> rama no hoja y sin subramas que obtuvimos de la funcion rama.recorrerRama\n
            nombre_nodo: es el nombre que va a llevar la rama\n
            is_hoja: booleano que modificará el estado del booleano rama.is_hoja para definir siserà una hoja o una rama\n
            sub_ramas: es un arreglo de ramas que se anexarà a la rama que estamos ramificando
        '''

        if(not is_hoja):
            rama.nodo = nombre_nodo
            rama.subramas = sub_ramas
        else:
            # es un nodo terminal, una hoja, y por tanto, no tiene ramificaciones
            rama.nodo = nombre_nodo
            

        # for nodo in self.arbol:
        #     if(nodo == nodo_value and nodo_value != self.arbol[0]):
        #         self.arbol[self.arbol.index(nodo_value)].append(ramas)
        #     elif(nodo == nodo_value):
        #         self.arbol.append(ramas)


