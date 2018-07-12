from flask_mail import Message


def emailer(package):
    msg = Message("Hello",
                  sender="bobby@example.com",
                  recipients=["victorfateh@yahoo.com"])
    package[0].send(msg)
