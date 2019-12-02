from Utils.skylineviewer import SkylineViewer
from typing import *


def skyline(buildings: List[Tuple[int, ...]], b: int, e: int) -> List[int]:
    def combiner(skyline_left: List[int], skyline_right: List[int]) -> List[int]:
        res = []
        left, right = 0, 0
        h_left, h_right = 0, 0
        previous = 0

        while left < len(skyline_left)-1 and right < len(skyline_right)-1:
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
        return res

    if e - b == 1:
        return [buildings[b][0], buildings[b][1], buildings[b][0] + buildings[b][2]]
    else:
        half = (b + e) // 2
        return combiner(skyline(buildings, b, half), skyline(buildings, half, e))


if __name__ == "__main__":
    buildings = [(1, 10, 3), (2, 5, 5), (3, 6, 3), (4, 7, 5), (10, 10, 3), (9, 4, 6), (20, 8, 4), (22, 6, 6), (25, 10, 2)]
    print(skyline(buildings, 0, len(buildings)))
    skyline = skyline(buildings, 0, len(buildings))
    viewer = SkylineViewer(skyline)
    for b in buildings:
        viewer.add_building(b)
    viewer.run()
