# Sorting
Different sorting algorithms in python compared to the .sort() from lib standard

## Speedtest
### FAST TESTS
Sorting 10 random int array of 1000 elements between -10 000 and 10 000.
* PySort      : 0.02 sec
* QuickSort   : 0.05 sec
* MergeSort   : 0.06 sec
* InsertSort  : 0.20 sec
* BubbleSort  : 1.87 sec

### MEDIUM TESTS
Sorting 10 random int array of 3000 elements between -10 000 and 10 000.
* PySort      : 0.07 sec
* QuickSort   : 0.17 sec
* MergeSort   : 0.20 sec
* InsertSort  : 1.75 sec
* BubbleSort  : Sorting is longer than 5 sec...Process killed

### LONG TESTS
Sorting 10 random int array of 10 000 elements between -10 000 and 10 000.
* PySort      : 0.22 sec
* QuickSort   : 0.61 sec
* MergeSort   : 0.71 sec
* InsertSort  : Sorting is longer than 5 sec...Process killed
* BubbleSort  : Sorting is longer than 5 sec...Process killed
