from geopy.geocoders import Nominatim
geoL = Nominatim()
location = geoL.geocode("382 Cavendish Dr Waterloo Ontario")
print(location)