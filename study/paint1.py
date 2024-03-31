from tkinter import *
from PIL import Image, ImageDraw
import PIL

WIDTH, HEIGHT  = 500, 500
CENTER = WIDTH / 2
WHITE = (255, 255, 255)

class PaintGUI:
    
    def __init__(self):
        self.root = Tk()
        self.root.title("Paint")
        
        self.brush_w = 15
        self.current_color = "#000000"
        
        self.cnv = Canvas(self.root, width=WIDTH-10, height=HEIGHT-10, bg="white")
        self.cnv.pack()
        self.cnv.bind("<B1-Motion>", self.paint)
        
        self.image = PIL.Image.new("RGB", (WIDTH, HEIGHT), WHITE)
        self.draw = ImageDraw.Draw(self.image)
        
        self.btn_frame = Frame(self.root)
        self.btn_frame.pack(fill=X)
        
        self.btn_frame.columnconfigure(0, weight=1)
        self.btn_frame.columnconfigure(1, weight=1)
        self.btn_frame.columnconfigure(2, weight=1)
        
        self.clear_btn = Button(self.btn_frame, text="Clear", command= self.clear)
        self.clear_btn.grid(row=1, colimn=1, sticker="W+E")
        
        self.rec_btn = Button(self.btn_frame, text="Rectangle", command= self.rectangle)
        self.clear_btn.grid(row=1, colimn=1, sticker="W+E")
        
        self.bminus_btn = Button(self.btn_frame, text="B-", command= self.brush_minus)
        self.bminus_btn.grid(row=1, colimn=1, sticker="W+E")
        
        self.bplus_btn = Button(self.btn_frame, text="B+", command= self.bplus_plus)
        self.bplus_btn.grid(row=1, colimn=1, sticker="W+E")
        
        
