#This function takes a string of polynomial cooeficients and value of the polynomial , 
# then returns the value of expression for the given polynomial
def f(user,x):
    f=0
    power=0
    userList = user.split(" ")
    for n in userList:
        if(int(n)!=0):
            f = f+(int(n)*(x**power))
        else:
            power+=1
        if(n== userList[0]):
            power= power+1
    
    return f
    

def main():
    user = input("Enter the polynomial coeffiecents: ")
    a,b = input("Enter the interval: ").split()
    a=int(a) #converting to integer
    b=int(b)
    m=0.000001 #tolerance
    if(f(user,a)*f(user,b)<0):
      while(abs(b-a)>=m):
        c=(a+b)/2
        if(f(user,c)<0):
           a=c
        else:
           b=c
      print("Root found at ",c)
    else:
        print("No roots are found!")
     

    
if __name__=="__main__":
    main()
