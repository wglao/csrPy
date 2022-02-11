"""
Plots ATL point clouds

Author: Wesley
Ver. 021022
"""

import icepyx as ipx
import icepyx.core.visualization as vis
import os

import xarray

"""
Modified from icepyx data read in example: https://github.com/icesat2py/icepyx/blob/main/examples/ICESat-2_Data_Read-in_Example.ipynb
"""

atlpath = r"C:\Users\wesle\Documents\CSR\csrPy\ATL files"
region = "New York"
regionpath = os.path.join(atlpath,region)
catpath = os.path.join(atlpath,"testcat.yml")
reader = ipx.Read(regionpath,"ATL03")
# reader = ipx.Read(regionpath,"ATL03",catalog=catpath)
reader.vars.append(var_list=['h_ph','lat_ph','signal_conf_ph'])
ds = reader.load()
ds.plot.scatter(x="latitude", y="elevation", hue="h_li", vmin=-100, vmax=2000)
# ds = reader.is2catalog.read()