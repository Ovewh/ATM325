import matplotlib.pyplot as plt
import numpy as np
import xarray as xr
import pandas as pd
import datetime as dt
import statsmodels.formula.api as smf
from statsmodels.regression.linear_model import OLS
import cartopy.feature as cfeature
import cartopy as cr
import cartopy.crs as ccrs
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER

def plot():
    fig = plt.figure(figsize=(14,16))
    gs = fig.add_gridspec(3,3)
    img_extent = (25.7871, 33.5742,70.9805, 79.6816)

    imgs_AOD = ['MODIS_N_India_AOD31-10-2019.png','MODIS_N_India_AOD04-11-2019.png',
                    'MODIS_N_India_AOD05-11-2019.png']
    imgs_AI = ['OMPS_N_India_AI31-10-2019.png', 'OMPS_N_India_AI04-11-2019.png', 
                'OMPS_N_India_AI05-11-2019.png']
    imgs_FA = ['MODIS_N_India_FA31-10-2019.png','MODIS_N_India_FA04-11-2019.png', 
            'MODIS_N_India_FA05-11-2019.png']

    pos_grid = 0
    axes = []

    for imgfile in imgs_FA:
        axes.append(fig.add_subplot(gs[pos_grid], projection=ccrs.PlateCarree()))
        img = plt.imread(imgfile)
        axes[-1].imshow(img, origin ='upper', extent = img_extent, 
                        transform =ccrs.PlateCarree())
        gl = axes[-1].gridlines(crs=ccrs.PlateCarree(), draw_labels=True, alpha=0.5, 
                                linestyle='--', linewidth = 1.2,
                            color = 'black')

        if pos_grid == 0:

            gl.xlabels_bottom = False
            gl.ylabels_right = False
            gl.xlabels_top = False
            gl.xformatter = LONGITUDE_FORMATTER
            gl.yformatter = LATITUDE_FORMATTER
        elif pos_grid == 1:
            
            gl.xlabels_top = False
            gl.xlabels_bottom = False
            gl.ylabels_right = False
            gl.ylabels_left = False
            gl.xformatter = LONGITUDE_FORMATTER
            gl.yformatter = LATITUDE_FORMATTER
        else:
            gl.xlabels_top = False
            gl.xlabels_bottom = False
            gl.ylabels_left = False
            gl.xformatter = LONGITUDE_FORMATTER
            gl.yformatter = LATITUDE_FORMATTER
        
        pos_grid += 1
    for imgfile in imgs_AOD:
        
        axes.append(fig.add_subplot(gs[pos_grid], projection=ccrs.PlateCarree()))
        img = plt.imread(imgfile)
        axes[-1].imshow(img, origin ='upper', extent = img_extent, 
                        transform =ccrs.PlateCarree())
        gl = axes[-1].gridlines(crs=ccrs.PlateCarree(), draw_labels=True, 
                                alpha=0.5, linestyle='--',color = 'black', linewidth = 1.2)
        if pos_grid == 4:

            gl.xlabels_bottom = False
            gl.ylabels_right = False
            gl.xlabels_top = False
            gl.ylabels_left = False
            gl.xformatter = LONGITUDE_FORMATTER
            gl.yformatter = LATITUDE_FORMATTER
        elif pos_grid == 5:
            gl.xlabels_top = False
            gl.xlabels_bottom = False
    #         gl.ylabels_right = False
            gl.ylabels_left = False
            gl.xlabels_bottom = False
            gl.xformatter = LONGITUDE_FORMATTER
            gl.yformatter = LATITUDE_FORMATTER
        else:
            gl.xlabels_top = False
            gl.xlabels_bottom = False
            gl.ylabels_right = False
            gl.xformatter = LONGITUDE_FORMATTER
            gl.yformatter = LATITUDE_FORMATTER
        
        pos_grid += 1
    for imgfile in imgs_AI:
        axes.append(fig.add_subplot(gs[pos_grid], projection=ccrs.PlateCarree()))
        img = plt.imread(imgfile)
        
        axes[-1].imshow(img, origin ='upper', extent = img_extent, 
                        transform =ccrs.PlateCarree())

        gl = axes[-1].gridlines(crs=ccrs.PlateCarree(), draw_labels=True, alpha=0.5, 
                                linestyle='--',color = 'black', linewidth = 1.2)

        if pos_grid == 6:
            gl.xlabels_top = False
            gl.ylabels_right = False        
            gl.xformatter = LONGITUDE_FORMATTER
            gl.yformatter = LATITUDE_FORMATTER
        elif pos_grid == 7:
            gl.xlabels_top = False
            gl.ylabels_right = False
            gl.ylabels_left = False
            gl.xformatter = LONGITUDE_FORMATTER
            gl.yformatter = LATITUDE_FORMATTER
        else:
            gl.xlabels_top = False
            gl.ylabels_left = False

            gl.xformatter = LONGITUDE_FORMATTER
            gl.yformatter = LATITUDE_FORMATTER
        pos_grid += 1


    axes[0].set_title('31.10.2019 - 08:10 UTC')
    axes[1].set_title('04.11.2019 - 08:10 UTC')
    axes[2].set_title('05.11.2019 - 08:10 UTC')
    axes[3].set_title('AOD MODIS Aqua')
    axes[4].set_title('AOD MODIS Aqua')
    axes[5].set_title('AOD MODIS Aqua')
    axes[6].set_title('AI OMPS')
    axes[7].set_title('AI OMPS')
    axes[8].set_title('AI OMPS')
    plt.savefig('firesInIndia.pdf',pad_inches=0.01)