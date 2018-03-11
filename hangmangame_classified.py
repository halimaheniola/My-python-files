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
        #fa.pickword(words.txt)word
    
            
            

