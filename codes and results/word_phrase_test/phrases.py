import nltk
# @Author Ayberk

whole_text = ""
for i in range(1, 10):
    file=open("C:\\Users\\ayber\\OneDrive\\Masaüstü\\hum\\2." + str(i)+".txt",'r')
    section_string = file.read()
whole_text += "\n" + section_string

analysis_of_text(whole_text, "The Utopia")

def analysis_of_text(utopia, header):

    word_tokenized = nltk.word_tokenize(utopia.lower())
    for n in range(2, 10):

        print("****** " + str(n) + " PHRASES IN " + header + " ******** ")
        arr = list(nltk.ngrams(lower_case_arr, n))
        freq_arr = nltk.FreqDist(arr)
        for array_of_strings, count in freq_arr.most_common(10):
            print(" ".join(list(array_of_strings)), "       ", count)


