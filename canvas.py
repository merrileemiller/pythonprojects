#***************************************************************#
# Merrilee Miller                                              	#
# November 26, 2013                                            	#
# CS 2100 - Python                                             	#
# Assignment 5                                                 	#
# A5canvas.py       	                                      	#
# DESCRIPTION:	This program creates a GUI with a canvas and 	#
#				options to create rectangles, ovals, polygons,	#
#				lines, and text in various colors and sizes.	#
#***************************************************************#

import tkinter as tk
from tkinter import filedialog
import time, threading


class GUI():

	def __init__(self, parent):
	
		self.parent = parent
		
		#- Canvas -
		self.canvas = tk.Canvas(self.parent, width=500, height=500, background='white')
		self.canvas.grid(row=1, rowspan=20, column=5)
		
		self.name = tk.Label(self.parent, text="Merrilee Miller - 11/26/2013", fg='grey')
		self.name.grid(row=20, column=3, columnspan=2)
		
		#- Shape -
		self.selectShapeLabel = tk.Label(self.parent, text="Shape:")
		self.selectShapeLabel.grid(row=3, column=1, sticky='E')
		
		self.stvar = tk.StringVar()
		self.stvar.set("Select shape...")
		self.option = tk.OptionMenu(self.parent, self.stvar, "Rectangle", "Oval", 
												"Polygon", "Line", "Text")
		self.option.pack()
		self.option.grid(row=3, column=4, sticky='W')
		self.stvar.trace('w', self.changed)
	
		#- Color -
		self.selectColorLabel = tk.Label(self.parent, text="Color:")
		self.selectColorLabel.grid(row=3, column=3, sticky='E')
			
		self.colorStr = tk.StringVar()
		self.colorStr.set("black")
		self.colorOption = tk.OptionMenu(self.parent, self.colorStr, "black", "red",  
										"orange", "yellow", "green", "blue", "cyan", 
										"purple", "magenta", "pink", "white")
		self.colorOption.pack()
		self.colorOption.grid(row=3, column=2, sticky='W')
		
		#- Background Color -
		self.selectBgLabel = tk.Label(self.parent, text="Background:")
		self.selectBgLabel.grid(row=2, column=1, sticky='E')
		self.colorStr2 = tk.StringVar()
		self.colorStr2.set("white")
		self.bgColor = tk.OptionMenu(self.parent, self.colorStr2, "black", "red",  
										"orange", "yellow", "green", "blue", "cyan",  
										"purple", "magenta", "pink", "white")
		self.bgColor.pack()
		self.bgColor.grid(row=2, column=2, sticky='W')
		self.colorStr2.trace('w', self.bgChanged)
		
		#- Coordinates -
		self.spin1 = tk.IntVar()
		self.spin2 = tk.IntVar()
		self.spin3 = tk.IntVar()
		self.spin4 = tk.IntVar()
		self.spin5 = tk.IntVar()
		self.spin6 = tk.IntVar()
		self.spin7 = tk.IntVar()
		self.spin8 = tk.IntVar()
		self.coordLabel1 = tk.Label(self.parent, text="X:")
		self.coordLabel2 = tk.Label(self.parent, text="Y:")
		self.coordLabel3 = tk.Label(self.parent, text="X:")
		self.coordLabel4 = tk.Label(self.parent, text="Y:")
		self.coordLabel5 = tk.Label(self.parent, text="X:")
		self.coordLabel6 = tk.Label(self.parent, text="Y:")
		self.coordLabel7 = tk.Label(self.parent, text="X:")
		self.coordLabel8 = tk.Label(self.parent, text="Y:")
		self.spinBox1 = tk.Spinbox(self.parent, from_=1, to=500, width=5, 
																textvariable=self.spin1)
		self.spinBox2 = tk.Spinbox(self.parent, from_=1, to=500, width=5, 
																textvariable=self.spin2)
		self.spinBox3 = tk.Spinbox(self.parent, from_=1, to=500, width=5,
		 														textvariable=self.spin3)
		self.spinBox4 = tk.Spinbox(self.parent, from_=1, to=500, width=5, 
																textvariable=self.spin4)
		self.spinBox5 = tk.Spinbox(self.parent, from_=1, to=500, width=5, 
												textvariable=self.spin5, state='disabled')
		self.spinBox6 = tk.Spinbox(self.parent, from_=1, to=500, width=5, 
												textvariable=self.spin6, state='disabled')
		self.spinBox7 = tk.Spinbox(self.parent, from_=1, to=500, width=5, 
												textvariable=self.spin7, state='disabled')
		self.spinBox8 = tk.Spinbox(self.parent, from_=1, to=500, width=5, 
												textvariable=self.spin8, state='disabled')
		self.coordLabel1.grid(row=5,  column=1, sticky='E')
		self.coordLabel2.grid(row=5,  column=3, sticky='E')
		self.coordLabel3.grid(row=7,  column=1, sticky='E')
		self.coordLabel4.grid(row=7,  column=3, sticky='E')
		self.coordLabel5.grid(row=9,  column=1, sticky='E')
		self.coordLabel6.grid(row=9,  column=3, sticky='E')
		self.coordLabel7.grid(row=11, column=1, sticky='E')
		self.coordLabel8.grid(row=11, column=3, sticky='E')
		self.spinBox1.grid(row=5,  column=2, sticky='W')
		self.spinBox2.grid(row=5,  column=4, sticky='W')
		self.spinBox3.grid(row=7,  column=2, sticky='W')
		self.spinBox4.grid(row=7,  column=4, sticky='W')
		self.spinBox5.grid(row=9,  column=2, sticky='W')
		self.spinBox6.grid(row=9,  column=4, sticky='W')
		self.spinBox7.grid(row=11, column=2, sticky='W')
		self.spinBox8.grid(row=11, column=4, sticky='W')
		
		#- Text - 
		self.size = tk.IntVar()
		self.textSizeLabel = tk.Label(self.parent, text="Text size:")
		self.textSizeLabel.grid(row=12, column=1, sticky='E')
		self.textSize = tk.Spinbox(self.parent, from_=1, to=500, width=5, 
										textvariable=self.size, state='disabled')
		self.textSize.grid(row=12, column=2, sticky='W')
		self.textLabel = tk.Label(self.parent, text="Text:")
		self.textLabel.grid(row=12, column=3, sticky='E')
		self.textBox = tk.Entry(self.parent, state='disabled')
		self.textBox.grid(row=12, column=4, sticky='W')
		
		#- Clear -
		self.button = tk.Button(self.parent, text="Clear", command=self.clearCanvas)
		self.button.grid(row=13, column=1, columnspan=2)
	
		
	def changed(self, *args):	 	# shape changed
		try:
			self.rectangleButton.grid_forget() # reset buttons
			self.ovalButton.grid_forget()
			self.polygonButton.grid_forget()
			self.lineButton.grid_forget()
			self.textButton.grid_forget()
		except AttributeError:
			pass
		if self.stvar.get() == "Rectangle":
			self.rectangle()
		elif self.stvar.get() == "Oval":
			self.oval()
		elif self.stvar.get() == "Polygon":
			self.polygon()
		elif self.stvar.get() == "Line":
			self.line()
		elif self.stvar.get() == "Text":
			self.text()
		else:
			pass
	def bgChanged(self, *args):		# changes bg color
		self.canvas.config(background=self.colorStr2.get())		
	
	def clearCanvas(self):
		self.canvas.delete("all")	
		
# ----------------------------------------------------------------------------------------
	def rectangle(self):
		
		self.spinBox3.config(state='normal')
		self.spinBox4.config(state='normal')
		self.spinBox5.config(state='disabled')
		self.spinBox6.config(state='disabled')
		self.spinBox7.config(state='disabled')
		self.spinBox8.config(state='disabled')
		self.textBox.config(state='disabled')
		self.textSize.config(state='disabled')
			
		self.rectangleButton = tk.Button(self.parent, text="Draw", 
														command=self.drawRectangle)
		self.rectangleButton.grid(row=13, column=3, columnspan=2)
		
	def drawRectangle(self):
		points = [self.spin1.get(), self.spin2.get(), self.spin3.get(), self.spin4.get()]
		self.canvas.create_rectangle(points, fill=self.colorStr.get())	
# ----------------------------------------------------------------------------------------
	def oval(self):
		
		self.spinBox3.config(state='normal')
		self.spinBox4.config(state='normal')
		self.spinBox5.config(state='disabled')
		self.spinBox6.config(state='disabled')
		self.spinBox7.config(state='disabled')
		self.spinBox8.config(state='disabled')
		self.textBox.config(state='disabled')
		self.textSize.config(state='disabled')
		
		self.ovalButton = tk.Button(self.parent, text="Draw", command=self.drawOval)
		self.ovalButton.grid(row=13, column=3, columnspan=2)
		
	def drawOval(self):
		points = [self.spin1.get(), self.spin2.get(), self.spin3.get(), self.spin4.get()]
		self.canvas.create_oval(points, fill=self.colorStr.get())	
# ----------------------------------------------------------------------------------------
	def polygon(self):
	
		self.spinBox3.config(state='normal')
		self.spinBox4.config(state='normal')
		self.spinBox5.config(state='normal')
		self.spinBox6.config(state='normal')
		self.spinBox7.config(state='normal')
		self.spinBox8.config(state='normal')
		self.textBox.config(state='disabled')
		self.textSize.config(state='disabled')
		
		self.polygonButton = tk.Button(self.parent, text="Draw", command=self.drawPolygon)
		self.polygonButton.grid(row=13, column=3, columnspan=2)
			
	def drawPolygon(self):
		points = [self.spin1.get(), self.spin2.get(), self.spin3.get(), self.spin4.get(),
				  self.spin5.get(), self.spin6.get(), self.spin7.get(), self.spin8.get()]
		self.canvas.create_polygon(points, fill=self.colorStr.get())
# ----------------------------------------------------------------------------------------
	def line(self):
		
		self.spinBox3.config(state='normal')
		self.spinBox4.config(state='normal')
		self.spinBox5.config(state='disabled')
		self.spinBox6.config(state='disabled')
		self.spinBox7.config(state='disabled')
		self.spinBox8.config(state='disabled')
		self.textBox.config(state='disabled')
		self.textSize.config(state='disabled')
		
		self.lineButton = tk.Button(self.parent, text="Draw", command=self.drawLine)
		self.lineButton.grid(row=13, column=3, columnspan=2)
		
	def drawLine(self):
		points = [self.spin1.get(), self.spin2.get(), self.spin3.get(), self.spin4.get()]
		self.canvas.create_line(points, fill=self.colorStr.get())	
# ----------------------------------------------------------------------------------------
	def text(self):
		
		self.spinBox3.config(state='disabled')
		self.spinBox4.config(state='disabled')
		self.spinBox5.config(state='disabled')
		self.spinBox6.config(state='disabled')
		self.spinBox7.config(state='disabled')
		self.spinBox8.config(state='disabled')
		self.textBox.config(state='normal')
		self.textSize.config(state='normal')
		
		self.textButton = tk.Button(self.parent, text="Draw", command=self.drawText)
		self.textButton.grid(row=13, column=3, columnspan=2)
		
	def drawText(self):
		points = [self.spin1.get(), self.spin2.get()]
		self.canvas.create_text(points, text=self.textBox.get(), 
							font=("Times", self.size.get()), fill=self.colorStr.get())
		#self.canvas.create_text(points, start=self.spin5.get(), extent=self.spin6.get(), 
															#)	
# ----------------------------------------------------------------------------------------			
def main():
	root = tk.Tk()
	root.title("Canvas")
	gui = GUI(root)
	
	root.mainloop()	
	
if __name__ == "__main__":
	main()

# END MAIN