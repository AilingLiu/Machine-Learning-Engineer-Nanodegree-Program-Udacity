from functools import wraps
import time
from IPython.display import display_html
import numpy as np
import pandas as pd

def timmer(func):
    'Return the value (in fractional seconds) of a performance counter.'

    @wraps(func)
    def wrapper_timmer(*args, **kwargs):

        t1 = time.perf_counter()
        result = func(*args, **kwargs)
        t2 = time.perf_counter()
        run_time=t2-t1
        print(f'Function {func.__name__} used {run_time: .4f} secs.')
        return result

    return wrapper_timmer


def getObjName(obj):
    
    return [x for x in globals() if globals()[x] is obj][0]

def display_side_by_side(*args):
    html_str=''
    for df in args:
        html_str+=df.to_html()
    display_html(html_str.replace('table','table style="display:inline"'),raw=True)
    
def missing_summary(df, threshold=0.3):
    """
    Generate a table of missing value counts, and its portion by column.
    According to the theshold provided, assign level of missing in [High, Low, Zero] class.
    """
    missing_summary = df.isnull().sum().sort_values(ascending=False).to_frame('counts')
    missing_summary['portion'] = missing_summary['counts']/len(df)
    missing_summary['Level.of.na'] = np.where(missing_summary['portion']>=threshold, 'High', 
                                        np.where(missing_summary['portion']==0, 'Zero', 'Low'))
    
    return missing_summary