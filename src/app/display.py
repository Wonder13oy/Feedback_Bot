from bot import Bot
from tkinter import Tk, Label, PhotoImage, filedialog, Button
from tkinter.ttk import Combobox
import os

print(os.listdir())


class GUI(Tk):
    def __init__(self):
        # Creating the window
        super(GUI, self).__init__()
        self.title('Feedback Bot')
        self.configure(background='black')

        # Adding logo
        # logo = PhotoImage(file='../assets/umuzi_logo.png')
        # Label(self, image=logo, bg='black').grid(row=0, column=0, columnspan=2)

        self.create_components()

    def create_components(self):
        # Selecting Cohort
        Label(self, text='Select cohort:', bg='black', fg='gray', font='none 12 bold').grid(row=1, column=0)
        self.combo = Combobox(width=30)
        self.combo['values'] = ('c16', 'c17', 'c18')
        self.combo.grid(row=1, column=1)

        # Selecting Department
        Label(self, text='Select Department:', bg='black', fg='gray', font='none 12 bold').grid(row=2, column=0)
        self.combo2 = Combobox(width=30)
        self.combo2['values'] = ('Web Development', 'Data Science', 'Java')
        self.combo2.grid(row=2, column=1)

        # Selecting Recruit
        Label(self, text='Select Recruit:', bg='black', fg='gray', font='none 12 bold').grid(row=3, column=0)
        self.combo3 = Combobox(width=30)
        self.combo3['values'] = ('wandile', 'boitshepo.masemola', 'masai.mahapa', 'ntokozo.mfene')
        self.combo3.grid(row=3, column=1)

        # Selecting Recruit
        Label(self, text='Select Status:', bg='black', fg='gray', font='none 12 bold').grid(row=4, column=0)
        self.combo4 = Combobox(width=30)
        self.combo4['values'] = ('excellent', 'competent', 'not_competent', 'red_flag')
        self.combo4.grid(row=4, column=1)

        # Drag-drop-feedback
        Button(self, text='Select File', width=10, command=self.select_file).grid(row=5, column=0)

        # Submit feedback
        Button(self, text='Submit Feedback', width=15, command=self.submit_feedback).grid(row=6, column=0)

    def select_file(self):
        self.file = filedialog.askopenfile()
        Label(self, text=self.file.name, bg='black', fg='gray', font='none 12 bold').grid(row=5, column=1)

    def submit_feedback(self):
        cohort = self.combo.get()
        dept = self.combo2.get()
        recruit = self.combo3.get()
        status = self.combo4.get()
        feedback = self.file.name

        feedback_bot = Bot(recruit, dept, status, feedback)
        feedback_bot.run()
        Label(self, text='Feedback submitted', bg='black', fg='gray', font='none 12 bold').grid(row=6, column=1)


if __name__ == '__main__':
    GUI().mainloop()
