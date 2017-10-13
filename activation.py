import os
import requests
import sys

item_id = sys.argv[1] # "20160713_193337_1058018_RapidEye-3"
item_type = "REOrthoTile"
asset_type = "visual"

# setup auth
session = requests.Session()
session.auth = (os.environ['PL_API_KEY'], '')

# request an item
item = \
        session.get(
                    ("https://api.planet.com/data/v1/item-types/" +
                            "{}/items/{}/assets/").format(item_type, item_id)
                )

# extract the activation url from the item for the desired asset
item_activation_url = item.json()[asset_type]["_links"]["activate"]
item_download_url = item.json()[asset_type]["location"]
# request activation

response = session.post(item_activation_url)
print response.status_code

print item_download_url
