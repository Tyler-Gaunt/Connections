### tyler gaunt's connections - dictionaries ###
### for use in the MainCode.py ###
### cool typewriter effect. just change delay on release.. ###

import time

def print_letter_by_letter(text, delay=0.02):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

