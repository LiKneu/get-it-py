#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  get-it.py
#  
#  Copyright 2019  <volker@rasppc>
#  
#  This script copies the functions of get-it.pl
#  

import tkinter as tk
import webbrowser

# The subprocess module is used to call system/operating system commands
#~ import subprocess

VERSION="12.05.2019"

# Opens bookmark window
def openBookmarkWn():
    btn_Bookmarks["bg"]="yellow"
    wn_Bookmarks = tk.Toplevel(
                                MainWindow,
                                height=200,
                                width=100,
                                )

    wn_Bookmarks.title("Bookmarks")
    url="https://comicguide.de/"
    webbrowser.open_new(url)
    return

# Opens files from the config directory, reads the content and returns
# data structure containing key-value pairs
def readConfigFiles():
    bookmarkFile = './config/Volkers_bookmarks.txt'
    with open(bookmarkFile, 'r') as f:
        #~ read_data = f.read()
        for line in f:
            print(line, end='')
    f.closed
    #~ print (read_data)
    return
    
    
MainWindow = tk.Tk()
MainWindow.title("get-it")

btn_Bookmarks = tk.Button(
                        MainWindow,
                        text="Bookmarks",
                        #~ command=openBookmarkWn
                        command=readConfigFiles
                        )
btn_Bookmarks.pack()

fr_StatusBar = tk.Frame(MainWindow,
                        #~ bd=2,
                        #~ bg="green",
                        #~ relief="ridge"
                        #~ padx=0,
                        #~ pady=20
                        )
fr_StatusBar.pack(side="left")


lbl_Version = tk.Label(
                        fr_StatusBar,
                        text=VERSION,
                        bd=2,
                        relief="ridge",
                        #~ bg="red",
                        #~ height=3,
                        #~ width=15,
                        padx=5,
                        #~ anchor="w",
                        
                        )
lbl_Version.pack(side="left")

lbl_Author = tk.Label(
                        fr_StatusBar,
                        text="V. Thomas",
                        bd=2,
                        relief="ridge",
                        #~ bg="yellow",
                        #~ width=15,
                        padx=5,
                        #~ anchor="w"
                        )
lbl_Author.pack(side="left")

MainWindow.mainloop()


