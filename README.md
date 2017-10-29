# CarbonChain

*Objective*: Incentivize people in developing nations to preserve and expand carbon-sinking forests.

*Problem*: Currently there isn’t a way to transparently and safely transfer money to developing countries and guarantee that natural carbon sinks i.e. forests will be preserved. A number of the problems are listed below:
* How do I trust that the money is going to preserve a carbon-sinking forest?
* How do I trust that the landowners are actually preserving their forest?

The solution to this involves creating a level of trust and partnership between purchaser of the carbon credit and landowner who controls a forest. This is the role of CarbonChain.

## Usage

### Getting Satellite Imagery
1. Use [geojson](http://geojson.io/#id=gist:anonymous/1d0efe01df5e1135e151ebb930d1379e&map=12/-0.5622/30.9924) to find the location you want.
1. Run `python satellite/search_endpoint.py areas/san_jose_new.json | jq` to get a list of candidate images, based on a geojson file. Use id to download it with the activator.
1. Activate and download the image you want by running `python activation.py 20160713_193337_1058018_RapidEye-3`, it saves to the `results/` directory.

### Getting ndvi of satellite imagery
Normalized Difference Vegetation Index (NDVI) is used to assess whether an area contains live green vegetation or not. It can show the difference between water and plants, bare soil and grass, whether plants are under stress, and what lifecycle stage a crop is in.

It compares how much more near-infrared light is reflected by chlorophyll vs visible red light

1. Download image from PS. Make sure it's 4-band PlanetScope Scene
1. Unzip it and move the `..._AnalyticMS.tif` as well as `..._metadata.xml`.
1. Run `python extract_bands.py` with the right xml and image file selected. This will spit out an image locally with the NDVI color scheme. 
