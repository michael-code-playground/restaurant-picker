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
    
        latitude = place['geometry']['location']['lat']
        longtitude = place['geometry']['location']['lng']
        
    
    
    if place_result['candidates']:
        if int(latitude) != 38 or int(longtitude) != -9:
            return  "Google says such a place exists, but either can't be found or it may not be Lisbon"
        
        return "Thanks for the recommendation!"
    else:
        return "Place does not exist, don't lie to me."