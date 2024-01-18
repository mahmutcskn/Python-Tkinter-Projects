from tkinter import *
import pyscreenrec

root = Tk()
root.geometry("400x600")
root.title("Screen Recorder")
root.config(bg="black")  # Arka plan rengini siyah yap

# Kayıt durumu etiketi
status_label = Label(root, text="Not Recording", bg="black", fg="white", font="arial 12 bold")
status_label.place(x=130, y=550)  # Status etiketinin konumunu belirledik

# FUNCTIONS
def start_rec():
    file = Filename.get()
    output_directory = "D:/Files/pythonCodes/Screen Recorder"  # Kendi dizin yolunuzu burada belirtin
    rec.start_recording(f"{output_directory}/{file}.mp4")
    status_label.config(text="Recording...")  # Kayıt durumu etiketini güncelledik

def pause_rec():
    rec.pause_recording()

def resume_rec():
    rec.resume_recording()

def stop_rec():
    rec.stop_recording()
    status_label.config(text="Not Recording")  # Kayıt durumu etiketini güncelledik

rec = pyscreenrec.ScreenRecorder()

# icon
image_icon = PhotoImage(file="icon_recorder.png")
root.iconphoto(False, image_icon)

# background images
image1 = PhotoImage(file="yellow.png")
Label(root, image=image1, bg="black").place(x=-2, y=35)

image2 = PhotoImage(file="blue.png")
Label(root, image=image2, bg="black").place(x=223, y=200)

# Heading
lbl = Label(root, text="Screen Recorder", bg="black", fg="white", font="arial 15 bold")
lbl.pack(pady=20)

image3 = PhotoImage(file="recording.png")
Label(root, image=image3, bd=0, bg="black").pack(pady=30)

# Entry
Filename = StringVar()
entry = Entry(root, textvariable=Filename, width=18, font="arial 15", justify="center")  # Center the text
entry.place(x=100, y=350)
Filename.set("recording25")

# Buttons
start = Button(root, text="Start", font="arial 22", bd=0, command=start_rec)
start.place(x=140, y=250)

image4 = PhotoImage(file="pause.png")
pause = Button(root, image=image4, bd=0, bg="black", command=pause_rec)
pause.place(x=50, y=450)

image5 = PhotoImage(file="resume.png")
resume = Button(root, image=image5, bd=0, bg="black", command=resume_rec)
resume.place(x=150, y=450)

image6 = PhotoImage(file="stop.png")
stop = Button(root, image=image6, bd=0, bg="black", command=stop_rec)
stop.place(x=250, y=450)

# Run the Codes
root.mainloop()
