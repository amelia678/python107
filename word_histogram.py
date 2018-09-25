# with user input, print dictionary containing tally of how many times each word in sentence
# was used

sentence = input("Please enter a sentence:").lower()
 
def histogram(str):
    counts = {} #empty dictionary
    words = str.split() #splits string into words

    for word in words:
        if word in counts:
            counts[word] += 1 #if word is already in dictionary, add count
        else:
            counts[word] = 1 # if word is not in dictionary, add key and value of 1
    return counts            

print(histogram(sentence))