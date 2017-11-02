class STEPS:
    def __init__(self, location, obj):
        print("DIRECTIONS:")
        for each_location in range(len(location)-1):
            for i in range(len(obj['route']['legs'][each_location]['maneuvers'])):
                print(obj['route']['legs'][each_location]['maneuvers'][i]['narrative'])
        print()
        
class TOTALDISTANCE:
    def __init__(self, obj):
        print("TOTAL DISTANCE: ",round(obj['route']['distance']), 'miles')
        print()
        
class TOTALTIME:
    def __init__(self, obj):
        print("TOTAL TIME: ", round(obj['route']['time']/60), 'minutes')
        print()
        
class LATLONG:
    def __init__(self, obj, location):
        print("LATLONG:")
        for i in range(len(location)):
            lat = round(obj['route']['locations'][i]['latLng']['lat'],2)
            lng = round(obj['route']['locations'][i]['latLng']['lng'],2)
            if lat < 0:
                lat = -lat
                lat = str(lat)+"S"
            else:
                lat = str(lat)+"N"
            if lng < 0:
                lng = -lng
                lng = str(lng)+"W"
            else:
                lng = str(lng)+"E"
            print(lat, lng)
        print()
        
class ELEVATION:
    def __init__(self, elev_obj,location):
        print("ELEVATION:")
        for response in elev_obj:
            print(round(response['elevationProfile'][0]['height']*3.280839895))
        print()
