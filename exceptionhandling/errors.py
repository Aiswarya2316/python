try:
    print('10'+'abcd')
except NameError:
    print("name eror")
except TypeError:
    print("type error")
else:
    print("else")
finally:
    print("finally")                