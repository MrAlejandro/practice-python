import folium

_map = folium.Map(location=[40.780281, -73.962950], zoom_start=13)

feature_group = folium.FeatureGroup(name="NYC")

feature_group.add_child(
    folium.Marker(
        location=(40.781340, -73.967373),
        popup='New York, Central Park )))',
        icon=folium.Icon(color='green')
    )
)

_map.add_child(feature_group)
_map.save('map.html')
