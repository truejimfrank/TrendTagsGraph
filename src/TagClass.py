import pandas as pd
import numpy as np
# from matplotlib import pyplot as plt
# import seaborn as sns
import datetime as dt

class TagsResearch(object):
    ''' Tag formatting and synthesizing data from the tags column.
    '''
    def tags_count(df):
        tags_series = pd.Series(df['tags'].str.replace('"', '').str.split('|'))
        df['tags_count'] = tags_series.apply(lambda x: len(x))
        df.loc[df['tags'] == "[none]", ['tags_count']] = 0
        return df

    def create_all_tags_list(df):
    # transform tags column into all tags df
        tags_series = pd.Series(df['tags'].str.replace('"', '').str.split('|'))
        flatten_matrix = [val for sublist in tags_series for val in sublist]
        return flatten_matrix
