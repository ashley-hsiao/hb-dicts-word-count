word_doc = open("test.txt")

def line_break(word_doc):
    combined_list_of_words = []

    for line in word_doc:
        line = line.rstrip()

        # print line

        words = line.split(" ")

        combined_list_of_words += words 
    print combined_list_of_words

    print len(combined_list_of_words)


    unique_words = {}
    
    value = 1

    for word in combined_list_of_words:
        unique_words[word] = value

        if word in unique_words:
            value += 1

    print unique_words

    print len(unique_words)

line_break(word_doc)




#     words_list = []

#     for word in words:
#         if word not in words_list:
#             words_list.append(word)

#     print words_list

# # word_doc.close()
