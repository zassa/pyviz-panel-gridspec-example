import param
import holoviews as hv
import geoviews as gv
import geoviews.tile_sources as gvts

hv.extension("bokeh", logo=False)


class HoloMap(param.Parameterized):

    number_of_points = param.Integer(default=2, bounds=(1, 3))

    def __init__(self, data):
        super().__init__(name="")

        self.eval_df = data

    @staticmethod
    def create_map(df):
        found_points = gv.Points(df, kdims=["longitude", "latitude"])
        opts = dict(marker="o", size=20.0)
        return gvts.OSM * found_points.options(**opts)

    @param.depends("number_of_points")
    def view(self):
        filtered_df = self.eval_df.head(self.number_of_points)
        return self.create_map(filtered_df)
