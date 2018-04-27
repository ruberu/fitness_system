from tkinter import *
import random
import time



root = Tk()
root.title('FITNESS SYSTEM')
root.geometry('1000x600+80+80')

header = Frame(root, width = 1000, height = 150, bg = 'powder blue', relief = SUNKEN)
header.pack(side = TOP)


main = Frame(root, width = 1000, height = 600, bg = 'goldenrod2', relief = SUNKEN)
main.pack(side = TOP)

#------------------------------------TIME-----------------------------------
localtime = time.asctime(time.localtime(time.time()))

#--------------------------------HEADER-------------------------------------
headerinfo = Label(header, font =('arial', 35, 'bold'), text = 'THE FITNESS SYSTEM', fg = 'Steel Blue', bd = 10, anchor = 'w')
headerinfo.grid(row = 0, column = 0)
headerinfo = Label(header, font = ('arial', 15, 'bold'), text = localtime, fg = 'Steel Blue', bd = 10, anchor = 'w')
headerinfo.grid(row = 1, column = 0)







root.mainloop()
