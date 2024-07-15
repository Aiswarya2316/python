                #single inheritance
# class college:
#     def __init__(s):
#         print('register')
#     def python(s):
#         print("python")
#     def php(self):
#         print("php")
#     def english(self):
#         print("fine tune") 
#     def accounting(self):
#         print("bank accounting") 
#     def span(self):
#         print("spanish")            

# class teachers(college):
#     def web_dev(self):
#         print("web developer")
#     def maths(self):
#         print("mathematics")    

# anu=college()
# anu.accounting

# achu=teachers()
# achu.maths
# achu.english





                #multiple inheritance

# class college:
#     def __init__(s):
#         print('register')
#     def python(s):
#         print("python")
#     def php(self):
#         print("php")
#     def english(self):
#         print("fine tune") 
#     def accounting(self):
#         print("bank accounting") 
#     def span(self):
#         print("spanish") 

# class teachers:
#     def web_dev(self):
#         print("web developer")
#     def maths(self):
#         print("mathematics") 

# class students(teachers,college):
#     def register(self):
#         print('std reg')

# anu=college()
# anu.php()

# achu=teachers()
# achu.web_dev()

# anju=students()
# anju.python()                





            #multilevel inheritence
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

         

           
           