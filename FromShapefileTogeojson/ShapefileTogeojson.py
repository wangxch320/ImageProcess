import shapefile
import codecs
from json import dumps


# read the shapefile
def shp2geo(file="line出产.shp"):
    reader = shapefile.Reader(file)
    fields = reader.fields[1:]
    field_names = [field[0] for field in fields]
    buffer = []
    for sr in reader.shapeRecords():
        record = sr.record
        record = [r.decode('gb2312', 'ignore') if isinstance(r, bytes)
                  else r for r in record]
        atr = dict(zip(field_names, record))
        geom = sr.shape.__geo_interface__
        buffer.append(dict(type="Feature", geometry=geom, properties=atr))

        # write the GeoJSON file

    geojson = codecs.open(file.split('.')[0] + "-geo.json", "w", encoding="gb2312")
    geojson.write(dumps({"type": "FeatureCollection", "features": buffer}, indent=2) + "\n")
    geojson.close()


if __name__ == '__main__':
    # import os
    # for z,x,c in os.walk('.'):
    #     for zz in c:
    #         if zz.endswith(".shp"):
    #             shp2geo(zz)

    # shp2geo(file='D.shp')
    shp2geo(file='tttttt.shp')
