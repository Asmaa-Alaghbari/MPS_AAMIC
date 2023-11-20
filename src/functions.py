
def maximun(list):
    if(list ==[]):
        return 0
    return max(list)

def minimun(list):
    if(list ==[]):
        return 0
    return min(list)

def average(list):
    if(list == []):
        return 0
    return sum(list)/ len(list)

def geometric_average(list):
    if(list == []):
        return 0
    aux = 1
    for x in list:
        aux = aux * x
    return pow(aux,1/len(list))

def harmonic_average(list):
    if(list == []):
        return 0
    aux = 0
    for x in list:
        if(x == 0):
            continue
        aux+= pow(x,-1)
    if(aux == 0):
        return 0
    return sum(list)/aux
    
def square_average(list):
    if(list == []):
        return 0
    aux = 0
    for x in list:
        aux+= x**2
    return pow(aux/len(list),1/2)

def function_dictionary(str):
    if("average" == str): 
        return average
    if("geometric_average" == str):
        return geometric_average
    if("harmonic_average" == str):
        return harmonic_average
    if("square_average" == str):
        return square_average
    if("maximun"== str):
        return maximun
    if( "minimun"== str):
        return minimun 
    return str