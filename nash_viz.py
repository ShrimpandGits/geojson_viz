from geojsonio import display

with open('open_it.geojson') as f:
    contents = f.read()
    display(contents)
