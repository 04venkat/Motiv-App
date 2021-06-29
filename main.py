from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from datetime import datetime
import json, random

Builder.load_file("design.kv")

u = ""
p = ""
make_list = ["If you want something, you can't wait for someone to make it happen for you.", "Once you make a decision, the universe conspires to make it happen.","If you really are passionate about it, you're just going to find a way to make it happen.","Know what it is that drives and motivates you; then you pursue it. Endeavor to work to make it happen.", "I follow my own head. And if I'm determined to do something, then I'll make sure that I make it happen."]

watch_list = ["Life just doesn't hand you things. You have to get out there and make things happen; that's the exciting part.", "Your ability to make things happen is what makes you different.", "There are times to let things happen, and times to make things happen. Now is that time. You will either make things happen, watch what happens, or wonder what happened.", "People make things happen. All the rest is just window dressing.", "You've got to be hungry for ideas, to make things happen and to see your vision made into reality."]

wonder_list = ["Adversity cleanses the lethargies of man.", "Lethargy is the forerunner of death to the public liberty.", "Living a healthy lifestyle will only deprive you of poor health, lethargy, and fat.", "Lethargy, bordering on sloth should remain the cornerstone of an investment style.", "The problem with lethargy is that doing nothing validates the fear that nothing can be done."]

class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = "signup_screen"

    def login(self, uname, pword):
        global u,p
        u = uname
        p = pword
        with open("users.json") as file:
            users = json.load(file)
            if uname in users and users[uname]["password"] == pword:
                self.manager.current = "login_screen_success"
            else:
                self.ids.wrong.text = "Wrong Credentials, Please try again!"      


class SignUpScreen(Screen):
    def add_user(self, uname, pword):
        with open("users.json") as file:
            users = json.load(file)
            users[uname] = {
                "username": uname,
                "password": pword,
                "type": "",
                "created": datetime.now().strftime("%Y:%m:%d %H:%M:%S")
            }
        with open("users.json", "w") as file:
            json.dump(users, file)

    def make_motivate(self, uname):
        with open("users.json", "r") as file:
            users = json.load(file)
            users[uname]["type"] = "make"
        with open("users.json", "w") as file:
             json.dump(users, file)
        self.manager.current = "signup_screen_success"                                    
        
    def watch_motivate(self, uname):
        with open("users.json", "r") as file:
            users = json.load(file)
            users[uname]["type"] = "watch"
        with open("users.json", "w") as file:
             json.dump(users, file)
        self.manager.current = "signup_screen_success"

    def wonder_motivate(self, uname):
        with open("users.json", "r") as file:
            users = json.load(file)
            users[uname]["type"] = "wonder"
        with open("users.json", "w") as file:
             json.dump(users, file)
        self.manager.current = "signup_screen_success"

class SignUpScreenSuccess(Screen):
    def back_to_login(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"

class LoginScreenSuccess(Screen):
    def log_out(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"

    def motivate(self):
        with open("users.json", "r") as file:
            users = json.load(file)
            if users[u]["type"] == "make":
                self.ids.motivate.text = f"Your type: You MAKE things happen!\n\n\nQuote for you:\n\n{random.choice(make_list)}"
            elif users[u]["type"] == "watch":
                self.ids.motivate.text = f"Your type: You WATCH things happen!\n\n\nQuote for you:\n\n{random.choice(watch_list)}"
            else:
                self.ids.motivate.text = f"Your type: You WAIT for things to happen!\n\n\nQuote for you:\n\n{random.choice(wonder_list)}"

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()
