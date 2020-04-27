from tkinter import Tk, Label, PhotoImage, filedialog, Button
from tkinter.ttk import Combobox


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
        combo = Combobox(width=30)
        combo['values'] = ('c16', 'c17', 'c18')
        combo.grid(row=1, column=1)

        # Selecting Department
        Label(self, text='Select Department:', bg='black', fg='gray', font='none 12 bold').grid(row=2, column=0)
        combo2 = Combobox(width=30)
        combo2['values'] = ('Web Development', 'Data Science', 'Java')
        combo2.grid(row=2, column=1)

        # Selecting Recruit
        Label(self, text='Select Recruit:', bg='black', fg='gray', font='none 12 bold').grid(row=3, column=0)
        combo3 = Combobox(width=30)
        combo3['values'] = ('boitshepo.masemola', 'masai.mahapa', 'ntokozo.mfene')
        combo3.grid(row=3, column=1)

        # Drag-drop-feedback
        Button(self, text='Select File', width=10, command=self.select_file).grid(row=4, column=0)

        # Submit feedback
        Button(self, text='Submit Feedback', width=15, command=self.submit_feedback).grid(row=5, column=0)

    def select_file(self):
        file = filedialog.askopenfile()
        Label(self, text=file.name, bg='black', fg='gray', font='none 12 bold').grid(row=4, column=1)

        return file.name

    def submit_feedback(self):
        Label(self, text='Feedback submitted', bg='black', fg='gray', font='none 12 bold').grid(row=5, column=1)


if __name__ == '__main__':
    GUI().mainloop()
