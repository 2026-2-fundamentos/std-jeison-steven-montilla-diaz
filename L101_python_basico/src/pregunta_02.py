import gzip


def pregunta_02():
    """
    Cuente cuántos registros hay para cada letra de la primera columna
    (`letter`). Retorne una lista de tuplas `(letra, cantidad)` ordenada
    alfabéticamente por la letra.

    Ejemplo del formato de la respuesta:

        [("A", 8), ("B", 7), ("C", 5), ...]
    """
    with gzip.open('data/data.csv.gz', 'rt') as archivo:
        cont = {}
        for linea in archivo:
            letra = linea.split('\t')[0]
            if letra in cont:
                cont[letra] += 1
            else:
                cont[letra] = 1
    return sorted(cont.items())
