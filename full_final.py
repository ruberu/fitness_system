from tkinter import *
import random
import time



root = Tk()
root.title('FITNESS SYSTEM')
root.geometry('1000x600+80+80')

header = Frame(root, width = 1000, height = 150, bg = 'sky blue', relief = SUNKEN)
header.pack(side = TOP)


main1 = Frame(root, width = 1000, height = 100,  relief = SUNKEN)
main1.pack(side = TOP)

main2 = Frame(root, width = 1000, height = 75,  relief = SUNKEN)
main2.pack(side = BOTTOM)
#------------------------------------TIME-----------------------------------
localtime = time.asctime(time.localtime(time.time()))

#--------------------------------HEADER-------------------------------------
headerinfo = Label(header, font =('arial', 35, 'bold'), text = 'THE FITNESS SYSTEM', fg = 'Steel Blue', bd = 10, anchor = 'w')
headerinfo.grid(row = 0, column = 0)
headerinfo = Label(header, font = ('arial', 15, 'bold'), text = localtime, fg = 'Steel Blue', bd = 10, anchor = 'w')
headerinfo.grid(row = 1, column = 0)

#==================================BUTTONS====================================

sinbutton = Button(root, padx = 60, pady = 18, bd = 10, fg = 'black', font = ('arial', 25, 'bold'),
                   text = 'SIGN IN', bg ='azure', command = '')
sinbutton.pack(side = TOP)

supbutton = Button(root, padx = 54, pady = 18, bd = 10, fg = 'black', font = ('arial', 25, 'bold'),
                   text = 'SIGN UP', bg ='azure')
supbutton.pack(side = TOP)

exitbutton = Button(root, padx = 25, pady = 12, bd = 10, fg = 'black', font = ('arial', 15, 'bold'),
                   text = 'EXIT', bg ='azure', command = quit)
exitbutton.pack(side = BOTTOM)




root.mainloop()
