from tree import Tree
from functions import *
import sys,random

def treeBuildRandom(Lines,Values,referencetable,roots,averages,lock):

    functions = [maximun,minimun,average,geometric_average,square_average,harmonic_average]
    root = Tree(random.choice(functions))

    for _ in range(random.randint(20,50)):
        f = random.choice(functions)
        root.insert_random(f)

    root.complete_tree(Values)
    for _ in range(random.randint(20,100)):
        root.insert_leaf(random.choice(Values))
    
    Fmeasures = []
    #calculates fmeasure for each line
    for i in range(len(Lines)):
        aux = root.solve_root(Values,Lines[i].split(','))
        aux= round(aux * 255)
        aux = min([aux,255])
        Fmeasures.append(float(referencetable[i+1][aux]))

    #fmeasure average
    lock.acquire()
    roots.append(root)
    averages.append(average(Fmeasures))
    lock.release()



if __name__=="__main__":
    n = len(sys.argv)
    if(n < 2):
        print("no file passed as argument")
        sys.exit()

    if(n < 3):
        print("no refference file passed as argument")
        sys.exit()

    filepath = sys.argv[1]
    file = open(filepath,'r')
    Lines = file.readlines()
    filepath = sys.argv[2]
    reference = open(filepath,'r')
    referencetable = list(map(lambda x:x.split(','),reference.readlines()))

    functions = [maximun,minimun,average,geometric_average,square_average,harmonic_average]
    root = Tree(random.choice(functions))

    Lines = list(map(lambda x:x[:-1] ,Lines))
    Values = Lines.pop(0).split(',')

    #build tree, randomly. add a random ammount of functions, and variables
    #might change the range idk
    for _ in range(random.randint(10,20)):
        f = random.choice(functions)
        root.insert_random(f)

    root.complete_tree(Values)
    for _ in range(random.randint(10,20)):
        root.insert_leaf(random.choice(Values))
    
    #save tree in file
    buf = root.show_tree()
    out = open("out.txt",'w')
    out.write(buf)
    out.close()

    Fmeasures = []
    #calculates fmeasure for each line
    for i in range(len(Lines)):
        aux = root.solve_root(Values,Lines[i].split(','))
        aux= round(aux * 255)
        aux = min([aux,255])
        Fmeasures.append(float(referencetable[i+1][aux]))

    #fmeasure average
    print(average(Fmeasures))
    