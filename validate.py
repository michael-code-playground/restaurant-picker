import googlemaps
from datetime import datetime
import os
def validate(user_spot):
    
    gmaps = googlemaps.Client(key=os.getenv('GOOGLE_MAPS_API'))

    # Geocoding an address
    place_result = gmaps.find_place(user_spot,'textquery', ['place_id', 'name', 'geometry'])


    #extract details to test the accuracy
    for place in place_result['candidates']:
        print(place)
    
    if place_result['candidates']:
        return "Thanks for the recommendation!"
    else:
        return "Place does not exist, don't lie to me."