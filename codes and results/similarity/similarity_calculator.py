import nltk
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.manifold import MDS
from scipy.cluster.hierarchy import ward, dendrogram
# @Author Ayberk
whole_text = []
titles_of_sections = [str(i) for i in range(1, 18)]
for i in range(1, 18):
    file=open("C:\\Users\\ayberk\\OneDrive\\Masaüstü\\hum\\second_iteration\\2." + str(i)+".txt",'r')
    bookStr = file.read()
    whole_text.append(bookStr)
(distances, positions) = similarity_holder(whole_text, "Utopia")

xvalues = positions[:, 0]
yvalues = positions[: ,1]

plt.figure(figsize=(10,10))
for x, y, name in zip(xvalues, yvalues, titles_of_sections):
    plt.scatter(x, y)
    plt.text(x, y, name.replace(".txt", ""))
plt.show()

def similarity_holder(holder, header):
    # simple lowercase tokenize
    tokens = nltk.word_tokenize(bookStr.lower())

    arr = set(
        [word.lower() for word in nltk.word_tokenize(" ".join(holder)) if any([holder for holder in word if holder.isalpha()])])
    frequency_arr = [nltk.FreqDist(nltk.word_tokenize(document.lower())) for document in holder]
    pd.DataFrame(frequency_arr).fillna(0)

    arr1 = TfidfVectorizer().fit_transform(holder)
    pd.DataFrame(arr1.toarray())

    holder_to_arr = TfidfVectorizer().fit_transform(holder)
    length_calculator = 1 - cosine_similarity(holder_to_arr)


    mds = MDS(dissimilarity="precomputed", random_state=1)
    positions = mds.fit_transform(length_calculator)

    return length_calculator, positions

plt.figure(figsize=(10,10))
linkage_matrix = ward(distances)
dendrogram(linkage_matrix, labels=titles_of_sections, orientation="right");
plt.show()