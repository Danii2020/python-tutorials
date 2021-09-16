import requests
import urllib

api_url = "http://www.mapquestapi.com/directions/v2/route?"
key = "pmcCEtp7SwbG8Y2YGdyqUFDnb9pvtQ4F"


while True:
    origin = input("Ingresa el origen: ")
    if origin == 'q':
        break
    destination = input("Ingresa el destino: ")
    if destination == 'q':
        break    
    url = api_url + urllib.parse.urlencode({"key":key, "from":origin, "to":destination})
    json_data = requests.get(url).json()
    status_code = json_data["info"]["statuscode"]
    if status_code == 0:
        trip_duration = json_data["route"]["formattedTime"]
        distance = json_data["route"]["distance"] * 1.61
        fuel_used = json_data["route"]["fuelUsed"] * 3.79
        print("=================================================")
        print(f"Información del viaje desde {origin.capitalize()} hasta {destination.capitalize()}.")
        print(f"Duración del viaje: {trip_duration}.")
        print("Distancia: " + str("{:.2f}".format(distance) + " Km"))
        print("Combustible usado: " + str("{:.2f}".format(fuel_used) + " L"))
        print("=================================================")
        print("Indicaciones del viaje")

        for each in json_data["route"]["legs"][0]["maneuvers"]:
            distance_remaining = distance - each["distance"] * 1.61            
            print(each["narrative"] + " (" + str("{:.2f}".format(distance_remaining)) + " Km faltantes)")
            distance = distance_remaining

    