# -*- coding: iso-8859-15 -*-
import wx
import watch



class BlocketWatcherGUI(wx.Frame):
	def __init__(self,parent,id,title):
		wx.Frame.__init__(self,parent, -1,title, size=wx.Size(300,500))
		self.scroll = wx.ScrolledWindow(self, -1)
		
		self.listSizer = wx.BoxSizer(wx.VERTICAL)
		
		
		self.windowActive = False
		
				
		self.icon = wx.Icon("accessories-text-editor.png", wx.BITMAP_TYPE_PNG)
		self.tray = wx.TaskBarIcon()
		self.tray.SetIcon(self.icon, "BlocketWatcher")
		wx.EVT_TASKBAR_RIGHT_UP(self.tray, self.exitProgram)
		wx.EVT_TASKBAR_LEFT_UP(self.tray, self.showItemsWindow)
		#wx.EVT_TASKBAR_MOVE(self.tray, showItemsWindow)

	def exitProgram(self, event):
		app.ExitMainLoop()

	def showItemsWindow(self, event):
		print "*showing item-window*"
		self.windowActive = not self.windowActive
		
			
		if self.windowActive:
			m = watch.findAds()	
			for item in m:								
				panel = wx.Panel(self,-1)
				itemText = wx.StaticText(panel,-1, item[1])			
				
				self.listSizer.Add(panel,0,wx.EXPAND)
				
				print "adding an item: " + item[1]
			
			
			
			self.scroll.SetAutoLayout(True)	
			self.scroll.SetSizer(self.listSizer)
			self.scroll.Layout()
			
			self.scroll.SetScrollRate(10, 10);
		
			self.Show()
		else:
			self.Hide()
		
		
		
# If the program is run directly or passed as an argument to the python
# interpreter then create a HelloWorld instance and show it
if __name__ == "__main__":
	app = wx.PySimpleApp()
	frame = BlocketWatcherGUI(None, -1,"BlocketWatcher")
	app.MainLoop()
