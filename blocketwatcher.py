#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import wx
import watch




class BlocketWatcherGUI(wx.Frame):
	""" The class to care for the GUI in BlocketWatcher"""
	
	TRAY_MENU_OPTIONS = wx.NewId()
	TRAY_MENU_ABOUT = wx.NewId()
	TRAY_MENU_CLOSE = wx.NewId()
	
	
	def __init__(self,parent,id,title):
		
		wx.Frame.__init__(self,None,-1,title,size=wx.Size(300,400))
		self.scroll = wx.ScrolledWindow(self, -1)
		
		self.windowActive = False

		# Set up tray-icon and various icons		
		self.icon = wx.Icon("tray.png", wx.BITMAP_TYPE_PNG)
		self.tray = wx.TaskBarIcon()
		self.tray.SetIcon(self.icon, "BlocketWatcher")
		wx.EVT_TASKBAR_RIGHT_UP(self.tray, self.OnTaskBarRight)
		wx.EVT_TASKBAR_LEFT_UP(self.tray, self.showItemsWindow)
		#wx.EVT_TASKBAR_MOVE(self.tray, showItemsWindow)
		wx.EVT_MENU(self.tray, self.TRAY_MENU_OPTIONS, self.onOptions)
		wx.EVT_MENU(self.tray, self.TRAY_MENU_ABOUT, self.onAbout)
		wx.EVT_MENU(self.tray, self.TRAY_MENU_CLOSE, self.exitProgram)

		self.newItemImage  = wx.Image("new_item.png")
		self.newItemBitmap = wx.BitmapFromImage(self.newItemImage)
		self.oldItemImage  = wx.Image("old_item.png")
		self.oldItemBitmap = wx.BitmapFromImage(self.oldItemImage)
		self.deleteImage   = wx.Image("delete.png")
		self.deleteBitmap  = wx.BitmapFromImage(self.deleteImage)

	def showItemsWindow(self, event):
		"""Function to be called when activating tray-icon."""
		
		
		self.windowActive = not self.windowActive
			
		if self.windowActive:
			itemList  = watch.findAds()	
			self.drawItemList(itemList)
	
			self.Show()
			print "*showing item-window*"
		else:
			self.Hide()
			print "*hiding item-window*"
		

	def drawItemList(self, itemList):
		"""Update the itemList in the GUI."""
		
		# Move on to sizers for positioning, as soon as we figure out 
		# how scrolling works with sizers
		
		x = 2
		y = 5
			
		for item in itemList:		
		
			windowWidth,windowHeight = self.GetSizeTuple()
			
			statusOffset = 25
			deleteOffset = 40;
			
			wx.StaticBitmap(self.scroll, -1, self.newItemBitmap,pos=wx.Point(x,y))
			
			x += statusOffset

			print item[0]
			itemText = wx.StaticText(self.scroll,-1, item[0], pos=wx.Point(x,y))
			endPoint = windowWidth-statusOffset-deleteOffset-10
			
			itemText.Wrap( endPoint ) 
			w,h = itemText.GetSizeTuple()
			
			x += endPoint+5
			wx.StaticBitmap(self.scroll, -1, self.deleteBitmap,pos=wx.Point(x,y))
			x -= endPoint+5
			
			dy = h + 2
			y += dy
			
			itemPrice = wx.StaticText(self.scroll,-1, item[1], pos=wx.Point(x,y))
			w,h = itemText.GetSizeTuple()
			
			dy = h + 5
			y += dy				
			x -= statusOffset

		self.scroll.SetScrollbars(0,dy,0,y/dy+1)


	def OnTaskBarRight(self, event):
		menu = wx.Menu()
		menu.Append(self.TRAY_MENU_OPTIONS, "Change the preferences")
		menu.Append(self.TRAY_MENU_ABOUT, "About the software")
		menu.Append(self.TRAY_MENU_CLOSE, "Close the program")
		
		self.tray.PopupMenu(menu)



	def onOptions(self, event):
		"""Show a window with various options for the application."""
		print "*show options*"
	def onAbout(self, event):
		"""Show an ordinary About-window."""
		d= wx.MessageDialog( None, "An application designed to watch (several)\n"
								"ad-sites and notify the user when an item of\n"
								"interest is put online.\n\n"
								"Developed by Anders Bennehag","About me", wx.OK)
							# Create a message dialog box
		d.ShowModal() # Shows it
		d.Destroy() # finally destroy it when finished.

		
	def OnSize(self, event):
		self.scroll.SetSize(self.GetClientSize())
	def exitProgram(self, event):
		app.ExitMainLoop()
		
	
	
	

	
	
# If the program is run directly or passed as an argument to the python
# interpreter then create a HelloWorld instance and show it
if __name__ == "__main__":
	app = wx.PySimpleApp()
	frame = BlocketWatcherGUI(None, -1,"BlocketWatcher")
	app.MainLoop()
