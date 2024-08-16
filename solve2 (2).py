def count_unique_words(sentence):
    words = sentence.split()   

    unique_words = set(words)
    
    return len(unique_words)

sentence = input("Enter a sentence: ")

num_unique_words = count_unique_words(sentence)

print(f"The number of unique words in the sentence is: {num_unique_words}")
