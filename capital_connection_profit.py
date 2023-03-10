import ui

IPHONE_XS_WIDTH = 375
SYSTEM_FONT = "<system>"


class CapitalConnectionProfitView(ui.View):
    __conn_city_citizen_field = None
    __cap_city_citizen_field = None
    __clear_on_calculate_switch = None
    __calculate_button = None

    @property
    def _conn_city_citizen_field(self):
        if not self.__conn_city_citizen_field:
            self.__conn_city_citizen_field = ui.TextField(
                name="conn_city_citizen_field",
                frame=(222, 72, 83, 32),
                font=("<system>", 17),
                border_width=1,
                corner_radius=5,
                keyboard_type=ui.KEYBOARD_NUMBER_PAD,
            )
        return self.__conn_city_citizen_field

    @property
    def _cap_city_citizen_field(self):
        if not self.__cap_city_citizen_field:
            self.__cap_city_citizen_field = ui.TextField(
                name="cap_city_citizen_field",
                frame=(222, 112, 83, 32),
                font=("<system>", 17),
                border_width=1,
                corner_radius=5,
                keyboard_type=ui.KEYBOARD_NUMBER_PAD,
            )
        return self.__cap_city_citizen_field

    @property
    def _clear_on_calculate_switch(self):
        if not self.__clear_on_calculate_switch:
            self.__clear_on_calculate_switch = ui.Switch(
                name="clear_on_calculate_switch", frame=(162, 347, 51, 31), value=True
            )
        return self.__clear_on_calculate_switch

    @property
    def _calculate_button(self):
        if not self.__calculate_button:
            self.__calculate_button = ui.Button(
                name="calc_button",
                title="Calculate",
                frame=(88, 250, 200, 47),
                font=(SYSTEM_FONT, 15),
                border_width=1,
                corner_radius=5,
                action=self._calculate,
            )
        return self.__calculate_button

    def __init__(self):
        self.frame = (0, 0, 150, 150)
        self.background_color = "#ffffff"
        self._build()

    def _build(self):
        # NOTE: only storing fields we need to interact with at the class level
        self.add_subview(
            ui.Label(
                name="title",
                frame=(0, 0, IPHONE_XS_WIDTH, 45),
                font=("<system-bold>", 24),
                text="Capital Connection Profit",
                alignment=ui.ALIGN_CENTER,
            )
        )
        self.add_subview(
            ui.Label(
                name="connecting_label",
                frame=(6, 72, 208, 32),
                font=(SYSTEM_FONT, 18),
                text="Connecting City Citizens",
            )
        )
        self.add_subview(self._conn_city_citizen_field)
        self.add_subview(
            ui.Label(
                name="capital_label",
                frame=(6, 112, 208, 32),
                font=(SYSTEM_FONT, 18),
                text="Capital City Citizens",
            )
        )
        self.add_subview(self._cap_city_citizen_field)
        self.add_subview(self._clear_on_calculate_switch)
        self.add_subview(self._calculate_button)

    def _calculate(self):
        pass

    def _build_input(self):
        self._build_connecting()
        self._build_capital()
        # swtich
        # calc button

    def _build_output(self):
        pass
        # gross yield
        # net yield


CapitalConnectionProfitView().present("fullscreen")
