import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Arial", 20, "italic")
WORD_FONT = ("Arial", 40, "bold")
current_card = {}
to_learn = {}

try:
  data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
  original_data = pandas.read_csv("french_words.csv")
  to_learn = original_data.to_dict(orient="records")
else:
  to_learn = data.to_dict(orient="records")


def next_card():
  global current_card, flip_timer
  window.after_cancel(flip_timer)
  current_card = random.choice(to_learn)
  canvas.itemconfig(language, text="French", fill="black")
  canvas.itemconfig(word, text=current_card["French"])
  canvas.itemconfig(front_img, image=card_front)
  flip_timer = window.after(3000, func=flip_card)


def flip_card():
  canvas.itemconfig(front_img, image=card_back)
  canvas.itemconfig(language, text="English", fill="white")
  canvas.itemconfig(word, current_card["English"], fill="white")


def is_known():
  to_learn.remove(current_card)
  data = pandas.DataFrame(to_learn)
  data.to_csv("words_to_learn.csv", index= False)
  next_card()


#creates window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

#creates first card and text on it
canvas = Canvas(width=800, height=526, highlightthickness=0)
card_front = PhotoImage(file="card_front.png")
card_back = PhotoImage(file="card_back.png")
front_img = canvas.create_image(400, 263, image=card_front)
canvas.config(bg=BACKGROUND_COLOR)
language = canvas.create_text(400, 100, text="title", font=LANGUAGE_FONT)
word = canvas.create_text(400, 263, text="word", font=WORD_FONT)
canvas.grid(column=0, row=0, columnspan=2)

#creates red cross button "wrong answer"
image_wrong = PhotoImage(file="wrong.png")
button_wrong = Button(image=image_wrong,
                      highlightthickness=0,
                      bg=BACKGROUND_COLOR,
                      command=next_card)
button_wrong.grid(column=0, row=1)

#creates green button "right answer"
image_right = PhotoImage(file="right.png")
button_right = Button(image=image_right,
                      highlightthickness=0,
                      bg=BACKGROUND_COLOR,
                      command=is_known)
button_right.grid(column=1, row=1)
next_card()

window.mainloop()
