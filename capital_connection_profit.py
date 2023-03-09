import ui


class CapitalConnectionProfitView(ui.View):
    def __init__(self):
        self.frame = (0, 0, 150, 150)
        self.background_color = "#ffffff"
        self.border_width = 3
        self.border_color = "#000000"


CapitalConnectionProfitView().present("fullscreen")
