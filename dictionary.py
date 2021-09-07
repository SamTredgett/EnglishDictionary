import json
import difflib
def word_search(user_in: str):
    
    data = json.load(open('data.json', 'r'))
    closest_word = difflib.get_close_matches(user_in,data.keys())[0]
    if user_in in data:
        print(f'Definition for {user_in}')
        for item in data[user_in]:
          print(f'-> {item}')
    elif closest_word in data:
        print(f'Definition for {closest_word}')
        for item in data[closest_word]:
          print(f'-> {item}')
    else:
        print('No dictionary entry found')
        redo = input('Try again? type Y or N: ')
        if redo.lower() == 'y':
            word_search(input('Please enter a word to have defined: '))
        else:
            print('Bye!')

print("Sam's compact dictionary.")
word_search(input('Please enter a word to have defined: '))
