import os
import time
import json
from selenium import webdriver

# Adding all environment variables
rocket_chat_server = os.getenv("CHAT_SERVER")
email = os.getenv("UMUZI_EMAIL")
password_ = os.getenv("UMUZI_PASSWORD")


class Bot:
    def __init__(self, name_of_recruit, recruit_repo, status, feedback=None):
        self.driver = webdriver.Chrome()
        self.name = name_of_recruit
        self.repo = recruit_repo
        self.status = status
        self.feedback = open(feedback).read()
        self.messages = json.load(open('../assets/messages.json'))

    def run(self):
        # Declaring application to start web browser
        self.driver.get(f'http://{rocket_chat_server}/direct/{self.name}')
        time.sleep(5)
        self.login(email, password_)
        time.sleep(20)
        msg = self.create_message()
        self.send_message(msg)

    def create_message(self):
        subject = self.messages['greeting'].format(self.name)
        body = self.messages[self.status].format(self.repo)
        reassurance = self.messages['reassurance']
        conclusion = self.messages['conclusion']

        if not self.feedback or self.status == 'competent':
            return subject + '\n\n' + body + '\n\n' + conclusion
        else:
            return subject + '\n\n' + body + '\n\n' + self.feedback + '\n\n' + reassurance + '\n\n' + conclusion

    def login(self, username_, pass_):
        # id="emailOrUsername"
        username = self.driver.find_element_by_id('emailOrUsername')
        username.send_keys(username_)

        # id='pass'
        password = self.driver.find_element_by_id('pass')
        password.send_keys(pass_)

        time.sleep(2)

        # class='login'
        login_button = self.driver.find_element_by_class_name('login')
        login_button.click()

    def send_message(self, message):

        print(f'The message you are about send:\n\n{message}')
        confirm = input('Are you sure you want send the message? y[Y] or n[N]')

        if confirm.lower() == 'y':
            msg_box = self.driver.find_element_by_class_name('js-input-message')
            msg_box.send_keys(message)

            send_button = self.driver.find_element_by_class_name('js-send')
            send_button.click()

