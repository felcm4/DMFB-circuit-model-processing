"""
Purpose: To process HDF5 file produce by Simscape Electrical model
         during simulation.

@author: Fred Love
"""

#Imports
import h5py
import numpy as np
import pandas as pd
import os

def load_h5data( dataset ):
    """Load data from a given dataset

    Parameters
    ----------
    dataset : str
       Searches from dataset.h5 in this file's directory

    Returns
    -------
    DataFrame
       
    """

    file_path = Path( os.path.dirname)
         

