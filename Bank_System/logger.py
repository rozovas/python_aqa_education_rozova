import logging
import sys

# creating a custom logger:
bank_logger = logging.getLogger('LanaBank')


def setup_logger():
    # creating and managing handlers:
    f_handler = logging.FileHandler('bank.log')
    # stream=sys.stdout added to prevent the issue of PyCharm:
    # https://youtrack.jetbrains.com/issue/IDEA-70016/error-mixing-stdoutstderr
    s_handler = logging.StreamHandler(stream=sys.stdout)
    f_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s'))
    s_handler.setFormatter(logging.Formatter('%(name)s - %(levelname)s: %(message)s'))

    # class InfoMessages(logging.Filter):
    #     """filtering only records of INFO level"""
    #     def filter(self, record):
    #         return record.levelname == 'INFO'
    #
    # s_handler.addFilter(InfoMessages())

    # setting levels:
    bank_logger.setLevel(logging.DEBUG)
    f_handler.setLevel(logging.WARNING)
    s_handler.setLevel(logging.INFO)

    # adding handlers to a logger:
    bank_logger.addHandler(f_handler)
    bank_logger.addHandler(s_handler)


    # function to test logger:
def test_log():
    print("==========================")
    print("Unit test 1. Тестируем лог")
    print("==========================")
    bank_logger.debug("DEBUG LOG")
    bank_logger.info("INFO LOG")
    bank_logger.warning("WARNING LOG")
    bank_logger.error("ERROR LOG")
    bank_logger.critical("CRITICAL LOG")
    # Этот вывод должен попасть в файл
    bank_logger.critical("John Cena wins. Congrats")
    print("==========================")
    print("Unit test 1. Тест окончен")
    print("==========================\n")


# setup_logger()
# test_log()
