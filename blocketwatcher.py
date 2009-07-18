# -*- coding: iso-8859-15 -*-
import wx
import watch



class BlocketWatcherGUI(wx.Frame):
	def __init__(self,parent,id,title):
		
		wx.Frame.__init__(self,None,-1,title,size=wx.Size(300,400))
		self.scroll = wx.ScrolledWindow(self, -1)
		#self.Show()
		
		self.windowActive = False
		
					
		self.icon = wx.Icon("tray.png", wx.BITMAP_TYPE_PNG)
		self.tray = wx.TaskBarIcon()
		self.tray.SetIcon(self.icon, "BlocketWatcher")
		wx.EVT_TASKBAR_RIGHT_UP(self.tray, self.exitProgram)
		wx.EVT_TASKBAR_LEFT_UP(self.tray, self.showItemsWindow)
		#wx.EVT_TASKBAR_MOVE(self.tray, showItemsWindow)

		self.newItemImage = wx.Image("new_item.png")
		self.newItemBitmap = wx.BitmapFromImage(self.newItemImage)
		self.oldItemImage = wx.Image("old_item.png")
		self.oldItemBitmap = wx.BitmapFromImage(self.oldItemImage)
		self.deleteImage = wx.Image("delete.png")
		self.deleteBitmap = wx.BitmapFromImage(self.deleteImage)

	def showItemsWindow(self, event):
		print "*showing item-window*"
		self.windowActive = not self.windowActive
			
		if self.windowActive:
			m = watch.findAds()	
			
			x = 2
			y = 5
			
			for item in m:		
			
				windowWidth,windowHeight = self.GetSizeTuple()
				
				statusOffset = 25
				deleteOffset = 40;
				
				wx.StaticBitmap(self.scroll, -1, self.newItemBitmap,pos=wx.Point(x,y))
				
				x += statusOffset

				itemText = wx.StaticText(self.scroll,-1, item[0], pos=wx.Point(x,y))
				endPoint = windowWidth-statusOffset-deleteOffset-10
				print windowWidth
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
	
				print "adding an item: " + item[1]
			

			self.scroll.SetScrollbars(0,dy,0,y/dy+1)

		
			self.Show()
		else:
			self.Hide()
		
		
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
