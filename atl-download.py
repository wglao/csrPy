"""
Downloads ATL files from specified packages (e.g. AT03, ATL08) and global location

Author: Wesley Lao
Ver. 021022
"""
from logging import warning
import icepyx as ipx
import os
import shutil
from datetime import datetime
import warnings
import re
import numpy as np

"""
Modified from icepyx download example: https://github.com/icesat2py/icepyx/blob/main/examples/ICESat-2_DAAC_DataAccess_Example.ipynb
"""

def download(atllist,daterange,region):
    """
    Creates query and downloads matching atl files based upon:
    - atllist: list of atl product types as a list of strings,
                    uses all proper atl products. Raises a warning
                    if invalid product is requested. Raises an
                    exception if there are no valid products.
            ex. ['ATL03','ATL08']
    - daterange: start and end dates as a list of strings,
                    formatted as 'YYYY-MM-DD'. If only one date is
                    given, it is used as the start date and the
                    current date is used as the end date. Rasies
                    an exception if the date is in the future or
                    if more than 2 dates are given.
            ex. ['2020-01-01','2021-01-01']
            ex. ['2020-01-01']
    - region: name of region as a string, checks region json
                    for match and pulls down necessary information.
                    Raises an exception if region is not found.
            ex. 'New York'
    """
    
    try:
        # handle ATL list input
        atlpattern = re.compile(r"ATL\\d\\d")
        validatls = []
        for atl in atllist:
            if atlpattern.match(atl, re.IGNORECASE):
                validatls += atl
            elif int(atl[4:5]) >= 2 and int(atl[4:5]) <= 21 and int(atl[4:5]) != 18:
                validatls += atl
            else:
                warnings.warn("Invalid ATL product. Excluding query.")
        if len(validatls) == 0:
            raise Exception("No valid ATL products.")

        # handle daterange input
        if len(daterange) == 1:
            today = datetime.today().strftime('%Y-%m-%d')
            if daterange > today:
                daterange += today
            else:
                raise Exception("Date is in the future.")
        elif len(daterange) > 2:
            raise Exception("More than 2 dates were provided.")
        else:
            if daterange[0] > daterange[1]:
                warnings.warn("First date is after the second. Reversing date order.")
                daterange = [daterange[1], daterange[0]]

        # TODO: add region recognition
        # New York, New York
        nyspatial = [-74.075,40.67,-73.9,40.825]

        # make directory if does not exist
        regionpath = os.path.join(atlpath,r"New York")
        os.makedirs(regionpath,exist_ok=True)

        # download ATL products
        for atl in validatls:
            query = ipx.Query(atl, nyspatial, daterange)
            query.earthdata_login('wlao', 'wesleygarlao@utexas.edu')
            query.download_granules(regionpath)

    except Exception as e:
        print(e)

        

if __name__ == "main":
    atllist = ['ATL03','ATL08']
    today = datetime.today().strftime('%Y-%m-%d')
    daterange = ['2021-11-13',today]

    # default download directory
    atlpath = r"C:\Users\wesle\Documents\CSR\csrPy\ATL files"

    # New York, New York
    nyspatial = [-74.075,40.67,-73.9,40.825]

    # make directory if does not exist
    regionpath = os.path.join(atlpath,r"New York")
    os.makedirs(regionpath,exist_ok=True)

    for atl in atllist:
        nyc = ipx.Query(atl, nyspatial, daterange)
        nyc.earthdata_login('wlao', 'wesleygarlao@utexas.edu')
        nyc.download_granules(regionpath)