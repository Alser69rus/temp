class Element:
    pass


class Menu:
    pass


class Widget:
    pass


class Menu1(Menu):
    def __init__(self):
        super().__init__()
        self.el1 = Element()
        self.el2 = Element()


class MainMenu(Widget):
    def __init__(self):
        super().__init__()

        #123
        self.menu1 = Menu1()

mainmenu=MainMenu()

mainmenu.menu1.el1