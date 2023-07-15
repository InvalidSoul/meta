import logging

declareFunctions = []
setFunctions = []
getFunctions = []
deleteFunctions = []

class main:
    def __setattr__(self, key, value):  # Sets/Declares New Variable
        try:  # Tries to see if variable already exists
            object.__getattribute__(self, key)  # If this errors (Variable doesn't exist) it goes straight the except
            object.__setattr__(self, key, value)  # Sets the existing variable
            for func in setFunctions:  # Loops through the functions in set
                func(key, value)  # Calls those functions
        except AttributeError:  # If it errors from running __getattribute__, it's as a declare
            object.__setattr__(self, key, value)  # Declares new variable
            for func in declareFunctions:  # Loops through declare functions
                try:  # Made for testing to see if it can call functions
                    if key != 'setFunction':
                        func(key, value)  # Calls those functions
                except TypeError:
                    logging.error(f'{func} missing arguments')  # Throws custom error if it fails to call functions

    def __getattribute__(self, item):  # Returns attribute value based on input
        try:
            for func in getFunctions:  # Loops through declare functions
                try:  # Made for testing to see if it can call functions
                    func(item)  # Calls those functions
                except TypeError:
                    logging.error(f'{func} missing arguments')  # Throws custom error if it fails to call functions
            return object.__getattribute__(self, item)  # If it doesn't error, it returns, if it does, it excepts
        except AttributeError:
            return False  # Returns False if no item was found

    def __delattr__(self, item):  # Fires functions when a variable is deleted
        try:
            object.__getattribute__(self, item)  # Sees if variable exists
            for func in deleteFunctions:  # Loops through the functions
                try:
                    func(item)  # Fires function passing through variable name that was deleted
                except TypeError:
                    logging.error(f'{func} missing arguments')
        except AttributeError:
            return False

    def setFunction(self, data):
        if data[1] in ['declare', 'set', 'get']:  # Checks to see if type input
            if callable(data[0]):  # If reference is callable
                if data[1] == 'declare':
                    declareFunctions.append(data[0])
                elif data[1] == 'set':
                    setFunctions.append(data[0])
                elif data[1] == 'get':
                    getFunctions.append(data[0])
                elif data[1] == 'delete':
                    deleteFunctions.append(data[0])
            else:
                logging.error('Not a function')  # Custom error if it's not
        else:
            logging.error(f"Invalid type '{data[1]}' | 'set', 'declare', 'get', 'delete' are options")

    setFunction = property(fset=setFunction)
meta = main()
