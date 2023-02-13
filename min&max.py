
import random

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickSelect(arr, low, high, k):
    if low == high:
        return arr[low]
    pivotIndex = partition(arr, low, high)
    if pivotIndex == k:
        return arr[pivotIndex]
    elif pivotIndex > k:
        return quickSelect(arr, low, pivotIndex - 1, k)
    else:
        return quickSelect(arr, pivotIndex + 1, high, k)

def kthSmallest(arr, l, r, k):
    return quickSelect(arr, l, r, k - 1)














Your Task:
You don't have to read input or print anything. Your task is to complete the function kthSmallest() which takes the array arr[], integers l and r denoting the starting and ending index of the array and an integer K as input and returns the Kth smallest element.
 
 
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(log(n))
Constraints:
1 <= N <= 105
1 <= arr[i] <= 105
1 <= K <= N
The function partition is used to divide the array into two parts based on a pivot element. The pivot element is selected randomly in this implementation, but it can also be selected as the median or any other value to optimize the algorithm.

The function quickSelect implements the QuickSelect algorithm, which is a variation of QuickSort. It selects the kth smallest element in the array by partitioning the array and checking the pivot index. If the pivot index is equal to k, then the pivot element is returned. If the pivot index is greater than k, then the function is called on the left part of the array. If the pivot index is less than k, then the function is called on the right part of the array.

The function kthSmallest takes the array arr, the starting index l, the ending index r, and the value of k as input and returns the kth smallest element in the array by calling the quickSelect function. Note that in the implementation of quickSelect, the kth smallest element is calculated as k - 1 because the array is zero-indexed.
