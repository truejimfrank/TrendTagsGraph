import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import datetime as dt

class CleanData(object):
    ''' Class with functions for manipulating trending video 
    YouTube data.
    '''
    # def __init__(self):
    #     pass

    # This didn't work as intended
    # def load_csv(self, file_path):
    #     return pd.read_csv(file_path)

    def load_csv(file_path):
        return pd.read_csv(file_path)

    def load_json(file_path):
        return pd.read_json(file_path)

    def fill_nan(df):
        df["description"] = df["description"].fillna(value="")
        return df

    def join_categories(df, df_json):
    # create category_name column from json files
        cat_dict = {}
        for cat in df_json["items"]:
            cat_dict[int(cat["id"])] = cat["snippet"]["title"]
        df['category_name'] = df['category_id'].map(cat_dict)
        return df

    def date_format(df):
    # ["trending_date", "publish_time"]
    # ["trend_end", "post_time"]
        df["trend_end"] = pd.to_datetime(df["trending_date"], format="%y.%d.%m")
        df["post_time"] = pd.to_datetime(df["publish_time"])
        return df

    def unique_reduce(df):
    # count # of days video appears on trending
        day_max = df[['video_id', 'trend_end']].groupby(['video_id']).max().iloc[:,0]
        day_min = df[['video_id', 'trend_end']].groupby(['video_id']).min().iloc[:,0]
        df["trend_begin"] = df["video_id"].map(day_min)
        delta_map = day_max - day_min + dt.timedelta(days=1)
        df["days_trending"] = df["video_id"].map(delta_map)
    # record initial viewcount on trending start
        min_map = df[['video_id', 'views']].groupby(['video_id']).min().iloc[:,0]
        df["views_initial"] = df["video_id"].map(min_map)
    # reduce df to most recent unique video data
        col_sel = ['video_id', 'title', 'channel_title', 'category_name', 'tags',
                 'views', 'views_initial','trend_begin', 'trend_end', 'days_trending',
                  'post_time', 'likes', 'dislikes', 'comment_count']
        return df[col_sel].groupby(['video_id']).max().copy()


