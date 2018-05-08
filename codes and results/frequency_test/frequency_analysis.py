import nltk
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
# @Author Ayberk
whole_text = ""
for i in range(1, 18):
    file=open("C:\\Users\\ayberk\\OneDrive\\Masaüstü\\hum\\2." + str(i)+".txt",'r')
    utopia_string = file.read()
    whole_text += u"{}".format(utopia_string)
    
def cloud_function(bookStr):
    # lower max_font_size
    stopwords = set(STOPWORDS)
    cloud_arr = WordCloud(max_font_size=50, background_color="white").generate_from_frequencies(bookStr)
    plt.figure()
    plt.imshow(cloud_arr, interpolation="bilinear")
    plt.axis("off")
    plt.show()
import io

def analysis_of_words(utopia_string, header):

    tokenized_words = nltk.word_tokenize(utopia_string.lower())
    lower_cased_words = [word for word in tokenized_words if word[0].isalpha()]

    frequency_of_lower_cased = nltk.FreqDist(lower_cased_words)
    cloud_function(frequency_of_lower_cased)


    frequency_of_lower_cased.tabulate(15)

    plt.figure()
    frequency_of_lower_cased.plot(15, title="Top Frequency Words in " + header)

    length_of_tokenized_words = [len(w) for w in lower_cased_words]

    frequency_of_tokenized_word_length = list(sorted(nltk.FreqDist(length_of_tokenized_words).items()))

    length_of_tokenized_frequency = [f[0] for f in frequency_of_tokenized_word_length]
    value_of_tokenized_words = [f[1] for f in frequency_of_tokenized_word_length]
    plt.figure()
    plt.plot(length_of_tokenized_frequency, value_of_tokenized_words)
    plt.title("Word Length Frequencies in " + header)
    plt.xlabel('Word Length')
    plt.ylabel('Word Count')

    plt.figure()
    words_array = nltk.corpus.stopwords.words("English")
    graph=nltk.FreqDist(lower_cased_words)
    graph.tabulate(15)
    graph.plot(15, title="Top Frequent Words in " + header)

    content_array=[]
    for word in lower_cased_words:
        if word not in words_array:
            content_array.append(word)
    content_term_graph=nltk.FreqDist(content_array)
    content_term_graph.tabulate(15)
    content_term_graph.plot(15, title="Top Frequent Content Terms in " + header)
    # noun division
    nouns=[]
    for sentence in content_array:
        for word,pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
            if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'):
             nouns.append(word)
    frequent_content_nouns = nltk.FreqDist(nouns)
    frequent_content_nouns.tabulate(15)
    frequent_content_nouns.plot(15, title="Top Frequency Nouns in " + header)
    #pronoun division
    pronouns=[]
    for sentence in content_array:
        for word,pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
            if (pos == 'PRP' or pos == 'PRP$'):
             pronouns.append(word)
             
    frequent_content_nouns = nltk.FreqDist(nouns)
    frequent_content_nouns.tabulate(15)
    frequent_content_nouns.plot(15, title="Top Frequent Nouns in " + header)

    pronoun_graph=nltk.FreqDist(pronouns)
    pronoun_graph.tabulate(15)
    pronoun_graph.plot(15, title=" Top Frequent Pronouns in " + header)

    #adjective division
    adjs=[]
    for sentence in content_array:
        for word,pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
            if (pos == 'JJ' or pos == 'JJR' or pos== 'JJS'):
             adjs.append(word)
    adj_graph=nltk.FreqDist(adjs)
    adj_graph.tabulate(15)
    adj_graph.plot(15, title=" Top Frequent Adjectives in " + header)
    #adverb division
    advb=[]
    for sentence in content_array:
        for word,pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
            if (pos == 'RB' or pos == 'RBR' or pos== 'RBS'):
             advb.append(word)
    advb_graph=nltk.FreqDist(advb)
    advb_graph.tabulate(15)
    advb_graph.plot(15, title=" Top Frequent Adverbs in " + header)
    
    cloud_function(frequent_content_nouns)
    cloud_function(pronoun_graph)
    cloud_function(adj_graph)
    cloud_function(advb_graph)
    
    
    theText = nltk.Text(tokenized_words)
analysis_of_words(whole_text, "The Utopia")
