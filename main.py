from tkinter import *


BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Arial", 20, "italic")
WORD_FONT = ("Arial", 40, "bold")

#creates window 
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#creates first card and text on it
canvas = Canvas(width=780, height=500, highlightthickness=0)
card_front = PhotoImage(file="card_front.png")
card_back = PhotoImage(file="card_back.png")
canvas.create_image(401, 264, image=card_front)
language = canvas.create_text(401, 75, text="French", font=LANGUAGE_FONT)
word = canvas.create_text(401, 275, text="word",font= WORD_FONT)
canvas.grid(column=0, row=0, columnspan=2)

#creates red cross button "wrong answer"
image_wrong = PhotoImage(file="wrong.png")
button_wrong = Button(image=image_wrong, highlightthickness=0)
button_wrong.grid(column=0, row=1)

#creates green button "right answer"
image_right = PhotoImage(file="right.png")
button_right = Button(image=image_right, highlightthickness= 0)
button_right.grid(column=1, row=1)






window.mainloop()