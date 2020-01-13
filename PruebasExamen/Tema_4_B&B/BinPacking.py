import math

from Utils.bab_scheme import BabPartialSolution, BabSolver, Solution
from random import seed, randint
from itertools import groupby
from typing import *


def liquid_binpacking(container_weights, capacity, objects):
    add = 0
    suma_pesos = 0
    min_rellenado = 0
    min_objeto = 0
    suma_descartados = 0
    if len(container_weights) > 0: min_rellenado = min(container_weights)
    if len(objects) > 0: min_objeto = min(objects)
    for object in objects:
        if capacity - min_rellenado >= object:
            suma_pesos += object
        else:
            suma_descartados += object
    for container_space in container_weights:
        if capacity - container_space >= min_objeto:
            suma_pesos -= min(capacity - container_space, suma_pesos)
        if suma_pesos == 0:
            break
    else:
        add = math.ceil((suma_pesos + suma_descartados) / capacity)
    return len(container_weights) + add


def binpacking_hard(container_weights: List, capacity, objects):
    for object in objects:
        for i, container_space in enumerate(container_weights):
            if capacity - container_space >= object:
                container_weights[i] += object
                break
        else:
            container_weights.append(object)
    return len(container_weights)


def binpacking_solve(objects: List[int], capacity: int):
    class BinPackingBabPS(BabPartialSolution):
        def __init__(self, decisions: Tuple[int, ...], container_weights: Tuple[int, ...]):
            self.decisions = decisions
            self.container_weights = container_weights
            self.n = len(decisions)
            self._opt = self.calc_opt_bound()
            self._pes = self.calc_pes_bound()

        # TODO: IMPLEMENTAR - Relaja el problema. Trata los objetos que quedan como si fueran un líquido
        def calc_opt_bound(self) -> Union[int, float]:
            return liquid_binpacking(list(self.container_weights), capacity,
                                     objects[self.n:])  # AHORA ES DEMASIADO OPTIMISTA

        # TODO: IMPLEMENTAR - Algoritmo voraz. Completa la solución parcial actual con "En el primero en el que quepa"
        def calc_pes_bound(self) -> Union[int, float]:
            return binpacking_hard(list(self.container_weights), capacity,
                                   objects[self.n:])  # AHORA ES DEMASIADO PESIMISTA

        def is_solution(self) -> bool:
            return self.n == len(objects)

        def get_solution(self) -> Solution:
            return self.decisions

        def successors(self) -> Iterable["BinPackingBabPS"]:
            if self.n < len(objects):
                object_weight = objects[self.n]
                for num_container, container_weight in enumerate(self.container_weights):
                    if container_weight + object_weight <= capacity:
                        list_cw = list(self.container_weights)  # copia tupla a lista
                        list_cw[num_container] += object_weight
                        yield BinPackingBabPS(self.decisions + (num_container,), tuple(list_cw))
                num_container = len(self.container_weights)
                yield BinPackingBabPS(self.decisions + (num_container,), self.container_weights + (object_weight,))

    initial_ps = BinPackingBabPS((), ())
    return BabSolver.solve_minimization(initial_ps)


def show_solution_grouped_by_containers(sol):
    print("\nSOLUTION GROUPED BY CONTAINERS (shows the weights of objects in each container):")
    for pos, g in groupby(sorted([o, i] for i, o in enumerate(sol)), lambda e: e[0]):
        print("\t{}: {}".format(pos, [objs[e[1]] for e in g]))


def create_exact_binpacking_problem(num_containers, objects_per_container):
    seed(5)
    objects = []
    num_c = num_containers
    num_e_c = objects_per_container
    min_v = 25
    max_v = 35
    capacity = max_v * num_e_c + 0
    for ic in range(num_c):
        s = 0
        for ie in range(num_e_c - 1):
            o = randint(min_v, max_v)
            objects.append(o)
            s += o
        objects.append(capacity - s)
    return capacity, sorted(objects, reverse=True)


# PROGRAMA PRINCIPAL -------------------------------------------------------
if __name__ == "__main__":
    # Descomenta la instancia del problema que quieras resolver:
    # C, objs = 10, [6, 6, 3, 3, 2, 2, 2, 2, 2, 2]  # SOLUCIÓN ÓPTIMA: 3 contenedores
    # C, objs = create_exact_binpacking_problem(6, 3)  # SOLUCIÓN ÓPTIMA: 6 contenedores
    C, objs = create_exact_binpacking_problem(12, 3)  # SOLUCIÓN ÓPTIMA: 12 contenedores

    print("PROBLEM TO SOLVE:")
    print("\tContainer capacity:", C)
    print("\tObjects (weights):", objs)

    solution = binpacking_solve(objs, C)

    print("\nBEST SOLUTION:")
    print("\tB&B solution: {0} containers. Details: {1}".format(max(solution) + 1, solution))

    show_solution_grouped_by_containers(solution)
