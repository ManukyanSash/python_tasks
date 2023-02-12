import dis

def myfunc(alist):
    return len(alist)   
    
dis.dis(myfunc)

#   4 ֊ ցույց է տալիս մինչև ֆունկցիայի ավարտ տողերի քանակը
#               0 LOAD_GLOBAL              0 (len) քանի որ print֊ը built-in type է, գլոբալ փոփոխականը տեղադրվում է stack
#               2 LOAD_FAST                0 (alist) քանի որ alist֊ը ֆունկցիայի լոկալ փոփոխական է, լոկալ փոփոխականը տեղադրվում է stack
#               4 CALL_FUNCTION            1 տեղի է ունենում len ֆունկցիայի կանչ
#               6 RETURN_VALUE               տեղի է ունենում ֆունկցիայի արժեքի վերադարձ (return)