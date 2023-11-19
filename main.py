import sys,random

max_tree_children = 5

class Tree:
    def __init__(self,data):
        self.data = data
        self.children = []

    def insert_random(self,data):
            r = random.randint(0,3)
            if (self.children == [] or (len(self.children) < max_tree_children and r == 0)):
                self.children.append(Tree(data))
            else:
                aux = random.choice(self.children)
                aux.insert_random(data)
            
    def show_tree(self):
        buffer = ""
        queue = [(self,0)]
        index = 0
        empty = Tree(lambda x:x)
        while(queue != []):
            aux,i = queue.pop(0)
            if (index < i):
                buffer+="\n"
                index = i
            if(aux == empty):
                buffer+= "leaf "
                continue
            buffer+= aux.data.__name__ + " "
            for child in aux.children:
                queue.append((child,i+1))
            for _ in range(max_tree_children - len(aux.children)):
                queue.append((empty,i+1))
            
        return buffer       

    def load_tree(self,buffer):
        queue = [self]
        for lines in buffer:
            node = queue.pop(0)
            index = 0
            for str in lines.split():
                if(index == max_tree_children):
                    node = queue.pop(0)
                    index = 0
                if(str != "leaf"):
                    aux = Tree(function_dictionary(str))
                    
                    node.children.append(aux)
                    queue.append(aux)
                index+=1



def average(list):
    return sum(list)/ len(list)

def geometric_average(list):
    aux = 1
    for x in list:
        aux = aux * x
    return pow(aux,1/sum(list))

def function_dictionary(str):
    if("average" == str): 
        return average
    if("geometric_average" == str):
        return geometric_average
    if("max"== str):
        return max
    if( "min"== str):
        return min 
    return lambda x:x


if __name__=="__main__":
    n = len(sys.argv)
    if(n < 2):
        print("no file passed as argument")
        sys.exit()
        
    filepath = sys.argv[1]
    file = open(filepath,'r')
    Lines = file.readlines()

    function = [max,min,average,geometric_average]
    root = Tree(lambda x:x)

    for line in Lines:
        f = random.choice(function)
        root.insert_random(f)
        print(line)
    
    buf = root.show_tree()
    print(buf)
    out = open("out",'w')
    out.write(buf)
    out.close()
    save = open("out",'r')
    Lines = save.readlines()

    root2 = Tree(lambda x:x)
    Lines.pop(0)
    root2.load_tree(Lines)
    
    print("\n\n")
    print(root2.show_tree())
    