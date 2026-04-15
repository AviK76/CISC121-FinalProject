# CISC121-FinalProject

# TA Grading Queue Organizer

A list of submissions (student_id, submitted_at, file_name) is to be sorted by submission time. New submissions can be added, which must once again be sorted, and everything must animated to breakdown the process for the user.

## Merge Sort

Merge sort was chosen for this problem for several reasons. The first, and most important is that it is a stable sorting algorithm, since multiple assignments can have the same submission time. The splitting of the data sets is also easier to understand visually compared to Quicksort, where the pivot will jump into place, as opposed to Merge Sort, where the list is sorted left to right. This does, however rely on the fact that each submission has a timestamp, though there is no reason this wouldn't be the case.
This of course relies on the fact that the dataset is mutable, so submissions must be stored in an array.
During the simulation, the user will see the dataset get divided into subsection. Then, as segments are sorted, the elements being compared will be highlighted, to indicate this. As sorted lists are merged, the same process will happen, with the top elements being highlighted as the new, merged list is created. When a new submissions are added, the entire process is repeated. 

## Demo video/gif/screenshot of test
Sorry for how quick the GIF is, Github doesn't allow very big files.

![Recording 2026-04-15 104311](https://github.com/user-attachments/assets/d172b5e2-5204-4201-a074-d1155fa5f7ba)


<img width="2559" height="1331" alt="image" src="https://github.com/user-attachments/assets/50f4e3bf-703a-4e23-a6b2-8951a060159f" />


## Problem Breakdown & Computational Thinking

Breaking down this problem, it starts with the input, an list of assignments each with a student_id, submission time, and a file name. Once given the list, it is sorted using a merge sort. Merge sort works by dividing the list into smaller and smaller segments, sorting the segments, then merging them together, creating a sorted list by picking the lowest number between the two segments to be merged and placing it at the start of a new, sorted, segment until the entire list is merged back together. Once the starting list is sorted, new assignments can be added, upon which everything will be sorted again
.
Merge sort works by repeatedly dividing up the list until everything is in separate parts. It then repeatedly compares parts finding the smallest element, then adding it to a new, merged list, repeating until there are no smaller elements left. After creating a merged list, it repeats for every smaller segment until every new list is the same size, then they are compared and merged to make new, larger merged lists until everything is merged into the original list but sorted.

The user will be shown the process of the list being split up, and then the comparison of each element. In particular, they will be shown the comparing and selecting of the next element to be in the list, and then the merging of segments. They will not be shown how each process gets called, nor the creation of new assignments, though they will see new assignments appear.

Each assignment will be a list made up of three strings: student_id, submitted_at.  The assignments will be stored in an array, file_name, which will be what the user sees at first. This array is then sorted, the process of which will be shown to the user,  eventually outputting a sorted array, which will be an output. When a new assignments is generated, given to the system, where it will be attached to the end of the array, then sorted again, which the user will once again watch. Finally, once everything is finished the output will be the new, sorted array, which will be the final output until the user adds another assignment.

## Steps to Run

In order to run this locally, simply run each cell. If you are a notebook, like google colab, the Gradio UI should appear directly below the last cell, along with a link that will open up the UI on it's own in your browser. If you are running it out of something like VSCode, a link should appear in the terminal.
To use the organizer, simply input as many submissions as you wish in the valid format; student_id, submitted_at, file_name (An example is also provided inside the input box) and adjust the animation speed. Once you submit the assignments, the animation should appear in the output box, ending with the full, sorted list, with any invalid formats excluded.

## Hugging Face Link

https://huggingface.co/spaces/Herbert43/CISC121-Project

## Testing

There were several tests and edge cases ran:
1. Invalid times (Ex. 2026-99-99 99:99)
  The function would still sort this as you might expect, with the numbers being sorted low to high, however, I didn't like this, so I decided to add in a function to check for times thatt can't exist and just exclude them from the sorting and final list if they were found.
2. Times in the future (Ex. 2027-04-10 12:00)
   The function would also sort these properly, but once again, I didn't like it, so I added in another check in the validation function that excludes times in the future, and made sure to bring up different messages.
3. Incorrect format (Ex. student1, 12:00)
   If a submission didn't include every single field, everything would crash, so I had to add in another validation that would exclude submissions that didn't fill in all the fields.
4. Blank fields (Ex. , 2026-04-10 12:00, )
  The final test was on blank fields. What I found was that as long as there was a valid time, things went ahead, which I think is a good outcome. I didn't make any changes, because there could be submissions with no files attached.

Screenshots:

<img width="2559" height="1331" alt="image" src="https://github.com/user-attachments/assets/06f4345c-8642-4d18-9068-73bbd192ee25" />


## Author & AI Acknowledgment

AI was used during this project. It was not used at all in any of the README, nor was it used the write the original merge sort function or the first draft of the project. It was used in the majority of the Gradio work, specifically in the animation, but all material was gone over by myself and editted + verified. 

Sources: 
https://www.youtube.com/watch?v=xqdTFyRdtjQ
https://www.gradio.app/guides/quickstart
