
from tkinter import*
from tkinter import ttk

import Registro_database

from tkinter import messagebox


windo1= Tk()
windo1.title("NaviPortans")
windo1.config(bg="#3CB371")
def on_closing():
            if messagebox.askokcancel("salir","¿ESTAS SEGURO QUE QUIERES SALIR ?"):
                windo1.destroy()

windo1.protocol("WM_DELETE_WINDOW", on_closing)
windo1.resizable(False,False)
ancho_ventana = 400
alto_ventana = 700

x_ventana = windo1.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = windo1.winfo_screenheight() // 2 - alto_ventana // 2

posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
windo1.geometry(posicion)

Etiqueta =  Label(windo1,text="Bienvenidos a Naviportans", font=("Arial",20), bg="white", fg="black", width="50", height="1").pack()
Etiqueta_1 = Label(windo1,text="Servicios de entrega a domicilio",font=("Arial",20),bg="#3CB371",fg="black").place(x=0,y=80)
def inicio1():
         
    from tkinter import messagebox
    from tkinter import ttk
    import Registro_database
   
    window3= Toplevel(windo1) 
    ancho_ventana = 400
    alto_ventana = 700
    def on_closing():
            if messagebox.askokcancel("salir","¿ESTAS SEGURO QUE QUIERES SALIR ?"):
                window3.destroy()

    window3.protocol("WM_DELETE_WINDOW", on_closing)
    x_ventana = window3.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = window3.winfo_screenheight() // 2 - alto_ventana // 2

    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
    window3.geometry(posicion)
    window3['bg'] = '#3CB371'
    window3.title("Inicio Sesion")
   
    window3.resizable(False,False)
    Etiqueta =  Label(window3,text="Bienvenido a Naviportans", font=("Franklin Gothic Medium Cond",30), bg="white", fg="black", width="50", height="1").pack()
    Etiqueta_1 = Label(window3,text="Nombre de Usuario",font=("Arial",15),bg="#3CB371",fg="black").place(x=110,y=80)
    Etiqueta_2 = Label(window3,text="Correo electronico",font=("Arial",15),bg="#3CB371",fg="black").place(x=110,y=150)
    Etiqueta_3 = Label(window3,text="Contrasena",font=("Arial",15),bg="#3CB371",fg="black").place(x=110,y=220)
    backimage = PhotoImage(file="back.png")

    def atras():
        window3.withdraw()
        windo1.deiconify()
        
    button_atras = Button(window3, text="Atras",
                        font=("Century Gothic", "5", "bold"),compound="top",image=backimage,width=20,height=20,bg="#2ac17e",
                        command=atras)
    button_atras.place(x=2, y=55)
    Imagen3=PhotoImage(file="Inicio.png")
    Imagen_4 =Label(window3, image=Imagen3,width=0,height=0)

    Imagen_4.place(x=60, y=420)
    ENTRY1 = Entry(window3,bg="white",width="30")
    ENTRY1.place(x=100,y=120)
    ENTRY2 = Entry(window3,bg="white",width="30")
    ENTRY2.place(x=100,y=190)

    ENTRY3 = Entry(window3,bg="white",width="30")
    ENTRY3.place(x=100,y=260)
    def boton1():
        
        nombre1 = ENTRY1.get()
        correo1 = ENTRY2.get()
        
        contraseña1= ENTRY3.get()
        nombre= ""
        correo=""
        contraseña=""
        
        navyportans = Registro_database.MyDatabase()
        senal=1
        senal=navyportans.read_db(nombre,correo,contraseña,nombre1,correo1,contraseña1,window3,windo1)
        
        if senal == 2:
            messagebox.showerror(message="Nombre de usuario, Correo Electrónico o Contraseña incorrectos", title="Incorrecto")
    
            
        
    boton1= Button(window3,text="Iniciar Sesion",width="15", height="1",font=("Franklin Gothic Medium Cond",20),bg="white", fg="black",command=boton1)
    boton1.place(x=89,y=360)


    window3.mainloop()
#---------------------------------------#
#pantalla2
#---------------------------------------#
def registrarse1():
        
        from tkinter import ttk
        
        import Registro_database
        import mysql.connector 
        window2= Toplevel(windo1) 
        window2.resizable(False,False)
        def on_closing():
            if messagebox.askokcancel("salir","¿ESTAS SEGURO QUE QUIERES SALIR ?"):
                window2.destroy()

        window2.protocol("WM_DELETE_WINDOW", on_closing)
        backimage = PhotoImage(file="back.png")
        ancho_ventana = 400
        alto_ventana = 700

        x_ventana = windo1.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = windo1.winfo_screenheight() // 2 - alto_ventana // 2

        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        window2.geometry(posicion)
        def atras():
            window2.withdraw()
            windo1.deiconify()
     
        frame_app = Frame(window2, width=400, height=400, bg="#3CB371")
        frame_app.pack()
        window2.title("Inicio de sesion ")
               
        button_atras = Button(window2, text="Atras",
                            font=("Century Gothic", "5", "bold"),compound="top",image=backimage,width=32,height=29,bg="#2ac17e",
                            command=atras)
        button_atras.place(x=1, y=12)
        Imagen3=PhotoImage(file="imagen.png")
        Imagen_4 =Label(window2, image=Imagen3,width=0,height=0)

        Imagen_4.place(x=80, y=125)
        
        
        nombre = StringVar()
        correo = StringVar()
        contraseña = StringVar()
        direccion = StringVar()
        
        def crear_registro():
            nombre = entry_nombre.get()
            correo = entry_correo.get()
            contraseña = entry_contrasena.get()
            direccion = entry_direccion.get()
            if direccion=="" or contraseña=="" or correo=="" or nombre=="":
                messagebox.showinfo(message="Le faltan datos", title="Incorrecto")
            else:
                inicio_db = Registro_database.MyDatabase()
                data = (nombre, correo, contraseña,direccion)
                print(data)
                inicio_db.insert_db(nombre, correo, contraseña,direccion)
                messagebox.showinfo(message="Se acaba de registrar en navyportans", title="correcto")
        frame_navbar = Frame(frame_app, width=400, height=100,bg="#3CB371")
        frame_navbar.grid(row=0, column=0)
        frame_title = Frame(frame_app, width=400, height=150,bg="#3CB371")
        frame_title.grid(row=1, column=0)
        frame_options = Frame(frame_app, width=400, height=600 ,bg="#3CB371")
        frame_options.grid(row=2, column=0)
        
        frame_food = Frame(frame_options, width=350, height=500, bg="#3CB371")
        frame_food.place(x=25, y=-10)
        label_nombre = Label(frame_food, 
                    text="Nombre de Usuario",
                    font=("Franklin Gothic Medium Cond", "22"),
                    fg="white",
                    bg="#3CB371")
        label_nombre.place(x=20, y=10)
        entry_nombre = Entry(frame_food, justify=CENTER, width=30, font=("Calibri", "14"))
        entry_nombre.place(x=20, y=47)
        label_correo = Label(frame_food, 
                    text="Correo Electronico ",
                    font=("Franklin Gothic Medium Cond", "22"),
                    fg="white",
                    bg="#3CB371")
        label_correo.place(x=20, y=80)
        entry_correo = Entry(frame_food, justify=CENTER, width=30, font=("Calibri", "14"))
        entry_correo.place(x=20, y=117)
        label_contrasena = Label(frame_food, 
                    text="Contraseña",
                    font=("Franklin Gothic Medium Cond", "22"),
                    fg="white",
                    bg="#3CB371")
        label_contrasena.place(x=20, y=150)
        entry_contrasena = Entry(frame_food, justify=CENTER, width=30, font=("Calibri", "14", "bold"))
        entry_contrasena.place(x=20, y=188)

        label_direccion = Label(frame_food, 
                    text="Direccion",
                    font=("Franklin Gothic Medium Cond", "22"),
                    fg="white",
                    bg="#3CB371")
        label_direccion.place(x=20, y=215)
        entry_direccion = Entry(frame_food, justify=CENTER, width=30, font=("Calibri", "14", "bold"))
        entry_direccion.place(x=20, y=250)


        boton= Button(window2,text="Registrarse",width="15", height="1",font=("Franklin Gothic Medium Cond",20),bg="white", fg="black",command=crear_registro)
        boton.place(x=100,y=530)


        title1 = Label(frame_title, 
                    text="BIENVENIDO A NAVIPORTANS", 
                    font=("Franklin Gothic Medium Cond", "24"),
                    justify=CENTER ,bg="#3CB371",fg="black")
        title1.place(x=25, y=-10)


        window2.mainloop()
def registrarse():
    windo1.withdraw()
    registrarse1()
def inicio():
    windo1.withdraw()
    inicio1()


boton1= Button(windo1,text="Iniciar sesión",width="15", height="1",font=("Arial",18),bg="white", fg="#000000",command=inicio)
boton1.place(x=90,y=399)
boton2= Button(windo1,text="Registrarse",width="15", height="1",font=("Arial",18),bg="white", fg="#000000",command=registrarse)
boton2.place(x=90,y=480)
Imagen=PhotoImage(file="titulo.png")
Imagen_2 =Label(windo1, image=Imagen,width=130,height=130).place(x=140, y=140)

windo1.mainloop()
