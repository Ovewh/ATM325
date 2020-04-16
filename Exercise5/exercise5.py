import xarray as xr
import matplotlib.pyplot as plt
import datetime as dt
import pandas as pd
import numpy as np
import h5py
#from IPython import embed
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()



def read_TCCCON_data(error_margin=10):
    dset = xr.open_dataset('ci20120920_20191202.public.nc', decode_times=False)
    timeInSec = dset.time.values*24*60*60
    time = pd.to_datetime(timeInSec,yearfirst=True, unit='s')
    dset = dset.assign_coords({"time" :time})
    df = dset.xco2_ppm.to_dataframe()
    df['xco2_ppm_error'] = dset.xco2_ppm_error.to_dataframe()
    df['xch4_ppm'] = dset.xch4_ppm.to_dataframe()*1000
    df['xch4_ppm_error'] = dset.xch4_ppm_error.to_dataframe()
    
    df['xco2_ppm'] = df['xco2_ppm'].loc[df.xco2_ppm_error < error_margin]
    df['xch4_ppm'] = df['xch4_ppm'].loc[df.xch4_ppm_error < error_margin]
    df = df.dropna().resample('D').mean()

    return df, dset.long_deg.values[0], dset.lat_deg.values[0]

def readGOSat(fileName, lon0,lat0, extentLat = 5, 
                    extentLon = 10, out_file=None):

    f = h5py.File(fileName,'r')
    keys = list(f.keys())
    time = f['time']
    dfGO = pd.DataFrame(time)
    dfGO['time'] = dfGO[0]
    dfGO = dfGO.drop(0, axis=1)
    dfGO['lat'] = f['lat'][:]
    dfGO['lon'] = f['lon'][:]
    dfGO['sounding_id'] = f['sounding_id']
    
    dfGO[keys[4]] = f[keys[4]]
    dfGO[keys[5]] = f[keys[5]]
    latLow = lat0 - extentLat
    latTop = lat0 + extentLat
    lonLow = lon0 - extentLon
    lonTop = lon0 + extentLon   
    lonSel = (dfGO.lon <= lonTop) & (dfGO.lon >= lonLow)
    latSel = (dfGO.lat <= latTop) & (dfGO.lat >= latLow)
    dfGO = dfGO.loc[(lonSel )& (latSel )]
    dfGO = dfGO.drop(['lat', 'lon', 'sounding_id'], axis=1)
    dfGO = dfGO.dropna()   
    timelist = dfGO.time.to_list()
    time_arr = []
    for i in range(len(timelist)):
        time_arr.append(pd.to_datetime(str(timelist[i])[2:-1], format='%Y-%m-%d %H:%M:%S'))
    dfGO.index = time_arr
    dfGO = dfGO.drop('time', axis =1)
    if out_file != None:
        dfGO.to_csv('data/'+ out_file)
    
    return dfGO

if __name__ == "__main__":
    print('Reading TCCON data')
    df, lon0, lat0 = read_TCCCON_data()
    df.to_csv('data/TCCCON_daily_avg.csv')
    print('Reading XCH4 large region...')
    #Save XCH4 large region
    df = readGOSat('GOSAT_NIES_XCH4_v02.75.h5', lon0, lat0, 
                    out_file='XCH4_large_region.csv')

    #Save XCH4 small region
    print('Reading XCH4 small region...')
    df = readGOSat('GOSAT_NIES_XCH4_v02.75.h5', lon0, lat0,
                    extentLon=5, extentLat=2.5, 
                    out_file='XCH4_small_region.csv')

    #Save XCO2 large region 
    print('Reading XCO2 large region...')
    df = readGOSat('GOSAT_NIES_XCO2_v02.75.h5', lon0, lat0, 
                    out_file='XCO2_large_region.csv')
    #Save XCO2 small region
    print('Reading XCO2 small region...')
    df = readGOSat('GOSAT_NIES_XCO2_v02.75.h5', lon0, lat0,
                    extentLon=5, extentLat=2.5, 
                    out_file='XCO2_small_region.csv')
    