import ui

IPHONE_XS_WIDTH = 375


class CapitalConnectionProfitView(ui.View):
    def __init__(self):
        self.frame = (0, 0, 150, 150)
        self.background_color = "#ffffff"
        self.border_width = 3
        self.border_color = "#000000"
        self._build()

    def _build(self):
        self._build_title()
        self._build_input()
        self._build_output()

    def _build_title(self):
        self.add_subview(
            ui.Label(
                name="title",
                frame=(0, 0, IPHONE_XS_WIDTH, 45),
                font_size=24,
                text="Capital Connection Profit",
                alignment="center",
            )
        )

    def _build_input(self):
        self._build_capital()
        self._build_connecting()
        # swtich
        # calc button

    def _build_capital(self):
        pass

    def _build_connecting(self):
        pass

    def _build_output(self):
        pass
        # gross yield
        # net yield


CapitalConnectionProfitView().present("fullscreen")
