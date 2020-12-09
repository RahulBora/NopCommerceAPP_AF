import logging

class LogGen:
    @staticmethod
    def log_gen():
        for handler in logging.root.handlers[:]:  #This will remove the default Looger so that,
            logging.root.removeHandler(handler)   #Log file can be genrated in Log folder
        print("Logger test")
        logging.basicConfig(filename=".\\Logs\\AutoTest.log",
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            filemode='w+'
                                )
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger