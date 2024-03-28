#Dictionaries has key and values denoted with curly braces
#Keys have to be unique and immutable- Values can be immutable, mutable nad duplicates
DICT = {"Name":"Simon", "Age":25, "Course":"BSIT","Units":['C++','Java', 'C','Python']}

#Adding values
DICT['Reg no'] = 'BSIT/2021'

#Accessing values
DICT['Name']  #Output- Simon

#Method .keys() and .values list keys and values

DICT.keys()
DICT.values()

#Keys can be only string, number and tuples

#Method del removes an item from the dictionary

del(['Age'])

#Keyword in used to check if an item is available

'Simon' in DICT #True