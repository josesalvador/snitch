import pytest
from snitch.snitch import Snitch
from snitch.constants import Constants


class TestSnitch:

    def test_snitch_on(self):
        mock_snitcher = self.__MockSnitcher()
        snitch = Snitch(mock_snitcher)
        
        snitch.snitch_on(self.__MESSAGE)
        
        assert mock_snitcher.snitched_message == self.__MESSAGE

    def test_snitch_message_can_not_be_null(self):
        mock_snitcher = self.__MockSnitcher()
        snitch = Snitch(mock_snitcher)
        with pytest.raises(ValueError):
            snitch.snitch_on(self.__NULL_MESSAGE)

    @pytest.mark.skipif("True")
    def test_mail_snitcher(self):
        from snitch.snitchers.mail_snitcher import MailSnitcher
        server = "mail.server.es"
        port = 25
        user = "user@domain.es"
        password = "password"
        from_address = "from@address.es"
        to_address = "to@address.es"
        mail_snitcher = MailSnitcher(server, port, user, password)
        mail_snitcher.from_address = from_address
        mail_snitcher.to_address = to_address
        snitch = Snitch(mail_snitcher)
        snitch.snitch_on("Message from mail snitcher")

    @pytest.mark.skipif("True")
    def test_snitch_message_is_not_empty(self):
        pass

    # private

    __MESSAGE = "message to be sitched"
    __NULL_MESSAGE = None


    class __MockSnitcher:

        def __init__(self):
            self.__snitched_message = Constants.DEFAULT_STRING 

        @property
        def snitched_message(self):
            return self.__snitched_message

        def snitch_on(self, message):
            self.__snitched_message = message
