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

    def load_csv(self, file_path):
        return pd.read_csv(file_path)

    def load_json(self, file_path):
        return pd.read_json(file_path)

    def fill_nan(self, df):
        df["description"] = df["description"].fillna(value="")
        return df

    def join(self):
    # join the category names from json files
        pass

    def date_format(self):
    # ["trending_date", "publish_time"]
    # 
        pass

    def unique_reduce(self):
    # reduce df to most recent unique video data
    # count # of days video appears on trending
    # record initial viewcount on trending start
        pass


class TagsResearch(object):
    ''' Tag formatting and synthesizing data from the tags column.
    '''
    def split_tags(self, tags_str):
        return tags_str.replace('"', '').split('|')

    def tags_format(self):
    # transform text string into pd series
        pass