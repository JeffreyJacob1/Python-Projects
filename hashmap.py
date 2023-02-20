import numpy as np
from itertools import permutations
def queen(n):
    result=[] 
    finalResult=[] 
    count=0
    for cl in permutations(range(n)): 
        mtrx = np.zeros(n*n).reshape(n,n)     
        check =0 
        for i in range(n):
            if check != i*(i-1)/2:
                break
            for j in range(1,n):
                if i >= j:
                    if cl[i] == cl[i-j]+j or cl[i] == cl[i-j]-j: 
                        check = 0
                        break
                    else:
                        check += 1
                else:
                    continue
            
            if check == n*(n-1)/2: 
                count+=1
               
                
                for r in range(n):
                    result.append(cl[r]+1)
               
                finalResult.append(result)
                result=[]
              
                
            else:
                pass
    print("The ",n,"-queen problem has ",count,"solutions")
    return finalResult
    
            

def main():
    
    num = int(input("Enter a number of queens\n"))
    #calling function n-queen
    x=queen(num)
    for m in x: 
        print(m)


if __name__ == "__main__":
	main()
