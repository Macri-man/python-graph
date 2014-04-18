import pylab

#list_of_files=[ ('binarysearchoutput.txt', 'Binary Search Insertion Sort'), ('heapoutput.txt', 'Heap Sort'), ('mergeoutput.txt', 'Merge Sort'), ('insertionoutput.txt', 'Insertionsort'),('selectionoutput.txt', 'Selection Sort'), ('quickoutput.txt', 'Quick Sort')]

#list_of_files=[ ('selectionoutput.txt',' QuickSort Selection'),('medianoutput.txt','Median of Medians')]

#list_of_files=[ ('binarysearchoutput.txt','Binary Search Insertion Sort'),('theorybinarysearchoutput.txt', 'Theoretical Values')]

#list_of_files=[ ('heapoutput.txt','Heap Sort'),('theoryheapoutput.txt', 'Theoretical Values')]

#list_of_files=[ ('mergeoutput.txt', 'Merge Sort'),('theorymergeoutput.txt', 'Theoretical Values')]

#list_of_files=[ ('insertionoutput.txt', 'Insertion Sort'),('theoryinsertionoutput.txt', 'Theoretical Values')]

#list_of_files=[ ('selectionoutput.txt', 'Selection Sort'),('theoryselectionoutput.txt', 'Theoretical Values')]

#list_of_files=[ ('quickoutput.txt', 'Quick Sort'),('theoryquickoutput.txt', 'Theoretical Values')]

#list_of_files=[ ('randquickoutput.txt','Randomized Quick Sort'),('theoryrandquickoutput.txt', 'Theoretical Values')]

datalist = [ ( pylab.loadtxt(filename), label ) for filename, label in list_of_files ]
pylab.figure()
for data, label in datalist:
    pylab.plot( data[:,0], data[:,1], label=label)
    

pylab.legend()
pylab.title("Running Times of Different Sorting Algorithms")
pylab.xlabel("Length of Array")
pylab.ylabel("Number of Comparisons")
pylab.show()
