import difflib

text1 = open(
    r"C:\Users\carlo\PycharmProjects\EI1022\Entregables\Entregable3_by_jaume\pruebas\pruebas.sol", encoding="utf-8").readlines()
text2 = open(
    r"C:\Users\carlo\PycharmProjects\EI1022\Entregables\Entregable3_by_jaume\pruebas\solucion.txt", encoding="utf-8").readlines()

for line in difflib.unified_diff(text1, text2):
    print(line)
