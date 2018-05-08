# @Author Ayberk
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

import plotly.plotly as py
#cloud=WordCloud(max_font_size=40, background_color="white").generate_from_frequencies(text)

#plt.imshow(cloud)
#plt.axis('off')
#plt.show()
y = [1.5, 5.25, 4.375, 2.987, 4.375, 1.375, 18.25, 84,265,23.0, -1.875, 1.5, -1.5, 0.875, 2.125, -3.375]
N = len(y)
x = range(N)
width = 1/1.5
plt.bar(x, y, width, color="blue")


fig = plt.gcf()
plot_url = py.plot_mpl(fig, filename='mpl-basic-bar')


