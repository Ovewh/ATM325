import xarray as xr
import matplotlib.pyplot as plt
import cartopy as cr 
import cartopy as cr
import cartopy.crs as ccrs
import numpy as np
import pandas as pd
from exercise4 import bin_Data
plt.rcParams['figure.constrained_layout.use'] = True

#Read inn datafiles

dset17 = xr.open_dataset('ATM325/oco2_LtCO2_170428_B9003r_180929035950s.nc4')
dset16 = xr.open_dataset('ATM325/oco2_LtCO2_160428_B9003r_180928144848s.nc4')

#Bin the data

print('Reading data...')
Xco2_binned_2016, qa_Xco2_binned_2016, df_2016 = bin_Data(dset16)
Xco2_binned_2017, qa_Xco2_binned_2017, df_2017 = bin_Data(dset17)

#Plotting of no qa XCO2

#Set up figure
print('Creating the figures..')
fig = plt.figure(figsize=(11,5))
gs = fig.add_gridspec(6,2)

ax1 = fig.add_subplot(gs[2:,0])

#Index adjusted so that datapoints is plotted in the middle of the bin intervall

ax1.errorbar(df_2016.index -5, df_2016['Xco2_mean'], df_2016['Xco2_std'], 
                 linestyle='--', fmt='-o', color = 'blue', elinewidth=0.6, capsize=3,
            label='28.4.2016')
ax1.grid(True)
ax1.set_xlabel('Upper limit of latitude bin', fontsize=14)
ax1.set_ylabel('$\mathrm{XCO}_2$ ppm', fontsize=14)
ax1.legend(fontsize=13)
ax1.set_xticks(df_2016['bins'])

# Plot 2017 data in the left panel

ax2 = fig.add_subplot(gs[2:,1])
ax2.errorbar(df_2017.index-5, df_2017['Xco2_mean'], df_2017['Xco2_std'], 
                 linestyle='--', fmt='-o', color = 'blue', elinewidth=0.6, capsize=3,
            label='28.4.2017')
ax2.grid(True)
ax2.set_xlabel('Upper limit of latitude bin', fontsize=14)
ax2.set_ylabel('$\mathrm{XCO}_2$ ppm', fontsize=14)
ax2.legend(fontsize=13)
ax2.set_xticks(df_2017['bins'])

# Add bar plot on top showing the number of datapoints in each bin

ax3 = fig.add_subplot(gs[:2,0], sharex=ax1)
ax3.bar(df_2016.index-5,df_2016['Xco2_nP'], width=10)
ax3.grid(True)
ax3.set_ylabel('n(obs)', fontsize=14)
ax3.tick_params(labelbottom=False)
ax3.annotate('$\mathrm{n}_{tot}$ =' + '{}'.format(df_2016['Xco2_nP'].sum()), xy=(0.715, 0.67),
            xycoords='axes fraction',fontsize=14)

ax4 = fig.add_subplot(gs[:2,1], sharex=ax2)
ax4.bar(df_2017.index-5,df_2017['Xco2_nP'], width=10)
ax4.grid(True)
ax4.set_ylabel('n(obs)', fontsize=14)
ax4.tick_params(labelbottom=False)
ax4.annotate('$\mathrm{n}_{tot}$ =' + '{}'.format(df_2017['Xco2_nP'].sum()), xy=(0.715, 0.67),
            xycoords='axes fraction',fontsize=14)

plt.savefig('xCO2.pdf')

#Plotting of qa_XCO2

fig = plt.figure(figsize=(11,5))
gs = fig.add_gridspec(6,2)
ax1 = fig.add_subplot(gs[2:,0])

#Index adjusted so that datapoints is in the middle of the bin intervall

ax1.errorbar(df_2016.index -5, df_2016['qa_Xco2_mean'], df_2016['qa_Xco2_std'], 
                 linestyle='--', fmt='-o', color = 'blue', elinewidth=0.6, capsize=3,
            label='28.4.2016')
ax1.grid(True)
ax1.set_xlabel('Upper limit of latitude bin', fontsize=14)
ax1.set_ylabel('$\mathrm{XCO}_2$ ppm', fontsize=14)
ax1.legend(fontsize=13)
ax1.set_xticks(df_2016['bins'])

# Plot 2017 data in the left panel

ax2 = fig.add_subplot(gs[2:,1])
ax2.errorbar(df_2017.index-5, df_2017['qa_Xco2_mean'], df_2017['qa_Xco2_std'], 
                 linestyle='--', fmt='-o', color = 'blue', elinewidth=0.6, capsize=3,
            label='28.4.2017')
ax2.grid(True)
ax2.set_xlabel('Upper limit of latitude bin', fontsize=14)
ax2.set_ylabel('$\mathrm{XCO}_2$ ppm', fontsize=14)
ax2.legend(fontsize=13)
ax2.set_xticks(df_2017['bins'])

# Add bar plot on top showing the number of datapoints in each bin

ax3 = fig.add_subplot(gs[:2,0], sharex=ax1)
ax3.bar(df_2016.index-5,df_2016['qa_Xco2_nP'], width=10)
ax3.grid(True)
ax3.set_ylabel('n(data \n points)', fontsize=14)
ax3.tick_params(labelbottom=False)
ax3.annotate('$\mathrm{n}_{tot}$ =' + '{}'.format(df_2016['qa_Xco2_nP'].sum()), xy=(0.715, 0.67),
            xycoords='axes fraction',fontsize=14)

ax4 = fig.add_subplot(gs[:2,1], sharex=ax2)
ax4.bar(df_2017.index-5,df_2017['qa_Xco2_nP'], width=10)
ax4.grid(True)
ax4.set_ylabel('n(data \n points)', fontsize=14)
ax4.tick_params(labelbottom=False)

ax4.annotate('$\mathrm{n}_{tot}$ =' + '{}'.format(df_2017['qa_Xco2_nP'].sum()), xy=(0.715, 0.67),
            xycoords='axes fraction',fontsize=14)

plt.savefig('qa_xCO2.pdf')
print('Done!')