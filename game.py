"""game guess number"""
import numpy as np

def random_predict(number: int= 1) -> int:
    """Function for determining the number and number of guessing attempts
    
    Args:
        number (int, optional): determined number. Defaults to 1.
        
    Returns:
        int: number, int:count of attempts
        """
    count= 0
    min_number= 1
    max_number= 100
    
    while True:
        count+=1
        mean= (max_number+min_number)//2 #midrange search
        if number < mean:
            max_number = mean #if the number is less then midrange,then
                              #the maximum limit is equal to the midrange
        elif number > mean:
            min_number = mean #if the number is greater then midrange,then
                              #the minimum limit is equal to the midrange
        else:
            return mean, count
        

val= np.random.randint(1,101) #setting a rndom number from1 to 100
print("Value= ", val)
print("Pradicted value & count: ", random_predict(val))