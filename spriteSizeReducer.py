import pygame
import tkinter as tk
from tkinter import filedialog
from os import walk, listdir, rmdir
import os.path as op


class SpriteCollection():
	pygame.init()
	def __init__(self):		
		
		self.master = tk.Tk()
		self.master.geometry("384x128")
		self.master.title("Sprite reducer by Ashardalon78")

		tk.Label(self.master,text="Red:").grid(row=0,column=0)
		self.T1 = tk.Text(self.master,height=1,width=5)
		self.T1.grid(row=0,column=1)
		self.T1.insert(tk.END,255)
		tk.Label(self.master,text="Green:").grid(row=1,column=0)
		self.T2 = tk.Text(self.master,height=1,width=5)
		self.T2.grid(row=1,column=1)
		self.T2.insert(tk.END,255)
		tk.Label(self.master,text="Blue:").grid(row=2,column=0)
		self.T3 = tk.Text(self.master,height=1,width=5)
		self.T3.grid(row=2,column=1)
		self.T3.insert(tk.END,255)
				
		tk.Button(self.master, text="Start", command=self.read_files).grid(row=3, column=0)		

		self.master.mainloop()				
		
	def read_files(self):
		self.red = int(self.T1.get('1.0',tk.END))
		self.green = int(self.T2.get('1.0',tk.END))
		self.blue = int(self.T3.get('1.0',tk.END))
		
		path = filedialog.askdirectory()
		if not path:
			return
	
		for root, subdirs, files in walk(path):			
			for name in files:
				if name.endswith(".png"):	
					print("Prosessing: " + str(op.join(root,name)))											
					sprite = pygame.image.load(op.join(root,name))
					sprite_red = self.reduce_sprite(sprite)
					pygame.image.save(sprite_red, op.join(root,name))
					
	def reduce_sprite(self, img):
		width = img.get_width()
		height = img.get_height()
		breakouter = False
		for i in range(width):
			for j in range(height):
				color = img.get_at((i, j))					
				if color[0] != self.red or color[1] != self.green or color[2] != self.blue:
					lim_left = i
					breakouter = True
					break
			if breakouter: break
		breakouter = False
		for i in range(width - 1, -1, -1):
			for j in range(height):
				color = img.get_at((i, j))
				if color[0] != self.red or color[1] != self.green or color[2] != self.blue:
					lim_right = i
					breakouter = True
					break
			if breakouter: break
		breakouter = False
		for j in range(height):
			for i in range(width):
				color = img.get_at((i, j))
				if color[0] != self.red or color[1] != self.green or color[2] != self.blue:
					lim_top = j
					breakouter = True
					break
			if breakouter: break
		breakouter = False
		for j in range(height - 1, -1, -1):
			for i in range(width):
				color = img.get_at((i, j))
				if color[0] != self.red or color[1] != self.green or color[2] != self.blue:
					lim_bottom = j
					breakouter = True
					break
			if breakouter: break
		
		#return img.subsurface((lim_right, lim_bottom, lim_left - lim_right, lim_top - lim_bottom))
		return img.subsurface((lim_left, lim_top, lim_right - lim_left + 1, lim_bottom - lim_top + 1))
	
AC = SpriteCollection()