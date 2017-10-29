# CarbonChain

*Objective*: Incentivize people in developing nations to preserve and expand carbon-sinking forests.

*Problem*: Currently there isn’t a way to transparently and safely transfer money to developing countries and guarantee that natural carbon sinks i.e. forests will be preserved. A number of the problems are listed below:
* How do I trust that the money is going to preserve a carbon-sinking forest?
* How do I trust that the landowners are actually preserving their forest?

The solution to this involves creating a level of trust and partnership between purchaser of the carbon credit and landowner who controls a forest. This is the role of CarbonChain.

## Usage

### Getting Satellite Imagery
1. Use [geojson](http://geojson.io/#id=gist:anonymous/1d0efe01df5e1135e151ebb930d1379e&map=12/-0.5622/30.9924) to find the location you want.
2. Take the coordinates, and replace them in `examples/demo_filters.py`
3. Run `python examples/search_endpoint.py | jq` to get a list of candidate images, use `id`
4. Activate the image you want by running `python activation.py 20160713_193337_1058018_RapidEye-3`
5. Download the image from the link provided by `activation.py`

### Getting ndvi of satellite imagery
1. Download image from PS. Make sure it's 4-band PlanetScope Scene
1. Unzip it and move the *_AnalyticMS.tif as well as *_metadata.xml.
1. Run `python extract_bands.py`. This will spit out an image locally with the NDVI color scheme. 

