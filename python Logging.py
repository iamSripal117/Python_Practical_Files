# Example 1 -- default logging level - Warning

# import logging
#
# logging.basicConfig(filename="AppInfo.log")
# logging.debug("This is debug message")
# logging.info("This is info message")
# logging.warning("This is warning message")
# logging.error("This is error message")
# logging.critical("This is critical message")



# example-2 --- logging from level (logging.DEBUG or logging.INFO)

# import logging
#
# logging.basicConfig(filename="AppInfo.log",level=logging.INFO)
# logging.debug("This is debug message")
# logging.info("This is info message")
# logging.warning("This is warning message")
# logging.error("This is error message")
# logging.critical("This is critical message")


# Example-3 logging using filemode="w"

# import logging
#
# logging.basicConfig(filename="AppInfo.log",filemode="w",level=logging.DEBUG)
# logging.debug("This is debug message")
# logging.info("This is info message")
# logging.warning("This is warning message")
# logging.error("This is error message")
# logging.critical("This is critical message")



# Example-4 -- specifying formatted msgs

# import logging
#
# logging.basicConfig(filename="AppInfo.log",filemode="w",level=logging.DEBUG,format='%(asctime)s - %(message)s')
# logging.info("This is info message")
# logging.warning("This is warning message")
# logging.debug("This is debug message")
# logging.info("This is info message")
# logging.warning("This is warning message")
# logging.error("This is error message")
# logging.critical("This is critical message")




# example-5 formatted msgs with date,time,message and line number

# import logging
#
# LOG_FORMAT = "%(asctime)s -%(name)s - %(message)s - %(lineno)d "
# logging.basicConfig(filename="AppInfo.log",filemode="w",level=logging.DEBUG,format=LOG_FORMAT)
# logging.info("This is info message")
# logging.warning("This is warning message")
# logging.debug("This is debug message")
# logging.info("This is info message")
# logging.warning("This is warning message")
# logging.error("This is error message")
# logging.critical("This is critical message")


# Example-6  formatting through placeholders

# import logging
#
# LOG_FORMAT = "{asctime} -{name} - {message} - {lineno} "
# logging.basicConfig(filename="AppInfo.log",filemode="w",level=logging.DEBUG,style='{' ,format=LOG_FORMAT)
# logging.debug("This is debug message")
# logging.info("This is info message")
# logging.warning("This is warning message")
# logging.error("This is error message")
# logging.critical("This is critical message")



# Example-7 : To change default name of logging from root to user defined name (RSR).

# import logging
#
# LOG_FORMAT = "{asctime} -{name} - {message} - {lineno} "
# logging.basicConfig(filename="AppInfo.log",filemode="w",level=logging.DEBUG,style='{' ,format=LOG_FORMAT)
# logger = logging.getLogger("RSR")
# logger.debug("This is debug message")
# logger.info("This is info message")
# logger.warning("This is warning message")
# logger.error("This is error message")
# logger.critical("This is critical message")

# Example-8

import logging

logging.basicConfig(filename='MyAppFlowInfo.txt',filemode ="w",level=logging.DEBUG)
logging.info("Program execution started")
try:
    logging.info("Entered to try block")
    a = int(input("Enter a number:"))
    logging.info("1st input was perfect")
    b=int(input("Enter a number:"))
    logging.info("2nd input was perfect")
    if b==0:
        logging.info("2nd input was zero")
        raise ZeroDivisionError
    else:
        c = a/b
        logging.info("Calculation was valid")
        print(f"Quotient of {a} and {b} is {int(c)}")
        logging.info("Output provided successfully")
except ZeroDivisionError:
         logging.exception("Can't divide by zero")
finally:
    logging.info("Program execution finished")

