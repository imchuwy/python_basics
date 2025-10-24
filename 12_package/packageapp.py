##import package and file. But its long
#import package.module
#package.module.function1()
#package.module.class1()


##This is bit better. The from
#from package.module import function1, class1
#function1()
#class1()


#This imports all functions or classes at once
from package import module
module.function1()
module.class1()