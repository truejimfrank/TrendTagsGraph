# A place to create graphs and get RESULTS!
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from TrendClass import CleanData
from TagClass import TagsResearch
from RunCode import run_pipeline
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

# ---- plotting and display options ----
# PLOT_COLORS = ["#268bd2", "#0052CC", "#FF5722", "#b58900", "#003f5c"]
# pd.options.display.float_format = '{:.2f}'.format
sns.set(style="ticks")
plt.rc('figure', figsize=(14, 8), dpi=100)
plt.rc('axes', labelpad=18, facecolor="#ffffff", linewidth=0.4, grid=True, labelsize=24)
plt.rc('patch', linewidth=0)
plt.rc('xtick.major', width=0.2)
plt.rc('ytick.major', width=0.2)
plt.rc('grid', color='#9E9E9E', linewidth=0.4)
plt.rc('font', weight='400', size=16)
# plt.rc('font', family='Arial', weight='400', size=10)
plt.rc('text', color='#282828')
plt.rc('savefig', pad_inches=0.3, dpi=100)

def word_cloud_image(big_string, file_path):
    # other colormaps default=viridis, cubehelix, CMRmap
    cloud = WordCloud(max_font_size=40, max_words=80, background_color="white", 
                        colormap="CMRmap").generate(big_string)
    cloud.to_file(file_path)

def image_histogram(hist_data, file_path, x_label, y_label):
    fig, ax = plt.subplots()
    sns.distplot(hist_data, kde=False, rug=False, hist_kws={'alpha': 1}, color='xkcd:dark purple')
    # sns.distplot(hist_data, hist_kws={'alpha': 1}, ax=ax)
    ax.set(xlabel=x_label, ylabel=y_label, xticks=range(0, 80, 10))
    plt.savefig(file_path)

def image_barh(bar_data, file_path, x_label, y_label):
    fig, ax = plt.subplots()
    # y="index", 
    sns.barplot(x="tag_num", y="index", data=bar_data,
                    palette=sns.cubehelix_palette(n_colors=20, reverse=True))
    # , ylabel=y_label
    ax.set(xlabel=x_label)
    plt.savefig(file_path)


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
# Tag count per video histogram
    # image_histogram(df['tags_count'], "images/tag_count_hist.png", 
    #                 "No. of tags per video", "No. of videos")
# All tag words histogram 100
    # bar_data = pd.Index(all_tags_list).value_counts().reset_index(name="tag_num").head(100)
    # image_barh(bar_data, "images/all_tags_hist_100.png", 
    #             "Counts of 100 most common tags", "Freq. of tag appearance")
    # cdf = df.groupby("channel_title").size().reset_index(name="video_count") \
    # .sort_values("video_count", ascending=False).head(20)
# All tag words histogram 20
    bar_20 = pd.Index(all_tags_list).value_counts().reset_index(name="tag_num").head(21)
    image_barh(bar_20[bar_20['index'] != "[none]"], "images/all_tags_hist_20.png", 
            "Count of tag appearances", "Freq. of tag appearance")
    