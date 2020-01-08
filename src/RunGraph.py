# A place to create graphs and get RESULTS!
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from TrendClass import CleanData
from TagClass import TagsResearch
from RunCode import run_pipeline
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

def word_cloud_image(big_string, file_path):
    # other colormaps default=viridis, cubehelix, CMRmap
    cloud = WordCloud(max_font_size=40, max_words=80, background_color="white", 
                        colormap="CMRmap").generate(big_string)
    cloud.to_file(file_path)

def plot_barh():
    plt.figure(figsize=(15,10))
    plt.xticks(rotation=50)
    plt.xlabel("X Label")
    plt.ylabel("Y Label")
    plt.show()

if __name__ == '__main__':
# filepath variables
    us_csv_path = "../data/trends/USvideos.csv"
    us_json_path = "../data/trends/US_category_id.json"
# load data to dataframes
    # df_us = CleanData.load_csv(us_csv_path)
    # df_us_json = CleanData.load_json(us_json_path)
# run the pipeline to pickle
    # df_us = run_pipeline(df_us, df_us_json)
    # df_us.to_pickle("../data/trends/USpipelined.pkl")
# read pickle for faster graphing
    df = pd.read_pickle("../data/trends/USpipelined.pkl")
    print(' --- dataframe columns and shape')
    print(df.columns)
    print(df.shape)
# wordcloud all tags image create
    all_tags_list = TagsResearch.create_tags_list(df)
    all_tags_str = TagsResearch.create_str_from_list(all_tags_list)
    # word_cloud_image(all_tags_str, "images/wc_all_standardstop.png")

