# Trending YouTube Videos | "tags" MetaData Analysis

A data science adventure by Jim Frank  
_YouTube trending video data from  [Kaggle: Trending YouTube Video Statistics](https://www.kaggle.com/datasnaek/youtube-new) ._

---

## Table of Contents
1. [Data Science Goals](#data-science-goals)
2. [The Data](#the-data)
3. [EDA And Data Wrangling](#eda-and-data-wrangling)
4. [Let's Visualize That Tag Data](#lets-visualize-that-tag-data)
5. [Topic Selection By Tags](#topic-selection-by-tags)
6. [Conclusion](#conclusion)

---

## Data Science Goals

<b>QUESTION:  </b> 
Do topically selected subsets of the trending data have varying characteristics? Basic characteristics such as view count, likes, and tag count.  

<b>GOALS:  </b> 
1. Extracting and manipulating the tags data with effective string processing
2. Find specific groupings within the tags data that relate to a particular topic  
3. Comparing video metadata across selected subsets of the dataset  

<b>WHY THIS SET OF GOALS?:  </b> 
How does one effectively and accurately find RELEVANT data hidden within the overwhelming deluge of information now available because of modern "BigData"? In this particular example, we are searching through tags data associated with YouTube. More broadly, it is hoped that this small-scale data investigation example gives a small glipse into how one might seek out the proverbial "needle in a haystack."

![needle in haystack](https://hackernoon.com/hn-images/0*3CWZPlNuPWUg5cgu)

## The Data

### Context

YouTube (the world-famous video sharing website) maintains a list of the top trending videos on the platform. According to Variety magazine, “To determine the year’s top-trending videos, YouTube uses a combination of factors including measuring users interactions (number of views, shares, comments and likes). Note that they’re not the most-viewed videos overall for the calendar year”.

### Content

This dataset includes several months of data on daily trending YouTube videos.  
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


## EDA And Data Wrangling

* <b>40,949</b> data rows in the unfiltered data.  
* <b>11/14/2017</b> is the earliest trending day.  
* <b>6/14/2018</b> is the latest trending day.  
* This is a period of 7 months.  
* View count range is surprisingly large 549 - 225,211,923 views  
* Viewcount is understandably corellated to:  
    likes (0.849), dislikes (0.472), & comment count (0.618)  

Videos appear multiple times in the 40949 rows of data.  
### <b>6,351</b> videos by unique video_id  
### <b>6,055</b> unique tag data fields  
This much unique tag data gives confidence in its usability for topic selection & discovery.

![youtube vid image](https://i.ytimg.com/vi/VYOjWnS4cMY/maxresdefault.jpg)

<sub><b>Figure: </b> Thumbnail for top viewed video in the dataset. Donald Glover is excited for some data science. How about you? </sub>

### Cleaning And Selection For Analysis

A main goal of the data pipeline would be to reduce the dataset down to rows associated with each unique video. This was done by selecting the most recent or max value for fields that varied over time. Fields such as "trending_date" and "views".

Tags data for each video was stored as one long string. Pandas string methods were used to clean this datafield for counting and graphing. Additional insights are possible after cleaning the tags data.

<b>126,729</b> total tags from unique videos  
<b>56,506</b> of these tags are unique  
<b>19.95</b> average tags per video  

## Let's Visualize That Tag Data

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

The tags "technology" and "science" are both top results in the preceding two categories.

## Topic Selection By Tags

Now lets filter by tags to see what sort of videos come up.  
First we'll search tags by:  
<b>"science" or "technology"  </b>  
(alternate notation: "science"|"technology" )  

277 videos are returned by this search  
4.4% of videos in the dataset  

So what are these videos? Let's explore by looking at the complete tag set from the search.

![top20 tags sci tech](https://github.com/truejimfrank/TrendTagsGraph/blob/master/images/top20_tags_sci_tech.png)

<sub><b>Figure: </b> Top 20 tags selected by "science"|"technology". </sub>

![tags sci tech categories](https://github.com/truejimfrank/TrendTagsGraph/blob/master/images/cat_tags_sci_tech.png)

<sub><b>Figure: </b> Categories selected by "science"|"technology". </sub>

![tags sci tech wordcloud](https://github.com/truejimfrank/TrendTagsGraph/blob/master/images/wc_pat_sci_tech_r.png)

<sub><b>Figure: </b> "science"|"technology" WordCloud </sub>

### Other Topics Selected By Tags

Now that a tool is built, what would you like to learn?  
With 56,506 unique tags, there are all sorts of things we could investigate.  
Here is a set of search terms associated with <b>hotels and travel</b>.  
'airbnb|hotel|hostel|motel|rental|vacation|tourist|travel|destination|passenger'

106 videos are returned by this search  
1.7% of videos in the dataset  

![tags airbnb wordcloud](https://github.com/truejimfrank/TrendTagsGraph/blob/master/images/wc_pat_airbnb_r.png)

<sub><b>Figure: </b> hotels and travel WordCloud </sub>

<b>Home and real estate</b> search terms  
'house|home|apartment|condo|townehome|ranch|castle|real estate|property'

332 videos are returned by this search  
5.2% of videos in the dataset  
"Recipe" and "cooking" have appeared in the WordCloud.

![tags house wordcloud](https://github.com/truejimfrank/TrendTagsGraph/blob/master/images/wc_pat_house_r.png)

<sub><b>Figure: </b> Home and real estate WordCloud </sub>

<b>Food and cooking</b> search terms  
'food|cook|kitchen|restaurant|breakfast|lunch|dinner|supper|hungry|tasty'

427 videos are returned by this search  
6.7% of videos in the dataset  
"Recipe" also appears in this visualization despite not being in the search terms.

![tags house wordcloud](https://github.com/truejimfrank/TrendTagsGraph/blob/master/images/wc_pat_food_r.png)

<sub><b>Figure: </b> Food and cooking WordCloud </sub>

## Conclusion

![comparison means](https://github.com/truejimfrank/TrendTagsGraph/blob/master/images/comp_means_dist.png)

<sub><b>Figure: </b> Comparing viewcount means from several data subsets </sub>

Going by the "eyeball test", there does appear to be differences in the mean values between topically selected subsets.

What were our goals again?  
<b>GOALS:  </b> 
1. Extracting and manipulating the tags data with effective string processing
2. Find specific groupings within the tags data that relate to a particular topic  
3. Comparing video metadata across selected subsets of the dataset  

### Final Thoughts

* The tags data proved to be full of interesting connections and associations.  
* It felt somewhat safe to assume the categories datafield would have some overlap with tags data. This appears to be the case.  
* When you dig a hole looking for one category of data, you end up with data treasure you didn't even know was there.  

![treasure](http://pagosasprings.com/wp-content/uploads/2013/04/gold.jpg)

http://pagosasprings.com/wp-content/uploads/2013/04/gold.jpg
<sub><b>Figure: </b> Buried Treasure </sub>
