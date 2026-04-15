import gradio as gr
import time
from datetime import datetime

def validate_time(time_str):
    """
    Validates whether a timestamp is:
    1. In the correct format
    2. A real calendar time
    3. Not in the future

    Used to prevent impossible submission times entering the system.
    """

    try:
        # Attempt to convert string into a datetime object
        parsed = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")

    except:
        # If parsing fails, format is invalid (e.g. "abc", "2026-99-99")
        return ("invalid_format", None)

    #Checks if the submission time is in the future 
    if parsed > datetime.now():
        return ("future_date", parsed)

    # If both checks pass, time is valid
    return ("valid", parsed)

steps = []

def merge(list_1, list_2):
    """
    Merges two already-sorted lists into a single sorted list.
    The elements of list_1 and list_2 must all be
    comparable to one another with < (less than).
    """
    list_m = [] #The merged list
    i = 0
    j = 0

    while i < len(list_1) and j < len(list_2):
        # Show comparison
        steps.append(("compare", list_1[i], list_2[j]))

        if list_1[i][1] <= list_2[j][1]:
            list_m.append(list_1[i])
            i += 1
        else:
            list_m.append(list_2[j])
            j += 1

        # Show merge progress
        steps.append(("merge", list_m.copy()))

    while i < len(list_1):
        list_m.append(list_1[i])
        i += 1
        steps.append(("merge", list_m.copy()))

    while j < len(list_2):
        list_m.append(list_2[j])
        j += 1
        steps.append(("merge", list_m.copy()))

    return list_m


def sort(submissions):
    """
    The function that actually sorts the lists.
    Begins by splitting up lists
    Recursively sorting the split pieces
    Finishes by merging the pieces back together
    """
    n = len(submissions)

    if n <= 1: #Base case
        return submissions

    # Show splitting
    steps.append(("split", submissions.copy()))
    
    #Recursively sorts both halves by submission time
    left = submissions[:n//2]
    right = submissions[n//2:]

    #Sorts each half then calls the previous function to merge them
    return merge(sort(left), sort(right))

def add_submission(submissions, student_id, submitted_at, file_name):
    """
    This function is how the submissions are actually put into the system.
    This is mainly just to use the validate_time function to check for invalid times.
    """
    #Using the validation function to only send valid times to be sorted
    status, parsed_time = validate_time(submitted_at)

    if status == "invalid_format":
        print(f" Invalid time format: {submitted_at}")
        return submissions

    if status == "future_date":
        print(f" Future date detected: {submitted_at}")
        return submissions

    #The actual adding of the valid submissions
    new_submission = (student_id, parsed_time, file_name, submitted_at)
    submissions.append(new_submission)

    return sort(submissions)

def format_event(event):
    """
    Converts an internal 'event' into a readable string for display in the UI.
    Each event is just the steps of merge sort to be displayed.
    This is why throughout the code there are strings.
    """
    kind = event[0]

    #This is when the list is to be split, the "split" message is displayed
    if kind == "split":
        lst = event[1]
        return " Splitting:\n" + "\n".join([f"{s[0]} | {s[1]}" for s in lst])
    
    #Same thing with when two lists are compared
    elif kind == "compare":
        a, b = event[1], event[2]
        return f" Comparing:\n{a[0]} ({a[1]})  VS  {b[0]} ({b[1]})"

    #And finally, when they are merged
    elif kind == "merge":
        lst = event[1]
        return " Merging:\n" + "\n".join([f"{s[0]} | {s[1]}" for s in lst])

  def animate_sort(text_input, delay):
    """
    This is the actual "animation"
    This is what goes through all the steps and puts them together
    """

    global steps
    steps = []

    submissions = []
    messages = []

    lines = text_input.strip().split("\n")

    for line in lines:

        #Checks format
        parts = line.split(",")

        if len(parts) != 3:
            messages.append(f" Invalid format: {line}")
            continue

        student_id, submitted_at, file_name = [p.strip() for p in parts]

        #Checks times
        status, parsed_time = validate_time(submitted_at)

        if status == "invalid_format":
            messages.append(f" Invalid timestamp: {submitted_at}")
            continue

        if status == "future_date":
            messages.append(f" Future date ignored: {submitted_at}")
            continue

        submissions.append((student_id, parsed_time, file_name, submitted_at))

    # Show validation messages first
    if messages:
        yield "\n".join(messages)
        time.sleep(delay)

    final_sorted = sort(submissions)

    for event in steps:
        yield format_event(event)
        time.sleep(delay)

    yield " FINAL SORTED LIST:\n\n" + "\n".join(
        [f"{s[0]} | {s[3]} | {s[2]}" for s in final_sorted]
    )

"""
This is the Gradio stuff
This is where most of the communication with Gradio happens
"""
with gr.Blocks() as demo:
    gr.Markdown("## TA Grading Queue Organizer") #This displays the title as a Markdown cell

    #These are the settings for the I/O boxes
    #The size of the boxes can be changed with the number of lines below
    with gr.Row():
        input_box = gr.Textbox(lines=15, label="Input", placeholder= "Ex. student_1, 2007-09-25 12:00:00, H3.pdf") #The example is the Halo 3 launch date
        output_box = gr.Textbox(lines=15, label="Animation")

    #This is where the settings for animation speed are
    #You can change the min/max speeds by editting the values below
    speed = gr.Slider(0.1, 5.0, value=2.5, step=0.1, label="Animation Speed (seconds)")

    btn = gr.Button("Start Sorting")

    btn.click(fn=animate_sort, inputs=[input_box, speed], outputs=output_box)

demo.launch()
