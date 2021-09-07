import json
def word_search(user_in: str):
    data = json.load(open('data.json', 'r'))
    try:
        for item in data[user_in]:
          print(f'-> {item}')
    except:
        print('No dictionary entry found')
        redo = input('Try again? type Y or N: ')
        if redo.lower() == 'y':
            word_search(input('Please enter a word to have defined: '))
        else:
            print('Bye!')

print("Sam's compact dictionary.")
word_search(input('Please enter a word to have defined: '))
