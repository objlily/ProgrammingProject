import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.title("B.A.N.K.")
window.geometry("400x400")

def load_image(name):
    return ImageTk.PhotoImage(Image.open(name))

bgimg = load_image("bg.png")
loginpageimg = load_image("loginpage.png")
loginimg = load_image("login1.png")
loginimg_pressed = load_image("login2.png")

signupimg = load_image("signup1.png")
signupimg_pressed = load_image("signup2.png")

bg = tk.Label(window, image=bgimg)
bg.place(x=0, y=0, relwidth=1, relheight=1)





loginpage = tk.Label(window, image=loginpageimg)
loginpage.place(x=37,y=63)

username_text_widget = tk.Text(window, height=1, width=20)
username_text_widget.place(x=38,y=236)


def loginFunction():
    print("login")
    
def signupFunction():
    print("signup")

def on_press_login(event):
    login.config(image=loginimg_pressed)

def on_release_login(event):
    login.config(image=loginimg)
    loginFunction()  

def on_press_signup(event):
    signup.config(image=signupimg_pressed)

def on_release_signup(event):
    signup.config(image=signupimg)
    signupFunction()


login = tk.Label(window, image=loginimg, bd=0)
login.place(x=90, y=329)

signup = tk.Label(window, image=signupimg, bd=0)
signup.place(x=35, y=329)

login.bind("<ButtonPress-1>", on_press_login)
login.bind("<ButtonRelease-1>", on_release_login)

signup.bind("<ButtonPress-1>", on_press_signup)
signup.bind("<ButtonRelease-1>", on_release_signup)
window.mainloop()

