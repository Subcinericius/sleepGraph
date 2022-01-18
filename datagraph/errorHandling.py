import logging
from functools import wraps
import sys
import traceback


# General Error Handling
# Need to add error handling for every method

# look at the inspect module (https://stockoverflow.com/questions/24438976/debugging-get-filename-and-line-number-from-which-a-function-is-called

# add line number finding traceback module
# will change this so when an exception occurs it doesnt cause a crash and instead just prints text
class ErrorHandling(object):
    """
    The Class deals with all expected and unexpected errors that could be caused by the modules in graph.
    Any errors that occur will be caught and a custom error will be printed, the full stack trace will also be printed.
    """
    def _handle_error(handler):
        """
        A decorator that deals will all of the errors.
        """
        log = logging.getLogger(__name__)

        @wraps(handler)
        def inner_func(self, *args, **kwargs):
            if handler.__name__ in ("get_data", "get_data_y", "get_data_x"):
                print(f"Handling Error, {handler.__name__}")
                try:
                    return handler(self, *args, **kwargs)  # Call the function:
                except Exception as e:
                    print(
                        f"Error: Something Went Wrong in executing {handler.__name__}. Please check if you have recieved any "
                        f"warnings and adjust the code to suit.")
                    print(
                        f"The most likely cause is that their is no data entered "
                        f"or the data is not numerical.\n\n")
                    print(f"##############FULL ERROR##############\n")
                    log.exception(f"Exception in {handler.__name__}")
                    print(f"{e}\n"
                          f"##############END ERROR##############\n\n")  # add custom messages here
            elif handler.__name__ in ("get_title_main", "get_title_y", "get_title_x"):
                try:
                    return handler(self, *args, **kwargs)  # Call the function:
                except Exception as e:
                    print(
                        f"Error: Something Went Wrong in executing {handler.__name__}. Please check if you have recieved any "
                        f"warnings and adjust the code to suit. The most likely error is that their was no title name entered\n\n "
                        f"##############FULL ERROR##############\n")
                    log.exception(f"Exception in {handler.__name__}")
                    print(f"{e}\n"
                          f"##############END ERROR##############\n\n")  # add custom messages here
            elif handler.__name__ in ("graph_bar"):
                try:
                    return handler(self, *args, **kwargs)  # Call the function:
                except Exception as e:
                    print(
                        f"Error: Something Went Wrong in executing {handler.__name__}. Please check if you have recieved any "
                        f"warnings and adjust the code to suit. \n##############FULL ERROR##############\n\n")
                    log.exception(f"Exception in {handler.__name__}")
                    print(f"{e}\n##############END ERROR##############\n\n")  # add custom messages here
            else:
                try:
                    return handler(self, *args, **kwargs)  # Call the function:
                except Exception as e:
                    print(
                        f"Error: Something Went Wrong in executing {handler.__name__}. Please check if you have recieved any "
                        f"warnings and adjust the code to suit. \n##############FULL ERROR##############\n\n")
                    log.exception(f"Exception in {handler.__name__}")
                    print(f"{e}\n##############END ERROR##############\n\n")  # add custom messages here
            print("End Handelling\n")
        return inner_func

    _handle_error = staticmethod(_handle_error)


# Specific Error Handling


def check_data(data, name, **kwargs):
    """
    Function that checks if a input variable meets the conditions listed in the kwargs. It will print warnings if the
    data is not as expected.
    :param data: the variable to be checked
    :param name: the name of the variable to be checked
    :param kwargs: the optional keywords arguments that control what is checked
        :keyword exept: if exept is set to True the method will cause exceptions
        :keyword none: Checks if the data is of type None
        :keyword list: Checks if the data is of type list
        :keyword integer: Checks if the data consists of a list of integers or is of type int
    :return: Nothing is returned
    """
    print("Checking Data!")
    try:
        exept = kwargs.get("exept")

        if kwargs.get("none"):
            if data is None:
                print("In none")
                if exept:
                    print("in Exception")
                    raise Exception(
                        f"Error: No Data Has Been Entered Into ({name}). Please check that data was entered "
                        f"when creating the graph object or creating a graph")
                else:
                    print(f"Warning: No Data Has Been Entered Into ({name}). Please check that data was entered when "
                          f"creating the graph object or creating a graph")

            elif kwargs.get("list"):
                if type(data) is not list:
                    if exept:
                        raise Exception(
                            f"Error: ({name}) needs to be of type list. Please check if the entered data is "
                            f"of the right format!. when printed it should be surrounded by '[]' and "
                            f"type('data') should return 'list'")
                    else:
                        print(f"Warning: ({name}) needs to be of type list. Please check if the entered data is "
                              f"of the right format!. when printed it should be surrounded by '[]' and "
                              f"type('data') should return 'list'")

            elif kwargs.get("integer"):
                if type(data) is list:
                    # check data in list
                    if not all(isinstance(i, int) for i in data):
                        if exept:
                            raise Exception(f"Error: All items in ({name}) need to be numerical. Please check if the "
                                            f"data you have entered are of type Integer. This can be check by using"
                                            f" type('data') and it should return 'int'")
                        print(f"Warning: All items in ({name}) need to be numerical. Please check if the "
                              f"data you have entered are of type Integer. This can be check by using"
                              f" type('data') and it should return 'int'")
                else:
                    # check individual data
                    if isinstance(data, int):
                        print("All items in ({name}) need to be numerical")
        else:
            print("Exception not dealt with in Exception Class Yet")

    except Exception:
        raise Exception("An Error Occurred in function (check_data)")

# error = ErrorHandelling._handle_error
#
# class Test(ErrorHandelling):
#     @error
#     def bar(self, text):
#         print("normal call in other class")
#
#     @error
#     def other(self):
#         print("testing")
#
#
# test = Test()
# test.bar(text="hello")
# test.other()
