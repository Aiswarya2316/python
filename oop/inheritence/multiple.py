            # multiple

class synnefo:
    def __init__(s):
        print('register')
    def python(s):
        s.database='mysql'
        print("python")
    def php(self):
        self.database='mysql'
        print("php",self.database)

class novavi:
    def dm(self):
        print("digital marketing")
    def web_dev(self):
        print("web developer")

class std(novavi,synnefo):
    def reg(self):
        print('std reg')

anu=synnefo()
anu.php()

achu=novavi()
achu.dm()

anju=std()
anju.python()