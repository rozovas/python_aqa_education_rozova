import logging

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

    class InfoMessages(logging.Filter):
        """filtering only records with INFO level"""
        def filter(self, record):
            return record.levelname == logging.INFO

    s_handler.addFilter(InfoMessages())
    # adding handlers to a logger:
    logger.addHandler(f_handler)
    logger.addHandler(s_handler)

    # setting levels:
    logger.setLevel(logging.DEBUG)
    f_handler.setLevel(logging.WARNING)
    s_handler.setLevel(logging.INFO)

    # function to test logger:
    def test_log():
        print("==========================")
        print("Unit test 1. Тестируем лог")
        print("==========================")
        logger.debug("DEBUG LOG")
        logger.info("INFO LOG")
        logger.warning("WARNING LOG")
        logger.error("ERROR LOG")
        logger.critical("CRITICAL LOG")
        # Этот вывод должен попасть в файл
        logger.critical("John Cena wins. Congrats!")
        print("==========================")
        print("Unit test 1. Тест окончен")
        print("==========================\n")

    # test_log()


if __name__ == '__main__':
    setup_logger()
