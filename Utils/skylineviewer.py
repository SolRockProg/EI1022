from easycanvas import EasyCanvas

class SkylineViewer(EasyCanvas):
    def __init__(self, skyline, unit = 30):
        EasyCanvas.__init__(self)
        self.unit = unit
        self.buildings = []
        self.skyline = skyline
        
    def add_building(self, b):
        self.buildings.append(b)
    
    def main(self):
        minx = min (self.skyline[0], min(b[0] for b in self.buildings) if self.buildings != [] else self.skyline[0]) - 1
        maxx = max (self.skyline[-1], max(b[2] for b in self.buildings) if self.buildings != [] else self.skyline[-1]) + 1
        maxh = max (self.skyline[i] for i in range(1, len(self.skyline), 2)) + 1
        
        screen_width = self.root.winfo_screenwidth()
        if (maxx-minx)*self.unit > screen_width:
            self.unit = (screen_width/(maxx-minx))
        self.easycanvas_configure(title = "Skyline",
                                  background = "white",
                                  size = ((maxx - minx) * self.unit, maxh * self.unit),  
                                  coordinates = (minx, -1, maxx, maxh)
                                  )
        c1 = "blue"
        c2 = "red"
        w1 = 1
        w2 = 1
        for b in self.buildings:
            self.create_rectangle(b[0], 0, b[0]+b[2], b[1], c1, width=w1)
        h = 0
        x = self.skyline[0]
        
        for i in range(1, len(self.skyline), 2):
            h2 = self.skyline[i]
            x2 = self.skyline[i+1]
            self.create_line(x, h, x, h2, c2, width=w2)
            self.create_line(x, h2, x2, h2, c2, width=w2)
            h = h2
            x = x2
        self.create_line(x, h, x, 0, c2, width=w2)
        
        # La tecla Escape cierra la ventana
        while self.readkey(True)!='Escape': pass