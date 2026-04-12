# CISC121-FinalProject

# TA Grading Queue Organizer

A list of submissions (student_id, submitted_at, file_name) is to be sorted by submission time. New submissions can be added, which must once again be sorted, and everything must animated to breakdown the process for the user.

## Merge Sort

Merge sort was chosen for this problem for several reasons. The first, and most important is that it is a stable sorting algorithm, since multiple assignments can have the same submission time. The splitting of the data sets is also easier to understand visually compared to Quicksort, where the pivot will jump into place, as opposed to Merge Sort, where the list is sorted left to right. This does, however rely on the fact that each submission has a timestamp, though there is no reason this wouldn't be the case.
This of course relies on the fact that the dataset is mutable, so submissions must be stored in an array.
During the simulation, the user will see the dataset get divided into subsection. Then, as segments are sorted, the elements being compared will be highlighted, to indicate this. As sorted lists are merged, the same process will happen, with the top elements being highlighted as the new, merged list is created. When a new submissions are added, the entire process is repeated. 

## Demo video/gif/screenshot of test

## Problem Breakdown & Computational Thinking

Breaking down this problem, it starts with the input, an list of assignments each with a student_id, submission time, and a file name. Once given the list, it is sorted using a merge sort. Merge sort works by dividing the list into smaller and smaller segments, sorting the segments, then merging them together, creating a sorted list by picking the lowest number between the two segments to be merged and placing it at the start of a new, sorted, segment until the entire list is merged back together. Once the starting list is sorted, new assignments can be added, upon which everything will be sorted again
.
Merge sort works by repeatedly dividing up the list until everything is in separate parts. It then repeatedly compares parts finding the smallest element, then adding it to a new, merged list, repeating until there are no smaller elements left. After creating a merged list, it repeats for every smaller segment until every new list is the same size, then they are compared and merged to make new, larger merged lists until everything is merged into the original list but sorted.

The user will be shown the process of the list being split up, and then the comparison of each element. In particular, they will be shown the comparing and selecting of the next element to be in the list, and then the merging of segments. They will not be shown how each process gets called, nor the creation of new assignments, though they will see new assignments appear.

Each assignment will be a list made up of three strings: student_id, submitted_at.  The assignments will be stored in an array, file_name, which will be what the user sees at first. This array is then sorted, the process of which will be shown to the user,  eventually outputting a sorted array, which will be an output. When a new assignments is generated, given to the system, where it will be attached to the end of the array, then sorted again, which the user will once again watch. Finally, once everything is finished the output will be the new, sorted array, which will be the final output until the user adds another assignment.

## Steps to Run

## Hugging Face Link

## Author & AI Acknowledgment
