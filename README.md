# Trending YouTube Videos | "tags" MetaData Analysis

A data science adventure by Jim Frank
_YouTube trending video data from  [Kaggle: Trending YouTube Video Statistics](https://www.kaggle.com/datasnaek/youtube-new) ._

---

## Table of Contents
1. [Data Science Goals](#data-science-goals)
2. [The Data](#the-data)
3. [EDA - (Exploratory Data Analysis)](#eda-exploratory-data-analysis)
4. [Data - Cleaning & Selection For Analysis](#data-cleaning--selection-for-analysis)
5. [Let's Look At The Tag Data](#lets-look-at-tag-data)
6. [Conclusion](#conclusion)


## Data Science Goals

<b>QUESTION:  </b> 
Do topically selected subsets of the trending data have varying characteristics? Basic characteristics such as view count, likes, and tag count.

<b>GOALS:  </b> 
1. Extracting and manipulating the tags data with effective string processing  
2. Find within the tags data specific groupings of tags that relate to a particular topic  
3. Comparing video metadata across selected subsets of the dataset  

<b>WHY THIS SET OF GOALS?:  </b> 
How does one effectively and accurately find RELEVANT data hidden within the overwhelming deluge of information now available because of modern "BigData"? In this particular example, we are searching through tags data associated with YouTube. More broadly, it is hoped that the following data processing investigation gives a proper framework for seeking out the proverbial "needle in a haystack."

![needle in haystack](https://hackernoon.com/hn-images/0*3CWZPlNuPWUg5cgu)

## The Data

### Context

YouTube (the world-famous video sharing website) maintains a list of the top trending videos on the platform. According to Variety magazine, “To determine the year’s top-trending videos, YouTube uses a combination of factors including measuring users interactions (number of views, shares, comments and likes). Note that they’re not the most-viewed videos overall for the calendar year”.

### Content

This dataset includes several months of data on daily trending YouTube videos.  
11/14/2017 is the earliest trending day.  
6/14/2018 is the latest trending day.  
This is a period of 7 months.  
Unless otherwise stated, information presented here will be from the USA data subset. Data files from a variety of countries are available on the Kaggle project website.

Here's an example of the raw data used for this project:

| video_id | trending_date | title | channel_title | category_id | 
| --- | --- | --- | --- | --- |
| puqaWrEC7tY | 17.14.11 | Nickelback Lyrics: Real or Fake? | Good Mythical Morning | 24 |
| sbcbvuitiTc | 17.14.11 | Stephon Marbury and Jimmer Fredette fight in C... | NBA Highlights · YouTube | 17 |

More of the relevant data fields:

| tags | views | likes |  dislikes | comment_count |
| --- | --- | --- | --- | --- |
| `"rhett and link"|"gmm"|"good mythical morning"` | 343168 | 10172 | 666 | 2146 |
| "NBA" "Basketball" "Sports" | 956169 | 2017 | 2425 | 1447 |


## EDA - (Exploratory Data Analysis)

Videos appear multiple times. 6351 videos by unique video_id. 40949 data rows in the unfiltered data.

View count range is surprisingly large 549 - 225,211,923

6055 / 6351 unique tag data fields to unique videos

spaghetti burrito|"diy burrito"|"spaghetti"|"burrito"|"burrito recipe"|"spaghetti deep fried"|"deep fried spaghetti"|"spgahetti sandwich"|"giant burrito"',
       'numberphile|"prime numbers"|"proth prime"',
       'Smart mug|"Heated thermos"|"tech"|"gift idea"|"unboxed"|"Ember mug"|"ember"|"Ember review"|"Heated mug"|"teardown"|"technology"|"Thermous"|"winter"|"holiday"|"christmas"|"gift"|"mug"|"unboxing"',
       'auth-jvardon-auth',
       'freaks and geeks|"jason segel"|"judd apatow"|"drums"|"rush"|"paul feig"|"drummer"|"nick andopolis"

Viewcount is understandably corellated to likes (0.849), dislikes (0.472), and comment count (0.618)

## Data - Cleaning & Selection For Analysis

dfsel = df.groupby(['video_id']).max().copy()

126,729 total tags from unique videos. 56,506 of these tags are unique.

## Let's Look At The Tag Data

![tag count histogram](https://github.com/truejimfrank/TrendTagsGraph/blob/master/images/tag_count_hist.png)

<sub><b>Figure: </b> Count of videos in database binned by No. of tags listed with the video. </sub>

![wordcloud all tags](https://github.com/truejimfrank/TrendTagsGraph/blob/master/images/wc_all_standardstop_r.png)

<sub><b>Figure: </b> WordCloud of all words contained in tags for the dataset. (A generic stopwords list has been used.) </sub>

![bar20 all tags](https://github.com/truejimfrank/TrendTagsGraph/blob/master/images/all_tags_hist_20_crop.png)

<sub><b>Figure: </b> Shows the 20 most used tags in the dataset. </sub>

![bar100 all tags](https://github.com/truejimfrank/TrendTagsGraph/blob/master/images/all_tags_hist_100_crop.png)

<sub><b>Figure: </b> The 100 most used tags in the dataset. </sub>

## Conclusion


