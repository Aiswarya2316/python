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

# class college:
#     def __init__(s):
#          print('register')
#     def python(s):
#          print("python")
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

# class staff(teachers):
#     def reg(self):
#         print('staff reg')

# anu=college()
# anu.php()

# achu=teachers()
# achu.web_dev()
# achu.php()

# anju=staff()
# anju.python()
# anju.reg

         

           

                        #hybrid        

# class college:
#     def __init__(s):
#          print('register')
#     def python(s):
#          print("python")
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

# class std(teachers):
#     def reg(self):
#         print('std reg')

# class staff(college,teachers):
#     def wrk(self):
#         print("staff reg")

# anu=college()
# anu.php()

# achu=teachers()
# achu.accounting()

# anju=std()
# anju.python()
# anju.reg

# ammu=staff()
# ammu.python()
# ammu.web_dev()
# ammu.wrk()  





                     #heirarchichal

# class college:
#     def __init__(s):
#          print('register')
#     def python(s):
#          print("python")
#     def php(self):
#         print("php")
#     def english(self):
#         print("fine tune") 
#     def accounting(self):
#         print("bank accounting") 
#     def span(self):
#         print("spanish") 
# class teachers(college):
#     def dm(self):
#         print("digital marketing")
#     def web_dev(self):
#         print("web developer")

# class std(college):
#     def reg(self):
#         print('std reg')

# anu=college()
# anu.php()

# achu=teachers()
# achu.dm()

# anju=std()
# anju.python()
# anju.reg
