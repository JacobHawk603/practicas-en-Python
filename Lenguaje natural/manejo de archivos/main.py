import spacy 

nlp = spacy.load("es_core_news_sm")
archivo_entrada = open('archivo_ejercicio_entrada.txt', encoding='utf8')

dataset = archivo_entrada.readlines()
archivo_entrada.close()

normalizado = ""

for lines in dataset:
    if(len(lines)>1):
        lines.replace('\n', '')
        doc = nlp(lines)

        for token in doc:
            print(token.text, token.pos_, token.dep_, token.lemma_)
            normalizado += token.lemma_.strip() + " "
        print(lines)
    else:
        normalizado += "\n"
    

print(normalizado)

archivo_salida = open('archivo_ejercicio_salida.txt', 'w')
archivo_salida.write(normalizado)
archivo_salida.close()