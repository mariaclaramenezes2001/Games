
import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}


WORDLIST_FILENAME = "words_words_game.txt"

def load_words():

    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

def get_word_score(word, n):
   
    word=str.lower(word)
    word_lenght = len(word)
    
    first= 0
    for letter in word:
        if letter != "*":
            first = first + SCRABBLE_LETTER_VALUES[letter]
        
    
    second = max(7*word_lenght - 3*(n-word_lenght), 1)
    score= first*second
    return score


#
def display_hand(hand):
    string=""
    for letter in hand.keys():
        for j in range(hand[letter]):
             string = string + letter + ' '
    print("\n")
    return string
             


def deal_hand(n):

    hand={}
    num_vowels = int(math.ceil(n / 3))-1

    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    wild = {"*": 1}
    hand.update(wild)
    
    return hand


def update_hand(hand, word):
    
    word=str.lower(word)
    new_hand = hand.copy()
    for letter in word:
        new_hand[letter] = new_hand.get(letter,0)-1
        if new_hand[letter] ==0:
            new_hand[letter] == 0
    return new_hand


def is_valid_word_pre(word, hand, word_list):
   
    low_word = str.lower(word)

    letters = hand.copy()
    if low_word not in word_list:
        return False
    
    for letter in low_word:
        if letters.get(letter,0)==0:
            print (letters.get(letter,0))
            return False
        else:
            letters[letter] =letters[letter] - 1
    else:
        return True
    
def is_valid_word(word, hand, word_list):
   
    low_word = str.lower(word)

    letters = hand.copy()
    
    okay=0
    if "*" not in low_word and low_word not in word_list:
        return False
    
    for letter in low_word:
        
        if letter=="*":
            for vowel in VOWELS:
                vowel_word = low_word.replace("*", vowel)
                if vowel_word not in word_list:
                    okay=okay+1
            if okay==5:
                return False
            
        
        elif letters.get(letter,0)==0:
            print (letters.get(letter,0))
            return False
        else:
            letters[letter] =letters[letter] - 1
    
    else:
        return True


def calculate_handlen(hand):
    n=0
    for x in hand:
        if hand[x]!=0:
            n=n+1
    return n

def play_hand(hand, word_list):  
    total_score = 0
    
    while not all(x == 0 for x in hand.values()): 
        
        print ("Current hand:",display_hand(hand))
        
        word=input("Enter word, or !! to indicate that you are finished:")
        
        if word == "!!":
            print("Score for this hand:", total_score)
            return total_score
        else:
            if is_valid_word(word, hand, word_list):
                hand=update_hand(hand, word)
                n = calculate_handlen(hand)             
                score= get_word_score(word,n)
                print("The word", word,"earned", score, "points.")
                total_score = total_score + score
                print("Total :", total_score)
            else:
                print("That is not a valid word. Please choose another word.")
    if all(x == 0 for x in hand.values()):
         print("You have ran out of letters.")
         print("Score for this hand:", total_score)
    
    return total_score
        
        

def substitute_hand(hand, letter):
    
    set = list(hand.keys())
    alphabet = string.ascii_lowercase
    dic=hand.copy()
    a= random.choice(alphabet)
    
    for i in range(dic[letter]):
        while a in set:
            a=random.choice(alphabet)
        else:
            if a in dic.keys():
                dic[a] = dic[a] +1
                a=random.choice(alphabet)
            else:
                dic[a] = 1
                a=random.choice(alphabet)
    dic[letter] = 0
        
    return dic
       
    
def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
   
    """
    number_of_hands = int(input("Enter total number of hands:"))
    final_score = 0
    substitute=0
    replay=0
    
    for i in range(number_of_hands):
        hand=deal_hand(HAND_SIZE)
        print("Current hand:", display_hand(hand))
        
        if substitute == 0:
            answer=input("Would you like to substitute a letter? Type yes or no: ")
        
            if answer == "no":
                old=play_hand(hand, word_list)
                final_score = final_score + old
                
                if replay ==0:
                    answer = input("Would you like to replay the hand?")
                    if answer == "yes":
                        final_score = final_score + max(old, play_hand(hand,word_list))
                        replay=1
                
            
            elif answer == "yes":
                
                substitute=1
                letter = input("Which letter?" )
                hand = substitute_hand(hand, letter)
                old=play_hand(hand, word_list)
                final_score = final_score + old
                if replay ==0:
                    answer = input("Would you like to replay the hand?")
                    if answer == "yes":
                        final_score = final_score + max(old, play_hand(hand,word_list))
                        replay=1

          
        
        else:
            print("New hand:")
            final_score = final_score + play_hand(hand,word_list)
            if replay ==0:
                    answer = input("Would you like to replay the hand?")
                    if answer == "yes":
                        final_score = final_score + max(old, play_hand(hand,word_list))
                        replay=1
            
    print("- - - - - - - - - - - - - - - -")        
    print("Game over!")
    print("Total:", final_score)
    return final_score




if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
