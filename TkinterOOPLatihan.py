import tkinter

window = tkinter.Tk()

label1 = tkinter.Label(window, text="label1")
label2 = tkinter.Label(window, text="label2")

tombol1 = tkinter.Button(window, text="tombol1")
tombol2 = tkinter.Button(window, text="tombol2")

# Methode Positioning

label1.pack()
label2.pack()

tombol1.pack()
tombol2.pack()

# Methode Menampilkan GUI

window.mainloop()

