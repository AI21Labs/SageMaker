import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
import math


def get_topK_categories_and_score(sentiments, k=5):
    """
        Given a list of sentiments and number of top categories, create data for dashboard

        Arguments:
        - sentiments       : list of sentiments, each in json format
        - k                : how many categories to return

        Returns:
        - category_names   : the scores each category can get (in this case, Positive and Negative)
        - scores           : dict,
                             each key is a category
                             each value
    """

    parsed_sentiments = []
    for sentiment in sentiments:
        try:
            parsed_sentiments.append(json.loads(sentiment))
        except SyntaxError:
            pass
    
    df = pd.DataFrame(parsed_sentiments)

    # extract the K categories with the most reviews    
    keys = df.count().sort_values(ascending=False)[:k].index.tolist()
    
    category_names = ['Negative', 'Positive']
    scores = {}

    for key in keys:
        scores[key] = [(df[key] == category_names[0]).sum(), (df[key] == category_names[1]).sum()]
        
    return scores, category_names



def plot_dashboard(scores, category_names):
    # Based on: https://matplotlib.org/stable/gallery/lines_bars_and_markers/horizontal_barchart_distribution.html#sphx-glr-gallery-lines-bars-and-markers-horizontal-barchart-distribution-py
    """
    Parameters
    ----------
    scores         : dict
        A mapping from question labels to a list of answers per category.
        It is assumed all lists contain the same number of entries and that
        it matches the length of *category_names*. The order is assumed
        to be from 'Strongly disagree' to 'Strongly aisagree'
    category_names : list of str
        The category labels.
    """
    
    labels = list(scores.keys())
    data = np.array(list(scores.values()))
    data_cum = data.cumsum(axis=1)
    middle_index = data.shape[1]//2
    offsets = data[:, range(middle_index)].sum(axis=1) + data[:, middle_index]/2
    
    # Color Mapping
    category_colors = plt.get_cmap('coolwarm_r')(
        np.linspace(0.15, 0.85, data.shape[1]))
    
    fig, ax = plt.subplots(figsize=(10, 5))
    
    # Plot Bars
    for i, (colname, color) in enumerate(zip(category_names, category_colors)):
        widths = data[:, i]
        if i == 0:
            starts = -data_cum[:, i]
        else:
            starts = data_cum[:, i] - data_cum[:, i]
        rects = ax.barh(labels, widths, left=starts, height=0.5,
                        label=colname, color=color)
    
    # Add Zero Reference Line
    ax.axvline(0, linestyle='--', color='black', alpha=.25)
    
    # X Axis
    # Find the range
    max_range = math.ceil(max(sum(scores.values(), [])) / 10)*10
    
    ax.set_xlim(-max_range, max_range)
    ax.set_xticks(np.arange(-max_range, max_range+1, 10))
    ax.xaxis.set_major_formatter(lambda x, pos: str(abs(int(x))))
    
    # Y Axis
    ax.invert_yaxis()
    
    # Remove spines
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_visible(False)
    
    # Ledgend
    ax.legend(ncol=len(category_names), bbox_to_anchor=(0, 1),
              loc='lower left', fontsize='small')
    
    # Set Background Color
    fig.set_facecolor('#FFFFFF')
    
    plt.title("Empire Hotel - Reviews Dashboard")

    return fig, ax