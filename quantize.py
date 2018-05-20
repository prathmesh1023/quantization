import PIL.Image
from PIL import Image, ImageTk
import glob
from tkinter import *
from tkinter import messagebox, ttk
from tkinter.filedialog import askopenfilename
import os
from tkinter.messagebox import showerror
import pyexiv2
import re



# self.button = Button(self, text="Browse", command=self.load_file, width=10) #alert message about all images in the folder should be from the same camera
# 		self.button.grid(row=1, column=0, sticky=W)

def load():
	fname = askopenfilename(filetypes=(("Template files", "*.jpg"),
										   ("HTML files", "*.html;*.htm"),
										   ("All files", "*.*") ))

	# forge_detect = ImageTk.PhotoImage(fname)
	# image = post_canvas.create_image(0,0,anchor=NW, image = forge_detect)
	head, tail = os.path.split(fname)
	pathname=head + "/*.jpg"
	m=auth(pathname)
	test(m,fname)
		

def auth(pathname):
	files = (pathname)
	i=1
	for file in glob.glob(files):
		im=PIL.Image.open(file)
		m=im.quantization
		if i==1:
			n=m 
		if i==2:
			p=m 
		if i==3:
			q=m 
		if i==4:
			break
		i=i+1
	if(n==p or n==q):
		return n
	if (p==n or p==q):
		return p 
	if (q==n or q==p):
		return q

def test(m,file): 
# files =(pathname) # for file in glob.glob(files): 
    flag=0 
    im=PIL.Image.open(file)
    flag=exif(file) 
    n=im.quantization
    if(m!=n or flag==1):
        msg = messagebox.showinfo("forged","forged")
        print("forged ",file,file=open("quan.txt","a"))     #show this in gui
    else:
        msg = messagebox.showinfo("original","original")
        print("original ",file,file=open("quan.txt","a")) 

def exif(pathname):
	pass
	flag=0
	patterns = ['Adobe','adobe','ADOBE','photoshop','Photoshop','Affinity','AFFINITY','affinity','PaintShop','PAINTSHOP','paintshop','Acorn','PhotLab','Camera+','Pixelmator ','Pixlr','GIMP','Paint.net','Sumo Paint','Aviary']
	data = pyexiv2.metadata.ImageMetadata(pathname)
	data.read()
	for key in data.exif_keys:
	 tag = data[key]
	 s=key
	 k=tag.value
	 if 'Software' in s:
	  #print(' %-40s%s' %(s, k))
	  for p in patterns:
	  	if re.search(p,k):
	  		flag=1
	return flag
	# if(flag==1):
	# 	print("eixf tag found")
	# else:
	# 	print("exif tag not found")	
top = Tk()
top.geometry('400x400')

frame = Frame(top)
frame.pack()

post_canvas = Canvas(frame, bg="blue", height=200, width=200)
post_canvas.pack(side="right")	

forgery_button = Button(top, text="Forgery Detection", command=load)
forgery_button.place(x=130,y=260)

if __name__ == '__main__':
	top.mainloop()
