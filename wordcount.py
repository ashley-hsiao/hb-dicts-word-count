word_doc = open("test.txt")

combined_list_of_words = []

for line in word_doc:
    line = line.rstrip()

    # print line

    words = line.split(" ")

    combined_list_of_words += words 

# Iterates each line from text.txt, split, and appends to combined_list_of_words.

print combined_list_of_words


unique_words = {}

value = 1

for word in combined_list_of_words:
    unique_words[word] = value

    # print word
    # print unique_words[word]
    # print value

    if word in unique_words:
        unique_words[word] += 1

    # else:
    #     pass


# We iterated through combined_list_of_words and assigned key value pairs to unique_words dictionary

print unique_words







#     words_list = []

#     for word in words:
#         if word not in words_list:
#             words_list.append(word)

#     print words_list

# # word_doc.close()
