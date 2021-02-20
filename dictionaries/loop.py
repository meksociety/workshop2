thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}

# EX1
for key in thisdict:
    print(key)


thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}

# EX2
for key in thisdict:
    print(thisdict[key])


thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}

# EX3
for key in thisdict.keys():
    print(key)


thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}

# EX4
for value in thisdict.values():
    print(value)


thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}

# EX1
for key, value in thisdict.items():
    print(key, value)
