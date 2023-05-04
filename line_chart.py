# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    line_chart.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yel-hadd <yel-hadd@mail.com>               +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/04 19:28:06 by yel-hadd          #+#    #+#              #
#    Updated: 2023/05/04 19:28:06 by yel-hadd         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import plotly.graph_objs as go
import pandas as pd

# Load world population data from CSV file
df = pd.read_csv('dataset1.csv')

df = df.loc[df['Country Name'] == 'Morocco']
df.pop('Indicator Name')
df.pop('Indicator Code')
df = df.melt(id_vars=['Country Name', 'Country Code'], var_name='Year', value_name='Population')

# Rename the columns
df.rename(columns={'Country Name': 'Country'}, inplace=True)

# Drop any rows that have missing values
df = df.dropna()

# Print the DataFrame
print(df.keys())

# Create a Plotly figure object
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=df['Year'],
    y=df['Population'],
    name='Morocco Population',
    mode='lines',
    line=dict(color='royalblue', width=2)
))

fig.update_layout(
    title='Morocco Population Over Time',
    xaxis_title='Year',
    yaxis_title='Population (in millions)'
)

fig.show()
