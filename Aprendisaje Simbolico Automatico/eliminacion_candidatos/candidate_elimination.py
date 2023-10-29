import hipotesis
from hipotesis import General, Especifica
import pandas as pd
from procesamiento_datasets import valores_observados

def Candidtae_Elimination(hipotesis_especificas:list[Especifica], hipotesis_generales:list[General], x_muestra:pd.DataFrame, y_muestra:pd.DataFrame, casos_positivos:list[bool] = [True, True, False]):
    
    #comenzamos a recorrer el dataset para ir moldeando nuestras hipotesis

    print("es esta impresion: ",hipotesis_especificas[0].etiquetas)
    print("es esta impresion: ",hipotesis_especificas[0].aceptados)

    for row, y in zip(x_muestra.values.tolist(), y_muestra):
        print(row, y)

        if casos_positivos[y-1]:
            #se trata de un ejemplo positivo, hay que generalizar nuestras hipotesis
            
            #primero comparamos cada elemento de nuestra hipotesis especifica

            for hipotesis_especifica in hipotesis_especificas:

                for aceptados_atributo, valor_observado, etiqueta in zip(hipotesis_especifica.aceptados, row, x_muestra.columns):

                    print(etiqueta, valor_observado)

                    if not aceptados_atributo.__contains__(valor_observado):
                        #aqui es donde hay que generalizar la hipotesis especifica

                        hipotesis_especifica.generalizar(etiqueta, valor_observado)

                print(hipotesis_especifica)
                print(hipotesis_especifica.aceptados)

            # break
                
            #ahora en la hipotesis general, tenemos que eliminar cualquier hipotesis que no cubra al caso positivo

            #si la hipotesis general es universal, tenemos que sustituir por las minimas especializaciones

            if hipotesis_generales[0].acepta_todo:
                
                #construimos el dominio de valores observados por cada atributo
                dominios:list[list[str]] = []

                for column in x_muestra.columns.tolist():
                    
                    dominios.append(valores_observados(x_muestra[column]))

                #sustituimos por minimas especializaciones
                hipotesis_generales = hipotesis.minimas_Especializaciones(hipotesis_generales[0], dominios)

                #eliminamos hipotesis que no cubren el caso positivo
                hipotesis_generales = hipotesis.validar_hipotesis_generales(hipotesis_generales, row)

            else:
                
                #Si las hipotesis generales ya no aceptan a todos los eleme4ntos, de las hipotesis generales que tenemos, solamente eliminamos las que no cubren al caso positivo
                hipotesis_generales = hipotesis.validar_hipotesis_generales(hipotesis_generales, row)

        else:

            #se trata de un ejemplo negatigo, hay que especificar la hipotesis

            #si la hipotesis general es universal, tenemos que sustituir por las minimas especializaciones

            if hipotesis_generales[0].acepta_todo:
                
                #construimos el dominio de valores observados por cada atributo
                dominios:list[list[str]] = []

                for column in x_muestra.columns.tolist():
                    
                    dominios.append(valores_observados(x_muestra[column]))

                print(dominios)

                #sustituimos por minimas especializaciones
                hipotesis_generales = hipotesis.minimas_Especializaciones(hipotesis_generales[0], dominios)

            #revisar que la hipotesis general no contenga al caso negativo o bien, que el caso negativo esté guardado en la lista de valores rechazados

            # for hipotesis_general in hipotesis_generales:

            #     for rechazados_atributo, valor_observado, etiqueta in zip(hipotesis_general.rechazados, row, corpus.columns):

            #         if not rechazados_atributo.__contains__(valor_observado):

            #             hipotesis_general.especializar(etiqueta, valor_observado)

            hipotesis_generales = hipotesis.validar_hipotesis_generales(hipotesis_generales, row, caso_positivo=False)

            # print("hola")

        print("evolucion de hipotesis: \n\n")

        for hipotesis_general in hipotesis_generales:

            print("general: \t",hipotesis_general)

        for hipotesis_especifica in hipotesis_especificas:
            
            print("especifica: \t", hipotesis_especifica)

        print(len(hipotesis_generales))

    
    return hipotesis_generales, hipotesis_especifica