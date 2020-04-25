import pandas as pd
import random
import time
import numpy as np
from sklearn.model_selection import train_test_split

from .constants import PATH_FILE_INFO, PATH_FILE_ATTR

def cleanDf(df, col_drop, row_na=20, drop_rows=True):
    
    df_ = normalizeNa(df)
    df_ = cleanCat(df_)
    df_ = drop_cols(df_, col_drop)
    if drop_rows:
        df_ = dropRowNa(df_, row_na)
    return df_


def drop_cols(df, col_drop):
    cols_ = set(df.columns).intersection(col_drop)
    return df.drop(cols_, axis=1)

def read_data(filename, portion=0.1, random_state=42):
    """
    Given file path, and portion of the data to be extracted, return a
    random subset of data within the specified portion.
    """

    start = time.time()
    
    if portion < 1:

        n = sum(1 for line in open(filename)) - 1 #number of records in file (excludes header)
        s = int(n*portion) #desired sample size
        print('Total rows in file: {}\nExtracting {} rows from file.'.format(n, s))
        print('Loading File...')

        random.seed(random_state)
        skip = sorted(random.sample(range(1,n+1),n-s)) #the 0-indexed header will not be included in the skip list
    else:
        skip = 0

    df = pd.read_csv(filename, skiprows=skip, sep=';')
    
    end = time.time()
    print('Loading succeed. Time used: {} seconds.'.format(int(end-start)))

    return df

def listtodict(aVal):
    """
    convert a list of value into dictionary with default value np.nan
    return dictionary
    
    example:
        >>> listtodict([-1])
        {-1: np.nan}
        >>> listtodict(['-1, 0'])
        {-1: np.nan, 0: np.nan}
    """
    if type(aVal[0])==str:
        nlist = [x if x.isalpha() else int(x) for x in aVal[0].replace(' ', '').split(',')]
        return dict.fromkeys(nlist, np.nan)
    return dict.fromkeys(aVal, np.nan)

# depreciated
def codetonan(df, code_df):
    """
    Standardize the unknown value indicated by code_df to np.nan
    return: none
    
    example:
    >>> df = pd.DataFrame({'AGER_TYP': [-1, -1, 10, 9, 1]})
    >>> code_df = pd.DataFrame({'missing_or_unknow': [-1]})
    >>> codetonan(df, code_df)
    >>> df
        AGER_TYP
    0    nan
    1    nan
    2    10
    3    9
    4    1
    """
    
    start = time.time()
    for att in code_df.index:
        try:
            df.loc[:, att].replace(listtodict(code_df.loc[att, 'missing_or_unknown']), inplace=True)
        except:
            continue

    end = time.time()
    print("Total execution time of this procedure: {:.2f} seconds".format(end-start))

# depreciated
def get_unknown():
    
    feat_info = pd.read_excel(PATH_FILE_INFO, header=1)
    feat_att = pd.read_excel(PATH_FILE_ATTR, header=1)
    feat_info.drop(feat_info.columns[0], axis=1, inplace=True) #dropping the first empty column
    feat_att.drop(feat_att.columns[0], axis=1, inplace=True)#dropping the first empty column

    # generate a summary of features where Meaning is unknown
    mask = feat_att['Meaning'].str.contains('unknown', case=False, na=False)
    unknown_code = feat_att.loc[mask, :].groupby('Attribute')['Value'].unique().to_frame('missing_or_unknown')
    unknown_code = unknown_code.join(feat_info[['Attribute', 'Description']].set_index('Attribute'), how='left')
    
    #found ['XX', 'X'] as missing values too
    ta = pd.DataFrame([[['X, XX'], 'CAMEO']]*2, index= ['CAMEO_DEU_2015', 'CAMEO_INTL_2015'], 
                  columns=['missing_or_unknown', 'Description'])
    
    unknown_code.loc['CAMEO_DEUG_2015', 'missing_or_unknown'] = ['-1, X, XX']
    
    return pd.concat([unknown_code, ta])

def normalizeNa(df):
    missing_val = [-1, 0, 9, 'X', 'XX', '-1', '0', '9']
    if 'RESPONSE' in df.columns:
        resp = df['RESPONSE']
        return df.replace(missing_val, np.nan).assign(RESPONSE=resp)
    else:
        return df.replace(missing_val, np.nan)


def strtoint(val):
    to_map = {'A': 0, 'B': 1, 'C': 2, 'D':3, 'E':4, 'F': 5, 'G': 6}
    if type(val) == str:
        if (val[0].isdigit()) and (val[1] in to_map):
            return int(val[0])*10 + to_map[val[1]]
    else:
        return val

#may depreciate
def encode_df(df):
    
    #CAMEO_DEU_2015: {'1A': 10, '1B': 11...}
    df['CAMEO_DEU'] = df['CAMEO_DEU_2015'].apply(lambda x: strtoint(x) if x is not np.nan else x)
    
    #change type
    df['CAMEO_DEUG']= df['CAMEO_DEUG_2015'].astype('float64')
    df['CAMEO_INTL'] = df['CAMEO_INTL_2015'].astype('float64')
    
    #EINGEFUEGT_AM: transform year to index
    df['EINGEFUEGT_AM'] = pd.to_datetime(df['EINGEFUEGT_AM'])
    max_year = df['EINGEFUEGT_AM'].max().year
    df['EINGEFUEGT_ind'] = (max_year - df['EINGEFUEGT_AM'].dt.year)    
    
    #PRAEGENDE_JUGENDJAHRE, convert mixed information code into seperate code
    pjtime = {1:0,2:0,3:1,4:1,5:2,6:2,7:2,8:3,9:3,10:4,11:4,12:4,13:4,14:5,15:5}
    pjavan = {1:0, 2:1, 3:0, 4:1, 5:0, 6:1, 7:1, 8:0, 9:1, 10:0, 11:1, 12:0, 13:1, 14:0, 15:1}
    
    df['pjtime'] = df['PRAEGENDE_JUGENDJAHRE'].map(pjtime)
    df['pjavan'] = df['PRAEGENDE_JUGENDJAHRE'].map(pjavan)
    
    # standardize binary column values to [0, 1]
    df['VERS_TYP'] = df['VERS_TYP'].replace({2: 0})
    df['ANREDE_KZ'] = df['ANREDE_KZ'].replace({2: 0})
    df['OST_WEST_KZ'] = df['OST_WEST_KZ'].replace({'W': '0', 'O': '1'}).astype('float64')
    
    # drop 'EINGEFUEGT_AM', 'PRAEGENDE_JUGENDJAHRE'
    
    return df.drop(['EINGEFUEGT_AM', 'CAMEO_DEU_2015', 'CAMEO_DEUG_2015', 'CAMEO_INTL'], axis=1)

def dropRowNa(df, num=20):
    maska = (df.isnull().sum(axis=1) <= num)
    maskb = (df['RESPONSE'] == 1)
    return df.loc[maska | maskb]

def cleanCat(df):
    
    #CAMEO_DEU_2015: {'1A': 10, '1B': 11...}
    df['CAMEO_DEU'] = df['CAMEO_DEU_2015'].apply(lambda x: strtoint(x))
    
    #change type
    df['CAMEO_DEUG']= df['CAMEO_DEUG_2015'].astype('float64')
    df['CAMEO_INTL'] = df['CAMEO_INTL_2015'].astype('float64')

    
    #EINGEFUEGT_AM: transform year to index
    df['EINGEFUEGT_ind'] = (2020 - pd.to_datetime(df['EINGEFUEGT_AM']).dt.year)
    df['OST_WEST'] = df['OST_WEST_KZ'].replace({'W': '0', 'O': '1'}).astype('float64')
    
    #PRAEGENDE_JUGENDJAHRE, convert mixed information code into seperate code
    pjtime = {1:0,2:0,3:1,4:1,5:2,6:2,7:2,8:3,9:3,10:4,11:4,12:4,13:4,14:5,15:5}
    pjavan = {1:0, 2:1, 3:0, 4:1, 5:0, 6:1, 7:1, 8:0, 9:1, 10:0, 11:1, 12:0, 13:1, 14:0, 15:1}
    
    df['pjtime'] = df['PRAEGENDE_JUGENDJAHRE'].map(pjtime)
    df['pjavan'] = df['PRAEGENDE_JUGENDJAHRE'].map(pjavan)
    
    # standardize binary column values to [0, 1]
    df['VERS_TYP_INT'] = df['VERS_TYP'].replace(2, 0)
    df['ANREDE_KZ_INT'] = df['ANREDE_KZ'].replace(2, 0)
    
    cols_=['EINGEFUEGT_AM', 'PRAEGENDE_JUGENDJAHRE', 'OST_WEST_KZ', 'CAMEO_DEU_2015', 'CAMEO_DEUG_2015', 'CAMEO_INTL', 'CAMEO_INTL_2015']
    return df.drop(cols_, axis=1)

def trioSampling(df_input, stratify_colname='y',
                                         frac_train=0.6, frac_val=0.15, frac_test=0.25,
                                         random_state=42):
    '''
    Splits a Pandas dataframe into three subsets (train, val, and test)
    following fractional ratios provided by the user, where each subset is
    stratified by the values in a specific column (that is, each subset has
    the same relative frequency of the values in the column). It performs this
    splitting by running train_test_split() twice.

    Parameters
    ----------
    df_input : Pandas dataframe
        Input dataframe to be split.
    stratify_colname : str
        The name of the column that will be used for stratification. Usually
        this column would be for the label.
    frac_train : float
    frac_val   : float
    frac_test  : float
        The ratios with which the dataframe will be split into train, val, and
        test data. The values should be expressed as float fractions and should
        sum to 1.0.
    random_state : int, None, or RandomStateInstance
        Value to be passed to train_test_split().

    Returns
    -------
    df_train, df_val, df_test :
        Dataframes containing the three splits.
    '''

    if frac_train + frac_val + frac_test != 1.0:
        raise ValueError('fractions %f, %f, %f do not add up to 1.0' % \
                         (frac_train, frac_val, frac_test))

    if stratify_colname not in df_input.columns:
        raise ValueError('%s is not a column in the dataframe' % (stratify_colname))

    X = df_input # Contains all columns.
    y = df_input[[stratify_colname]] # Dataframe of just the column on which to stratify.

    # Split original dataframe into train and temp dataframes.
    df_train, df_temp, y_train, y_temp = train_test_split(X,
                                                          y,
                                                          stratify=y,
                                                          test_size=(1.0 - frac_train),
                                                          random_state=random_state)

    # Split the temp dataframe into val and test dataframes.
    relative_frac_test = frac_test / (frac_val + frac_test)
    df_val, df_test, y_val, y_test = train_test_split(df_temp,
                                                      y_temp,
                                                      stratify=y_temp,
                                                      test_size=relative_frac_test,
                                                      random_state=random_state)

    assert len(df_input) == len(df_train) + len(df_val) + len(df_test)

    return df_train, df_val, df_test
    