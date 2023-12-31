import sys
import subprocess
from osgeo import gdal,ogr,osr

def GetExtent(gt,cols,rows):
    ''' Return list of corner coordinates from a geotransform
    '''
    ext=[]
    xarr=[0,cols]
    yarr=[0,rows]

    for px in xarr:
        for py in yarr:
            x=gt[0]+(px*gt[1])+(py*gt[2])
            y=gt[3]+(px*gt[4])+(py*gt[5])
            ext.append([x,y])
        yarr.reverse()
    return ext

def ReprojectCoords(coords,src_srs,tgt_srs):
    ''' Reproject a list of x,y coordinates.
    '''
    trans_coords=[]
    transform = osr.CoordinateTransformation( src_srs, tgt_srs)
    for x,y in coords:
        print(type(x))
        print(type(y))
        x,y,z = transform.TransformPoint(x,y,0)
        trans_coords.append([x,y])
    return trans_coords

def AutoGdalTranslate(geo_extent,cols,rows,raster):
    gdal_translate="gdal_translate -of VRT -a_srs EPSG:4326 -gcp 0 0 " + str(geo_extent[0][0]) + " " + str(geo_extent[0][1]) + " -gcp " + str(cols) + " 0 " + str(geo_extent[3][0]) + " " + str(geo_extent[3][1]) + " -gcp " + str(cols) + " " + str(rows) + " " + str(geo_extent[2][0]) + " " + str(geo_extent[2][1]) + " " + raster + " " + raster[:-4] + ".vrt"
    subprocess.Popen(gdal_translate)
def AutoGdal2Tiles(raster):
    gdal2tiles="python C:\Python27\Lib\site-packages\osgeo\scripts\gdal2tiles1bto4b.py -p mercator -a 0,0,0 " + raster[:-4] + ".vrt"
    subprocess.Popen(gdal2tiles)

raster=sys.argv[1]
print(raster)
ds=gdal.Open(raster)

gt=ds.GetGeoTransform()
cols = ds.RasterXSize
rows = ds.RasterYSize
extent=GetExtent(gt,cols,rows)

src_srs=osr.SpatialReference()
src_srs.ImportFromWkt(ds.GetProjection())
#tgt_srs=osr.SpatialReference()
#tgt_srs.ImportFromEPSG(4326)
tgt_srs = src_srs.CloneGeogCS()

geo_extent=ReprojectCoords(extent,src_srs,tgt_srs)

AutoGdalTranslate(geo_extent,cols,rows,raster)
AutoGdal2Tiles(raster)