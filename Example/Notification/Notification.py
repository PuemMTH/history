# download 
# 3 package 
# 1.win10toast
# 2.pypiwin32
# 3.setuptools

from win10toast import ToastNotifier

def sandmessage(topic,message):
    saymessage = ToastNotifier()
    saymessage.show_toast(topic,message,icon_path="ico_Iru_icon.ico",duration=10,threaded=None)
def main():
    topic = "Hacker"
    message = "i will hacked your computer."
    sandmessage(topic,message)
if __name__ == "__main__":
    main()