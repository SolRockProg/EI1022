from Utils.skylineviewer import SkylineViewer
from typing import *
import sys


def read_file(fichero):
    res = []
    for line in open(fichero, "r"):
        values = line.split()
        values = [int(a) for a in values]
        res.append(tuple(values))
    return res


def skyline(buildings: List[Tuple[int, ...]], b: int, e: int) -> List[int]:
    def combiner(skyline_left: List[int], skyline_right: List[int]) -> List[int]:
        res = []
        left, right = 0, 0
        h_left, h_right = 0, 0
        previous = 0
        skyline_left.append(0)  #Se añade un 0 al final de las dos listas para así tener en cuenta que la altura del último punto es 0
        skyline_right.append(0)
        while left < len(skyline_left) - 1 and right < len(skyline_right) - 1:
            if skyline_left[left] < skyline_right[right]:
                h_left = skyline_left[left + 1]
                x = skyline_left[left]
                left += 2
            elif skyline_left[left] > skyline_right[right]:
                h_right = skyline_right[right + 1]
                x = skyline_right[right]
                right += 2
            else:
                h_right = skyline_right[right + 1]
                h_left = skyline_left[left + 1]
                x = skyline_right[right]
                right += 2
                left += 2
            max_h = max(h_left, h_right)
            if previous is not max_h:
                res.append(x)
                res.append(max_h)
                previous = max_h
        for i in range(left, len(skyline_left)):
            res.append(skyline_left[i])
        for i in range(right, len(skyline_right)):
            res.append(skyline_right[i])
        res.pop() #elimina el último elemento ya que será un 0
        return res

    if e - b == 1:
        return [buildings[b][0], buildings[b][1], buildings[b][0] + buildings[b][2]]
    else:
        half = (b + e) // 2
        return combiner(skyline(buildings, b, half), skyline(buildings, half, e))


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        buildings = read_file(sys.argv[1])
        sol = skyline(buildings, 0, len(buildings))
        for s in sol:
            print(s, end=" ")
        if len(sys.argv) == 3 and sys.argv[2] == "-g":
            skyline = skyline(buildings, 0, len(buildings))
            viewer = SkylineViewer(skyline)
            for b in buildings:
                viewer.add_building(b)
            viewer.run()
