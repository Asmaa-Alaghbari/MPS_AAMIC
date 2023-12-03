from treeBulid import *
import threading

if __name__=="__main__":
    n = len(sys.argv)
    if(n < 2):
        print("no file passed as argument")
        sys.exit()

    if(n < 3):
        print("no refference file passed as argument")
        sys.exit()

    if(n < 4):
        print("no max number of threads")
        sys.exit()

    filepath = sys.argv[1]
    file = open(filepath,'r')
    Lines = file.readlines()
    filepath = sys.argv[2]
    reference = open(filepath,'r')

    referencetable = list(map(lambda x:x.split(','),reference.readlines()))
    Lines = list(map(lambda x:x[:-1] ,Lines))
    Values = Lines.pop(0).split(',')

    Nthreads = int(sys.argv[3])

    lock = threading.Lock()
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


