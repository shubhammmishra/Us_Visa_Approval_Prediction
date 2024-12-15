from us_visa.logger import logging
from us_visa.exception import USvisaException

import sys
try:
    a = 1/'a'
    

except Exception as e:
    logging.info(USvisaException(e,sys))
    raise USvisaException(e,sys) from e