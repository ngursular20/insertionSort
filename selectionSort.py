def selectionSort(array, size):
    for step in range(size):
        minimum = step 
        for i in range(step +1, size):
            if array[i] < array[minimum]:
                minimum = i
        (array[step], array[minimum]) = (array[minimum], array[step])






