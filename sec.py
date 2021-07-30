import logging
#for changing the root
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(levelname)s : %(name)s : %(message)s : %(asctime)s',datefmt='%m/%d/%Y %I:%M:%S %p')
#for the logging file
file_handler = logging.FileHandler('sec.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

class bank:
    def __init__(self, name, account_name: str):
        self.name = name
        self.account_name = account_name
        if len(account_name) == 10:
            logger.info('{} logged in this time: '.format(self.details))
            print("Welcome {}".format(self.name))
        else:
            logger.warning("Re-enter your account number")
            print("Re-enter your account number")
    @property
    def details(self):
        return 'Account name:{}, Account number:{}'.format(self.name, self.account_name)    

#name = input("Enter your name: ")
#account_name = input("Enter your account number: ")

customer = bank("joshua", "1227365349")
