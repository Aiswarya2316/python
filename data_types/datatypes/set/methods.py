s={1,2,3,"a","b",}
s1={2,4,6,3,8,10,"c","d"}


#        #  1) add

# s.add("f") 
# print(s)  


#         #  2) clear

# s.clear()
# print(s)  


#         #  3) copy

# c=s.copy()
# print(c)
    


#         #  4) difference

# print(s.difference(s1))
       


#         #  5) discard

# s.discard("a")  
# print(s)   



#         #  6)  remove

# s1.remove(4)
# print(s1) 



#         #  7) intersection

# print(s1.intersection(s))



#         #   8)isdisjoint

# print(s1.isdisjoint(s))        



#         #  9)issubset

# print(s1.issubset({2,4,6,8,10,3,"c","d"}))      



#         #  10)issuperset

# print(s1.issuperset({2,4,6,8,10,3,"c","d"})) 
    


#         #  11)pop

# s.pop()
# print(s)



#         #  12)symmetriv_difference

# print(s.symmetric_difference({10,11,12}))   



#         #  13)union

# print(s.union({10,11,12,6}))   



#         #  14)update

# s.update({10,11,12,15,3,7})   
# print(s)



        # difference_update

print(s.difference({10,11,12,9}))
print(s.symmetric_difference({10,11,12,9}))           
      