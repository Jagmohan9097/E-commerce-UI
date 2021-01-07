
    root.destroy()
# first row
 
clear = Button(btns_frame, text = "CLEAR", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "pencil", command = lambda: bt_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)

exit = Button(btns_frame, text = "EXIT", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "pencil", command = lambda: root.destroy()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
