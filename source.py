import logging

declareFunctions = []
setFunctions = []
getFunctions = []
deleteFunctions = []

class meta:
    def __setattr__(self, key, value):
        try:
            object.__getattribute__(self, key)
            object.__setattr__(self, key, value)
            for func in setFunctions:
                func(key, value)
        except AttributeError:
            object.__setattr__(self, key, value)
            for func in declareFunctions:
                try:
                    if key != 'setFunction':
                        func(key, value)
                except TypeError:
                    logging.error(f'{func} missing arguments')

    def __getattribute__(self, item):
        try:
            for func in getFunctions:
                try:
                    func(item)
                except TypeError:
                    logging.error(f'{func} missing arguments')
            return object.__getattribute__(self, item)
        except AttributeError:
            return False

    def __delattr__(self, item):
        try:
            object.__getattribute__(self, item)
            for func in deleteFunctions:
                try:
                    func(item)
                except TypeError:
                    logging.error(f'{func} missing arguments')
        except AttributeError:
            return False

    def variables(self):
        return self.__dict__

    def _setFunction(self, data):
        if data[1] in ['declare', 'set', 'get', 'delete']:
            if callable(data[0]):
                if data[1] == 'declare':
                    declareFunctions.append(data[0])
                elif data[1] == 'set':
                    setFunctions.append(data[0])
                elif data[1] == 'get':
                    getFunctions.append(data[0])
                elif data[1] == 'delete':
                    deleteFunctions.append(data[0])
            else:
                logging.error('Not a function')
        else:
            logging.error(f"Invalid type '{data[1]}' | 'set', 'declare', 'get', 'delete' are options")

    setFunction = property(fset=_setFunction)
Meta = meta()
