# Trending YouTube Videos | "tags" MetaData Analysis

A data science adventure by Jim Frank  
_YouTube trending video data from  [Kaggle: Trending YouTube Video Statistics](https://www.kaggle.com/datasnaek/youtube-new) ._

---

## Table of Contents
1. [Data Science Goals](#data-science-goals)
2. [The Data](#the-data)
3. [EDA - (Exploratory Data Analysis)](#eda-exploratory-data-analysis)
4. [Data - Cleaning & Selection For Analysis](#data-cleaning--selection-for-analysis)
5. [Let's Look At The Tag Data](#lets-look-at-the-tag-data)
6. [Conclusion](#conclusion)

---

## Data Science Goals

<b>QUESTION:  </b> 
Do topically selected subsets of the trending data have varying characteristics? Basic characteristics such as view count, likes, and tag count.# tags per video average
    ve string processing  
2. Find within the tags data specific groupings of tags that relate to a particular topic  
3. Comparing video metadata across selected subsets of the dataset  

<b>WHY THIS SET OF GOALS?:  </b> 
How does one effectively and accurately find RELEVANT data hidden within the overwhelming deluge of information now available because of modern "BigData"? In this particular example, we are searching through tags data associated with YouTube. More broadly, it is hoped that this small-scale data investigation example gives a small glipse into how one might seek out the proverbial "needle in a haystack."

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
| "rhett and link" "gmm" "good mythical morning" | 343168 | 10172 | 666 | 2146 |
| "NBA" "Basketball" "Sports" | 956169 | 2017 | 2425 | 1447 |


## EDA - (Exploratory Data Analysis)

40949 data rows in the unfiltered data. 

View count range is surprisingly large 549 - 225,211,923

Viewcount is understandably corellated to likes (0.849), dislikes (0.472), and comment count (0.618)

Videos appear multiple times. 6351 videos by unique video_id.

<b>6055</b> unique tag data fields  
<b>6351</b> unique videos  
This much unique tag data gives great confidence in it being usable for topic selection & discovery.

## Data - Cleaning & Selection For Analysis

dfsel = df.groupby(['video_id']).max()

<b>126,729</b> total tags from unique videos  
<b>56,506</b> of these tags are unique  
<b>19.95</b> average tags per video  


## Let's Look At The Tag Data

![tag count histogram](https://github.com/truejimfrank/TrendTagsGraph/blob/master/images/tag_count_hist.png)

<sub><b>Figure: </b> Count of videos in database binned by No. of tags listed with the video. </sub>

![wordcloud all tags](https://github.com/truejimfrank/TrendTagsGraph/blob/master/images/wc_all_standardstop_r.png)

<sub><b>Figure: </b> WordCloud of all words contained in tags for the dataset. (A generic stopwords list has been used.) </sub>

![bar20 all tags](https://github.com/truejimfrank/TrendTagsGraph/blob/master/images/all_tags_hist_20.png)

<sub><b>Figure: </b> Shows the 20 most used tags in the dataset. </sub>

![bar100 all tags](https://github.com/truejimfrank/TrendTagsGraph/blob/master/images/all_tags_hist_100_crop.png)

<sub><b>Figure: </b> The 100 most used tags in the dataset. </sub>

### Categories

![categories count](https://github.com/truejimfrank/TrendTagsGraph/blob/master/images/categories_count_crop.png)

<sub><b>Figure: </b> The count of videos in each category. </sub>

![top20 sci tech](https://github.com/truejimfrank/TrendTagsGraph/blob/master/images/top20_sci_tech.png)

<sub><b>Figure: </b> Top 20 tags in Science & Technology category. </sub>

![top20 education](https://github.com/truejimfrank/TrendTagsGraph/blob/master/images/top20_education.png)

<sub><b>Figure: </b> Top 20 tags in Education category. </sub>

The tags "technology" and "science" are both top results in each category.

### Topic Selection By Tags

1st 20 char of pattern = science|technology
(277, 14)
4.4%

![top20 tags sci tech](https://github.com/truejimfrank/TrendTagsGraph/blob/master/images/top20_tags_sci_tech.png)

<sub><b>Figure: </b> Top 20 tags selected by "science"|"technology". </sub>

![tags sci tech categories](https://github.com/truejimfrank/TrendTagsGraph/blob/master/images/cat_tags_sci_tech.png)

<sub><b>Figure: </b> Categories selected by "science"|"technology". </sub>

![tags sci tech wordcloud](https://github.com/truejimfrank/TrendTagsGraph/blob/master/images/wc_pat_sci_tech_r.png)

<sub><b>Figure: </b> "Science" | "Technology" WordCloud </sub>

### Other Topics Selected By Tags

1st 20 char of pattern = airbnb|hotel|hostel|
(106, 14)
1.7%

![tags airbnb wordcloud](https://github.com/truejimfrank/TrendTagsGraph/blob/master/images/wc_pat_airbnb_r.png)

<sub><b>Figure: </b> airbnb | hotel | travel WordCloud </sub>

1st 20 char of pattern = house|home|apartment
(332, 14)
5.2%

![tags house wordcloud](https://github.com/truejimfrank/TrendTagsGraph/blob/master/images/wc_pat_house_r.png)

<sub><b>Figure: </b> house | home WordCloud </sub>

1st 20 char of pattern = food|cook|kitchen|re
(427, 14)
6.7%

![tags house wordcloud](https://github.com/truejimfrank/TrendTagsGraph/blob/master/images/wc_pat_food_r.png)

<sub><b>Figure: </b> food | cook | hungry WordCloud </sub>

## Conclusion


