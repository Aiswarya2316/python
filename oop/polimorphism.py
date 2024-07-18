                #runtime


class sample:
    def display(self):
        print('sample class')
    def s1(self):
        print('sample clas s1')
class demo(sample):
    def display(self):
        print('demo display')
        super()
        print('start')
    def d1(self):
        print('demo class d1')

obj=demo()
obj.display()            