#open a file
# generate dict

#def rename_files():
    # (1) get file names from a folder
    #file_list = os.listdir(r"C:\Users\BudgIT\Pictures\prank")
    #print(file_list)
    # (2) for each file, rename file
WORDLIST_FILENAME = "words.txt"

def load_words():
    withinFile = open(WORDLIST_FILENAME, 'r')
    content = withinFile.read()
    wordlist = content.split()
    return wordlist


list_of_words = load_words()



#def link_with_dict(word_length):
    #if word in wordlist:
         #and len(word) == 3
            #print("\nThree letter words from list are: ", {"3letter":[]}, word)
    #else:
        #if word in wordlist:
            #and len(word) == 2
                #print("\nTwo letter words are: ", {"2letters":[]}, word)
    
#return 0
def generate_dict(wordlist):
    word_dict = {} #init
    for word in wordlist:
        print(word)
        word_dict[word] = len(word)
    return word_dict



#print(generate_dict(list_of_words))



def dict_group(wordlist):
    word_group_dict = {}
    for word in wordlist:
        word_key = str(len(word)) + "letters"
        if word_key in word_group_dict.keys():
            word_group_dict[word_key].append(word)
        else:
            new_list = [word]
            word_group_dict[word_key] = new_list
    return word_group_dict
print(dict_group(list_of_words))['3letters']
#print(dict_group(list_of_words))





