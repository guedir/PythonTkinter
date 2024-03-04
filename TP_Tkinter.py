import tkinter

#Interface graphique
fenetre = tkinter.Tk()
fenetre.geometry("200x80")
fenetre.resizable(False,False)
fenetre.title("convertisseur")
fenetre.configure(bg="#091821")

convert = lambda nombre , taux : round(nombre*taux, 2)
def convertir():
    m = montant.get()
    resultat.config(text=str(convert(m,1.12)) +" Dollars US")

montant = tkinter.DoubleVar()
label = tkinter.Label(fenetre , text="Montant en euro?" , bg="#091821" , fg="white")
zone_saisi = tkinter.Entry(fenetre , textvariable = montant , bd=3)
boutton = tkinter.Button(fenetre , text="Convertir" , command=convertir , bd=2 ,bg="#FFA500" ,fg="White" )
resultat = tkinter.Message(fenetre , width=200 , bg="#091821" , fg="white")

label.grid(column=0 , row=0)
zone_saisi.grid(column=0 , row=1 , padx=5)
boutton.grid(column=1 , row=1)
resultat.grid(column=0 ,row=2 , columnspan=3)

fenetre.mainloop()