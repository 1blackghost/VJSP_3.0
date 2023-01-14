import random

def generate(n):
    '''n:the length of random string to be generated 
    '''
    #This function generates a random string value that can be used to identify a user
    string="asdfasdasdsdasasassdfvergrtgertvgergferfreferfcnweccwcnwdcndcjciernvswefbwefvi3fg9r983"
    generated=""
    for i in range(n):
        r=random.randint(0,80)
        generated=generated+str(string[r])
    return generated
        
