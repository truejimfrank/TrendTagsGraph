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
plt.rc('font', weight='400', size=18)
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
    sns.distplot(hist_data, kde=False, rug=False, hist_kws={'alpha': 0.7}, color='xkcd:dark teal')
    # sns.distplot(hist_data, hist_kws={'alpha': 1}, ax=ax)
    ax.set(xlabel=x_label, ylabel=y_label, xticks=range(0, 80, 10))
    plt.savefig(file_path)

def image_barh(bar_data, file_path, x_label, y_label):
    sel_palette = sns.cubehelix_palette(n_colors=20, start=2.1, reverse=True)
    fig, ax = plt.subplots()
    ## tags data
    # sns.barplot(x="tag_num", y="index", data=bar_data,
    #                 palette=sel_palette)
    ## categories data
    # sns.barplot(x="category_name", y="index", data=bar_data,
    #                 palette=sel_palette)
    ## categories sci_tech
    sns.barplot(y="category_name", x="video_id", data=bar_data,
                    palette=sel_palette)
    ax.set(xlabel=x_label, ylabel=y_label)
    ax.tick_params(labelsize=18)
    plt.tight_layout(pad=1.)
    plt.savefig(file_path)

def word_cloud_topic(txt_pattern, file_path):
    # Generate wordcloud from regex pattern
    df_pat = df.loc[df["tags"].str.contains(txt_pattern)]
    tags_list = TagsResearch.create_tags_list(df_pat)
    tags_str = TagsResearch.create_str_from_list(tags_list)
    word_cloud_image(tags_str, file_path)

def print_sel_shape(txt_pattern):
    print('20 char of pattern = ' + txt_pattern[:20])
    print(df.loc[df["tags"].str.contains(txt_pattern)].shape)

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
    print(' --- dataframe info --- ')
    # print(df.columns)
    print(df.shape)
# wordcloud all tags image create
    # all_tags_list = TagsResearch.create_tags_list(df)
    # all_tags_str = TagsResearch.create_str_from_list(all_tags_list)
    # word_cloud_image(all_tags_str, "images/wc_all_standardstop.png")
# Tag count per video histogram
    # image_histogram(df['tags_count'], "images/tag_count_hist.png", 
    #                 "No. of tags per video", "No. of videos")
# All tag words histogram 100
    # bar_data = pd.Index(all_tags_list).value_counts().reset_index(name="tag_num").head(100)
    # image_barh(bar_data[bar_data['index'] != "[none]"], "images/all_tags_hist_100.png", 
    #             "Counts of 100 most common tags", "Tags")
# All tag words histogram 20
    # bar_20 = pd.Index(all_tags_list).value_counts().reset_index(name="tag_num").head(21)
    # image_barh(bar_20[bar_20['index'] != "[none]"], "images/all_tags_hist_20.png", 
    #         "Count of tag appearances", "Tags")
# Categories Video Count
    # cat_data = df["category_name"].value_counts().to_frame().reset_index()
    # image_barh(cat_data, "images/categories_count.png", 
    #         "No. of videos", "Category")
# Sci & Tech top20 tags
    # tags_list_sci_tech = TagsResearch.create_tags_list(df.loc[df["category_name"] == "Science & Technology"])
    # bar_20 = pd.Index(tags_list_sci_tech).value_counts().reset_index(name="tag_num").head(21)
    # image_barh(bar_20[bar_20['index'] != "[none]"], "images/top20_sci_tech.png", 
    #         "Count of tag appearances", "Science & Technology Tags")
# Education top20 tags
    # tags_list_sci_tech = TagsResearch.create_tags_list(df.loc[df["category_name"] == "Education"])
    # bar_20 = pd.Index(tags_list_sci_tech).value_counts().reset_index(name="tag_num").head(20)
    # image_barh(bar_20[bar_20['index'] != "[none]"], "images/top20_education.png", 
    #         "Count of tag appearances", "Education Tags")
# topically selected wordclouds
    # txt patterns for selecting data subset
    pat_sci_tech = 'science|technology'
    pat_airbnb = 'airbnb|hotel|hostel|motel|rental|vacation|tourist|travel|destination|passenger'
    pat_house = 'house|home|apartment|condo|townehome|ranch|castle|real estate|property'
    pat_food = 'food|cook|kitchen|restaurant|breakfast|lunch|dinner|supper|hungry|tasty'
    # printing pattern selection size, # of rows
    print_sel_shape(pat_sci_tech)
    print_sel_shape(pat_airbnb)
    print_sel_shape(pat_house)
    print_sel_shape(pat_food)
    # wordcloud images
    # word_cloud_topic(pat_sci_tech, "images/wc_pat_sci_tech.png")
    # word_cloud_topic(pat_airbnb, "images/wc_pat_airbnb.png")
    # word_cloud_topic(pat_house, "images/wc_pat_house.png")
    # word_cloud_topic(pat_food, "images/wc_pat_food.png")
# TAGS 'science|technology' top20
    df_tags_scitech = df.loc[df["tags"].str.contains(pat_sci_tech)]
    # tags_list_sci_tech = TagsResearch.create_tags_list(df_tags_scitech)
    # bar_20 = pd.Index(tags_list_sci_tech).value_counts().reset_index(name="tag_num").head(20)
    # image_barh(bar_20[bar_20['index'] != "[none]"], "images/top20_tags_sci_tech.png", 
    #         "Count of tag appearances", "Tags")
# Category counts from 'science|technology'
    df_graph = df_tags_scitech.reset_index().groupby("category_name").count().reset_index().sort_values('video_id', ascending=False)
    image_barh(df_graph, "images/cat_tags_sci_tech.png", 
            "No. of videos", 'Tags "Science"|"Technology" Categories')

