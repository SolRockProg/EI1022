import difflib

text1 = open(
    r"C:\Users\carlo\PycharmProjects\EI1022git\Entregables\Entregable3_by_jaume\pruebas\solucion.txt").readlines()
text2 = open(
    r"C:\Users\carlo\PycharmProjects\EI1022git\Entregables\Entregable3_by_jaume\pruebas\pruebas.sol").readlines()

for line in difflib.unified_diff(text1, text2):
    print(line)
