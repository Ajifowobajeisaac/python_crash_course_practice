'''This program prompts users for their wishlist and saves in a txt file'''

from pathlib import Path

cwd = Path.cwd()
path = Path(f'{cwd}/8_files/text_files/wishlist.txt')

prompt = "\nWhat items would you like to add to your wish list?"
prompt += " (Enter 'q' to save and quit):\n"


user_list = ''

print(prompt)
while True:
    user_input = input("")
    if user_input == 'q':
      break
    user_list += user_input + '\n' 

path.write_text(user_list)
 