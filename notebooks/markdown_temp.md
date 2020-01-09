# templates to use

# Italics
_The text to make italicized_

# Internet Link
[name of link to youtube video](https://www.youtube.com/watch?v=1CR0QmCaMTs)

# Image File 
![tag count histogram](https://github.com/truejimfrank/TrendTagsGraph/blob/master/images/tag_count_hist.png)
# YouTube video thumbnail
![youtube vid image](https://i.ytimg.com/vi/1CR0QmCaMTs/maxresdefault.jpg)
# Divider Line
---

# Python Code
```python
import networkx as nx
from src.example_graphs import simple_undirected_graph

# The dictionary graph shown earlier
simple_graph = simple_undirected_graph()
G = nx.from_dict_of_lists(simple_graph)
```

# alternate image post format (width and height optional)
<img src="images/toy-graph-1.png" alt="Toy Undirected Graph" width="400" height="400">

# FIGURE name below a picture (<b>bold text here<b>)
<sub><b>Figure: </b> A toy undirected graph that I used for developing custom graph classes. There was a lot of whiteboard doodling during this project. </sub>

# TABLE with bold column names
| subreddit | In-Degree (Uniques) | In-Degree (Total) |
| --- | --- | --- |
| askreddit | 5448 | 24295 |
| iama | 4508 | 11624 |
| pics | 3335 | 11728 |
| gaming | 1746 | 5584 |
| news | 1610 | 7005 |
| gifs | 1591 | -- |
| politics | -- | 5511 |

## Table of Contents (with links to section headings)
1. [Motivation](#motivation)
2. [The Data](#the-data)
3. [Graph Theory Terminology](#graph-theory-terminology)
4. [Representing the Data Computationally](#representing-the-data-computationally)
5. [Questions & Answers](#questions--answers)
    * [Who's the most connected? (Max Degree: In-Degree and Out-Degree)](#whos-the-most-connected-max-degree-in-degree-and-out-degree)
    * [How many distinct networks are there? (Component Analysis)](#how-many-distinct-networks-are-there-component-analysis)

## Representing the Data Computationally
## Questions & Answers
### Who's the most connected? (Max Degree: In-Degree and Out-Degree)
