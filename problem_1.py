import gpxpy
import matplotlib.pyplot as plt
import datetime
from geopy import distance
from math import sqrt, floor
import numpy as np
import pandas as pd 
import gmplot

def read_file():
    xml_file = open('Problem.gpx', 'r')
    gpx = gpxpy.parse(xml_file)
    return gpx.tracks[0].segments[0].points


def get_insights():
    data = read_file()
    alt_dif = [0]
    time_dif = [0]
    dist_vin = [0]
    dist_hav = [0]
    dist_no_alt = [0]
    dist_hav_no_alt = [0]
    dist_dif_hav_2d = [0]
    dist_dif_2d = [0]
    moving_time = 0
    max_speed = -1

    for index in range(len(data)):
        if index == 0:
            pass
        else:
            start = data[index-1]        
            stop = data[index]        
            distance_2d = distance.vincenty((start.latitude, start.longitude), (stop.latitude, stop.longitude)).m
            dist_dif_2d.append(distance_2d)                
            dist_no_alt.append(dist_no_alt[-1] + distance_2d)        
            alt_d = start.elevation - stop.elevation        
            alt_dif.append(alt_d)        
            time_delta = (stop.time - start.time).total_seconds()        
            time_dif.append(time_delta)

            if distance_2d != 0:
                moving_time += time_delta

            speed = distance_2d / moving_time
            if speed > max_speed:
                max_speed = speed
            
    print('Total distance : ', dist_no_alt[-1], 'm')
    print('altitute       : ', alt_dif[-1])
    print('moving time    : ', moving_time, 's')
    print('average speed  : ', dist_dif_2d[-1] / moving_time, 'm/s')
    print('max speed      : ', max_speed, 'm/s')
    print('Total Time     : ', floor(sum(time_dif)/60),' min ', int(sum(time_dif)%60),' sec ')



if __name__ == "__main__":
    get_insights()
