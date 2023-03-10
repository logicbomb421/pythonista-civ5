import ui

road_cost_per_tile = 1

@ui.in_background
def calculate(sender):
    cap_city_citizens_field = sender.superview["cap_city_citizen_field"]
    conn_city_citizens_field = sender.superview["conn_city_citizen_field"]
    num_tiles_field = sender.superview['num_tiles_field']
    gross_yield_label = sender.superview["gross_yield_label"]
    net_yield_label = sender.superview['net_yield_label']

    cap_city_citizens = float(cap_city_citizens_field.text)
    conn_city_citizens = float(conn_city_citizens_field.text)
    gross_yield = (conn_city_citizens * 1.1) + (cap_city_citizens * 0.15) - 1
    net_yield = gross_yield - (float(num_tiles_field.text) * road_cost_per_tile)
    gross_yield_label.text = str(round(gross_yield, 2))
    net_yield_label.text = str(round(net_yield, 2))


v = ui.load_view("home")
v.size_to_fit()
v.present("fullscreen")
