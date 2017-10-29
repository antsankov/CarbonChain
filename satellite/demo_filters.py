import json
import sys

def gather_aoi(geojson_loc):
    with open(geojson_loc) as data_file:    
        data = json.load(data_file)
        # print data
        geo_json_geometry = data["features"][0]["geometry"] 
    """
    # the geo json geometry object we got from geojson.io
    geo_json_geometry = {
      "type": "Polygon",
      "coordinates": [
        [
            [
                -121.89640045166016,
                37.32667630606142
                                                        
            ],
            [
                -121.88685178756714,
                37.32667630606142
                                                        
            ],
            [
                -121.88685178756714,
                37.33196563536119
                                                        
            ],
            [
                -121.89640045166016,
                37.33196563536119
                                                        
            ],
            [
                -121.89640045166016,
                37.32667630606142                                        
            ]
        ]
      ]
    }
    """
# filter for items the overlap with our chosen geometry
    geometry_filter = {
      "type": "GeometryFilter",
      "field_name": "geometry",
      "config": geo_json_geometry
    }

# filter images acquired in a certain date range
    date_range_filter = {
      "type": "DateRangeFilter",
      "field_name": "acquired",
      "config": {
        "gte": "2017-10-01T00:00:00.000Z",
        "lte": "2017-10-21T00:00:00.000Z"
      }
    }

# filter any images which are more than 50% clouds
    cloud_cover_filter = {
      "type": "RangeFilter",
      "field_name": "cloud_cover",
      "config": {
        "lte": 0.5
      }
    }

# create a filter that combines our geo and date filters
# could also use an "OrFilter"
    aoi = {
      "type": "AndFilter",
      "config": [geometry_filter, date_range_filter, cloud_cover_filter]
    }

    return aoi
