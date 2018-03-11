class FileAction():
    def __init__(self, filename):
        self.filename = filename
        return None
    def _loadWords(self):
        wordfile = open(self.filename, 'r')
        content = wordfile.read()
        wordlist = content.split()
        return wordlist
    import random
    def pick_random_word(self):
        word = random.choice(self.loadWords())
        return word
    # output = fileAction(words.txt) to instantiate the class above
      #output.pickord
    # PART TWO for staight up use without initialising
    #from gamefiles import FileAction as fa
    class FileAction():
        def __init__(self, filename):
            self.filename = filename
            return None
        def _loadWords(self):
            wordfile = open(self.filename, 'r')
            content = wordfile.read()
            wordlist = content.split()
            return wordlist
        @classmethod #decorating a method with classmethod does init behind the scene self-contained ready for use for you
        #you don't have to init before using it
        def pickword(self):
            word = random.choice(self.loadWords())
            return word

            #usage of the class above
        #fa.pickword(words.txt)
    from FileAction import pick_random_word
    class GameEngine():
        #class variables
        word = choose_word('words.txt')
        length = len(word)
        max_attempts = length + 1
        available_letters = "a b c d e f g h i j k l m n o p q r s t u v w x y z"

        def _get_guess(): #_get_guess makes it only accessible to 
            guess = input("/n/nPlease get a letter").lower()
            return guess
        def _del_alphabeth(alphabet, choice_range):
            if alphabeth in choice_range:
                letters_remaining = str.replace(choice_range,alphabeth,"_ ")
            return letters_remaining
        def _progress_so_far(word, guessed_letters):
            newstring = []
            for index in range(len(word)):  # strings are indexed just like numbers
                letters = word[index]
                if letters in guessed_letters:
                    newstring.append(letters)
                else:
                    newstring.append("_")
            return newstring
        @classmethod
        def eval_guess(self):
            guess = self,_get_guess()
            word = self.word
            max_attempts = self.length + 1
            #available_letters = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
            guessed_letters = []
            newstring = []
            correct_guesses = 0
            wrong_guesses = 0
            while True  and max_attempts > 1:
        # Ensures that only a single alphabeth is entered at a time 
                while (guess == '' or len(guess) > 1) : # 
                     print ("  Guess must be a single letter !")
                     guess = get_guess()
        # Prevents guessing any letter more than once
                if guess in guessed_letters:
                    print (" This letter has been guessed!")
                    guess = get_guess()
            
                else:
                    guessed_letters.append(guess)
            # performs the actual check for the guessed letter in the word

                    if guess not in word:
                        print ("   Opps!", guess, "is not in the word")
                        print ("   -----------------")
                        max_attempts -= 1  
                        print ("  you have ", max_attempts, "attempts left")
                        available_letters = del_alphabeth(guess,available_letters)
                        print ("  Available letters: ", available_letters)
                        wrong_guesses += 1
                        guess = get_guess()

                    else:  
                        print ("   Good guess: '", guess, "' appeared", word.count(guess), "times")
                        print ("   progress so far: ", progress_so_far(word,guessed_letters))
                        available_letters = del_alphabeth(guess,available_letters)
                        print ("\n  Available Letters:  ", available_letters)

                        correct_guesses += word.count(guess) # gets 
                        if  correct_guesses == length:
                            print (" \n\n\t\t Great Job! the word is ", word.upper(), "!!!")
                            print ("\t\t wrong guesses: ",wrong_guesses)
                            break
                        else:
                            guess = get_guess()
                            guess = get_guess()
            else:
                print ("\n\t ************************************")
                print ("\t\t\t\tGame Over!".upper()) # terminate the game
                print ("\t ************************************")
                print ("\n\t\t The word is ", word.upper())
                exit()
                            
            
            
