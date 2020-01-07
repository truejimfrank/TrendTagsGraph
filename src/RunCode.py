# A place to call on data and functions to get RESULTS!
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import datetime as dt
from TrendClass import CleanData
from TrendClass import TagsResearch

if __name__ == '__main__':
    us_csv_path = "../data/trends/USvideos.csv"
    us_json_path = "../data/trends/US_category_id.json"
    df_us = CleanData.load_csv(us_csv_path)
    df_us_json = CleanData.load_json(us_json_path)
    print(df_us.head())