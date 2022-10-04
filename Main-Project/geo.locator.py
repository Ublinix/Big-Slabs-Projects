from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="geoapiExercises")

a = input("Enter the your Area Code : ") 
area_code = a

location = geolocator.geocode(area_code)

print("Your Area Code : ",area_code) 
print("Details about your Area Code : ") 
print(location) 


