from pathlib import Path


# PATH_PROJECT will be called from the root of the project or from one of the subfolders
PATH_PROJECT = Path('..') if Path('.').resolve().name == 'Arvato_Customer_Segmentation' else Path('.')
PATH_DATA_AZD = PATH_PROJECT / '../../data/Term2/capstone/arvato_data/Udacity_AZDIAS_052018.csv'
PATH_DATA_CUST = PATH_PROJECT / '../../data/Term2/capstone/arvato_data/Udacity_CUSTOMERS_052018.csv'
PATH_FILE_INFO = PATH_PROJECT / 'DIAS Information Levels - Attributes 2017.xlsx'
PATH_FILE_ATTR = PATH_PROJECT / 'DIAS Attributes - Values 2017.xlsx'