#! /usr/bin/python

from bs4 import BeautifulSoup
from urllib2 import urlopen
import re
import nltk


''' this code base is for mapping a collection of lat-lon points onto a map 
using the google maps api V3. 
to use it in offline mode, you need to cache-manifest, look here
http://stackoverflow.com/questions/6294782/using-google-maps-v3-offline-e-g-with-cache-manifest
on how to do it'''



def kmz_to_tagged_xml(location):
    """
    unpack kmz file
    """
    # xml = open("doc.kml").read()
    # soup = BeautifulSoup(xml,'lxml')
    xml_line = open("doc.kml").readlines()
    pass


def find_tags(xml_line):
#   """ find the tag"""
#   name = soup.findAll('name')
#   loc = soup.findAll('coordinates')
    # don't use soup, it only retrieves 20 out of 131 tags. 
    lines = []
    names ={}
    names_no_hood = {}
    names_no_cord = {}

    group_event = False
    coords_event = False
    
    for cnt, line in enumerate(xml_line):
        tempname = None
        tempcord = None
        if '<Placemark>' in line:
            group_event = True
            print cnt+1, 'Placemark live'
        
        if group_event and '<name>' in line:
            tempname =line[line.find('>'):line.find('</')]
            print cnt+1, 'name live'
        
        if group_event and '<coordinates>' in line:
            coords_event = True
            continue

        if '-' in line and coords_event and group_event:
            tempcord = parse_coords(line, num = cnt+1)  
            print cnt+1, 'coordinates live'

        if group_event and '</coordinates>' in line:
            coords_event = False    

        if '</Placemark>' in line:
            group_event = False

        if tempname and tempcord:
            names[tempname] = tempcord
        
        if tempname and not tempcord:
            names_no_hood[tempname] = 'missing'

        if tempcord and not tempname:
            ll = "line_%s"%(cnt+1)
            names_no_cord[ll] = 'missing'    



    return names, names_no_cord, names_no_hood    

    # trim names that don't have a coordinate

def parse_coords(loc, append = False, num=0, google_maps = False):

    tmp = str(loc).split('\t')  
    get_latlon = [LL for LL in tmp if len(LL)>20]
    print "latlon is", type(get_latlon)
    print "latlon[0] is", type(get_latlon[0])
    locs_tmp = get_latlon[0].split(',')
    # except IndexError:
    #     print num, locs_tmp

    # lon = [item.replace('0 ','') for item in locs_tmp[0:-1:2]]
    lon = [item.replace('0 ','') for item in locs_tmp[0:-1:2]]
    lat = locs_tmp[1::2]
    locs = zip(lat, lon)
    # names are returned twice, thanks beautifulsoup
    if google_maps:
        for item in locs:
            print "new google.maps.LatLng"+str(item)+','
        
    
    return locs
    # 
def parse_names(name):
    names = [str(item) for item in name]
    names = [names[l][names[l].find('>')+1:names[l].find('<', 3)] for l,i in enumerate(names)]

    return names


def make_name_latlon_dict(loc, names):
    hoods ={}

    for cnt, name in enumerate(names):
        latlon = parse_coords(loc[cnt])
        print "now parsinf%s"%name 
        hoods[name] = parse_coords(loc[cnt])

    return hoods


def rearange_latlons(loc, name):

    pairs = {}


    
        





