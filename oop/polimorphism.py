                #runtime
class sample:
    def __init__(self,name,age):
        print('sample class')
        print(name,age)
    def s1(self):
        print('sample clas s1')
class demo(sample):
    def __init__(self,name,age):
        print(name,age)
        print('demo display')
        super().__init__(name,age)
        print('start')
    def d1(self):
        print('demo class d1')

obj=demo('achu',17)
            