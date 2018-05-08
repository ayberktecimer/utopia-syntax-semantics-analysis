# @Author Ayberk
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import numpy as np

objects = ('Introduction to Utopia','Cities, Amaurot','Magistrates','Occupations','Social Relations',' Travel',' Wealth','Philosophies','Learning','Slaves','Death','Marriage','Laws and Punishments','Foreign Policies','military affairs',' Religions','True Commonwealth')
y_pos = np.arange(len(objects))
performance = [1.5, 5.25, 4.375, 2.987, 4.375, 1.375, 18.25, 84.265,23.0, -1.875, 1.5, -1.5, 0.875, 2.125, -3.375,42.875, 10.75]

 
plt.barh(y_pos, performance, align='center', alpha=0.5, color='r')
plt.yticks(y_pos, objects)
plt.xlabel('Sentiment Positivity')
plt.title('Utopia Sentiment Analysis')
 
plt.show()


