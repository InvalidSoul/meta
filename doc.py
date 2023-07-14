"""
from source Import Meta -> Imports Module

Meta.setFunction = (reference, type) -> Attaches function to variable events
Meta.variables() -> Prints all variables attached to Meta
Meta.custom_variable = value -> Makes a new meta variable

__ TYPES __
'declare' - Fires all functions attached to this event when a new variable is declared/created -> (Name, Value)
'set' - Fires all functions attached to this event when an existing variables value has been changed -> (Name, Value)
'get' - Fires all functions attached to this event when an existing variable has been referenced -> (Name)
'delete' - Fires all functions attached to this event when an existing variable has been deleted -> (Name)
___________

__ EXAMPLES __
def example1(name, value)
    print(f'{name} = {value}) -> 'Number = 1'

Meta.setFunction = (example1, 'declare')
Meta.Number = 1 [TRIGGERS 'declare']

~ example1 functions gets fired with an input of (Number, 1)
_____________________________________________________________________

def example2(name)
    print(name) -> Number

Meta.setFunction = (example2, 'get')
Meta.Number = 1
Reference = Meta.Number [TRIGGERS 'get']

~ example2 functions gets fired with an input of (Number)
_____________________________________________________________________

Meta.Number = 1
Meta.String = "Test"

print(Meta.variables()) -> {'Number': 1, 'String': 'Test'}
"""
