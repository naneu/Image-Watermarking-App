import os
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image, ImageDraw, ImageFont, UnidentifiedImageError

class App:
    def __init__(self):
        self.label = Label(text='Add Watermark to your image!',font=('Montserrat', 14), background='#F0F4F8', fg='#41668B')
        self.label.grid(column=0, row=0)

        self.btn = Button(text='Select image', bg='#41668B', activebackground='#41668B',activeforeground='white', fg='white' ,font=('Montserrat', 14), command=self.upload_image, pady=7)
        self.btn.place(x=900, y=0)

        self.my_entry = Entry(window, font=("Montserrat",24))
        self.my_entry.place(x=200, y=650)

       
        self.btn2 = Button(window, text="Add text", command=self.add_watermark, font=('Montserrat', 14), bg='#41668B', fg='white', activebackground='#41668B',activeforeground='white', pady=7)
        self.btn2.place(x=650, y=650)

        self.btn3 = Button(window, text="Clear",command=self.clear_image_label, font=('Montserrat', 14), bg='#41668B', fg='white', activebackground='#41668B',activeforeground='white', pady=7, width=7)
        self.btn3.place(x=800, y=650)

    def clear_image_label(self):
        try:
            self.icon.destroy()
            # self.label1.destroy()
        except AttributeError:
            pass
        

    def upload_image(self):

        try:
            f_types = [('Image File', '*.*'), 
            ('Text Document', '*.txt'),
            ('CSV files',"*.csv")]
            self.path=filedialog.askopenfilename(title='Upload a file', initialdir='/', filetypes=f_types)
            self.filename= os.path.basename(self.path)

            self.img= Image.open(self.path)
            self.img = self.img.resize((700,500), Image.ANTIALIAS)
            tkimage= ImageTk.PhotoImage(self.img)
            self.icon=Label(window,image=tkimage)
            self.icon.image = tkimage
            self.icon.place(x=100, y= 100)

        except TypeError:
            pass
        except AttributeError:
            pass

        except UnidentifiedImageError:
            self.label1 = Label(text='Images only!',font=('Montserrat', 18), background='#F0F4F8', fg='red')
            self.label1.place(x=300, y=300)
       
            self.label1.after(3000, self.label1.destroy)

    def add_watermark(self):

        txt = self.my_entry.get()
        font = ImageFont.load_default()
        self.edit_img = ImageDraw.Draw(self.img)
        self.edit_img.text((80, 40), txt, ("red"), font=font)

        #save 
        self.img.save(f"watermarked/{self.filename}")

        #clear entry box
        self.my_entry.delete(0, END)
        self.my_entry.insert(0, "Saving File....")

        # wait a bit
        self.icon.after(2000,self.show_pic)


    def show_pic(self):
        global marked_pic
        #show new image
        file=f"watermarked/{self.filename}"
        marked_pic= Image.open(file)
        m_tkimage= ImageTk.PhotoImage(marked_pic)
        self.icon.image = m_tkimage
        self.icon.config(image=m_tkimage)

        #clear entry box
        self.my_entry.delete(0, END)

if __name__ == "__main__":

    window = Tk()
    window.title("Image Watermarking App")
    window.minsize(width=1200, height=800)
    window.config(padx=50,pady=50)
    window.configure(bg='#f0f4f8')

    my_app = App()
    my_app


    window.mainloop()
