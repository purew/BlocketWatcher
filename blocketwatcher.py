#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import wx
import watch

# Globals
newItemBitmap = 0
oldItemBitmap = 0


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

		global newItemBitmap
		global oldItemBitmap
		global deleteBitmap
		newItemImage  = wx.Image("new_item.png")
		newItemBitmap = wx.BitmapFromImage(newItemImage)
		oldItemImage  = wx.Image("old_item.png")
		oldItemBitmap = wx.BitmapFromImage(oldItemImage)
		deleteImage   = wx.Image("delete.png")
		deleteBitmap  = wx.BitmapFromImage(deleteImage)


	def showItemsWindow(self, event):
		"""Function to be called when activating tray-icon."""

		self.windowActive = not self.windowActive

		if self.windowActive:
			itemList  = watch.findAds()
			self.drawItemList(itemList)

			self.Show()

		else:
			self.Hide()



	def drawItemList(self, itemList):
		"""Update the itemList in the GUI."""

		for item in itemList:

			widget = itemWidget(self.scroll, item[0])
			self.sizer.Add(widget, 0, wx.LEFT|wx.ALL, 5)

		self.scroll.SetSizer(self.sizer_container)


	def OnTaskBarRight(self, event):
		"""What happens on a rightclick on tray-icon."""
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
		self.tray.RemoveIcon()
		app.ExitMainLoop()



class itemWidget(wx.BoxSizer):
	def __init__(self, parent, name):
		wx.BoxSizer.__init__(self,wx.HORIZONTAL)

		#self.SetSize((200,20))

		self.container = wx.BoxSizer(wx.HORIZONTAL)
		self.Add(self.container)

		self.statusIcon = wx.StaticBitmap(parent, wx.ID_ANY, newItemBitmap)
		self.nameText = wx.Button(parent,wx.ID_ANY, name)
		self.deleteButton = wx.BitmapButton(parent, wx.ID_ANY, deleteBitmap)

		border = 2
		self.container.Add(self.statusIcon, 0, wx.LEFT|wx.ALIGN_RIGHT,border)
		self.container.Add(self.nameText, 0,  wx.ALL|wx.EXPAND,border)
		self.container.Add(self.deleteButton, 0,  wx.RIGHT,border)



# If the program is run directly or passed as an argument to the python
# interpreter then create a HelloWorld instance and show it
if __name__ == "__main__":
	app = wx.PySimpleApp()
	frame = BlocketWatcherGUI(None, -1,"BlocketWatcher")
	app.MainLoop()
