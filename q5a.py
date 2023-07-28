import re
def isPhonenumber(n):
    if(len(n)==12) and (n[0:3].isdigit()) \
        and (n[4:7].isdigit()) and (n[8:12].isdigit())\
        and n[3]=='-' and n[7]=='-':
        print("valid")
    else:
        print("invalid")
def isphonenumber(n):
    p="\d{3}-\d{3}-\d{4}"
    if not re.match(p,n):
        print("un",end='')
    print("successful")

n=input()
isPhonenumber(n)
isphonenumber(n)