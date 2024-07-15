        #single

# class synnefo:
#     def __init__(s):
#         print('register')
#     def python(s):
#         s.database='mysql'
#         print("python")
#     def php(self):
#         self.database='mysql'
#         print("php",self.database)

# class novavi(synnefo):
#     def dm(self):
#         print("digital marketing")
#     def web_dev(self):
#         print("web developer")

# anu=synnefo()
# anu.php()

# achu=novavi()
# achu.dm()
# achu.python()

            #multiple

# class synnefo:
#     def __init__(s):
#         print('register')
#     def python(s):
#         s.database='mysql'
#         print("python")
#     def php(self):
#         self.database='mysql'
#         print("php",self.database)

# class novavi:
#     def dm(self):
#         print("digital marketing")
#     def web_dev(self):
#         print("web developer")

# class std(novavi,synnefo):
#     def reg(self):
#         print('std reg')

# anu=synnefo()
# anu.php()

# achu=novavi()
# achu.dm()

# anju=std()
# anju.python()

            #multilevel

# class synnefo:
#     def __init__(s):
#         print('register')
#     def python(s):
#         s.database='mysql'
#         print("python")
#     def php(self):
#         self.database='mysql'
#         print("php",self.database)

# class novavi(synnefo):
#     def dm(self):
#         print("digital marketing")
#     def web_dev(self):
#         print("web developer")

# class staff(novavi):
#     def reg(self):
#         print('std reg')

# anu=synnefo()
# anu.php()

# achu=novavi()
# achu.dm()
# achu.php

# anju=staff()
# anju.python()
# anju.reg


            #heirarchichal


# class synnefo:
#     def __init__(s):
#         print('register')
#     def python(s):
#         s.database='mysql'
#         print("python")
#     def php(self):
#         self.database='mysql'
#         print("php",self.database)

# class novavi(synnefo):
#     def dm(self):
#         print("digital marketing")
#     def web_dev(self):
#         print("web developer")

# class std(synnefo):
#     def reg(self):
#         print('std reg')

# anu=synnefo()
# anu.php()

# achu=novavi()
# achu.dm()
# achu.database

# anju=std()
# anju.python()
# anju.reg


            #hybrid

# class synnefo:
#     def __init__(s):
#         print('register')
#     def python(s):
#         s.database='mysql'
#         print("python")
#     def php(self):
#         self.database='mysql'
#         print("php",self.database)

# class novavi(synnefo):
#     def dm(self):
#         print("digital marketing")
#     def web_dev(self):
#         print("web developer")

# class std(novavi):
#     def reg(self):
#         print('std reg')

# class staff(synnefo,novavi):
#     def wrk(self):
#         print("works")

# anu=synnefo()
# anu.php()

# achu=novavi()
# achu.dm()
# achu.database

# anju=std()
# anju.python()
# anju.reg

# ammu=staff()
# ammu.python()
# ammu.web_dev()
# ammu.wrk


            #or

class A:
    def a1(self):
        print('a1')
class B:
    def b1(self):
        print('b1')
class F:
    def f1(self):
        print('f1')        
class C(A,B):
    def c1(self):
        print('c1')
class D(B,F):
    def d1(self):
        print('d1')
class E(C,D):
    def e1(self):
        print('e1')
                                        

aa=A()
aa.a1()

ee=E()
ee.a1()
ee.b1()
ee.c1()
ee.d1()
ee.e1()