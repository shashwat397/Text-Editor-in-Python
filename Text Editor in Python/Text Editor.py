from tkinter import *
from PIL import Image, ImageTk

if __name__ == '__main__':
    #Basic tkinter setup
imaginary_tech_root = Tk()
# width x height

imaginary_tech_root.geometry("1044x934")
imaginary_tech_root.title("Text Editor")

# width,height

imaginary_tech_root.minsize(300,100)
# width,height
imaginary_tech_root.maxsize(1200,988)
# Add TextArea
TextArea = Text(root, font="lucida 13")
file = None

# Lets Create a menubar
Menubar = Menu(root)
#File Menu Starts
FileMenu = Menu(MenuBar, tearoff=0)
# To open new file
FileMenu.add_command(label="New", command=newFile)

#To open already eisting file
FileMenu.add_command(label="Open", command = openFile)

# To save the current file

FileMenu.add_command(label = "Save", command = saveFile)
FileMenu.add_separator()
FileMenu.add_command(label = "Exit", command = quitApp)
Menubar.add_cascade(label = "File", menu=FileMenu)
# File Menu Ends

# Edit Menu Starts
EditMenu = Menu(Menubar, tearoff=0)
#To give a feature of cut, copy and paste
EditMenu.add_command(label = "Cut", command=cut)
EditMenu.add_command(label = "Copy", command=copy)
EditMenu.add_command(label = "Paste", command=paste)

EditMenu.add_cascade(label="Edit", menu = EditMenu)

# Edit Menu Ends

# Help Menu Starts
HelpMenu = Menu(MenuBar, tearoff=0)
HelpMenu.add_command(label = "About Notepad", command=about)
Menubar.add_cascade(label="Help", menu=HelpMenu)

# Help Menu Ends

imaginary_tech_root.config(menu=Menubar)


shashwat = Label(text ="Shashwat is a good boy and this is his GUI")
shashwat.pack()
# Adding images to GUI
photo = PhotoImage(file="2.png")             # After installing pillow we can use jpg images.
shashwat_label = Label(image=photo)
shashwat_label.pack()

# For Jpg images
# image = Image.open("photo.jpg")
# photo = ImageTk.PhotoImage(image)





imaginary_tech_root.mainloop()


