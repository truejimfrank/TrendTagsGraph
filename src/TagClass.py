import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import datetime as dt

class TagsResearch(object):
    ''' Tag formatting and synthesizing data from the tags column.
    '''
    def tags_count(df):
        df['tags_count'] = tags_list.value_counts
        # df[df['tags'] == "[none]"]['tags_count'] = 0
        pass

    def tags_series(self):
    # transform text string into pd series
        tags_list = pd.Series(df['tags'].str.replace('"', '').str.split('|'))

        pass