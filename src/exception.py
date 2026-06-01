import sys  # system-related functions ke liye
import logging


# Error message ko detailed banane wala function
def error_message_detail(error, error_detail: sys):

    # Current exception ki information nikalta hai
    _, _, exc_tb = error_detail.exc_info()

    # Jis file me error aayi uska naam nikalta hai
    file_name = exc_tb.tb_frame.f_code.co_filename

    # Custom error message banata hai
    error_message = (
        "Error occurred in python script name [{0}] "
        "line number [{1}] "
        "error message [{2}]".format(
            file_name,          # file name
            exc_tb.tb_lineno,   # line number
            str(error)          # actual error
        )
    )

    return error_message


# Custom exception class
class CustomException(Exception):

    # Constructor
    def __init__(self, error_message, error_detail: sys):

        # Parent Exception class ko call karta hai
        super().__init__(error_message)

        # Detailed error message store karta hai
        self.error_message = error_message_detail(
            error_message,
            error_detail=error_detail
        )

    # Print karne par custom message return karega
    def __str__(self):
        return self.error_message
    

        