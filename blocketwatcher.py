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

		wx.Frame.__init__(self, None, -1)
		self.Bind(wx.EVT_SIZE, self.OnSize)

		self.scroll = wx.ScrolledWindow(self)
		self.scroll.SetScrollRate(10,10)
		self.scroll.EnableScrolling(True,True)

		self.sizer_container = wx.BoxSizer( wx.VERTICAL )
		self.sizer = wx.BoxSizer( wx.VERTICAL )
		self.sizer_container.Add(self.sizer,1)

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

		for item in itemList:

			widget = itemWidget(self.scroll, self.newItemBitmap, item[0])
			self.sizer.Add(widget, 0, wx.LEFT|wx.ALL, 5)

		self.scroll.SetSizer(self.sizer_container)


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



class itemWidget(wx.Window):
	def __init__(self, parent, statusBitmap, name):
		wx.Window.__init__(self,parent)

		#self.SetSize((200,50))

		self.container = wx.BoxSizer(wx.VERTICAL)
		self.SetSizer(self.container)

		self.statusIcon = wx.StaticBitmap(self, -1, statusBitmap)
		self.nameText = wx.StaticText(self,-1, name)

		self.container.Add(self.statusIcon, 0, wx.ALL,5)
		self.container.Add(self.nameText, 1,  wx.ALL|wx.EXPAND,5)

		self.SetSizer(self.container)
		self.container.Fit(self)

# If the program is run directly or passed as an argument to the python
# interpreter then create a HelloWorld instance and show it
if __name__ == "__main__":
	app = wx.PySimpleApp()
	frame = BlocketWatcherGUI(None, -1,"BlocketWatcher")
	app.MainLoop()
