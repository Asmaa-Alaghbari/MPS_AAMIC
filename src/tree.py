import sys,random
from functions import *
#constant, max children a node cand have
max_tree_children = 5

class Tree:
    #init a node, data should be the function
    def __init__(self,data):
        self.data = data
        self.children = []

    #inserts a new node randomly inside tree
    def insert_random(self,data):
        r = random.randint(0,3)
        if (self.children == [] or (len(self.children) < max_tree_children and r == 0)):
            self.children.append(Tree(data))
        else:
            aux = random.choice(self.children)
            aux.insert_random(data)
    #inserts leaf inside tree randomly (sometines it cannot insert)
    def insert_leaf(self,data):
        r = random.randint(0,5)
        if (self.children == [] or (len(self.children) < max_tree_children and r == 0)):
            self.children.append(Tree(data))
        else:
            aux = random.choice(self.children)
            if(not isinstance(aux.data,str)):
                aux.insert_random(data)
    #makes sure every node has at least 2 leafs
    def complete_tree(self,data):
        if (self.children == []):
            for _ in range(random.randint(2,max_tree_children)):    
                self.children.append(Tree(random.choice(data)))
        else:
            Len = len(self.children)
            if(Len == 1 ):
                for _ in range(random.randint(1,max_tree_children-1)):    
                    self.children.append(Tree(random.choice(data)))
            for child in self.children:
                if(not isinstance(child.data,str)):
                    child.complete_tree(data)

    #returns the tree as a string
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
            if(isinstance(aux.data,str)):
                buffer+= aux.data + " "
                continue
            else:
                buffer+= aux.data.__name__ + " "
            for child in aux.children:
                queue.append((child,i+1))
            for _ in range(max_tree_children - len(aux.children)):
                queue.append((empty,i+1))
            
        return buffer       

    #loads a tree in memory from a string
    def load_tree(self,buffer):
        queue = [self]
        for lines in buffer:
            node = queue.pop(0)
            index = 0
            for Str in lines.split():
                if(index == max_tree_children):
                    node = queue.pop(0)
                    index = 0
                if(Str != "leaf"):
                    aux = Tree(function_dictionary(Str))
                    
                    node.children.append(aux)
                    if(not isinstance(aux.data,str)):
                        queue.append(aux)
                index+=1
    
    #solves values based on line
    def solve_root(self,values,line):
        if(isinstance(self.data,str)):
            return float(line[values.index(self.data)])
        par = []
        for child in self.children:
            par.append(child.solve_root(values,line))
        return self.data(par)

if __name__=="__main__":
    n = len(sys.argv)
    if(n < 2):
        print("no file passed as argument")
        sys.exit()
        
    filepath = sys.argv[1]
    file = open(filepath,'r')
    Lines = file.readlines()

    function = [maximun,minimun,average,geometric_average]
    root = Tree(lambda x:x)

    #for each line i add another node inside the tree
    for line in Lines:
        f = random.choice(function)
        root.insert_random(f)
        print(line)
    
    #print and save tree in file
    buf = root.show_tree()
    print(buf)
    out = open("out",'w')
    out.write(buf)
    out.close()

    #opens file and loades tree in memory
    save = open("out",'r')
    Lines = save.readlines()

    root2 = Tree(lambda x:x)
    Lines.pop(0)
    root2.load_tree(Lines)
    
    print("\n\n")
    print(root2.show_tree())
    
    #checks if copied properly
    print("\n\n")
    print(root.show_tree() == root2.show_tree())
    