   #multilevel

class synnefo:
    def __init__(s):
        print('register')
    def python(s):
        s.database='mysql'
        print("python")
    def php(self):
        self.database='mysql'
        print("php",self.database)

class novavi(synnefo):
    def dm(self):
        print("digital marketing")
    def web_dev(self):
        print("web developer")

class staff(novavi):
    def reg(self):
        print('std reg')

anu=synnefo()
anu.php()

achu=novavi()
achu.dm()
achu.php

anju=staff()
anju.python()
anju.reg
