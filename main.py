from tkinter import *
import pandas
from random import randint

words = {}


# Get data
def get_data():
    data = pandas.read_csv('/Users/joachimlehmann/PycharmProjects/FlashCards/data/french_words.csv')

    fr_dict = data.to_dict(orient='records')
    wordset = fr_dict[randint(0, 99)]
    return wordset


def next_card():
    global words
    my_can.itemconfig(card_image, image=my_image_front)
    words = get_data()
    my_can.itemconfig(french, text='French', fill='black')
    my_can.itemconfig(word, text=words['French'], fill='black')
    window.after(3000, flip_card)


def flip_card():
    global words
    my_can.itemconfig(card_image, image=my_image_back)
    my_can.itemconfig(french, text='English', fill='white')
    my_can.itemconfig(word, text=words['English'], fill='white')


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
button_corr = Button(image=my_image_corr, highlightthickness=0, padx=50, pady=50, command=next_card)
button_corr.grid(row=1, column=1)

# Wrong button
button_wro = Button(image=my_image_wro, highlightthickness=0, padx=50, pady=50, command=next_card)
button_wro.grid(row=1, column=0)
##################################

# Texts
french = my_can.create_text(400, 150, text='French', font=('Arial', 40, 'italic'))
word = my_can.create_text(400, 263, text='Test', font=('Arial', 60, 'bold'))
##################################


next_card()

window.mainloop()
