from tkinter import *
import time
from tkinter import PhotoImage

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, qb):
        self.window = Tk()
        self.quiz = qb
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR)
        self.score = 0
        a=IntVar(value=1)
        b=IntVar(value=0)
        self.display_score = Label(text=f"Score: {self.score}", pady=20, bg=THEME_COLOR, fg='white', font=('Arial',12,'bold'))
        self.white = Canvas(width=300, height=250, bg='white')
        self.que = self.white.create_text(150,125,text='Welcome',width=200, font=('Arial',20,'italic'))
        self.display_score.grid(row=0, column=2)
        true = PhotoImage(file='images/true.png')
        false = PhotoImage(file='images/false.png')
        exit = PhotoImage(file="images/down.png")
        self.tick = Button(image=true, highlightthickness=0, textvariable=a, command=lambda:self.check(a))
        self.wrong = Button(image=false, highlightthickness=0, textvariable=b, command=lambda:self.check(b))
        self.white.grid(row=5, column=1, rowspan=4, padx=20, pady=20, columnspan=2)
        self.tick.grid(row=10, column=1, rowspan=6, pady=50)
        self.wrong.grid(row=10, column=2, pady=50)
        self.quit = Button(image=exit, command=lambda: self.window.quit(), state=DISABLED)
        self.quit.grid(row=18, column=0, columnspan=3)
        self.get_question()
        self.window.mainloop()

    def get_question(self):
        current = self.quiz.next_question()
        self.white.itemconfig(self.que, text=current)

    def check(self, val):
        if self.quiz.check_answer(val.get()):
            self.white.configure(bg='green')
            self.window.after(1000, lambda: self.white.configure(bg='white'))
            self.score += 1
            self.display_score.config(text=f"Score: {self.score}")
            # self.white.configure(bg='white')
            if self.quiz.still_has_questions():
                self.get_question()
            else:
                self.white.itemconfig(self.que, text=f"You got {self.score} out of 10 Correct. CONGRATULATIONS!")
                time.sleep(2)
                self.tick.config(state=DISABLED)
                self.wrong.config(state=DISABLED)
                self.quit.config(state=NORMAL)

        else:
            self.white.configure(bg='red')
            self.window.after(1000, lambda: self.white.configure(bg='white'))
            if self.quiz.still_has_questions():
                self.get_question()
            else:
                self.tick.config(state=DISABLED)
                self.wrong.config(state=DISABLED)
                self.quit.config(state=NORMAL)
                time.sleep(2)
                self.white.itemconfig(self.que, text=f"You got {self.score} out of 10 Correct. CONGRATULATIONS!")



