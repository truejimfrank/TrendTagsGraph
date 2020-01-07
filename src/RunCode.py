# A place to call on data and functions to get RESULTS!
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import datetime as dt
from TrendClass import CleanData
from TagClass import TagsResearch

if __name__ == '__main__':
# filepath variables
    us_csv_path = "../data/trends/USvideos.csv"
    us_json_path = "../data/trends/US_category_id.json"
# load data to dataframes
    df_us = CleanData.load_csv(us_csv_path)
    df_us_json = CleanData.load_json(us_json_path)
    # print(df_us.head())
    # print(df_us_json.head())
# data cleaning pipeline
    CleanData.fill_nan(df_us)
    # print(df_us.info())
    CleanData.join_categories(df_us, df_us_json)
    # print(df_us['category_name'].head(10))
    CleanData.date_format(df_us)
    # ["trend_end", "post_time"]
    # df_view = pd.DataFrame(df_us["trend_end"].unique())
    # print(df_view.sort_values(0, ascending=False).head(3))
    # print(df_us["trend_end"].dtype)
    # print(df_us["post_time"].dtype)
# groupby video_id, select columns, make df copy
    df_us_vid = CleanData.unique_reduce(df_us)
    # print(df_us_vid.columns)
# Tags formatting and splitting
    TagsResearch.tags_count(df_us_vid)
    # print(df_us_vid.info())
    xlsx_columns = ['title', 'channel_title', 'category_name', 'tags',
                 'views', 'views_initial', 'tags_count']
    df_us_vid.to_excel("../data/trends/USvideos_tags.xlsx", columns=xlsx_columns)
