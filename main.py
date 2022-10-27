from tkinter import *
import pandas
from random import randint

wordset = {}
randindex = 0
words = {}
to_learn = []


# Get data
def get_data():
    global wordset, randindex, fr_dict
    try:
        data = pandas.read_csv('data/words_to_learn.csv')
    except FileNotFoundError:
        data = pandas.read_csv('data/french_words.csv')
    fr_dict = data.to_dict(orient='records')
    return fr_dict


def select_wordset():
    global randindex, wordset
    randindex = randint(0, len(fr_dict) - 1)
    wordset = fr_dict[randindex]
    return wordset


def next_card():
    global words, word_timer
    word_timer = window.after(3000, flip_card)
    if len(fr_dict) > 0:
        words = select_wordset()
        my_can.itemconfig(card_image, image=my_image_front)
        my_can.itemconfig(french, text='French', fill='black')
        my_can.itemconfig(word, text=words['French'], fill='black')
    else:
        my_can.itemconfig(card_image, image=my_image_front)
        my_can.itemconfig(french, text='Done!', fill='black')
        my_can.itemconfig(word, text='fin!', fill='black')
        with open(file='data/words_to_learn.csv', mode='w') as outputfile:
            outputfile.writelines("French,English\n")
            for i in to_learn:
                outputfile.writelines(f'{i["French"]},{i["English"]}\n')


def flip_card():
    global words
    my_can.itemconfig(card_image, image=my_image_back)
    my_can.itemconfig(french, text='English', fill='white')
    my_can.itemconfig(word, text=words['English'], fill='white')
    if words not in to_learn:
        to_learn.append(words)
    print(to_learn)


def add_to_learn():
    global words, to_learn, word_timer
    window.after_cancel(word_timer)
    if words not in to_learn:
        to_learn.append(words)
    next_card()


def bcorrect():
    global word_timer
    window.after_cancel(word_timer)
    print(len(fr_dict))
    if len(fr_dict) > 0:
        fr_dict.remove(fr_dict[randindex])
        next_card()


##########################

# Tkinter Stuff

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
window.title('Flashy')

##################################
# images
my_image_corr = PhotoImage(file='images/right.png')
my_image_wro = PhotoImage(file='images/wrong.png')
my_image_front = PhotoImage(file='images/card_front.png')
my_image_back = PhotoImage(file='images/card_back.png')

##################################
# Front card
my_can = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
card_image = my_can.create_image(400, 263, image=my_image_front)
my_can.grid(row=0, column=0, columnspan=2)

##################################
# Buttons

# Correct button
button_corr = Button(image=my_image_corr, highlightthickness=0, padx=50, pady=50, command=bcorrect)
button_corr.grid(row=1, column=1)

# Wrong button
button_wro = Button(image=my_image_wro, highlightthickness=0, padx=50, pady=50, command=add_to_learn)
button_wro.grid(row=1, column=0)
##################################

# Texts
french = my_can.create_text(400, 150, text='French', font=('Arial', 40, 'italic'))
word = my_can.create_text(400, 263, text='Test', font=('Arial', 60, 'bold'))
##################################

fr_dict = get_data()

next_card()

window.mainloop()
