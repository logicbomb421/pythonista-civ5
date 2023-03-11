import ui
from constants import *
from capital_connection_profit import CapitalConnectionProfitView


class MainView(ui.View):
    def __init__(self):
        self.background_color = "#ffffff"
        self.add_subview(
            ui.Button(
                name="cap_city_conn_button",
                title="Capital City Connection Yield",
                font=(SYSTEM_FONT, 15),
                border_width=1,
                corner_radius=5,
                action=lambda sender: self.navigation_view.push_view(CapitalConnectionProfitView()),
            )
        )


ui.NavigationView(MainView()).present(
    style="default",
    animated=True,
    popover_location=(0, 0),
    hide_title_bar=False,
    title_bar_color=None,
    title_color=None,
    orientations=["portrait"],
    hide_close_button=False,
)
