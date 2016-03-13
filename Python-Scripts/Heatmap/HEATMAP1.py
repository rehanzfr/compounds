import matplotlib.pyplot as plt
from matplotlib import cm
import pandas as pd
from urllib2 import urlopen
import numpy as np

page = urlopen("http://datasets.flowingdata.com/ppg2008.csv")
nba = pd.read_csv(page, index_col=0)

# Normalize data columns
nba_norm = (nba - nba.mean()) / (nba.max() - nba.min())

# Sort data according to Points, lowest to highest
# This was just a design choice made by Yau
# inplace=False (default) ->thanks SO user d1337
nba_sort = nba_norm.sort('PTS', ascending=True)

nba_sort['PTS'].head(10)


# Plot it out
fig, ax = plt.subplots()
heatmap = ax.pcolor(nba_sort, cmap=plt.cm.Greens, alpha=0.7)

# Format
fig = plt.gcf()
fig.set_size_inches(15, 20)

# turn off the frame
ax.set_frame_on(False)


# put the major ticks at the middle of each cell
ax.set_yticks(np.arange(nba_sort.shape[0]) + 0.5, minor=False)
ax.set_xticks(np.arange(nba_sort.shape[1]) + 0.3, minor=False)

# want a more natural, table-like display
ax.invert_yaxis()
ax.xaxis.tick_top()

# Set the labels

# label source:https://en.wikipedia.org/wiki/Basketball_statistics
labels = [
    'Games', 'Minutes', 'Points', 'Field goals made', 'Field goal attempts', 'Field goal percentage', 'Free throws made', 'Free throws attempts', 'Free throws percentage',
    'Three-pointers made', 'Three-point attempt', 'Three-point percentage', 'Offensive rebounds', 'Defensive rebounds', 'Total rebounds', 'Assists', 'Steals', 'Blocks', 'Turnover', 'Personal foul']

# note I could have used nba_sort.columns but made "labels" instead
ax.set_yticklabels(nba_sort.index, minor=False)
ax.set_xticklabels(labels, rotation=45, ha='left', minor=False)


ax.grid(False)

# Turn off all the ticks
ax = plt.gca()

for t in ax.xaxis.get_major_ticks():
    t.tick1On = False
    t.tick2On = False

for t in ax.yaxis.get_major_ticks():
    t.tick1On = False
    t.tick2On = False
# For ploting the values
cbar = plt.colorbar(heatmap)
cbar.set_label('Some Units')
plt.show()
# You can also directly save the plot by uncommenting this command but it is better to save using plt.show() as earlier.
#plt.savefig('figure.png')
