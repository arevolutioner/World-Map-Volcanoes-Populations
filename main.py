
import folium
import pandas
data_frame = pandas.read_csv("volcano.csv")

lat = list(data_frame["Latitude"])
lon = list(data_frame["Longitude"])
names = list(data_frame["V_Name"])
active = list(data_frame["H_active"])


def color_producer(activity):
    if activity == 1:
        return "red"
    else:
        return "green"


map_1 = folium.Map(location=[41.489042, 24.848290])

fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, nm, act in zip(lat, lon, names, active):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=8, popup=(nm, str(act)),
                                     fill_color=color_producer(act), color="grey", fill_opacity=0.8))

fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf - 8 sig").read(),
                            style_function=lambda x:
                            {"fillColor": "green" if x["properties"]["POP2005"] < 10000000
                             else "orange" if 10000000 <= x["properties"]["POP2005"] <= 20000000 else "red"}))


map_1.add_child(fgv)
map_1.add_child(fgp)
map_1.add_child(folium.LayerControl())

map_1.save("map_1.html")


