def oops():
    raise KeyError


try:
    oops()
except IndexError:
    print("Oops, Index Error!")
except KeyError:
    print("Oops, Key Error")
