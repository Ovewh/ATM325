import xarray as xr
import matplotlib.pyplot as plt
import cartopy as cr 
import cartopy as cr
import cartopy.crs as ccrs
import numpy as np
import pandas as pd

"""
Creates equal bins every 10 degree intervall
Then calculates mean and std 

Argument:
    xarray dataset OCO2

Returns:
    List -- latitude binned data XCO2 
    List -- latitude binned data XCO2 quality flags applied 
    Dataframe -- mean, standard diviation, N datapoints in each bin 

"""
def bin_Data(dset):
    lats = dset.latitude
    lons = dset.longitude
    biascorrXco2 =  dset.xco2
    xCO2q_flag = dset.xco2_quality_flag 
    qa_biascorrXco2 = biascorrXco2.where(xCO2q_flag==1)
    bin_bounds = np.arange(np.ceil(lats.min()/10)*10, np.ceil(lats.max()/10)*10, 10)
    biasCorrXCO2Bins, qa_biasCorrXco2Bins, qa_mean = [],[],[]
    nP, qa_nP = [],[]
    mean = []
    qa_std = []
    std = []
    df = pd.DataFrame()
    for i in range(1,len(bin_bounds)):
        sel =lats[(lats.values>= bin_bounds[i-1]) & (lats.values<= bin_bounds[i])]
        tempXco2 = biascorrXco2.loc[sel.sounding_id]
        tempQa_Xco2 = qa_biascorrXco2.loc[sel.sounding_id]
        biasCorrXCO2Bins.append(tempXco2)
        qa_biasCorrXco2Bins.append(tempQa_Xco2)
        mean.append(tempXco2.values.mean())

        qa_mean.append(tempQa_Xco2.values[~np.isnan(tempQa_Xco2.values)].mean())
        std.append(tempXco2.values.std())
        qa_std.append(tempQa_Xco2.values[~np.isnan(tempQa_Xco2.values)].std())
        nP.append(len(tempXco2))
        qa_nP.append(tempQa_Xco2.values[~np.isnan(tempQa_Xco2.values)].size)
        
        

    df['Xco2_mean'] = mean
    df['Xco2_std'] = std
    df['Xco2_nP'] = nP
    df['qa_Xco2_mean'] = qa_mean
    df['qa_Xco2_std'] = qa_std
    df['qa_Xco2_nP'] = qa_nP
    df.index = bin_bounds[1:]
    return biasCorrXCO2Bins, qa_biasCorrXco2Bins, df