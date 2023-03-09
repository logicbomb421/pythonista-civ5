import ui


@ui.in_background
def calculate(sender):
    cap_city_citizens_field = sender.superview["cap_city_citizen_field"]
    conn_city_citizens_field = sender.superview["conn_city_citizen_field"]
    result_label = sender.superview["result_label"]

    cap_city_citizens = float(cap_city_citizens_field.text)
    conn_city_citizens = float(conn_city_citizens_field.text)
    result = (conn_city_citizens * 1.1) + (cap_city_citizens * 0.15) - 1
    result_label.text = str(result)


v = ui.load_view("home")
v.present("fullscreen")
