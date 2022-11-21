import tkinter
import cv2
import PIL.Image, PIL.ImageTk
from functools import partial
import threading
import time
import imutils


stream = cv2.VideoCapture("videos/video1.mp4")
flag = True

# Functions
def play(speed):
    global flag
    print(f"You clicked on play. Speed is {speed}.")
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1+speed)

    grabbed, frame = stream.read()
    if not grabbed:
        print("Video ended and thus quitting. Replay the program if you wish to see again.")
        exit()
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

    # This will show a "Decision pending" text on the video while playing and it will blink
    if flag:
        canvas.create_text(140, 40, fill="yellow", font="Times 26 bold", text="Decision Pending", anchor=tkinter.SW)
    flag = not flag

def pending(decision):
    # 1. Display decision pending image
    frame = cv2.cvtColor(cv2.imread("images/pending.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    # 2. Wait for 3 seconds
    time.sleep(3)
    # 3. Display waiting (loading) image
    frame = cv2.cvtColor(cv2.imread("images/loading.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    # 4. Wait for 3 seconds
    time.sleep(3)
    # 5. Display Goal/Not Goal
    if decision == 'goal':
        decisionImg = "images/goal.png"

    elif decision == 'not goal':
        decisionImg = "images/not_goal.png"

    elif decision == 'foul':
        decisionImg = "images/foul.png"

    elif decision == 'not foul':
        decisionImg = "images/not_foul.png"

    elif decision == 'offside':
        decisionImg = "images/offside.png"

    else:
        decisionImg = "images/not_offside.png"

    frame = cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

def goal():
    thread = threading.Thread(target=pending, args=("goal",))
    thread.daemon = 1
    thread.start()
    print("It is a goal")

def not_goal():
    thread = threading.Thread(target=pending, args=("not goal",))
    thread.daemon = 1
    thread.start()
    print("It is not a goal")

def offside():
    thread = threading.Thread(target=pending, args=("offside",))
    thread.daemon = 1
    thread.start()
    print("It is an offside")

def not_offside():
    thread = threading.Thread(target=pending, args=("not offside",))
    thread.daemon = 1
    thread.start()
    print("It is not an offside")

def foul():
    thread = threading.Thread(target=pending, args=("foul",))
    thread.daemon = 1
    thread.start()
    print("It is a foul")

def not_foul():
    thread = threading.Thread(target=pending, args=("not foul",))
    thread.daemon = 1
    thread.start()
    print("It is not a foul")


# Global Variables - Width and height of our main screen
SET_WIDTH = 650
SET_HEIGHT = 368


# Creating the window for the program. Tkinter GUI starts here
window = tkinter.Tk()
window.title("Virtual Assistant Referee by Srijit")
cv_img = cv2.cvtColor(cv2.imread("images/welcome.png"), cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width=SET_WIDTH, height= SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0, 0, anchor=tkinter.NW, image=photo)
canvas.pack()


# Buttons to control playback
btn = tkinter.Button(window, text="<< Backward (fast)", width=50, command=partial(play, -25))
btn.pack()
btn = tkinter.Button(window, text="<< Backward (slow)", width=50, command=partial(play, -2))
btn.pack()
btn = tkinter.Button(window, text="Forward (fast) >>", width=50, command=partial(play, 25))
btn.pack()
btn = tkinter.Button(window, text="Forward (slow) >>", width=50, command=partial(play, 2))
btn.pack()
btn = tkinter.Button(window, text="Goal", width=50, command=goal)
btn.pack()
btn = tkinter.Button(window, text="Not Goal", width=50, command=not_goal)
btn.pack()
btn = tkinter.Button(window, text="Foul", width=50, command=foul)
btn.pack()
btn = tkinter.Button(window, text="Not Foul", width=50, command=not_foul)
btn.pack()
btn = tkinter.Button(window, text="Offside", width=50, command=offside)
btn.pack()
btn = tkinter.Button(window, text="Not Offside", width=50, command=not_offside)
btn.pack()

window.mainloop()