import nltk
import matplotlib.pyplot as plt

# @Author Ayberk

whole_text = ""
for i in range(1, 10):
    file=open("C:\\Users\\ayber\\OneDrive\\Masaüstü\\hum\\2." + str(i)+".txt",'r')
    bookStr = file.read()
    whole_text += "\n" + bookStr


def analysis_of_word_pos(utopia, header):
    tokenized_words = nltk.word_tokenize(utopia.lower())
    arr = nltk.pos_tag(tokenized_words)

    arr1 = [pos for word, pos in arr]
    titles = [pos if pos.isalpha() else "." for pos in arr1]
    frequency_of_titles = nltk.FreqDist(titles)
    frequency_of_titles.tabulate(25)
    frequency_of_titles.plot(25, title="Tag Frequencies in " + header)

def pos_percentage_calculator(string, pos):
    tokenized_words = nltk.word_tokenize(string)
    arr = nltk.pos_tag(tokenized_words)
    arr1 = [word for word, p in arr if pos == p]
    return len(arr1) / len(arr)

analysis_of_word_pos(whole_text, "The Utopia")
print("Utopia" + " has", '{:.2%}'.format(pos_percentage_calculator(bookStr, "JJ")), "adjectives")
print("Utopia" + " has", '{:.2%}'.format(pos_percentage_calculator(bookStr, "NN")), "noun")
print("Utopia" + " has", '{:.2%}'.format(pos_percentage_calculator(bookStr, "NNS")), "noun")
print("Utopia" + " has", '{:.2%}'.format(pos_percentage_calculator(bookStr, "NNP")), "noun")
print("Utopia" + " has", '{:.2%}'.format(pos_percentage_calculator(bookStr, "NNPS")), "noun")
print("Utopia" + " has", '{:.2%}'.format(pos_percentage_calculator(bookStr, "PRP")), "pronoun")
print("Utopia" + " has", '{:.2%}'.format(pos_percentage_calculator(bookStr, "PRP$")), "pronoun")
print("Utopia" + " has", '{:.2%}'.format(pos_percentage_calculator(bookStr, "JJR")), "adj")
print("Utopia" + " has", '{:.2%}'.format(pos_percentage_calculator(bookStr, "JJS")), "adj")
print("Utopia" + " has", '{:.2%}'.format(pos_percentage_calculator(bookStr, "RB")), "adverb")
print("Utopia" + " has", '{:.2%}'.format(pos_percentage_calculator(bookStr, "RBR")), "adverb")
print("Utopia" + " has", '{:.2%}'.format(pos_percentage_calculator(bookStr, "RBS")), "adverb")
