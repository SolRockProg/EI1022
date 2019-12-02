from skylineviewer import SkylineViewer

buildings = [(1, 10, 3), (2, 5, 5), (3, 6, 3), (4, 7, 5), (10, 10, 3), (9, 4, 6), (20, 8, 4), (22, 6, 6), (25, 10, 2)]

skyline = [1, 10, 4, 7, 9, 4, 10, 10, 13, 4, 15, 0, 20, 8, 24, 6, 25, 10, 27, 6, 28]

viewer = SkylineViewer(skyline)

for b in buildings:
    viewer.add_building(b)

viewer.run()