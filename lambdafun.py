
def lambda_filetr():
    numbers=[2,3,4,5,6,7,8,9]
    res=filter(lambda x:x%2==0,numbers)
    doubled_even = [x * 2 for x in res]  
    doubled_even.sort() 
    print(doubled_even)
lambda_filetr()