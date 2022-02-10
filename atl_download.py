"""
Downloads ATL files from specified packages (e.g. AT03, ATL08) and global location

Author: Wesley Lao
Ver. 021022
"""
import icepyx as ipx
import os
import shutil
from datetime import datetime

"""
Modified from icepyx download example: https://github.com/icesat2py/icepyx/blob/main/examples/ICESat-2_DAAC_DataAccess_Example.ipynb
"""

atllist = ['ATL03','ATL06']
today = datetime.today().strftime('%Y-%m-%d')
daterange = ['2018-10-13',today]

# New York, New York
nyspatial = [-74.075,40.67,73.9,40.825]
for atl in atllist:
    nyc = ipx.Query(atl, nyspatial, daterange)
    nyc.earthdata_login('wlao', 'wesleygarlao@utexas.edu')
    nyc.download_granules(path)