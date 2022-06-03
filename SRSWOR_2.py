import random
import math


class get_comb:
    draw= 3
    r=0
    b=0
    g=0
    while (r==b or b==g or g==r):
        print("Enter Dissimilar Values of the Number of balls")
        
        r=int(input("Enter the number of Red Balls"))
        b=int(input("E4nter the number of Blue Balls"))
        g=int(input("Enter the number of Green Balls"))
        
    r1=r
    b1=b
    g1=g
    x=1
        
         
        
    def c(a,b):
        #Calculating nCr
        return(math.factorial(a) / (math.factorial(b)*math.factorial(a-b)))
    
    while draw>1:
    #Calculating permutation for first two draws    


        list = [[0,0,2],[0,2,0],[2,0,0],[1,1,0],[1,0,1],[0,0,1]]                #Number of permutations for three picks
        LR= random.choice(list)
        #print(LR)
    
        x*=float(c(r,LR[0])*c(b,LR[1])*c(g,LR[2]))
        r=r-LR[0]
        b=b-LR[1]
        g=g-LR[2]
        draw=draw-1
    #Calculating Permutation for the third draw
    
    list1 = [[0,0,2],[0,2,0],[2,0,0]]                                           #Calculating Number of Similar Cases for third draw
    LR1= random.choice(list1)
    #print(LR1)
    
    x*=float(c(r,LR1[0])*c(b,LR1[1])*c(g,LR1[2]))

    j=r1+b1+g1
    total=float(c(j,2)*c(j-2,2)*c(j-4,2))                                       #Calculating Total Number of Outcomes
    
    print("Number of Picks have been considered 2 as per the question")
    
    print("Probability of picking same colored balls in the third draw is :", x/total)import random
import math


class get_comb:
    draw= 3
    r=0
    b=0
    g=0
    while (r==b or b==g or g==r):
        print("Enter Dissimilar Values of the Number of balls")
        
        r=int(input("Enter the number of Red Balls"))
        b=int(input("E4nter the number of Blue Balls"))
        g=int(input("Enter the number of Green Balls"))
        
    r1=r
    b1=b
    g1=g
    x=1
        
         
        
    def c(a,b):
        #Calculating nCr
        return(math.factorial(a) / (math.factorial(b)*math.factorial(a-b)))
    
    while draw>1:
    #Calculating permutation for first two draws    


        list = [[0,0,2],[0,2,0],[2,0,0],[1,1,0],[1,0,1],[0,0,1]]                #Number of permutations for three picks
        LR= random.choice(list)
        #print(LR)
    
        x*=float(c(r,LR[0])*c(b,LR[1])*c(g,LR[2]))
        r=r-LR[0]
        b=b-LR[1]
        g=g-LR[2]
        draw=draw-1
    #Calculating Permutation for the third draw
    
    list1 = [[0,0,2],[0,2,0],[2,0,0]]                                           #Calculating Number of Similar Cases for third draw
    LR1= random.choice(list1)
    #print(LR1)
    
    x*=float(c(r,LR1[0])*c(b,LR1[1])*c(g,LR1[2]))

    j=r1+b1+g1
    total=float(c(j,2)*c(j-2,2)*c(j-4,2))                                       #Calculating Total Number of Outcomes
    
    print("Number of Picks have been considered 2 as per the question")
    
    print("Probability of picking same colored balls in the third draw is :", x/total)
