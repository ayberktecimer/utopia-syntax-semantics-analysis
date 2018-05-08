import nltk
import seaborn
from nltk.corpus import sentiwordnet as swn
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#@Author Ayberk
def sentiment_analyze(utopia, header):
    tokenized_word = nltk.word_tokenize(utopia.lower())

    tokenized_scores = sentiment_word(tokenized_word)
    print("Sentiment Score for " + header + ": " + str(tokenized_scores[0]))
    return tokenized_scores[0]

whole_text = ""
arr_of_results = []
indexes = [i for i in range(18)]
for i in range(1, 18):
    file=open("C:\\Users\\ayber\\OneDrive\\Masaüstü\\hum\\second_iteration\\2." + str(i)+".txt",'r')
    section_string = file.read()
    whole_text += "\n" + section_string
    arr_of_results.append(sentiment_analyze(section_string, "Book " + str(i)))
    print()
sns.axes_style('white')
sns.set_style('white')

def sentiment_word(dummy, arr=[]):
    matched = nltk.pos_tag(dummy)
    arr_of_positives = []
    arr_of_negatives = []
    temp_result = 0
    for my_arr, treebank in matched:
        last_result = sentiment_text(my_arr, treebank, arr)
        if last_result:
            temp_result += last_result
            if last_result > 0:
                arr_of_positives.append(my_arr.lower())
            else:
                arr_of_negatives.append(my_arr.lower())
    return temp_result, set(arr_of_positives), set(arr_of_negatives)

def data_of_sentiment(collosum, arr=[]):
    holder = {}
    arr_of_positives = []
    arr_of_negatives = []
    for section_holder in collosum.fileids():
        arr = collosum.words(section_holder)
        results, plus, minus = sentiment_word(arr, arr)
        holder[section_holder] = results
        [arr_of_positives.append(positive) for positive in plus]
        [arr_of_negatives.append(negative) for negative in minus]
    return holder, set(arr_of_positives), set(arr_of_negatives)

def sentiment_text(word, holder, arr=[]):
    my_arr = pos_analysis(holder, arr)
    if my_arr:
        temp_result = list(swn.senti_synsets(word, my_arr))
        if temp_result:
            return temp_result[0].pos_score() - temp_result[0].neg_score()




