def towerofhanoi(n , From, To, Left): 
    if n>=1:
        towerofhanoi(n-1, From, Left, To)
        print (f"Move disk from {From} to {To}") 
        towerofhanoi(n-1, Left, To, From)

towerofhanoi(3, '1','3','2')
   
