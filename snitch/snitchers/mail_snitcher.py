import smtplib

class MailSnitcher:

    def __init__(self, server, port, user, password):
        self.__server = server
        self.__port = port
        self.__user = user
        self.__password = password
        self.from_address = ""
        self.to_address = ""

    def snitch_on(self, message):
        server = smtplib.SMTP(self.__server, self.__port)
        server.login(self.__user, self.__password)
        server.sendmail(self.from_address, self.to_address, message)
        server.quit() 
