import panel as pn
import pandas as pd

from widgets import maps


def report_dboard():

    input_data = pd.DataFrame.from_dict(
        {
            "longitude": [-0.155, 0.2795, -0.12344],
            "latitude": [51.5229, 51.5560, 51.5046313],
        }
    )

    interactive_map = maps.HoloMap(input_data)

    gspec = pn.GridSpec(sizing_mode="stretch_both")
    gspec[0, 0] = interactive_map.param
    gspec[1, 0] = interactive_map.view

    return gspec


dashboard = report_dboard()
dashboard.servable()
