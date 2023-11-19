from tree import Tree,average,geometric_average
import sys,random

def maximun(list):
    if(list ==[]):
        return 0
    return max(list)

def minimun(list):
    if(list ==[]):
        return 0
    return min(list)

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

    functions = [maximun,minimun,average,geometric_average]
    root = Tree(random.choice(functions))

    Lines = list(map(lambda x:x[:-1] ,Lines))
    Values = Lines.pop(0).split(',')

    #build tree, randomly. add a random ammount of functions, and variables
    #might change the range idk
    for _ in range(random.randint(10,20)):
        f = random.choice(functions)
        root.insert_random(f)

    for _ in range(random.randint(40,80)):
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
        Fmeasures.append(float(referencetable[i+1][aux]))

    #fmeasure average
    print(average(Fmeasures))
    
    
    