#importing package - make sure auth token is correctly adjusted on github and in config file 
from geojsonio import display


#from the package, open Nashville District data 
# found here: https://data.nashville.gov/General-Government/Council-Districts-Map-/mfy7-e5qx

with open('nashville.geojson') as f:
    contents = f.read()
    display(contents)
