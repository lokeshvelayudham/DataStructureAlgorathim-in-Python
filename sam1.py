def check_ab(str):
    if (len(str)==0):
        return True
    
    if (str[0] == 'a'):
        
        if (len(str[1:])>1 and str[1:3] == 'bb'):
            return check_ab(str[3:])
        
        else:
            return check_ab(str[1:])
        
    else:
        return False
    

str = input()
if (check_ab(str)):
    print("true")
else:
    print("false")