

if __name__ == '__main__':

    estados = ['q0', 'q1', 'q2', 'q3', 'q4']

    cadena = list("00001111\0")
    estado = estados[0]
    puntero = 0
    bandera = True

    while bandera:
        if puntero < len(cadena):
            if cadena[puntero] == '0':
                if estado == estados[0]:
                    cadena[puntero] = 'X'
                    puntero+=1
                    estado=estados[1]
                elif estado == estados[1]:
                    cadena[puntero] = '0'
                    puntero+=1
                    estado=estados[1]
                elif estado == estados[2]:
                    cadena[puntero] = '0'
                    puntero-=1
                    estado=estados[2]
                else:
                    print("cadena rechazada")
                    exit(0)
            elif cadena[puntero] == '1':
                if estado == estados[1]:
                    cadena[puntero] = 'Y'
                    puntero-=1
                    estado=estados[2]
                else:
                    print("cadena rechazada")
                    exit(0)
            elif cadena[puntero] == 'X':
                if estado == estados[2]:
                    cadena[puntero] = 'X'
                    puntero+=1
                    estado=estados[0]
                else:
                    print("cadena rechazada")
                    exit(0)
            elif cadena[puntero] == 'Y':
                if estado == estados[0]:
                    cadena[puntero] = 'Y'
                    puntero+=1
                    estado=estados[3]
                elif estado == estados[1]:
                    cadena[puntero] = 'Y'
                    puntero+=1
                    estado=estados[1]
                elif estado == estados[2]:
                    cadena[puntero] = 'Y'
                    puntero-=1
                    estado=estados[2]
                elif estado == estados[3]:
                    cadena[puntero] = 'Y'
                    puntero+=1
                    estado=estados[3]
                else:
                    print("cadena rechazada")
                    exit(0)
                
            
            elif cadena[puntero] == '\0':
                if estado == estados[3]:
                    cadena[puntero] = 'B'
                    puntero+=1
                    estado=estados[4]
                    bandera = False

        imprimible = "".join(cadena)
        print("ultimo estado: {}\tcadena: {}".format(estado, imprimible))