class synnefo:
    def python(s):
        s.database='mysql'
        print("python")
    def php(self):
        print("php",self.database)
anu=synnefo()
anu.python()
anu.php()  
print(anu.database)