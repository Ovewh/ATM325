import xarray as xr
import matplotlib.pyplot as plt
import cartopy as cr
import cartopy.crs as ccrs
import matplotlib as mpl
from mpl_toolkits.axes_grid1 import make_axes_locatable
import numpy as np
import os


def plot_yearly_gridded(path, vmax, title=None, save=False ,cmap ='YlOrBr'):
    dset = xr.open_dataset(path)
    lons = dset.lon
    lats = dset.lat

    data = dset[list(dset.keys())[0]]

    fig =  plt.figure(figsize=(12,8))
    ax = plt.axes(projection = ccrs.PlateCarree())
    if title == None:
        ax.set_title(dset.attrs['plot_hint_title'] + '\n' + 
                    dset.attrs['plot_hint_subtitle'] , fontsize = 14)
    else:
        ax.set_title(title, fontsize = 14)
    gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True, color = 'grey', 
                    alpha=0.6, linestyle = '--')
    gl.xlabels_top = False
    gl.ylabels_right = False


    im = ax.pcolormesh(lons,lats,data, transform = ccrs.PlateCarree(), cmap=cmap,
                    vmin =0, vmax = vmax)

    cax = fig.add_axes([ax.get_position().x1+0.01,ax.get_position().y0,0.02,ax.get_position().height])
    plt.colorbar(im,cax=cax,label = data.units, extend='max')
    ax.coastlines()
    if save:
        plt.savefig(('figs/{}_{}.png').format(data.product_short_name, dset.start_time[:4]), dpi=300,bbox_inches='tight')
        return fig, ax
    else:
        return fig, ax

if __name__ == "__main__":
    for path in os.listdir('data/NO2/'):
        plot_yearly_gridded('data/NO2/'+ path ,2e16, cmap='viridis', save=True)
        plt.cla()
    for path in os.listdir('data/SO2/'):
        plot_yearly_gridded('data/SO2/'+ path ,2.7, cmap='viridis', save=True)
        plt.cla()

