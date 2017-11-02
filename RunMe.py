#Author: Dustin Ngo
#Date: 5/15/2015

from API_Interaction import build_search_url,search_http_action, parsing_json, build_elevation_url, elevation_http_action
from output import STEPS, TOTALDISTANCE, TOTALTIME, LATLONG, ELEVATION


def user_input() -> list:
    '''Gets all the user inputs which includes location and the order of the put the user
    would want to output. Then would put the location and output order in list to later
    determine what order of location and output the user wants.'''
    print("Welcome to this program that will allow you type in 2+ addresses and get various information back using MapQuest's API.")
    location = []
    output_order = []
    print("Please format address in as shown: XXXX Example Drive, Los Angeles, CA.")
    number_of_locations = int(input("Input the number of adresses you would like to search up: "))
    for i in range(number_of_locations):
        address = input("Address: ")
        location.append(address)
    print("The possible type of information you can receive are: STEPS, TOTALDISTANCE, TOTALTIME, LATLONG, and ELEVATION. ")
    types_of_input = int(input("Out of these 5, how many types of information would you like to know about? "))
    for i in range(types_of_input):
        output = input("Type: ")
        output_order.append(output)
    return location, output_order

def print_output_order(location: list, output_order: list, obj: object, elev_obj: object) -> None:
    '''Here we use the output_order list to scan through the list in order to figure out the order
    and then uses classes in order to print out the desired output in the desired order.'''
    for output_type in output_order:
        if output_type == 'STEPS':
            STEPS(location, obj)
        elif output_type == 'TOTALDISTANCE':
            TOTALDISTANCE(obj)
        elif output_type == 'TOTALTIME':
            TOTALTIME(obj)
        elif output_type == 'LATLONG':
            LATLONG(obj, location)
        elif output_type == 'ELEVATION':
            ELEVATION(elev_obj,location)
        else:
            return MAPQUEST_ERROR
    
def main() -> None:
    '''Main Function'''
    try:
        information = user_input()
        location = information[0]
        output_order = information[1]

        search_url = build_search_url(location)
        search_response = search_http_action(search_url)
        obj = parsing_json(search_response)
            
        elevation_urls = build_elevation_url(location, obj)
        elev_obj = elevation_http_action(elevation_urls)
        print_output_order(location,output_order, obj, elev_obj)
    except KeyError:
        print("NO ROUTE FOUND")
    except IndexError:
        print("NO ROUTE FOUND")
    except:
        print("MAPQUEST ERROR")
    finally:
            print("Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors.")
            input("Program Done. Please press any key to exit...")
if __name__ == "__main__":
    main()
    
    

