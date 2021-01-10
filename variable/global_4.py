x = "awesome"


def myfunc():
    global x
    print("Python is " + x)
    x = "fantastic"


myfunc()
print("Python is " + x)

# Output : Python is awesome
# OutPut : Python is fantastic
