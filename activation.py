import os
import requests
import sys
import time
import shutil
import datetime

item_id = sys.argv[1] # "20160713_193337_1058018_RapidEye-3"
item_type = "REOrthoTile"
asset_type = "visual"

# setup auth
session = requests.Session()
session.auth = (os.environ['PL_API_KEY'], '')

def download_file(url, dest):
    print "DOWNLOADING " + item_id
    local_filename = dest + item_id + "-" + datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S") + '.tif'
    r = requests.get(url, stream=True) 
    with open(local_filename, 'wb') as f:
        shutil.copyfileobj(r.raw, f)
        print "File saved to: " + local_filename

# request an item
item = \
        session.get(
                    ("https://api.planet.com/data/v1/item-types/" +
                            "{}/items/{}/assets/").format(item_type, item_id)
                )

# extract the activation url from the item for the desired asset
item_activation_url = item.json()[asset_type]["_links"]["activate"]
# request activation

for i in range (0,300):
    response = session.post(item_activation_url)

    if response.status_code == 204:
        print "ACTIVATED"
        item_download_url = item.json()[asset_type]["location"]
        download_file(item_download_url, './results/')
        break

    if response.status_code == 202:
        print "WAITING"
    time.sleep(1)

