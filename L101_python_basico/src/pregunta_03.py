import gzip


def pregunta_03():
    """
    Sume los valores de la segunda columna (`value`) para cada letra de la
    primera columna (`letter`). Retorne una lista de tuplas `(letra, suma)`
    ordenada alfabéticamente por la letra.

    Ejemplo del formato de la respuesta:

        [("A", 53), ("B", 36), ("C", 27), ...]
    """
    with gzip.open('data/data.csv.gz', 'rt') as archivo:
        cont = {}
        for linea in archivo:
            letra = linea.split('\t')[0]
            valor = int(linea.split('\t')[1])
            if letra in cont:
                cont[letra] += valor
            else:
                cont[letra] = valor


    raise NotImplementedError
