import json
import difflib
from os import close
def word_search(user_in: str):
    
    data = json.load(open('data.json', 'r'))
    if user_in in data.keys():
        print(f'Definition for {user_in}')
        for item in data[user_in]:
          print(f'-> {item}')

    elif len(difflib.get_close_matches(user_in,data.keys(),cutoff=0.8)) > 0:
        closest_word = difflib.get_close_matches(user_in,data.keys(),cutoff=0.8)[0]
        print(f"You searched for '{user_in}', but this doesn't return any results.")
        user_choice = input(f'Did you mean to search for {closest_word}? Y/N: ')
        # Take a user choice to see if they'd like to proceed with suggested word
        if user_choice.lower() == 'y':
            print(f'Definition for {closest_word}')
            for item in data[closest_word]:
                print(f'-> {item}')
        else:
            word_search(input('Please enter a new word: '))
    else:
        print('No dictionary entry found')
        redo = input('Try again? type Y or N: ')
        if redo.lower() == 'y':
            word_search(input('Please enter a word to have defined: '))
        else:
            print('Bye!')

print("Sam's compact dictionary.")
word_search(input('Please enter a word to have defined: '))
