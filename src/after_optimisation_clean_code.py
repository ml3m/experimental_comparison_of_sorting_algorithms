from PySortAlgos import BubbleSort, SelectionSort, InsertSort, QuickSort, MergeSort, HeapSort, isSorted
import time, random

TEST_E = 30 # ~ 1bil only for test puposes
START_E = 2 # 2^2 = 4
MAX_E = 16 # 2^22 = 4.194.304
TRIES = 1  # default will be 1, maybe a better implementation for final paper

TOTEST = (
    
   #(Class,         Name,            Max)
   # (BubbleSort,    "BubbleSort",    17),
   # (SelectionSort, "SelectionSort", 17),
   # (InsertSort,    "InsertSort",    18),
    (HeapSort,      "HeapSort",      16),
    (MergeSort,     "MergeSort",     16),
    (QuickSort,     "QuickSort",     16),
    )

nameList = "\t\t".join(r[1] for r in TOTEST)

print("Elements\t\t" + nameList)

e = START_E
while e <= MAX_E:
    res = []
    max = -1
    for algorithm, name, limit in TOTEST:
        if e > limit:
            res.append(None)
        else:
            sum = 0
            for _ in range(TRIES):
                list_to_sort = list(range(0, 2**e))
                random.shuffle(list_to_sort)

                t1 = time.time()
                sortedlist = algorithm().sort(list_to_sort) 

                sum += time.time() - t1
                if not isSorted(sortedlist):
                    print("Error in " + name)

            res.append(sum / TRIES)
            if res[-1] > max:
                max = res[-1]


    tp = "2^" + str(e) + " = " + str(2**e) + " \t\t"
    for v in res:
        if v == None:
            tp += " \t\t"
        else:
            p = "0"
            if max > 0:
                p = str(round(100*v/max, 2))
            tp += str(round(v, 5)) + "s (" + p + "%)"
            if v == 0: tp += "   "
        tp += "    \t"
    print(tp)
    e += 1
       
print("\nFinish :)")
