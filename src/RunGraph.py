# A place to create graphs and get RESULTS!
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from TrendClass import CleanData
from TagClass import TagsResearch
from RunCode import run_pipeline
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

def plot_barh():
    plt.figure(figsize=(15,10))
    country.size().sort_values(ascending=False).plot.bar()
    plt.xticks(rotation=50)
    plt.xlabel("Country of Origin")
    plt.ylabel("Number of Wines")
    plt.show()

if __name__ == '__main__':
# filepath variables
    us_csv_path = "../data/trends/USvideos.csv"
    us_json_path = "../data/trends/US_category_id.json"
# load data to dataframes
    # df_us = CleanData.load_csv(us_csv_path)
    # df_us_json = CleanData.load_json(us_json_path)
# run the pipeline
    # df_us = run_pipeline(df_us, df_us_json)
    # print(df_us.columns)
    # df_us.to_pickle("../data/trends/USpipelined.pkl")
# read pickle for faster graphing
    df = pd.read_pickle("../data/trends/USpipelined.pkl")
    print(df.columns)
    print(df.shape)

# Groupby by country
country = df.groupby("country")

# Summary statistic of all countries
country.describe().head()
