        #1

import module1
module1.fun()
module1.fun1()


        #2

import module1 as mod1
mod1.fun()
mod1.fun1()


        #3

from module1 import fun,fun1
fun(),fun1()


        #4

from module1 import*
fun()
fun1()