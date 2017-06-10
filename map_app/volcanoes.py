import pandas, folium

_map = folium.Map(location=[40.780281, -73.962950], zoom_start=2)
feature_group = folium.FeatureGroup(name="Volcanoes")

volcanoes = pandas.read_csv('volcanoes.txt')[0:21] # get first n only

def get_marker_color_by_elevation(el):
    if (el <= 1000):
        color = 'green'
    elif (el <= 3000):
        color = 'orange'
    else:
        color = 'red'

    return color

lat = list(volcanoes['Latitude'])
lon = list(volcanoes['Longitude'])
elevation = list(volcanoes['Elevation'])

for lt, ln, el in zip(lat, lon, elevation):
    popup_text = 'Elevation: ' + str(el) + ' m'

    feature_group.add_child(
        folium.CircleMarker(
            location=[lt, ln],
            radius=5,
            popup=popup_text,
            fill_color=get_marker_color_by_elevation(el),
            color='black'
        )
    )

feature_group.add_child(
    folium.GeoJson(
        data=open('world.json', 'r', encoding="utf-8-sig"),
        style_function=lambda item: {
                'fillColor':
                    'green' if item['properties']['POP2005'] < 10000000
                    else 'orange' if item['properties']['POP2005'] < 20000000
                    else 'red'
            }
    )
)

_map.add_child(feature_group)
_map.save('volcanoes.html')
