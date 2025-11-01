# Utilities for preparing Samburu text/audio datasets

import os
import pandas as pd

def load_metadata(path):
    return pd.read_csv(path)
