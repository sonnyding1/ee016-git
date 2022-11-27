# @arg arr The input list like object to be sorted
# @arg cmp A compare function which takes two element in the array, 
#          cmp(a,b)<0   if a should be placed before b,
#          cmp(a,b)==0  if arr is still sorted after a and b are exchanged,
#          cmp(a,b)>0   if a should be placed behind b.
def multi_sort(arr, cmp, method="None"):
    if(method=="quick"):
        quick_sort(arr,cmp)
    elif(method=="merge"):
        merge_sort(arr,cmp)
    elif(method=="None"): # do nothing
        return
    else:
        print("invalid argument!")
        
        
        
        
# must be in-place sort
def merge_sort(arr,cmp):
    pass
# must be in-place sort
def quick_sort(arr,cmp):

    #used to find pivot position and partition the array 
    def partition(array, low, high, idx_pivot):

        #move pivot to the beginning for now
        pivot = array[idx_pivot]
        array[low], array[idx_pivot] = array[idx_pivot], array[low]
        i = low + 1
        j = low + 1

        #partition
        while j <= high:
            if cmp(array[j],  pivot) < 0:

                array[j], array[i] = array[i], array[j]
                i += 1
            j += 1

        #move pivot to where it should be
        array[low], array[i - 1] = array[i - 1], array[low]
        return i - 1

    def quicksort(array, low=0, high=None):
        if high == None:
            high = len(array) - 1
        if high - low < 1:
            return array
        idx_pivot = random.randint(low, high)
        i = partition(array, low, high, idx_pivot)
        quicksort(array, low, i - 1)
        quicksort(array, i + 1, high)

        return array

    return quicksort(arr, 0, None)
