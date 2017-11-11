# based on https://www.planet.com/docs/guides/quickstart-ndvi/
import time
import rasterio
import numpy
from xml.dom import minidom
import matplotlib.pyplot as plt

def calculate_vegetation(strategy, image_file, xml_file):
    xmldoc = minidom.parse(xml_file)
    nodes = xmldoc.getElementsByTagName("ps:bandSpecificMetadata")
    # XML parser refers to bands by numbers 1-4
    coeffs = {}
    for node in nodes:
        bn = node.getElementsByTagName("ps:bandNumber")[0].firstChild.data
        if bn in ['1', '2', '3', '4']:
            i = int(bn)
            value = node.getElementsByTagName("ps:reflectanceCoefficient")[0].firstChild.data
            coeffs[i] = float(value)
    
    if strategy == "evi":
        with rasterio.open(image_file) as src: 
            band_blue = src.read(1) * coeffs[1]
            print("SUCCESSFULLY EXTRACTED BLUE")
    
    # Load red and NIR bands - note all PlanetScope 4-band images have band order BGRN
    with rasterio.open(image_file) as src:
        band_red = src.read(3) * coeffs[3]
        print("SUCCESSFULLY EXTRACTED RED")
    
    with rasterio.open(image_file) as src:
        band_nir = src.read(4) * coeffs[4]
        print("SUCCESSFULLY EXTRACTED NIR")

    # Allow division by zero
    numpy.seterr(divide='ignore', invalid='ignore')
     
    # Calculate NDVI
    if strategy == "ndvi":
        vegetation = (band_nir.astype(float) - band_red.astype(float)) / (band_nir + band_red)
    # Calculate evi (https://gis.stackexchange.com/questions/30439/envi-vegetation-index-calculator)
    elif strategy == "evi":
        vegetation = 2.5 * ((band_nir.astype(float) - band_red.astype(float)) / ( band_nir.astype(float) + 6 *  band_red.astype(float) - 7.5 * band_blue.astype(float) + 1 ))
    
    print("SUCCESSFUL CALCULATION: " + strategy)
    # Set spatial characteristics of the output object to mirror the input
    kwargs = src.meta 
    kwargs.update(
        dtype=rasterio.float32,
        count = 1
    )
    
    timestr = time.strftime("%Y%m%d-%H%M%S-")
    # Create the file
    with rasterio.open(timestr + 'vegetation.tif', 'w', **kwargs) as dst:
        dst.write_band(1, vegetation.astype(rasterio.float32))

    # Select color pallatte:http://matplotlib.org/examples/color/colormaps_reference.html
    plt.imsave(timestr+"vegetation-cmap.png", vegetation, cmap=plt.cm.binary)
    print("SUCCESSFULLY SAVED FILES")

def main():
    image_file = "./farm_jul/analytic.tif"
    xml_file ="./farm_jul/metadata.xml"
    
    calculate_vegetation("evi", image_file, xml_file)

if __name__ == "__main__":
    main()
