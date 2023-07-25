# Demonstrate how to customize logging output

import logging

extData = {'user': 'li@example.com'}


# TODO: add another function to log from

def anotherFunction():
    logging.debug("This is a debug-level log message", extra=extData)


# set the output file and debug level, and
# TODO: use a custom formatting specification

fmtStr = "%(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d User:%(user)s %(message)s"
dateStr = "%m/%d/%Y %I:%M:%S %p"

logging.basicConfig(filename="output.log",
                    format=fmtStr,
                    datefmt=dateStr,
                    level=logging.DEBUG)

logging.info("This is an info-level log message",extra=extData)
logging.warning("This is a warning-level message",extra=extData)
anotherFunction()
