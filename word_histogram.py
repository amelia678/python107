# with user input, print dictionary containing tally of how many times each word in sentence
# was used

sentence = input("Please enter a sentence:").lower()
 
def histogram(str):
    counts = {}
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts            

print(histogram(sentence))