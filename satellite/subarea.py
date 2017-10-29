from osgeo import gdal
from requests.auth import HTTPBasicAuth
import os
import requests

item_id = "20161109_173041_0e0e"
item_type = "PSScene3Band"
asset_type = "visual"
item_url = 'https://api.planet.com/data/v1/item-types/{}/items/{}/assets'.format(item_type, item_id)

# Request a new download URL
result = requests.get(item_url, auth=HTTPBasicAuth(os.environ['PLANET_API_KEY'], ''))
download_url = result.json()[asset_type]['location']
