# 1.Grading of the test marks of a student                                   sample input:  Grade(90)             marks
# 2.current bill                                                             sample input:  Bill(600)             units of bill
# 3.Print a triangle of height h                                             sample input:  Triangle("b",5)       srting,height
# 4.Armstrong or not, if not prints next armstrong                           sample input:  Armstrong(1)          number
# 5.Prime or not b/w a and b gives count andlist of primes                   sample input:  Prime(1,20)           start and end number
# 6.palindrome or not and prints next palindrome                             sample input:  Palindrome(931)       number
# 7.count of repeated numbers in a list                                      sample input:  Duplicatecount(5)     size of list                                                             
# 8.number of permutations of a list and what are they                       sample input:  Perlist(5)            size of list
# 9.vowels,consonants,digits,symbols in seperate string                      sample input:  Strcount(a)           string
# 10.difference of string a and b                                            sample input:  Diffstr("hel","gel")  2 strigs
# 11.number of alphabets and digits and white spaces and symbols             sample input:  Statement("ASD$")     string

def Grade(a):
    if (a<=100 and a>=86):
        print("Hey Congrats..! You got A+ Grade")
    elif(a<=85 and a>=76):
        print("Hey Congrats..! You got A Grade")
    elif(a<=75 and a>=66):
        print("Hey Congrats..! You got B Grade")
    elif(a<=65 and a>=51):
        print("Hey Congrats..! You got C Grade")
    elif(a<=50 and a>=36):
        print("Hey Congrats..! You got E Grade")
    elif(a<=35 and a>=0):
        print("Better Luck Next Time..! You got F Grade")
    else:
        print("Invalid Marks PLEASE ENTER AGAIN...!!")

def Bill(x):
    a=int(input())
    price=0
    if a>=0:
        if a<=50:
            price=a*3
        elif a<=51 and a>=200:
            price=50*3
            a=a-50
            price=price+a*4
        elif a<=200 and a>=450:
            price=50*3
            price=price+150*4
            a=a-200
            price=price+a*5
        else:
            price=50*3
            price=price+150*4
            price=price+150*5
            a=a-450
            price=price+a*6
        print(price)

def Triangle(c,b):
    for i in range(b):
        print((" ")*(b-i)+(c+" ")*(i+1))

def Armstrong(d):
    armstrong=d
    arm=0
    while(d>0):
        rem=d%10
        arm=arm+(rem*rem*rem)
        d=d//10
    if(armstrong==arm):
        print(str(arm)+" is a Armstrong Number")
    elif(armstrong!=arm):
        e=armstrong+1
        Armstrong(e)

def Prime(f,h):
    prlist=[]
    allcount=0
    for j in range(f,h+1):
        count=0
        for i in range(1,j+1):
            if (j%i==0):
                count=count+1
        if(count==2):
            prlist.append(j)
            allcount=allcount+1
    print(allcount,prlist)

def Palindrome(x):
    num=x
    rev=0
    while(x>0):
        rem=x%10
        rev=(rev*10)+rem
        x=x//10
    if num==rev:
        print(str(num)+" is a Palindrome")
    else:
        Palindrome(num+1)

def Duplicatecount(k):
    size=k
    orglist=[]
    sortedlist=[]
    print("Enter List Elements")
    for i in range(k):
        l=int(input())
        orglist.append(l)
    for i in orglist:
        if i not in sortedlist:
            sortedlist.append(i)
    print(sortedlist)
    for i in sortedlist:
        cou=0
        for j in orglist:
            if i==j:
                cou=cou+1
        print(i,"->",cou)

def Perlist(x):
    size=x
    list2=[]
    list3=[]
    count=0
    print("Enter List Elements")
    for i in range(x):
        b=int(input())
        list2.append(b)
    for i in range(len(list2)-1):
        for j in range(i+1):
            list3.append((list2[i],list2[j]))
            count=count+1
    print(count)
    print(list3)

def Statement(x):
    b,c,d,f="","","",""
    w,t,y,z=0,0,0,0
    for i in x:
        if(i.islower() or i.isupper()):
            b=b+i
            w=w+1
        elif(not i.isalnum() and i!=" "):
            c=c+i
            t=t+1
        elif(i.isdigit()):
            d=d+i
            y=y+1
        else:
            f=f+"space"
            z=z+1
    print(w,b)
    print(t,c)
    print(y,d)
    print(z,f)

def Diffstr(a,b):
    for i in b:
        if i not in a:
            print(i,end=" ")
def Strcount(a):
    count=0
    dig=0
    sp=0
    const=0
    for i in a:
        if i == "a" or i=="e" or i == "i" or i=="o" or i == "u" or i=="A" or i == "E" or i=="I" or i == "O" or i=="U":
            count=count+1
        elif i=="1" or i=="2" or i=="3"or i=="4" or i=="5" or i=="6"or i=="7"or i=="8"or i=="9" or i=="0":
            dig=dig+1
        elif not i.isalnum():
            sp=sp+1
        else:
            const=const+1
    print("Vowels ->",count)
    print("Consonents ->",const) 
    print("Numbers ->",dig)
    print("Special Characters ->",sp)
             








    
