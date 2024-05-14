##############################################
#				                    	     #
#    Experimental Comparison                 #
#               of Sorting Algorithms        #
#              				                 #
#		        github.com/ml3m		         #
#					                         #
##############################################

import math, random

_defaultCompare = lambda x, y: x - y
_defaultKey = lambda a: a

# my isSorted method to make sure everything is sorted at the end
def isSorted(l, compare=_defaultCompare, key=_defaultKey, ascending=False):   
    for i in range(len(l)-1):
        if 0 < compare(key(l[i]), key(l[i+1])) * (-1 if ascending else 1):
            return False
    return True

# we declare a _Template that will be inherited by each sorting function in order 
# to facilitate of function like sort, _exchangeByIndex or _compareByIndex
class _Template(object): 
    def __init__(self, compare=_defaultCompare, key=_defaultKey, ascending=False):
        self._compare = compare
        self._key = key
        self._ascending = ascending
        self._sortingInput = None
        self._sortingList = []
    
    def _compareByIndex(self, a, b):
        return self._compareElements(self._sortingList[a], self._sortingList[b])
                                     
    def _compareElements(self, a, b):
        com = self._compare(self._key(a), self._key(b))
        if self._ascending: com *= -1
        return com
    
    def _exchangeByIndex(self, a, b):
        tmp = self._sortingList[a]
        self._sortingList[a] = self._sortingList[b]
        self._sortingList[b] = tmp

    def _copyList(self, fr):
        return list(fr)

# main sorting method used on all of the algorithms bellow
    def sort(self, o, cloneBeforeSort=True):
        self._sortingInput = o
        self._sortingList = self._copyList(o) if cloneBeforeSort else o
        self._do()
        return self._sortingList
    
    def _do(self):
        raise NotImplementedError


class BubbleSort(_Template):
    def _do(self):
        for i in range(0, len(self._sortingList)-1):
            changed = False
            for j in range(0, len(self._sortingList)-i-1):
                if self._compareByIndex(j, j+1) > 0:
                    self._exchangeByIndex(j, j+1)
                    changed = True

            if not changed:
                break

class SelectionSort(_Template):
    def _do(self):
        for sortedCounter in range(0, len(self._sortingList)):
            max = 0
            for i in range(1, len(self._sortingList)-sortedCounter):
                if self._compareByIndex(i, max) > 0:
                    max = i
            if max != len(self._sortingList)-sortedCounter-1:
                self._exchangeByIndex(max, len(self._sortingList)-sortedCounter-1)
    
class InsertSort(_Template):
    def _do(self):
        for i in range(1, len(self._sortingList)):
            j = i - 1
            tmp = self._sortingList[i]
            while j >= 0 and self._compareElements(self._sortingList[j], tmp) > 0:
                self._sortingList[j+1] = self._sortingList[j]
                j -= 1
            self._sortingList[j+1] = tmp

class QuickSort(_Template):
    def _do(self):
        self._rek(0, len(self._sortingList)-1)
    
    def _rek(self, left, right):
        li = left
        re = right
        vergl = self._sortingList[int((left + right) / 2)]

        first = True
        while first or li <= re:
            first = False
            while self._compareElements(self._sortingList[li], vergl) < 0:
                li += 1
            while self._compareElements(self._sortingList[re], vergl) > 0:
                re -= 1
            if li <= re:
                self._exchangeByIndex(li, re)
                li += 1
                re -= 1
        if left < re:
            self._rek(left, re)
        if right > li:
            self._rek(li, right)

class MergeSort(_Template):
    def _do(self):
        self._rek(1)
    
    def _rek(self, block):
        tmp = self._copyList(self._sortingList)
        
        if block < len(self._sortingList):
            for compNo in range(int(math.ceil(len(self._sortingList) / (2.0 * block)))):
                s1 = block * 2 * compNo
                s2 = s1 + block
                i1 = s1
                i2 = s2
                                
                for c in range(2 * block):
                    i1AmLimit = i1 >= s2
                    i2AmLimit = i2 >= s2 + block
                    
                    used = 1
                    if not (i1AmLimit or i2AmLimit):
                        used = 1 if self._compareByIndex(i1, i2) < 0 else 2
                    elif i1AmLimit:
                        used = 2

                    tmp[s1 + c] = self._sortingList[i1 if used == 1 else i2]
                    if used == 1:
                        i1 += 1
                    else:
                        i2 += 1
                    
            self._sortingList = tmp    
            self._rek(block * 2)

class HeapSort(_Template):
    def drain(self, i, l, r):
        drainNeed = True
        tmp = self._sortingList[i]
        
        while 2*(i-l)+1+l <= r:
            j = 2 * (i - l) + 1 + l
            if j+1 <= r and self._compareByIndex(j, j+1) < 0:
                j += 1
            if self._compareElements(tmp, self._key(self._sortingList[j])) < 0:
                self._sortingList[i] = self._sortingList[j]
                i = j
            else:
                self._sortingList[i] = tmp
                i = r
                drainNeed = False
        
        if drainNeed:
            self._sortingList[i] = tmp
        
    def _do(self):
        for i in range(int((len(self._sortingList)+1)/2))[::-1]:
            self.drain(i, 0, len(self._sortingList)-1)
        for i in range(len(self._sortingList))[::-1]:
            self._exchangeByIndex(0, i)
            self.drain(0, 0, i-1)

class Timsort(_Template):
    MIN_MERGE = 32

    def _insertion_sort(self, arr, start, end):
        for i in range(start + 1, end + 1):
            key = arr[i]
            j = i - 1
            while j >= start and self._compareElements(arr[j], key) > 0:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    def _merge(self, arr, l, m, r):
        len1, len2 = m - l + 1, r - m
        left, right = arr[l:l + len1], arr[m + 1:m + 1 + len2]

        i, j, k = 0, 0, l

        while i < len1 and j < len2:
            if self._compareElements(left[i], right[j]) <= 0:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len1:
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len2:
            arr[k] = right[j]
            j += 1
            k += 1

    def _do(self):
        min_run = self.MIN_MERGE
        n = len(self._sortingList)

        # Insertion sort on small subarrays
        for start in range(0, n, min_run):
            end = min(start + min_run - 1, n - 1)
            self._insertion_sort(self._sortingList, start, end)

        # Merge sort on larger subarrays
        size = min_run
        while size < n:
            for start in range(0, n, size * 2):
                mid = min(n - 1, start + size - 1)
                end = min(n - 1, mid + size)
                if mid < end:
                    self._merge(self._sortingList, start, mid, end)
            size *= 2

class SmoothSort(_Template):
    def _siftdown(self, start, end):
        root = start

        while root * 2 + 1 <= end:
            child = root * 2 + 1
            swap = root

            if self._compareByIndex(swap, child) < 0:
                swap = child

            if child + 1 <= end and self._compareByIndex(swap, child + 1) < 0:
                swap = child + 1

            if swap == root:
                return
            else:
                self._exchangeByIndex(root, swap)
                root = swap

    def _do(self):
        n = len(self._sortingList)
        
        # Build heap
        for i in range(n // 2 - 1, -1, -1):
            self._siftdown(i, n - 1)
        
        # Smooth down heap
        for i in range(n - 1, 0, -1):
            self._exchangeByIndex(0, i)
            self._siftdown(0, i - 1)

class RadixSort(_Template):
    def _do(self):
        maximum = max(self._sortingList)
        exp = 1
        while maximum // exp > 0:
            self._do_radix(self._sortingList, exp)
            exp *= 10

    def _do_radix(self, arr, exp):
        n = len(arr)
        output = [0] * n
        count = [0] * 10

        for i in range(n):
            index = arr[i] // exp
            count[index % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = n - 1
        while i >= 0:
            index = arr[i] // exp
            output[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1
            i -= 1

        for i in range(0, len(arr)):
            arr[i] = output[i]

class CombSort(_Template):
    def _do(self):
        n = len(self._sortingList)
        gap = n
        shrink = 1.3
        sorted = False

        while not sorted:
            gap = int(gap / shrink)
            if gap <= 1:
                gap = 1
                sorted = True

            i = 0
            while i + gap < n:
                if self._compareByIndex(i, i + gap) > 0:
                    self._exchangeByIndex(i, i + gap)
                    sorted = False
                i += 1
