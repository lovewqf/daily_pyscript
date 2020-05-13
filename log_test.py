import logging
logging.basicConfig(filename='example.log',level=logging.WARNING,format="%(asctime)s %(name)s :%(levelname)s:%(message)s")
logging.debug('this message should go to the log file')
logging.info('so should this')
logging.warning('And this,too')