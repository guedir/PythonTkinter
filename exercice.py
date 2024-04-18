import tkinter
from tkinter import messagebox
from tkinter import Tk

fenetre = tkinter.Tk()
fenetre.geometry("450x180+450+200")
fenetre.title("Addition")
fenetre.resizable(True,False)
fenetre.configure(bg="#2F4F4F")


def addition():
        try:
            nb = nombre.get()
            addi = nb * 2
            resultat.config(text=f"Le double de {nb} est {addi} ")
        except Exception as e:
            #print(e)
            messagebox.showerror("Erreur","Veuillez saisir un nombre !!!")

def effacer():
     nombre.set(0)  
     resultat.config(text="")
     messagebox.showinfo("Information","vous avez rénitialiser les champs")

def quitter():
     quit()

nombre = tkinter.IntVar()
lbl1 = tkinter.Label(fenetre , text="Entrer N" , bg="#2F4F4F" , font=("sans serif",10,"bold"))
zone_saisi = tkinter.Entry(fenetre , textvariable=nombre, bd=3 , font=("sans serif",10,"bold"))
lbl2 = tkinter.Label(fenetre , text="Le double de N =" , bg="#2F4F4F", font=("sans serif",10,"bold"))
resultat = tkinter.Label(fenetre , text="" , fg="red" , bg="#2F4F4F", font=("sans serif",10,"bold"))
btn = tkinter.Button(fenetre , text="VALIDER" , command=addition, bd=3, font=("sans serif",8,"bold"), width=10)
btn2 = tkinter.Button(fenetre , text="RENITIALISER" , command=effacer,  bd=3, font=("sans serif",8,"bold"), width=10)
btn3 = tkinter.Button(fenetre, text="QUITTER", command=quitter,  bd=3, font=("sans serif",8,"bold"), width=10 )

lbl1.grid(column=0 , row=0 , padx=25 , pady=25)
zone_saisi.grid(column=1 , row=0 )
lbl2.grid(column=0 , row=1 , padx=25)
resultat.grid(column=1 , row=1)
btn.grid(column=0 , row=2 , pady=25, padx=10 )
btn2.grid(column=1 , row=2 , pady=25)
btn3.grid(column=2 , row=2 , pady=25)

fenetre.mainloop()