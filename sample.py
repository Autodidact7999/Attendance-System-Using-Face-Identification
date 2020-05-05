import tkinter as tk
window=tk.Tk()
window.title("Face_Recogniser")
dialog_title = 'QUIT'
dialog_text = 'Are you sure?'
# answer = messagebox.askquestion(dialog_title, dialog_text)

# window.geometry('1280x720')
window.configure(background='black')

# window.attributes('-fullscreen', True)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

# path = "profile.jpg"

# Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
# img = ImageTk.PhotoImage(Image.open(path))

# The Label widget is a standard Tkinter widget used to display a text or image on the screen.
# panel = tk.Label(window, image = img)


# panel.pack(side = "left", fill = "y", expand = "no")

# cv_img = cv2.imread("img541.jpg")
# x, y, no_channels = cv_img.shape
# canvas = tk.Canvas(window, width = x, height =y)
# canvas.pack(side="left")
# photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img))
# Add a PhotoImage to the Canvas
# canvas.create_image(0, 0, image=photo, anchor=tk.NW)

# msg = Message(window, text='Hello, world!')

# Font is a tuple of (font_family, size_in_points, style_modifier_string)


message = tk.Label(window, text="Face-Recognition-Based-Attendance-Management-System" ,bg="Green"  ,fg="white"  ,width=50  ,height=3,font=('times', 30, 'italic bold underline'))

message.place(x=200, y=20)

lbl = tk.Label(window, text="Enter ID",width=20  ,height=2  ,fg="red"  ,bg="yellow" ,font=('times', 15, ' bold ') )
lbl.place(x=400, y=200)

txt = tk.Entry(window,width=20  ,bg="yellow" ,fg="red",font=('times', 15, ' bold '))
txt.place(x=700, y=215)

lbl2 = tk.Label(window, text="Enter Name",width=20  ,fg="red"  ,bg="yellow"    ,height=2 ,font=('times', 15, ' bold '))
lbl2.place(x=400, y=300)

txt2 = tk.Entry(window,width=20  ,bg="yellow"  ,fg="red",font=('times', 15, ' bold ')  )
txt2.place(x=700, y=315)

lbl3 = tk.Label(window, text="Notification : ",width=20  ,fg="red"  ,bg="yellow"  ,height=2 ,font=('times', 15, ' bold underline '))
lbl3.place(x=400, y=400)

message = tk.Label(window, text="" ,bg="yellow"  ,fg="red"  ,width=30  ,height=2, activebackground = "yellow" ,font=('times', 15, ' bold '))
message.place(x=700, y=400)

lbl3 = tk.Label(window, text="Attendance : ",width=20  ,fg="red"  ,bg="yellow"  ,height=2 ,font=('times', 15, ' bold  underline'))
lbl3.place(x=400, y=650)


message2 = tk.Label(window, text="" ,fg="red"   ,bg="yellow",activeforeground = "green",width=30  ,height=2  ,font=('times', 15, ' bold '))
message2.place(x=700, y=650)
window.mainloop()