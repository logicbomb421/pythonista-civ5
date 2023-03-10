import ui

IPHONE_XS_WIDTH = 375


class CapitalConnectionProfitView(ui.View):
    def __init__(self):
        self.frame = (0, 0, 150, 150)
        self.background_color = "#ffffff"
        # self.border_width = 3
        # self.border_color = "#000000"
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
                font=("<system-bold>", 24),
                text="Capital Connection Profit",
                alignment=ui.ALIGN_CENTER,
            )
        )

    def _build_input(self):
        self._build_connecting()
        self._build_capital()
        # swtich
        # calc button

    def _build_connecting(self):
        self.add_subview(
            ui.Label(
                name="connecting_label",
                frame=(6, 72, 208, 32),
                text="Connecting City Citizens",
            )
        )
        self.add_subview(
            ui.TextField(
                name="conn_city_citizen_field",
                frame=(222, 72, 83, 32),
                border_width=1,
                corner_radius=5,
                keyboard_type=ui.KEYBOARD_NUMBERS,
            )
        )

    def _build_capital(self):
        self.add_subview(
            ui.Label(
                name="capital_label",
                frame=(6, 112, 208, 32),
                text="Capital City Citizens",
            )
        )
        self.add_subview(
            ui.TextField(
                name="cap_city_citizen_field",
                frame=(222, 112, 83, 32),
                border_width=1,
                corner_radius=5,
                keyboard_type=ui.KEYBOARD_NUMBERS,
            )
        )

    def _build_output(self):
        pass
        # gross yield
        # net yield


CapitalConnectionProfitView().present("fullscreen")
