#dictionary

# create the dictionary:
    # word = {}
    # word = dict()
    # 2 ways 

#dictionary{'key1':'value1', 'key2':'value2', 'key3':'value3', ...}

dictionary1 = {'A':'1', 'B':'2', 'C':'3'}
print(dictionary1)

#get the values in the dictionary:
    #dictionary[key] = value
    #get() 

print(dictionary1['B'])

print(dictionary1['D'] if 'D' in dictionary1 else 'D does not exist in this dictionary')

    #get()
    #dictionary.get('key','default value')      如果字典里没有这个key（参数），则会返回默认值

print(dictionary1.get('D','6'))

# List: []
key = ['A','B','C','D']
value = ['4','3','2','1']

dictionary2 = dict(zip(key, value))

# zip 2 lists and transfer the zip to the dictionary

print(dictionary2)

#delete the dictionary 
    # del dictionary_name

# del dictionary1


# delete all tuples in the dictionary:
    # dictionary.clear()
