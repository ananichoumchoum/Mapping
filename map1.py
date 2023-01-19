import folium
import pandas

data1 = pandas.read_csv("Volcanoes.txt")
lat = list(data1["LAT"])
lon = list(data1["LON"])
elev = list(data1["ELEV"])
name = list(data1["NAME"])

data2 = pandas.read_csv("NPCanada.txt")
lati = list(data2["Lat"])
long = list(data2["Lon"])
names = list(data2["Name"])

data3 = pandas.read_csv("CanadaVolcanoes.txt")
lat2 = list(data3["Lati"])
lon2 = list(data3["Long"])
elev2 = list(data3["Elev"])
name2 = list(data3["Name"])

data4 = pandas.read_csv("USANP.txt")
lati2 = list(data4["Latitude"])
long2 = list(data4["Longitude"])
names2 = list(data4["Name"])

def color_code(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[39.11, -111.41],zoom_start=4, tiles="Stamen Terrain")
folium.TileLayer('openstreetmap').add_to(map)

fgv  = folium.FeatureGroup(name="Volcanoes Map")
fgnp  = folium.FeatureGroup(name="National Park Map")
fgp  = folium.FeatureGroup(name="Population Density Map")

for lt, ln, el, nm in zip(lat, lon, elev, name):
    fgv.add_child(folium.CircleMarker(location=[lt,ln], radius=6, popup=[nm,"Elevation:",str(el)+"m"], fill_color=color_code(el), fill=True, color='grey', fill_opacity=0.7))

for lt, ln, el, nm in zip(lat2, lon2, elev2, name2):
    fgv.add_child(folium.CircleMarker(location=[lt,ln], radius=6, popup=[nm,"Elevation:",str(el)+"m"], fill_color=color_code(el), fill=True, color='grey', fill_opacity=0.7))

for lt, ln, na in zip(lati, long, names):
    fgnp.add_child(folium.Marker(location=[lt,ln], popup=[na], icon=folium.Icon(color='blue')))

for lt, ln, na in zip(lati2, long2, names2):
    fgnp.add_child(folium.Marker(location=[lt,ln], popup=[na], icon=folium.Icon(color='blue')))

fgp.add_child(folium.GeoJson(data=open("world.json", encoding='utf-8-sig').read(),style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] <10000000
else 'yellow' if 10000000 <= x['properties']['POP2005'] < 50000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgnp)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")
