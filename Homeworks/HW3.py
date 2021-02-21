#Explain your work

#Day3Homework
def prime_first(num):
    num=int(input("Please enter an integer value"))
    def prime_second(num):  
        num=int(input("Please enter an integer value"))
        for i in range(0,1000):
            for i in range(0,500):  
                if num>1:       
                    for i in range(2,num):      
                        if (num%i)==0:  
                           print(num,"is not a prime number")      
                print(i,"times",num//i,"is",num)
                break       
            else:   
                print(num,"is a prime number")

                
    for i in range(500,1000):
         if num>1:       
             for i in range(2,num):      
                        if (num%i)==0:  
                           print(num,"is not a prime number")       
                           print(i,"times",num//i,"is",num)     
                           break        
             else:   
                print(num,"is a prime number")
