#API Interaction

import http.client
import urllib.request
import urllib.error

import json
import urllib.parse


APP_KEY = 'Fmjtd%7Cluu82q01l9%2Can%3Do5-94ya0f'
BASE_MAPQUEST_URL = 'http://open.mapquestapi.com/directions/v2/route?key='
BASE_ELEVATION_URL = 'http://open.mapquestapi.com/elevation/v1/profile?key='



def build_search_url(location: list) -> str:
    '''Builds the search url through the information of the user inputs. Sets the first
    as from and the ones after that to locations. Then it parse the url together with
    base url, app key, and query parameters. Returns a single string'''
    query_parameters = []
    for i in range(len(location)):
        if i == 0:
            query_parameters.append(('from', location[i] + ')'))
        if i > 0:
            query_parameters.append(('to', location[i] + ')'))
    search_url = BASE_MAPQUEST_URL + APP_KEY + '&' + urllib.parse.urlencode(query_parameters)
    return search_url

def search_http_action(url: str) -> str:
    '''Opens the url and reads it and then converts from bytes to strings. Closes the file
    afterwards and then returns the url data in str type.'''
    http_response = urllib.request.urlopen(url)
    data = http_response.read()
    string_data = data.decode(encoding = 'utf-8')
    http_response.close()
    return string_data

def parsing_json(search_response: str) -> object:
    '''Parses the url data and returns an object'''
    x = search_response
    obj = json.loads(x)        
    return obj

def build_elevation_url(location: list,obj: object) -> list:
    '''Builds a url made just for Mapquest Open Elevation API. Creates a url for each location
    and appends it into a single list. Returns a single list.'''
    each_elevation_url = []
    for i in range(len(location)):
        z = ''
        x = str(obj['route']['locations'][i]['latLng']['lat'])
        y = str(obj['route']['locations'][i]['latLng']['lng'])
        z = (x + ',' + y)
        elevation_parameters = [('latLngCollection', z)]
        elevation_url = BASE_ELEVATION_URL + APP_KEY + '&' + urllib.parse.urlencode(elevation_parameters)
        each_elevation_url.append(elevation_url)
    return each_elevation_url

def elevation_http_action(elevation_urls: list) -> list:
    '''Get the list of urls from each location and then opens it, reads it, decode it into str
    types, and parses it. Returns the converted list'''
    http_responses = []
    for each_url in elevation_urls:
        response = urllib.request.urlopen(each_url)
        data = response.read()
        string_data = data.decode(encoding = 'utf-8')
        response.close()
        elev_obj = json.loads(string_data)
        http_responses.append(elev_obj)
    return http_responses
        

