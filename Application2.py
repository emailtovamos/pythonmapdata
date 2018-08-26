import folium
import pandas

df=pandas.read_csv("Volcanoes-USA.txt")
#Create Map object
map=folium.Map(location=[df['LAT'].mean(),df['LON'].mean()],zoom_start=6, tiles='Stamen Terrain')

def color(elev):
    minimum=int(min(df['ELEV']))
    step=int((max(df['ELEV'])-min(df['ELEV']) )/3.0)
    if elev in range(minimum, minimum+step ):
        col='green'
    elif elev in range(minimum+step,minimum+step*2):
        col='orange'
    else:
        col='red'
    return col

for lat, lon, name, elev in zip(df['LAT'], df['LON'], df['NAME'], df['ELEV']):
    #map.simple_marker(location=[lat,lon],popup=name,marker_color='green' if elev in range(0,1000) else 'orange' if elev in range(1000,3000) else 'red' )
    map.add_child(folium.Marker(location=[lat,lon],popup=name,icon=folium.Icon(color=color(elev), icon_color='green')))
    #folium.Marker() is the marker which has arguments

map.save(outfile="test.html")

#map.create_map(path='test.html')
