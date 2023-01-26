from tkinter import *

root=Tk()
root.title("To Do List")
root.geometry("800x400")

def Add():
    temp=duty.get("1.0", "end")
    #print("oku: {}".format(len(temp.strip())))
    if temp != " " and temp != None and len(temp)!=0 and len(temp.strip()) != 0:
        print("temp: {}".format(temp))
        listbox.insert(0,temp)

def Delete():
    selection = listbox.curselection()
    if selection != None and selection!= "" and selection:
        print("selection: {}".format(selection))
        listbox.delete(selection)

Label(root,text="Yapılacak Görev:").pack()
duty=Text(root,width=30,height=1)
duty.pack()
Button(root, text="Ekle",command=Add, width=20).pack(padx=10,pady=10)
Button(root, text="Sil",command=Delete, width=20).pack(padx=5,pady=5)
listbox=Listbox(root,height=15,width=60)
listbox.pack()
root.mainloop()