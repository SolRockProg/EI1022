from easycanvas import EasyCanvas
class TestEC(EasyCanvas):
    def main(self):
        self.easycanvas_configure(title = 'Test', size = (600,600))
        self.create_filled_circle(750,750,250,'black','blue')
        self.create_circle(250,250,250,'red')
        self.create_text(500,500,"Press any key to exit",12)
        self.readkey(True)
TestEC().run()