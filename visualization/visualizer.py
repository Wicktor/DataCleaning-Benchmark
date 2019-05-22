import plotly
import sys
from plotly.offline import plot as off_plot
import plotly.graph_objs as go
from collections import Counter

def bar_chart_summary(cloths):
    filter = [
        'product_name',
        'mrp',
        'price',
        'brand_name',
        'product_category',
        'retailer',
        'rating',
        'review_count',
        # 'total_size',
        # 'available_size',
        'color'
    ]
    attributes_amount = get_attribute_amount(cloths, filter)

    for attribute_name, attribute_summary in attributes_amount.items():
        create_bar_chart_for_attribute(attribute_name, attribute_summary)

def get_attribute_amount(cloths, whitelist_filter:list):
    '''
    Takes a list of cloths and counts the amount of values for each attribute. E.g. the
    amount of occurrence's of the brand name 
    :param cloths: list of cloth instances
    :return: dict with entry for each attribute that contains a dict that could e.g. look like 
             the following for the attribute color: {'blue': 3, 'red': 2, 'yellow': 1}
    '''
    # create dict
    attributes_values = {}
    attributes_amount = {}
    for attr, value in cloths[0].__dict__.items():
        if attr not in whitelist_filter:
            continue
        attributes_values[attr] = []

    # collect values
    for cloth in cloths:
        for attr, value in cloth.__dict__.items():
            if attr not in whitelist_filter:
                continue
            attributes_values[attr].append(value)

    # count amount of values
    for attr, value in attributes_values.items():
        amount = Counter(value)
        attributes_amount[attr] = dict(amount)

    return attributes_amount

def create_bar_chart_for_attribute(attribute_name, attribute_summary):
    x = []
    y = []
    for key, value in attribute_summary.items():
        x.append(key)
        y.append(value)

    sortx = [x for _, x in sorted(zip(y, x))]
    sorty = sorted(y)

    data = [go.Bar(
        x=sortx,
        y=sorty,
        # orientation='h',
        hoverinfo='x+y'
    )]

    layout = go.Layout(
        title=go.layout.Title(
            text=attribute_name
        ),
        font = dict(family='Arial', size=12, color='#7f7f7f')
    )

    fig = go.Figure(data=data, layout=layout)
    # off_plot(fig, filename='./output/visualization/summary_' + str(attribute_name) + '.html')
    off_plot(fig, filename='./output/visualization/summary_' + str(attribute_name) + '.html')