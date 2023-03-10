import ui

# Pythonista Constants
IPHONE_XS_WIDTH = 375
SYSTEM_FONT = "<system>"
COLOR_RED = "#ff0000"
COLOR_GREEN = "#00ff00"
COLOR_WHITE = "#ffffff"
DEFAULT_CONTROL_HEIGHT_PX = 32

# Civ V Constants
ROAD_COST_PER_TILE = 1


class CapitalConnectionProfitView(ui.View):
    __conn_city_citizen_field = None
    __cap_city_citizen_field = None
    __num_tiles_field = None
    __machu_pichu_switch = None
    __arabia_switch = None
    __calculate_button = None
    __gross_yield_label = None
    __net_yield_label = None

    @property
    def _conn_city_citizen_field(self):
        if not self.__conn_city_citizen_field:
            self.__conn_city_citizen_field = ui.TextField(
                name="conn_city_citizen_field",
                frame=(222, 72, 83, DEFAULT_CONTROL_HEIGHT_PX),
                font=(SYSTEM_FONT, 17),
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
                frame=(222, 112, 83, DEFAULT_CONTROL_HEIGHT_PX),
                font=(SYSTEM_FONT, 17),
                border_width=1,
                corner_radius=5,
                keyboard_type=ui.KEYBOARD_NUMBER_PAD,
            )
        return self.__cap_city_citizen_field

    @property
    def _num_tiles_field(self):
        if not self.__num_tiles_field:
            self.__num_tiles_field = ui.TextField(
                name="num_tiles_field",
                frame=(222, 152, 83, DEFAULT_CONTROL_HEIGHT_PX),
                font=(SYSTEM_FONT, 17),
                border_width=1,
                corner_radius=5,
                keyboard_type=ui.KEYBOARD_NUMBER_PAD,
            )
        return self.__num_tiles_field

    @property
    def _machu_pichu_switch(self):
        if not self.__machu_pichu_switch:
            self.__machu_pichu_switch = ui.Switch(
                name="machu_pichu_switch", frame=(222, 192, 51, DEFAULT_CONTROL_HEIGHT_PX), value=False
            )
        return self.__machu_pichu_switch

    @property
    def _arabia_switch(self):
        if not self.__arabia_switch:
            self.__arabia_switch = ui.Switch(
                name="arabia_switch", frame=(222, 232, 51, DEFAULT_CONTROL_HEIGHT_PX), value=False
            )
        return self.__arabia_switch

    @property
    def _calculate_button(self):
        if not self.__calculate_button:
            self.__calculate_button = ui.Button(
                name="calc_button",
                title="Calculate",
                frame=(88, 322, 200, 47),
                font=(SYSTEM_FONT, 15),
                border_width=1,
                corner_radius=5,
                action=lambda sender: self._calculate(sender),
            )
        return self.__calculate_button

    @property
    def _gross_yield_label(self):
        if not self.__gross_yield_label:
            self.__gross_yield_label = ui.Label(
                name="gross_yield_label",
                frame=(184, 385, 150, DEFAULT_CONTROL_HEIGHT_PX),
                font=(SYSTEM_FONT, 18),
                alignment=ui.ALIGN_CENTER,
            )
        return self.__gross_yield_label

    @property
    def _net_yield_label(self):
        if not self.__net_yield_label:
            self.__net_yield_label = ui.Label(
                name="net_yield_label",
                frame=(184, 425, 150, DEFAULT_CONTROL_HEIGHT_PX),
                font=(SYSTEM_FONT, 18),
                alignment=ui.ALIGN_CENTER,
            )
        return self.__net_yield_label

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
                frame=(6, 72, 208, DEFAULT_CONTROL_HEIGHT_PX),
                font=(SYSTEM_FONT, 18),
                text="Connecting City Citizens",
            )
        )
        self.add_subview(self._conn_city_citizen_field)
        self.add_subview(
            ui.Label(
                name="capital_label",
                frame=(6, 112, 208, DEFAULT_CONTROL_HEIGHT_PX),
                font=(SYSTEM_FONT, 18),
                text="Capital City Citizens",
            )
        )
        self.add_subview(self._cap_city_citizen_field)
        self.add_subview(
            ui.Label(
                name="num_tiles_label",
                frame=(6, 152, 208, DEFAULT_CONTROL_HEIGHT_PX),
                font=(SYSTEM_FONT, 18),
                text="Tiles to Connect",
            )
        )
        self.add_subview(self._num_tiles_field)
        self.add_subview(
            ui.Label(
                name="machu_pichu_label",
                frame=(6, 192, 208, DEFAULT_CONTROL_HEIGHT_PX),
                font=(SYSTEM_FONT, 18),
                text="Machu Pichu in Conn City?",
            )
        )
        self.add_subview(self._machu_pichu_switch)
        self.add_subview(
            ui.Label(
                name="arabia_label",
                frame=(6, 232, 208, DEFAULT_CONTROL_HEIGHT_PX),
                font=(SYSTEM_FONT, 18),
                text="Are You Arabia?",
            )
        )
        self.add_subview(self._arabia_switch)
        self.add_subview(self._calculate_button)
        self.add_subview(
            ui.Label(
                name="gy_label",
                text="Gross Yield",
                frame=(17, 385, 150, DEFAULT_CONTROL_HEIGHT_PX),
                alignment=ui.ALIGN_CENTER,
                font=(SYSTEM_FONT, 22),
            )
        )
        self.add_subview(self._gross_yield_label)
        self.add_subview(
            ui.Label(
                name="ny_label",
                text="Net Yield",
                frame=(17, 425, 150, DEFAULT_CONTROL_HEIGHT_PX),
                alignment=ui.ALIGN_CENTER,
                font=(SYSTEM_FONT, 22),
            )
        )
        self.add_subview(self._net_yield_label)

    def _calculate(self, sender):
        """
        ref: https://gaming.stackexchange.com/a/8207
        """
        # TODO: implement arabia modifier
        gross_yield = (
            (float(self._conn_city_citizen_field.text) * (1.1 if not self._machu_pichu_switch.value else 1.3))
            + (float(self._cap_city_citizen_field.text) * 0.15)
            - 1
        )
        net_yield = gross_yield - (float(self._num_tiles_field.text) * ROAD_COST_PER_TILE)
        self._gross_yield_label.text = str(round(gross_yield, 2))
        self._net_yield_label.background_color = COLOR_RED if net_yield <= 0 else COLOR_GREEN
        self._net_yield_label.text = str(round(net_yield, 2))


CapitalConnectionProfitView().present("fullscreen")
