"""A program that demonstrates inputs and while loops."""

# This programs asks how many songs a person has listened to today


prompt = "\nHow many songs have you listened to today?\n"


# Pseudocode
# ask question\
# if less than 2. must be a nice song
# if more than 2 but less than 6. music is good for the soul
# if less more than 5. you are an audiophile
# use a status flag to continue or end the program

continuation_prompt = "\nWould you like to play again? please type 'yes' or 'no'.\n"

while True:
    songs = input(prompt)
    songs = int(songs)

    if songs < 1:
        print("Music is good for the soul")
    elif songs < 2:
        print("Must be a nice song")
    elif songs >= 2 and songs <= 5:
        print("You're on the right track")
    else:
        print("You're an audiophile")

    status = input(continuation_prompt)
    if status == 'yes':
        continue
    elif status == 'no':
        break


