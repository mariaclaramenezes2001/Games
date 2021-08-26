
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
  
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
  
    return random.choice(wordlist)


wordlist = load_words()
secret_word=choose_word(wordlist)



def is_word_guessed(secret_word, letters_guessed): 
    word_letters=[]
    for i in range(len(secret_word)):
        word_letters=word_letters+[secret_word[i]]
        
    word_letters=list(set(word_letters))

    found=[]
    
    letters_guessed = list(set(letters_guessed))
    
    for i in range(len(word_letters)):
        if word_letters[i] not in letters_guessed:
            found=found+[1]          

    if found ==[]:
        return True
    else:
        return False
    
    
        

def get_guessed_word(secret_word, letters_guessed):
    word_as_str=" "
    word_as_list=[]
    
    for i in range(len(secret_word)): 
        '''converte a palavra secreta numa lista de letras ordenadas e repetidas
        '''
        word_as_list=word_as_list+[secret_word[i]]
     
    
    for i in range(len(word_as_list)):
        '''
        compara cada letra na palavra secreta com as letras adivinhadas e forma a 
        palavra com _ e letras
        '''
        
        if word_as_list[i] in letters_guessed:
            word_as_str = word_as_str + word_as_list[i]
            word_as_str = word_as_str + " "
        else:
            word_as_str = word_as_str + "_"
            
            word_as_str = word_as_str + " "
    return word_as_str


def get_available_letters(letters_guessed):
    available=''
    for i in range(len(string.ascii_lowercase)):
        if string.ascii_lowercase[i] not in letters_guessed:
            available=available+string.ascii_lowercase[i]
    return available
    
def not_repeated(letter, letters_guessed):
    if letter not in letters_guessed:
        return True
    
def round (guesses, warnings, letters_guessed): 
        print("You have", guesses, "guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))
        
def add(letter,letters_guessed):
    letters_guessed = letters_guessed +[letter]
    return letters_guessed
    
def remove_guesses(guesses):
    guesses=guesses-1
    return guesses
    
def remove_warnings(warnings):
    warnings = warnings -1
    return warnings
def is_vowel(letter):
    if (letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u" ):
        return True
        

def hangman(secret_word):
   
    
    print("\n")
    print("Welcome to the game of Hangman!")
    print("The secret word is", len(secret_word), "letters long.")
    print("You have 3 warnings left.")
    
    
   
    guesses = 6
    warnings = 3
    letters_guessed=[]
    
    while not is_word_guessed(secret_word, letters_guessed):
        guesses_remaining = 6 - guesses
        unique = len (list(set(secret_word)))  
        score = guesses_remaining*unique
        
        if guesses == 0:
            print ("Zero guesses left. You lost.")
            print("The secret word was",secret_word)
            
            return 0
        
        else:
            print("* * * * * * * * * * * * *")
            round(guesses, warnings, letters_guessed)
    
            letter= input("Please guess a letter:    ")
            
      
            if letter in string.ascii_lowercase and not_repeated(letter, letters_guessed):
                letters_guessed = add(letter, letters_guessed)
                if letter not in secret_word:
                    print("That letter is not in the secret word :( ")
                    print(get_guessed_word(secret_word, letters_guessed))
                    if is_vowel(letter):
                        guesses = remove_guesses(guesses)
                        guesses= remove_guesses(guesses)
                    else:
                        guesses= remove_guesses(guesses)
                        
                        
                else:
                    print("Good Guess!")
                    print(get_guessed_word(secret_word, letters_guessed))
            
            
            elif letter not in string.ascii_lowercase:
                print("Oops! That is not a valid letter.")
                
        
                if warnings!=0:
                    warnings = remove_warnings(warnings)
                else:
                    guesses = remove_guesses(guesses)
                print("You have", warnings ,"warnings left.")
                print(get_guessed_word(secret_word, letters_guessed))
                
                
            elif not not_repeated(letter, letters_guessed):
                print("OOPS! You have already guessed that letter.")
        
                if warnings!=0:
                    warnings = remove_warnings(warnings)
                    print("You now have", warnings ,"warnings left.")
                else:
                    guesses = remove_guesses(guesses)
                    print("You now have", guesses ,"guesses left.")
                
                print(get_guessed_word(secret_word, letters_guessed))
                
    
        
    if is_word_guessed(secret_word, letters_guessed):
        
        print("*************************************")
        print("Congratulations! You won the hangman's game")
        print("*************************************")
        print("Your Score is", score)
  
           
          




def match_with_gaps(my_word, other_word):
    my_word=my_word.replace(" ","")
    okay=[]
    if len(my_word)!=len(other_word):
        return False
    else:
        for i in range(len(my_word)):
            if my_word[i] == "_":
                if other_word[i] not in my_word:
                    okay=okay+[]
                else:
                    return False
            elif my_word[i] != other_word[i]:
                okay=okay+[1]
        if okay==[]:
            return True
        else:
            return False
            


def show_possible_matches(my_word):
   matches=[]
   my_word=my_word.replace(" ","")
   for other_word in wordlist:
       if match_with_gaps(my_word, other_word):
           matches=matches + [other_word]
   return matches



def hangman_with_hints(secret_word):
    '''
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    '''
    
    print("\n")
    print("Welcome to the game of Hangman!")
    print("The secret word is", len(secret_word), "letters long.")
    print("You have 3 warnings left.")
    
    
   
    guesses = 6
    warnings = 3
    letters_guessed=[]
    
    while not is_word_guessed(secret_word, letters_guessed):
        guesses_remaining = 6 - guesses
        unique = len (list(set(secret_word)))  
        score = guesses_remaining*unique
        
        if guesses == 0:
            print ("Zero guesses left. You lost.")
            print("The secret word was",secret_word)
            
            return 0
        
        else:
            print("* * * * * * * * * * * * *")
            round(guesses, warnings, letters_guessed)
    
            letter= input("Please guess a letter:    ")
            
            if letter == "*":
                print("The possible words are:")
                print(show_possible_matches(get_guessed_word(secret_word, letters_guessed)))
                
                
            elif letter in string.ascii_lowercase and not_repeated(letter, letters_guessed):
                letters_guessed = add(letter, letters_guessed)
                if letter not in secret_word:
                    print("That letter is not in the secret word :( ")
                    print(get_guessed_word(secret_word, letters_guessed))
                    if is_vowel(letter):
                        guesses = remove_guesses(guesses)
                        guesses= remove_guesses(guesses)
                    else:
                        guesses= remove_guesses(guesses)
                        
                        
                else:
                    print("Good Guess!")
                    print(get_guessed_word(secret_word, letters_guessed))
            
            
            elif letter not in string.ascii_lowercase:
                print("Oops! That is not a valid letter.")
                
        
                if warnings!=0:
                    warnings = remove_warnings(warnings)
                else:
                    guesses = remove_guesses(guesses)
                print("You have", warnings ,"warnings left.")
                print(get_guessed_word(secret_word, letters_guessed))
                
                
            elif not not_repeated(letter, letters_guessed):
                print("OOPS! You have already guessed that letter.")
        
                if warnings!=0:
                    warnings = remove_warnings(warnings)
                    print("You now have", warnings ,"warnings left.")
                else:
                    guesses = remove_guesses(guesses)
                    print("You now have", guesses ,"guesses left.")
                
                print(get_guessed_word(secret_word, letters_guessed))
                
    
        
    if is_word_guessed(secret_word, letters_guessed):
        
        print("*************************************")
        print("Congratulations! You won the hangman's game")
        print("*************************************")
        print("Your Score is", score)
  
           






    
#hangman(secret_word)
hangman_with_hints(secret_word)
