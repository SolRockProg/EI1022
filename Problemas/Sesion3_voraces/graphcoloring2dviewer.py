'''
Created on 02/10/2013

@author: david
'''
from easycanvas import EasyCanvas
from algoritmia.datastructures.digraphs import UndirectedGraph
from math import pi

colors = [
    "#000000", "#FFFF00", "#1CE6FF", "#FF34FF", "#FF4A46", "#008941", "#006FA6", "#A30059",
    "#FFDBE5", "#7A4900", "#0000A6", "#63FFAC", "#B79762", "#004D43", "#8FB0FF", "#997D87",
    "#5A0007", "#809693", "#FEFFE6", "#1B4400", "#4FC601", "#3B5DFF", "#4A3B53", "#FF2F80",
    "#61615A", "#BA0900", "#6B7900", "#00C2A0", "#FFAA92", "#FF90C9", "#B903AA", "#D16100",
    "#DDEFFF", "#000035", "#7B4F4B", "#A1C299", "#300018", "#0AA6D8", "#013349", "#00846F",
    "#372101", "#FFB500", "#C2FFED", "#A079BF", "#CC0744", "#C0B9B2", "#C2FF99", "#001E09",
    "#00489C", "#6F0062", "#0CBD66", "#EEC3FF", "#456D75", "#B77B68", "#7A87A1", "#788D66",
    "#885578", "#FAD09F", "#FF8A9A", "#D157A0", "#BEC459", "#456648", "#0086ED", "#886F4C",

    "#34362D", "#B4A8BD", "#00A6AA", "#452C2C", "#636375", "#A3C8C9", "#FF913F", "#938A81",
    "#575329", "#00FECF", "#B05B6F", "#8CD0FF", "#3B9700", "#04F757", "#C8A1A1", "#1E6E00",
    "#7900D7", "#A77500", "#6367A9", "#A05837", "#6B002C", "#772600", "#D790FF", "#9B9700",
    "#549E79", "#FFF69F", "#201625", "#72418F", "#BC23FF", "#99ADC0", "#3A2465", "#922329",
    "#5B4534", "#FDE8DC", "#404E55", "#0089A3", "#CB7E98", "#A4E804", "#324E72", "#6A3A4C",
    "#83AB58", "#001C1E", "#D1F7CE", "#004B28", "#C8D0F6", "#A3A489", "#806C66", "#222800",
    "#BF5650", "#E83000", "#66796D", "#DA007C", "#FF1A59", "#8ADBB4", "#1E0200", "#5B4E51",
    "#C895C5", "#320033", "#FF6832", "#66E1D3", "#CFCDAC", "#D0AC94", "#7ED379", "#012C58"
]


class GraphColoring2DViewer(EasyCanvas):
    def __init__(self, g, colors=None, window_size=(400, 400)):
        EasyCanvas.__init__(self)
        self.colors = colors
        # check 'g' type
        if not isinstance(g, UndirectedGraph) or \
                any([type(p) != type((1, 1)) and type(p) != type((1.0, 1.0)) or len(p) != 2 for p in g.V]):
            raise TypeError("The graph must be an UnirectedGraph of two integer tuples")

        self.g = g
        self.right = max(p[0] for p in self.g.V)
        self.bottom = min(p[1] for p in self.g.V)
        self.left = min(p[0] for p in self.g.V)
        self.top = max(p[1] for p in self.g.V)
        self.window_size = window_size
        self.height = self.top - self.bottom
        self.width = self.right - self.left
        self.ar = self.width / self.height
        ar = self.window_size[0] / self.window_size[1]
        if ar < self.ar:
            self.window_size = (self.window_size[0], self.window_size[0] / self.ar)
        else:
            self.window_size = (self.window_size[1] * self.ar, self.window_size[1])

    def main(self):
        rad = (self.window_size[0] * self.window_size[1] / (pi * 7000)) ** 0.5 * self.width / self.window_size[0]
        margin = rad * 2
        self.easycanvas_configure(title='Graph Coloring 2D Viewer',
                                  background='white',
                                  size=self.window_size,
                                  coordinates=(
                                  self.left - margin, self.bottom - margin, self.right + margin, self.top + margin))
        for u, v in self.g.E:
            self.create_line(u[0], u[1], v[0], v[1], 'gray')

        for u in self.g.V:
            color_relleno = 'red' if colors is None else colors[self.colors[u] % len(colors)]
            self.create_filled_circle(u[0], u[1], rad, color='black', relleno=color_relleno)
        # Wait for a key   
        self.readkey(True)


if __name__ == '__main__':
    g = UndirectedGraph(E=[((-3, -2), (0, 0)), ((0, 0), (1, 1))])
    color_dic = {(-3, -2): 0, (0, 0): 1, (1, 1): 2}
    viewer = GraphColoring2DViewer(g, color_dic, window_size=(800, 800))
    viewer.run()
