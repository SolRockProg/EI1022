from algoritmia.datastructures.prioritymaps import HeapMap

if __name__ == "__main__":
    k = HeapMap(opt=min, data={(1, 0): 3, (3, 2): 5, (0, 0): 4}, redimMap=lambda k,v: -k)
    print(k.extract_opt())
    k[(0,0)]+=2
    print(k.extract_opt())
    print(k.extract_opt())