import matplotlib.pyplot as plt
import datetime as dt
import pandas as pd
import numpy as np
from pandas.plotting import register_matplotlib_converters
from exercise5 import *
import statsmodels.formula.api as smf

def create_scatter(ax,dfGo, df_TCCCON, key1, key2):
    validate = df_TCCCON[key1]
    validate = pd.DataFrame(validate)
    validate[key2] = dfGo[key2].values
    validate = validate.dropna()
    bias =  validate[key1] - validate[key2]
    mbias = bias.mean()
    #OLS fit
    formula = '{} ~ {}'.format(key1,key2)
    model = smf.ols(formula=formula, data=validate)
    fit = model.fit()
    alpha = fit.params[0]
    beta = fit.params[1]
    r2 = fit.rsquared

    x = np.linspace(min(validate[key2]),max(validate[key2]),100)

    ax.scatter(validate[key2], validate[key1], s=1.4)
    ax.plot(x, alpha + beta*x, color = 'crimson', linestyle = '--', 
        label=('Fitted line, slope = {:.3f} \n'.format(beta) 
                + '$R^2$ = {:.3f}'.format(r2)))
    ax.plot(x,x, color = 'grey', linestyle = '--', label='1:1 line')
    ax.grid(True)
    ax.legend(fontsize=12,loc ='upper left')
    ax.annotate('Mean bias {:.3f}'.format(mbias),xy = (0.5,0.1),
        xycoords ='axes fraction',zorder =1000, 
        fontsize = 16, color = 'blue')
    
    return ax 

