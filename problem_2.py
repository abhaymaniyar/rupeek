import gpxpy
import pandas as pd
import gmplot

def read_file():
    xml_file = open('Problem.gpx', 'r')
    gpx = gpxpy.parse(xml_file)
    return gpx.tracks[0].segments[0].points

def plot_graph(map_file):
    data = read_file()
    min_lat = None
    max_lat = None
    min_lon = None
    max_lon = None

    ## Create empty map with zoom level 16

    df = pd.DataFrame(columns=['lon', 'lat', 'alt', 'time'])

    for point in data:
        df = df.append({'lon': point.longitude, 'lat' : point.latitude, 'alt' : point.elevation, 'time' : point.time}, ignore_index=True)
        
        
    min_lat, max_lat, min_lon, max_lon = \
    min(df['lat']), max(df['lat']), \
    min(df['lon']), max(df['lon'])

    mymap = gmplot.GoogleMapPlotter(
        min_lat + (max_lat - min_lat) / 2, 
        min_lon + (max_lon - min_lon) / 2, 
        16)

    mymap.plot(df['lat'], df['lon'], 'blue', edge_width=1)
    mymap.draw(map_file + ".html")


if __name__ == "__main__":
    map_file = input("Enter map file name : ")
    plot_graph(map_file)    