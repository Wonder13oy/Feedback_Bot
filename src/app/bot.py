import os
import time
import json
from selenium import webdriver

# Declaring application to start web browser
driver = webdriver.Chrome()

# Adding all environment variables
rocket_chat_server = os.getenv("CHAT_SERVER")
email = os.getenv("UMUZI_EMAIL")
password_ = os.getenv("UMUZI_PASSWORD")


class Bot:
    def __init__(self, name_of_recruit, recruit_repo, status, feedback=None):
        self.name = name_of_recruit
        self.repo = recruit_repo
        self.status = status
        self.feedback = str(open(feedback).read())
        self.messages = json.load(open('../assets/messages.json'))

    def run(self):
        driver.get(f'http://{rocket_chat_server}/direct/{self.name}')
        time.sleep(5)
        self.login(email, password_)
        time.sleep(5)
        self.send_message(self.feedback)

    def create_message(self):
        subject = self.messages['greeting'].format(self.name)
        body = self.messages[self.status].format(self.repo)
        conclusion = self.messages['conclusion']

        if not self.feedback:
            return subject + '\n\n' + body + '\n\n' + conclusion
        else:
            return subject + '\n\n' + body + '\n\n' + self.feedback + '\n\n' + conclusion

    def login(self, username_, pass_):
        # id="emailOrUsername"
        username = driver.find_element_by_id('emailOrUsername')
        username.send_keys(username_)

        # id='pass'
        password = driver.find_element_by_id('pass')
        password.send_keys(pass_)

        time.sleep(2)

        # class='login'
        login_button = driver.find_element_by_class_name('login')
        login_button.click()

    def send_message(self, message):
        msg_box = driver.find_element_by_class_name('js-input-message')
        msg_box.send_keys(message)

        print(f'The message you are about send:\n\n{message}')
        confirm = input('Are you sure you want send the message? y[Y] or n[N]')

        send_button = driver.find_element_by_class_name('js-send')

        if confirm.lower() == 'y':
            send_button.click()


print(Bot('wandile', 'repo', 'red_flag', '../assets/masai.mahapa.md').create_message())
