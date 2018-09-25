#with user input, print dictionary containing tally of how many times each letter was used

#user input

word = input("Please enter a word:").lower()
#create function
def histogram(txt):
    letter_dict = {}
    i = 0
    for x in set(txt):
        letter_dict[x] = txt.count(x)
    return letter_dict

print(histogram(word))