import sys
import logging
def error_message_details( error, error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    error_message = "error occured in python script name [{0}] and linenumber[{1}] and error message [{2}]".format(filename,exc_tb.tb_lineno,str(error))
    return error_message
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message,error_detail=error_detail)
    def __str__(self):
        return self.error_message
    
if __name__ == "__main__":

    try : 
        result = 1/0
        logging.info("Division by zero ")

    except Exception as e:

        logging.info("Division by zero ")
        raise CustomException(e,sys)