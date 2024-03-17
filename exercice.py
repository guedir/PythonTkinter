import tkinter

fenetre = tkinter.Tk()
fenetre.geometry("350x180")

def addition():
    nb = nombre.get()
    addi = (nb*2)
    resultat.config(text=f"{addi}")

nombre = tkinter.IntVar()
lbl1 = tkinter.Label(fenetre , text="Entrer N")
zone_saisi = tkinter.Entry(fenetre , textvariable=nombre )
lbl2 = tkinter.Label(fenetre , text="Le double de N =")
resultat = tkinter.Label(fenetre , text="")
btn = tkinter.Button(fenetre , text="Valider l'operation" , command=addition)

lbl1.grid(column=0 , row=0 , padx=25 , pady=25)
zone_saisi.grid(column=1 , row=0 )
lbl2.grid(column=0 , row=1 , padx=25)
resultat.grid(column=1 , row=1)
btn.grid(column=1 , row=2 , pady=25)

fenetre.mainloop()