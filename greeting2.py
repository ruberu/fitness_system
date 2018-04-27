 global pwordE # These globals just make the variables global to the entire script, meaning any definition can use them
+    global nameE
+    global roots
+ 
+    roots = Tk() # This creates the window, just a blank one.
+    roots.title('Signup') # This renames the title of said window to 'signup'
+    intruction = Label(roots, text='Please Enter new Credidentials\n') # This puts a label, so just a piece of text saying 'please enter blah'
+    intruction.grid(row=0, column=0, sticky=E) # This just puts it in the window, on row 0, col 0. If you want to learn more look up a tkinter tutorial :)
+ 
+    nameL = Label(roots, text='New Username: ') # This just does the same as above, instead with the text new username.
+    pwordL = Label(roots, text='New Password: ') # ^^
+    nameL.grid(row=1, column=0, sticky=W) # Same thing as the instruction var just on different rows. :) Tkinter is like that.
+    pwordL.grid(row=2, column=0, sticky=W) # ^^
+ 
+    nameE = Entry(roots) # This now puts a text box waiting for input.
+    pwordE = Entry(roots, show='*') # Same as above, yet 'show="*"' What this does is replace the text with *, like a password box :D
+    nameE.grid(row=1, column=1) # You know what this does now :D
+    pwordE.grid(row=2, column=1) # ^^
+ 
+    signupButton = Button(roots, text='Signup', command=FSSignup) # This creates the button with the text 'signup', when you click it, the command 'fssignup' will run. which is the def
+    signupButton.grid(columnspan=2, sticky=W)
+    roots.mainloop() # This just makes the window keep open, we will destroy it soon
