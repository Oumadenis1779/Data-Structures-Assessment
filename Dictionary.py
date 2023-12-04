import string

def word_frequency(sentence):

    # convert to lowercase and remove puntuations
    translator = str.maketrans("", "", string.punctuation)
    sentence = sentence.translate(translator).lower()

    
    words = sentence.split()

    # Counting the frequency of each word using a dictionary
    frequency_dict = {}
    for word in words:
        frequency_dict[word] = frequency_dict.get(word, 0) + 1

    return frequency_dict

# Sample input
sentence = "This is a test sentence. This sentence is a test."

result = word_frequency(sentence)
print(result)
