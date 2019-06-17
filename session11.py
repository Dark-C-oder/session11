# In python every thing is dynamic.........

class Login:

    def loginUser(self):
        print(">>Login dear User!!!")
class GoogleLogin(Login):

    def loginUser(self, email, password):
        print(">> Google Login Done !!!!")


class OTPLogin(Login):

    def loginUser(self, phone):
        print(">> OTP Login Done !!!!")


class facebookLogin(Login):

    def loginUser(self, fbUsername, password):
        print(">> facebook Login Done !!!!")

# Polymorhism : Runtime polymorhism

login = Login()
login.loginUser()

print()

login = GoogleLogin()
login.loginUser("john@gmail.com", "pass123")

print()

login = OTPLogin()
login.loginUser("+91 99992229992")