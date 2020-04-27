from bot import Bot
from wrangler import *
from tkinter import Tk, Label, PhotoImage, filedialog, Button, Entry
from tkinter.ttk import Combobox


class GUI(Tk):
    def __init__(self):
        # Creating the window
        super(GUI, self).__init__()
        self.title('Feedback Bot')
        self.configure(background='black')
        self.file = None

        # Combo boxes
        self.recruit = Entry(self, width=32)
        self.recruit.grid(row=1, column=1)
        self.cohort = Combobox(postcommand=self.filter_values, state='readonly', width=30)
        self.cohort.grid(row=2, column=1)
        self.department = Combobox(postcommand=self.filter_values, state='readonly', width=30)
        self.department.grid(row=3, column=1)
        self.repo = Entry(self, width=32)
        self.repo.grid(row=4, column=1)
        self.status = Combobox(state='readonly', width=30)
        self.status.grid(row=5, column=1)

        # Adding logo
        # logo = PhotoImage(file='../assets/umuzi_logo.png')
        # Label(self, image=logo, bg='black').grid(row=0, column=0, columnspan=2)

        self.create_components()

    def filter_values(self):
        cohort = self.cohort.get()
        dept = self.department.get()
        recruit = self.recruit.get()
        repo = self.repo.get()

        if cohort:
            self.department['values'] = return_recruit_with('department', 'cohort', cohort)
        elif dept:
            self.cohort['values'] = return_recruit_with('cohort', 'department', dept)

    def create_components(self):
        # Selecting Recruit
        Label(self, text='Select Recruit:', bg='black', fg='gray', font='none 12 bold').grid(row=1, column=0)

        # Selecting Cohort
        Label(self, text='Select cohort:', bg='black', fg='gray', font='none 12 bold').grid(row=2, column=0)
        self.cohort['values'] = return_certain('cohort')

        # Selecting Department
        Label(self, text='Select Department:', bg='black', fg='gray', font='none 12 bold').grid(row=3, column=0)
        self.department['values'] = return_certain('department')

        # Selecting Repo
        Label(self, text='Select Repo:', bg='black', fg='gray', font='none 12 bold').grid(row=4, column=0)

        # Selecting Status
        Label(self, text='Select Status:', bg='black', fg='gray', font='none 12 bold').grid(row=5, column=0)
        self.status['values'] = ('excellent', 'competent', 'not_competent', 'red_flag')

        # Drag-drop-feedback
        Button(self, text='Select File', width=15, command=self.select_file).grid(row=6, column=0)

        # Submit feedback
        Button(self, text='Submit Feedback', width=15, command=self.submit_feedback).grid(row=7, column=0)

    def select_file(self):
        self.file = filedialog.askopenfile(initialdir='../assets')
        Label(self, text=self.file.name, bg='black', fg='gray', font='none 12 bold').grid(row=5, column=1)

    def exit(self):
        self.destroy()
        self.exit()

    def submit_feedback(self):
        recruit = self.recruit.get()
        status = self.status.get()
        repo = self.repo.get()

        if self.file:
            feedback = self.file.name
        else:
            feedback = None

        feedback_bot = Bot(recruit, repo, status, feedback)
        feedback_bot.run()
        Button(self, text='Exit', width=15, command=self.exit).grid(row=7, column=0)


if __name__ == '__main__':
    GUI().mainloop()
