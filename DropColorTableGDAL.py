import gdal
import os, glob

in_directory = r''
files_to_process = glob.glob(os.path.join(in_directory, '*.tif'))

for file in files_to_process:
    fullpath = os.path.join(files_to_process, file)
    ds = gdal.Open(fullpath, gdal.GA_Update)
    band = ds.GetRasterBand(1)
    band.SetColorTable(None)
    ds = None
