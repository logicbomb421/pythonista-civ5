import ui
from capital_connection_profit import CapitalConnectionProfitView


class NavigationView(ui.NavigationView):
    __capital_city_connection_yield_button = None

    @property
    def _capital_city_connection_yield_button(self):
        if not self.__capital_city_connection_yield_button:
            self.__capital_city_connection_yield_button = ui.Button(
                name="cap_city_conn_button",
                title="Capital City Connection Yield",
                font=(SYSTEM_FONT, 15),
                border_width=1,
                corner_radius=5,
                action=lambda sender: self.push_view(CapitalConnectionProfitView()),
            )

    def __init__(self):
        self.add_subview(self._capital_city_connection_yield_button)


class MainView(ui.View):
    def __init__(self):
        self.add_subview(NavigationView())


MainView().present("fullscreen")
