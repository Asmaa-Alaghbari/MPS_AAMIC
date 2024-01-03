from treeBulid import *
import threading
from concurrent.futures import ThreadPoolExecutor,as_completed

def mode1_buildtrees(Lines,Values,referencetable,lock):
    trees = []
    Fmeasures = []

    threads = []
    for _ in range (Nthreads):
        aux = threading.Thread(target=treeBuildRandom,args=(Lines,Values,referencetable,trees,Fmeasures,lock))
        aux.start()
        threads.append(aux)

    for thread in threads:
        thread.join()
    
    aver = max(Fmeasures)
    print(aver)
    print(Fmeasures)
    root = trees[Fmeasures.index(aver)]
    #save tree in file
    buf = root.show_tree()
    out = open("out.txt",'w')
    out.write(buf)
    out.close()

def mode2_test_tree(Lines,Values,referencetable,filepath,Nthreads):
    input = open(filepath,'r')

    input_lines = input.readlines()

    root = input_lines.pop(0)
    root2 = Tree(function_dictionary(root[:len(root)-2]))
    root2.load_tree(input_lines)
    input.close()
    Fmeasures = []

    with ThreadPoolExecutor(max_workers=Nthreads) as pool:
        futures = []
        for i in range(len(Lines)):
            future = pool.submit(solve_Line,root2,Values,Lines[i].split(','),referencetable,i)
            futures.append(future)
            
        for completed in as_completed(futures):
            Fmeasures.append(completed.result())

    print(average(Fmeasures))

if __name__=="__main__":
    n = len(sys.argv)
    mode = 1
    if(n < 2):
        print("no file passed as argument")
        sys.exit()

    if(n < 3):
        print("no refference file passed as argument")
        sys.exit()

    if(n < 4):
        print("no max number of threads")
        sys.exit()

    if(n < 5):
        mode = 0

    filepath = sys.argv[1]
    file = open(filepath,'r')
    Lines = file.readlines()
    filepath = sys.argv[2]
    reference = open(filepath,'r')

    referencetable = list(map(lambda x:x.split(','),reference.readlines()))
    Lines = list(map(lambda x:x[:-1] ,Lines))
    Values = Lines.pop(0).split(',')

    Nthreads = int(sys.argv[3])

    if (mode == 0):
        lock = threading.Lock()
        mode1_buildtrees(Lines,Values,referencetable,lock)
    if (mode == 1):
        mode2_test_tree(Lines,Values,referencetable,sys.argv[4],Nthreads)

    file.close()
    reference.close()

    


