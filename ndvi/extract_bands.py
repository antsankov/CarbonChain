# based on https://www.planet.com/docs/guides/quickstart-ndvi/

import datetime
import rasterio
import numpy
from xml.dom import minidom
import matplotlib.pyplot as plt

image_file = "./farm1/analytic.tif"
xml_file ="./farm1/metadata.xml"

xmldoc = minidom.parse(xml_file)
nodes = xmldoc.getElementsByTagName("ps:bandSpecificMetadata")
print nodes
# XML parser refers to bands by numbers 1-4
coeffs = {}
for node in nodes:
    bn = node.getElementsByTagName("ps:bandNumber")[0].firstChild.data
    print bn
    if bn in ['1', '2', '3', '4']:
        i = int(bn)
        value = node.getElementsByTagName("ps:reflectanceCoefficient")[0].firstChild.data
        coeffs[i] = float(value)

# Load red and NIR bands - note all PlanetScope 4-band images have band order BGRN
with rasterio.open(image_file) as src:
    band_red = src.read(3)

with rasterio.open(image_file) as src:
    band_nir = src.read(4)

band_red = band_red * coeffs[3]
band_nir = band_nir * coeffs[4]

# Allow division by zero
numpy.seterr(divide='ignore', invalid='ignore')

# Calculate NDVI
ndvi = (band_nir.astype(float) - band_red.astype(float)) / (band_nir + band_red)

# Set spatial characteristics of the output object to mirror the input
kwargs = src.meta
kwargs.update(
    dtype=rasterio.float32,
    count = 1
)

# Create the file
with rasterio.open('ndvi.tif', 'w', **kwargs) as dst:
    dst.write_band(1, ndvi.astype(rasterio.float32))

# Select color pallatte:http://matplotlib.org/examples/color/colormaps_reference.html
plt.imsave("ndvi_cmap.png", ndvi, cmap=plt.cm.gist_heat)
