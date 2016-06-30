class Snitch:

    def __init__(self, snitcher):
        self.__snitcher = snitcher

    def snitch_on(self, message):
        self.__check_message_is_not_null(message)
        self.__snitcher.snitch_on(message)

    # private

    def __check_message_is_not_null(self, message):
        if (message == None):
            raise ValueError
