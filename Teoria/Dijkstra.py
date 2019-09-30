from algoritmia.datastructures.digraphs import Digraph, WeightingFunction
from algoritmia.utils import argmin
from algoritmia.data.mallorca import Mallorca, km


def dijkstra(g: Digraph, d: WeightingFunction, v_inicial, v_final):
    D = {}
    added = set()
    recorrido = []
    for v in g.V: D[v] = float("infinity")
    D[v_inicial] = 0
    frontera = {v_inicial: v_inicial}
    while len(frontera) > 0:
        v_destino = argmin(frontera.keys(), lambda v: D[v])
        added.add(v_destino)
        v_origen = frontera[
            v_destino]  # Como en el recorrido de backpointers, aquí el origen del v_destino es el valor de los vertices frontera
        recorrido.append((v_origen, v_destino))
        del frontera[v_destino]
        if v_destino == v_final:
            break
        for i in g.succs(v_destino):
            if i not in added and D[v_destino] + d(v_destino, i) < D[i]:
                frontera[i] = v_destino
                D[i] = D[v_destino] + d(v_destino, i)
    return recorrido


def backpointer(aristas, target):
    dic = {v: u for (u, v) in aristas}
    camino = [target]
    while target != dic[target]:
        target = dic[target]
        camino.append(target)
    camino.reverse()
    return camino


recorrido_aristas = dijkstra(Mallorca, km, 'Andratx', 'Manacor')
print(backpointer(recorrido_aristas, 'Manacor'))
