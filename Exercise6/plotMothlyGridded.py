import xarray as xr
import matplotlib.pyplot as plt
import cartopy as cr
import cartopy.crs as ccrs
import matplotlib as mpl
from mpl_toolkits.axes_grid1 import make_axes_locatable
import numpy as np
import os

def plotMonthlyGridded(path, title_plot ,file_title=None, vmax=None):
    dset = xr.open_dataset(path)
    lons = dset.lon
    lats = dset.lat
    data = dset[list(dset.keys())[0]].transpose()
    plt.cla()
    fig = plt.figure(figsize=(10,8))
    
    ax = plt.axes(projection = ccrs.PlateCarree())
    ax.set_title(title_plot, fontsize = 16)
    if vmax == None:
        im = ax.pcolormesh(lons, lats, data, transform = ccrs.PlateCarree(), vmin = 0) 
    else:
        im = ax.pcolormesh(lons, lats, data, transform = ccrs.PlateCarree(), vmin = 0, vmax = vmax)
    gl = ax.gridlines(crs = ccrs.PlateCarree(), draw_labels = True, 
                        color = 'grey', alpha =0.6, linestyle = '--')
    gl.xlabels_top = False
    gl.ylabels_right = False
    ax.coastlines()
    cax = fig.add_axes([ax.get_position().x1+0.01,ax.get_position().y0,0.02,ax.get_position().height])
    plt.colorbar(im,cax=cax,label = data.units, extend='max')
    if file_title == None:
        return fig, ax
    
    else:
        plt.savefig(('figs/{}.png').format(file_title), dpi=300,bbox_inches='tight')
        return fig, ax
        

if __name__ == "__main__":
    direcOmi = 'data/OMI_NO2/'
    direcTropomi = 'data/TROPOMI_NO2/'
    months = ['January', 'February', 'March', 'April', 'May', 'June', 
                'July', 'August', 'September', 'October', 'November', 'December']
    # for month, ncfile in zip(months,os.listdir(direcOmi)):
    #     plotMonthlyGridded(direcOmi + ncfile, 'Time averaged monthly map of OMI troposheric NO2 {} 2019'.format(month) 
    #                     ,'OMI_2019_{}'.format(month), 27)
    
    for month, ncfile in zip(months,os.listdir(direcTropomi)):
        plotMonthlyGridded(direcTropomi + ncfile, 'Time averaged monthly map of TROPOMI troposheric NO2 {} 2019'.format(month) 
                        ,'TROPOMI_2019_{}'.format(month), 27)
    