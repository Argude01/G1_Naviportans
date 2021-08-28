from logging import root
from tkinter import*
import Registro_database
from tkinter import ttk
from tkinter import messagebox
window= Tk()
window.title("Navi Portans")
window.config(bg="white")
ancho_ventana = 400
alto_ventana = 700

x_ventana = window.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = window.winfo_screenheight() // 2 - alto_ventana // 2

posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
window.geometry(posicion)
window.resizable(False,False)

frame_navbar= Frame(window, width=400, height=150, bg="#2ac17e").place(x=0,y=0)
label=Label(frame_navbar, width=7, height=2, bg="#2ac17e", text="Tienda" ,font=("Franklin Gothic Medium Cond",30),fg="white").place(x=1 ,y=50)
label2=Label(window,width=17, height=2, bg="white", text="Todas las categorías", font=("Arial Black",20),fg="black").place(x=2, y=140)
label3=Label(window,width=17, height=2, bg="white", text="¡Oferta Especial!", font=("Sans Serif",10),fg="black").place(x=5, y=450)
label4=Label(window,width=17, height=2, bg="white", text="Pizza Gigante Pizza Hut", font=("Sans Serif",10),fg="black").place(x=5, y=475)
label5=Label(window,width=17, height=2, bg="white", text="¡Oferta Especial!", font=("Sans Serif",10),fg="black").place(x=225, y=470)
label6=Label(window,width=20, height=2, bg="white", text="Tacos Mexicanos Caseros", font=("Sans Serif",10),fg="black").place(x=215, y=505)

def on_closing():
            if messagebox.askokcancel("salir","¿ESTAS SEGURO QUE QUIERES SALIR ?"):
                window.destroy()

window.protocol("WM_DELETE_WINDOW", on_closing)    

image_perfil = PhotoImage(file="ícono perfil.png")
image_inicio = PhotoImage(file="acerca.png")
image_comestibles = PhotoImage(file="ícono comestibles.png")
image_bebidas = PhotoImage(file="ícono bebidas.png")
image_refrigerados = PhotoImage(file="ícono refrigerados.png")
image_Pizza = PhotoImage(file="Pizza Oferta.png")
image_Tacos = PhotoImage(file="Tacos Oferta.png")
def comestibles1():
        root= Toplevel(window)
        import Registro_database
        import tkinter as tk
        from tkinter import messagebox
        

        def on_closing():
            if messagebox.askokcancel("salir","¿ESTAS SEGURO QUE QUIERES SALIR ?"):
                root.destroy()

        root.protocol("WM_DELETE_WINDOW", on_closing)
        ancho_ventana = 400
        alto_ventana = 700

        x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = root.winfo_screenheight() // 2 - alto_ventana // 2

        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        root.geometry(posicion)
        
        root.resizable(False,False)
        root.title("NAVYPORTANS")
        root.configure(background="white")
        backimage = PhotoImage(file="back.png")

        def atras():
            root.withdraw()
            window.deiconify()

        def suma():
            a=int(Entry_1.get())
            a=a+1
            var.set(a)
        def resta():
            a=int(Entry_1.get())
            if a>0:
                a=a-1
            
            var.set(a)

        def suma1():
            a=int(Entry_2.get())
            a=a+1
            var1.set(a)
        def resta1():
            a=int(Entry_2.get())
            if a>0:
                a=a-1
            var1.set(a)
        def suma2():
            a=int(Entry_3.get())
            a=a+1
            var2.set(a)
        def resta2():
            a=int(Entry_3.get())
            if a>0:
                a=a-1
            var2.set(a)
        def suma3():
            a=int(Entry_4.get())
            a=a+1
            var3.set(a)
        def resta3():
            a=int(Entry_4.get())
            if a>0:
                a=a-1
            var3.set(a)
        frame_caja = Frame(root, width=400, height=100, bg="#2ac17e")
        frame_caja.place(x=0,y=0)
        texto1= Label(frame_caja, text="Comestibles",font=("Arial",50),fg="white",bg="#2ac17e").place(x=20,y=20)
        button_atras = Button(frame_caja, text="Atras",
                            font=("Century Gothic", "5", "bold"),compound="top",image=backimage,width=32,height=29,bg="#2ac17e",
                            command=atras)
        button_atras.place(x=1, y=0)
        Imagen=PhotoImage(file="1.png")
        Imagen_2 =Label(frame_caja, image=Imagen,width=0,height=0)
        var= IntVar()
        var1=IntVar()
        var2= IntVar()
        var3=IntVar()
        Imagen_2.place(x=330, y=0)

        Imagen3=PhotoImage(file="2.png")
        Imagen_4 =Label(root, image=Imagen3,width=0,height=0)

        Imagen_4.place(x=30, y=150)
        texto2= Label(root, text="Pizza",font=("Arial",20),fg="black",bg="white").place(x=60,y=113)
        texto3= Label(root, text="Hamburguesa",font=("Arial",20),fg="black",bg="white").place(x=212,y=113)
        Imagen5=PhotoImage(file="3.png")

        Imagen_6 =Label(root, image=Imagen5,width=0,height=0)

        Imagen_6.place(x=210, y=150)
        Imagen7=PhotoImage(file="4.png")
        Imagen_8 =Label(root, image=Imagen7,width=0,height=0)

        Imagen_8.place(x=30, y=400)
        texto4= Label(root, text="Tacos",font=("Arial",20),fg="black",bg="white").place(x=70,y=360)
        Imagen9=PhotoImage(file="5.png")
        Imagen_10 =Label(root, image=Imagen9,width=0,height=0)

        Imagen_10.place(x=220, y=400)
        texto5= Label(root, text="Camarones",font=("Arial",20),fg="black",bg="white").place(x=235,y=360)
        boton1= Button(root,width="5", text="-",height="1",font=("arial",15), fg="black",command=resta)
        boton1.place(x=30,y=275)
        boton2= Button(root,width="5", text="+",height="1",font=("arial",15), fg="black",command=suma)
        boton2.place(x=110,y=275)
        preciopizza=Label(root, text="Precio 150 lmp",font=("Arial",12),fg="black",bg="white").place(x=30,y=250)
        Entry_1 = Entry(root,width=20,textvariable=var)
        Entry_1.place(x=35,y=320)#pizza entry
        boton3= Button(root,width="5", text="-",height="1",font=("arial",15), fg="black",command=resta1)
        boton3.place(x=30,y=540)
        Entry_2 = Entry(root,width=20,textvariable=var1)
        Entry_2.place(x=45,y=590)
        preciotacos=Label(root, text="Precio 100 lmp",font=("Arial",12),fg="black",bg="white").place(x=30,y=510)
        boton4= Button(root,width="5", text="+",height="1",font=("arial",15), fg="black",command=suma1)
        boton4.place(x=130,y=540)
        Entry_3 = Entry(root,width=20,textvariable=var2)
        Entry_3.place(x=250,y=590)

        boton5= Button(root,width="5", text="-",height="1",font=("arial",15), fg="black",command=resta2)
        boton5.place(x=230,y=540)
        boton6= Button(root,width="5", text="+",height="1",font=("arial",15), fg="black",command=suma2)
        boton6.place(x=320,y=540)
        Entry_4 = Entry(root,width=20,textvariable=var3)
        Entry_4.place(x=250,y=320)
        preciocamarones=Label(root, text="Precio 140 lmp",font=("Arial",12),fg="black",bg="white").place(x=250,y=510)
        boton7= Button(root,width="5", text="-",height="1",font=("arial",15), fg="black",command=resta3)
        boton7.place(x=230,y=275)
        preciohamburguesa=Label(root, text="Precio 200 lmp",font=("Arial",12),fg="black",bg="white").place(x=250,y=250)
        boton7= Button(root,width="5", text="+",height="1",font=("arial",15), fg="black",command=suma3)
        boton7.place(x=320,y=275)
        def pizza():
            a=Entry_1.get()
            b=Entry_2.get()
            c=Entry_3.get()
            d=Entry_4.get()
            a=str(a)
            pizza=a , " pizza,"
            pizza=''.join(pizza) 
            hamburguesa = d , " hambueguesa,"
            hamburguesa =''.join(hamburguesa) 
            tacos=b , " tacos,"
            tacos=''.join(tacos) 
            camarones = c ," camarones  "
            camarones= ''.join(camarones) 
            Descripcion = pizza , hamburguesa,tacos,camarones
            Descripcion = ''.join(Descripcion) 
            navyportans = Registro_database.MyDatabase()
            data = (Descripcion)
            ppizza=150
            phamburguesa=200
            pcamarones=140
            ptacos=100
            Precio=int((int(ppizza)*int(a))+(int(phamburguesa)*int(d))+(int(pcamarones)*int(c))+(int(ptacos)*int(b)))
            print(data)
            print(Precio)
            Id_categoria=1
            navyportans.insert_producto(Descripcion,Precio,Id_categoria)
            messagebox.showinfo(message=f"Se ha realizado su compra de: {Descripcion} con un precio a pagar: {Precio}",title="Compra Realizada" )
        



        enviar= Button(root,width="6", text="ENVIAR",height="1",font=("arial",15), fg="black",command=pizza)
        enviar.place(x=150,y=620)
        root.mainloop()
#---------------------------------------------------------------------------#
#pantalla3#
#---------------------------------------------------------------------------#
def bebidas1():
            import Registro_database
            root1= Toplevel(window)
            ancho_ventana = 400
            alto_ventana = 700
            def on_closing():
                if messagebox.askokcancel("salir","¿ESTAS SEGURO QUE QUIERES SALIR ?"):
                    root1.destroy()

            root1.protocol("WM_DELETE_WINDOW", on_closing)
            x_ventana = root1.winfo_screenwidth() // 2 - ancho_ventana // 2
            y_ventana = root1.winfo_screenheight() // 2 - alto_ventana // 2

            posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
            root1.geometry(posicion)
            root1.resizable(False,False)
            root1.title("NAVYPORTANS")
            root1.configure(background="white")
            backimage = PhotoImage(file="back.png")
            def atras():
                root1.withdraw()
                window.deiconify()

            def suma():
                a=int(Entry_1.get())
                a=a+1
                var.set(a)
            def resta():
                a=int(Entry_1.get())
                if a>0:
                    a=a-1
                
                var.set(a)

            def suma1():
                a=int(Entry_2.get())
                a=a+1
                var1.set(a)
            def resta1():
                a=int(Entry_2.get())
                if a>0:
                    a=a-1
                var1.set(a)
            def suma2():
                a=int(Entry_3.get())
                a=a+1
                var2.set(a)
            def resta2():
                a=int(Entry_3.get())
                if a>0:
                    a=a-1
                var2.set(a)
            def suma3():
                a=int(Entry_4.get())
                a=a+1
                var3.set(a)
            def resta3():
                a=int(Entry_4.get())
                if a>0:
                    a=a-1
                var3.set(a)
            frame_caja = Frame(root1, width=400, height=100, bg="#2ac17e")
            frame_caja.place(x=0,y=0)
            texto1= Label(frame_caja, text="Bebidas",font=("Arial",50),fg="white",bg="#2ac17e").place(x=20,y=20)
            button_atras = Button(frame_caja, text="Atras",
                                font=("Century Gothic", "5", "bold"),compound="top",image=backimage,width=32,height=29,bg="#2ac17e",
                                command=atras)
            button_atras.place(x=1, y=0)
            Imagen=PhotoImage(file="1.png")
            Imagen_2 =Label(frame_caja, image=Imagen,width=0,height=0)
            var= IntVar()
            var1=IntVar()
            var2= IntVar()
            var3=IntVar()
            Imagen_2.place(x=330, y=0)

            Imagen3=PhotoImage(file="HORCHATA.png")
            Imagen_4 =Label(root1, image=Imagen3,width=0,height=0)

            Imagen_4.place(x=30, y=150)
            texto2= Label(root1, text="Horchata",font=("Arial",20),fg="black",bg="white").place(x=60,y=113)
            texto3= Label(root1, text="Mora",font=("Arial",20),fg="black",bg="white").place(x=280,y=113)
            Imagen5=PhotoImage(file="mora.png")

            Imagen_6 =Label(root1, image=Imagen5,width=0,height=0)

            Imagen_6.place(x=270, y=150)
            Imagen7=PhotoImage(file="limonada.png")
            Imagen_8 =Label(root1, image=Imagen7,width=0,height=0)

            Imagen_8.place(x=30, y=400)
            texto4= Label(root1, text="Limonada",font=("Arial",20),fg="black",bg="white").place(x=70,y=360)
            Imagen9=PhotoImage(file="coca cola.png")
            Imagen_10 =Label(root1, image=Imagen9,width=0,height=0)

            Imagen_10.place(x=220, y=400)
            texto5= Label(root1, text="Coca cola",font=("Arial",20),fg="black",bg="white").place(x=235,y=360)
            boton1= Button(root1,width="5", text="-",height="1",font=("arial",15), fg="black",command=resta)
            boton1.place(x=30,y=275)
            boton2= Button(root1,width="5", text="+",height="1",font=("arial",15), fg="black",command=suma)
            boton2.place(x=110,y=275)
            preciopizza=Label(root1, text="Precio 20 lmp",font=("Arial",12),fg="black",bg="white").place(x=30,y=250)
            Entry_1 = Entry(root1,width=20,textvariable=var)
            Entry_1.place(x=35,y=320)#pizza entry
            boton3= Button(root1,width="5", text="-",height="1",font=("arial",15), fg="black",command=resta1)
            boton3.place(x=30,y=540)
            Entry_2 = Entry(root1,width=20,textvariable=var1)
            Entry_2.place(x=45,y=590)
            preciotacos=Label(root1, text="Precio 25 lmp",font=("Arial",12),fg="black",bg="white").place(x=30,y=510)
            boton4= Button(root1,width="5", text="+",height="1",font=("arial",15), fg="black",command=suma1)
            boton4.place(x=130,y=540)
            Entry_3 = Entry(root1,width=20,textvariable=var2)
            Entry_3.place(x=250,y=590)

            boton5= Button(root1,width="5", text="-",height="1",font=("arial",15), fg="black",command=resta2)
            boton5.place(x=230,y=540)
            boton6= Button(root1,width="5", text="+",height="1",font=("arial",15), fg="black",command=suma2)
            boton6.place(x=320,y=540)
            Entry_4 = Entry(root1,width=20,textvariable=var3)
            Entry_4.place(x=250,y=320)
            preciocamarones=Label(root1, text="Precio 10 lmp",font=("Arial",12),fg="black",bg="white").place(x=250,y=510)
            boton7= Button(root1,width="5", text="-",height="1",font=("arial",15), fg="black",command=resta3)
            boton7.place(x=230,y=275)
            preciohamburguesa=Label(root1, text="Precio 15 lmp",font=("Arial",12),fg="black",bg="white").place(x=250,y=250)
            boton7= Button(root1,width="5", text="+",height="1",font=("arial",15), fg="black",command=suma3)
            boton7.place(x=320,y=275)
            def pizza():
                a=Entry_1.get()
                b=Entry_2.get()
                c=Entry_3.get()
                d=Entry_4.get()
                a=str(a)
                horchata=a , " Horchata,"
                horchata=''.join(horchata) 
                Mora = d , " Mora,"
                Mora =''.join(Mora) 
                limonada=b , " limonada,"
                limonada=''.join(limonada) 
                coca_cola = c ," coca cola "
                coca_cola= ''.join(coca_cola) 
                Descripcion = horchata , Mora,limonada,coca_cola
                Descripcion = ''.join(Descripcion) 
                inicio_db = Registro_database.MyDatabase()
                data = (Descripcion)
                phorchata=20
                pmora=15
                plimonada=25
                pcocacola=10
                Precio=int((int(phorchata)*int(a))+(int(pmora)*int(d))+(int(plimonada)*int(b))+(int(pcocacola)*int(c)))
                print(data)
                print(Precio)
                Id_categoria=2
                inicio_db.insert_producto(Descripcion,Precio,Id_categoria)
                messagebox.showinfo(message=f"Se ha realizado su compra de: {Descripcion} con un precio a pagar: {Precio}",title="Compra Realizada" )
        
                
            enviar= Button(root1,width="6", text="ENVIAR",height="1",font=("arial",15), fg="black",command=pizza)
            enviar.place(x=150,y=620)
            root1.mainloop()

#pantalla de postre#
def postres1():
        
        import Registro_database
        root3= Toplevel(window)
        ancho_ventana = 400
        alto_ventana = 700
        def on_closing():
            if messagebox.askokcancel("salir","¿ESTAS SEGURO QUE QUIERES SALIR ?"):
                root3.destroy()

        root3.protocol("WM_DELETE_WINDOW", on_closing)
        x_ventana = root3.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = root3.winfo_screenheight() // 2 - alto_ventana // 2

        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        root3.geometry(posicion)
        root3.resizable(False,False)
        root3.title("NAVYPORTANS")
        root3.configure(background="white")
        backimage = PhotoImage(file="back.png")
        def atras():
            root3.withdraw()
            window.deiconify()

        def suma():
            a=int(Entry_1.get())
            a=a+1
            var.set(a)
        def resta():
            a=int(Entry_1.get())
            if a>0:
                a=a-1
            
            var.set(a)

        def suma1():
            a=int(Entry_2.get())
            a=a+1
            var1.set(a)
        def resta1():
            a=int(Entry_2.get())
            if a>0:
                a=a-1
            var1.set(a)
        def suma2():
            a=int(Entry_3.get())
            a=a+1
            var2.set(a)
        def resta2():
            a=int(Entry_3.get())
            if a>0:
                a=a-1
            var2.set(a)
        def suma3():
            a=int(Entry_4.get())
            a=a+1
            var3.set(a)
        def resta3():
            a=int(Entry_4.get())
            if a>0:
                a=a-1
            var3.set(a)
        frame_caja = Frame(root3, width=400, height=100, bg="#2ac17e")
        frame_caja.place(x=0,y=0)
        texto1= Label(frame_caja, text="Postres",font=("Arial",50),fg="white",bg="#2ac17e").place(x=40,y=20)
        button_atras = Button(frame_caja, text="Atras",
                            font=("Century Gothic", "5", "bold"),compound="top",image=backimage,width=32,height=29,bg="#2ac17e",
                            command=atras)
        button_atras.place(x=1, y=0)
        Imagen=PhotoImage(file="1.png")
        Imagen_2 =Label(frame_caja, image=Imagen,width=0,height=0)
        var= IntVar()
        var1=IntVar()
        var2= IntVar()
        var3=IntVar()
        Imagen_2.place(x=330, y=0)

        Imagen3=PhotoImage(file="helados.png")
        Imagen_4 =Label(root3, image=Imagen3,width=0,height=0)

        Imagen_4.place(x=20, y=150)
        texto2= Label(root3, text="Helado",font=("Arial",20),fg="black",bg="white").place(x=60,y=113)
        texto3= Label(root3, text="Pan de ajo",font=("Arial",20),fg="black",bg="white").place(x=250,y=113)
        Imagen5=PhotoImage(file="pan.png")

        Imagen_6 =Label(root3, image=Imagen5,width=0,height=0)

        Imagen_6.place(x=270, y=150)
        Imagen7=PhotoImage(file="tarta.png")
        Imagen_8 =Label(root3, image=Imagen7,width=0,height=0)

        Imagen_8.place(x=50, y=400)
        texto4= Label(root3, text="TARTA",font=("Arial",20),fg="black",bg="white").place(x=60,y=360)
        Imagen9=PhotoImage(file="yogurt.png")
        Imagen_10 =Label(root3, image=Imagen9,width=0,height=0)

        Imagen_10.place(x=240, y=400)
        texto5= Label(root3, text="YOGURT",font=("Arial",20),fg="black",bg="white").place(x=235,y=360)
        boton1= Button(root3,width="5", text="-",height="1",font=("arial",15), fg="black",command=resta)
        boton1.place(x=30,y=275)
        boton2= Button(root3,width="5", text="+",height="1",font=("arial",15), fg="black",command=suma)
        boton2.place(x=110,y=275)
        preciopizza=Label(root3, text="Precio 50 lmp",font=("Arial",12),fg="black",bg="white").place(x=30,y=250)
        Entry_1 = Entry(root3,width=20,textvariable=var)
        Entry_1.place(x=35,y=320)#pizza entry
        boton3= Button(root3,width="5", text="-",height="1",font=("arial",15), fg="black",command=resta1)
        boton3.place(x=30,y=540)
        Entry_2 = Entry(root3,width=20,textvariable=var1)
        Entry_2.place(x=45,y=590)
        preciotacos=Label(root3, text="Precio 40 lmp",font=("Arial",12),fg="black",bg="white").place(x=30,y=510)
        boton4= Button(root3,width="5", text="+",height="1",font=("arial",15), fg="black",command=suma1)
        boton4.place(x=130,y=540)
        Entry_3 = Entry(root3,width=20,textvariable=var2)
        Entry_3.place(x=250,y=590)

        boton5= Button(root3,width="5", text="-",height="1",font=("arial",15), fg="black",command=resta2)
        boton5.place(x=230,y=540)
        boton6= Button(root3,width="5", text="+",height="1",font=("arial",15), fg="black",command=suma2)
        boton6.place(x=320,y=540)
        Entry_4 = Entry(root3,width=20,textvariable=var3)
        Entry_4.place(x=250,y=320)
        preciocamarones=Label(root3, text="Precio 30 lmp",font=("Arial",12),fg="black",bg="white").place(x=250,y=510)
        boton7= Button(root3,width="5", text="-",height="1",font=("arial",15), fg="black",command=resta3)
        boton7.place(x=230,y=275)
        preciohamburguesa=Label(root3, text="Precio 10 lmp",font=("Arial",12),fg="black",bg="white").place(x=250,y=250)
        boton7= Button(root3,width="5", text="+",height="1",font=("arial",15), fg="black",command=suma3)
        boton7.place(x=320,y=275)
        def pizza():
            a=Entry_1.get()
            b=Entry_2.get()
            c=Entry_3.get()
            d=Entry_4.get()
            a=str(a)
            helado=a , "helado ,"
            helado=''.join(helado) 
            pan = d , " pan,"
            pan =''.join(pan) 
            tarta=b , " tarta,"
            tarta=''.join(tarta) 
            yogurt = c ," yogurt "
            yogurt= ''.join(yogurt) 
            Descripcion = helado , pan,tarta,yogurt
            Descripcion = ''.join(Descripcion) 
            inicio_db = Registro_database.MyDatabase()
            data = (Descripcion)
            p1=50
            p2=10
            p3=40
            p4=30
            Precio=int((int(p1)*int(a))+(int(p2)*int(d))+(int(p3)*int(b))+(int(p4)*int(c)))
            print(data)
            print(Precio)
            Id_categoria=3
            inicio_db.insert_producto(Descripcion,Precio,Id_categoria)
            messagebox.showinfo(message=f"Se ha realizado su compra de: {Descripcion} con un precio a pagar: {Precio}",title="Compra Realizada" )
        
                
            
        enviar= Button(root3,width="6", text="ENVIAR",height="1",font=("arial",15), fg="black",command=pizza)
        enviar.place(x=150,y=620)
        root3.mainloop()
def perfil1():
        
        from tkinter import ttk
        import Registro_database
        root5= Toplevel(window)
        def on_closing():
            if messagebox.askokcancel("salir","¿ESTAS SEGURO QUE QUIERES SALIR ?"):
                root5.destroy()

        root5.protocol("WM_DELETE_WINDOW", on_closing)
        root5.title("Navi Portans")
        root5.config(bg="white")
        ancho_ventana = 400
        alto_ventana = 700

        x_ventana = root5.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = root5.winfo_screenheight() // 2 - alto_ventana // 2

        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        root5.geometry(posicion)
        root5.resizable(False, False)
        
        frame_app = Frame(root5, width=400, height=600, bg="white")
        frame_app.grid(row=1, column=0)
        frame_head = Frame(root5, width=400, height=100, bg="#2ac17e")
        frame_head.grid(padx=0, row=0, column=0)


        def atras():
            root5.withdraw()
            window.deiconify()


        # Frame_head
        Etiqueta = Label(frame_head, text="Perfil", font=("Arial", 25, "bold"), bg="#2ac17e", fg="white").place(x=125, y=25)

        backimage = PhotoImage(file="back.png")

        button_atras = Button(frame_head, text="Atras",
                            font=("Century Gothic", "10", "bold"), compound="top", image=backimage, width=50, height=60,
                            bg="#2ac17e",
                            command=atras)
        button_atras.place(x=300, y=20)
        # Frame_app
        cuentaimage = PhotoImage(file="account.png")
        direccionimage = PhotoImage(file="password.png")
        correoimage = PhotoImage(file="email.png")
        cerrarimage = PhotoImage(file="exit.png")
        def cerrar():
            if messagebox.askokcancel("salir","¿ESTAS SEGURO QUE QUIERES SALIR ?"):
                root5.destroy()

        
        
        
        
        Etiqueta = Label(frame_app, bg="white", image=cuentaimage,
                        height="0").grid(row=0, column=0, rowspan=2,pady=20)
        usuario = Label(frame_app, text="", font=("Arial", 15), bg="white", fg="black", width="0",
                        height="0").grid(row=0, column=1,pady=10)
        Etiqueta2 = Label(frame_app, bg="white", image=correoimage,
                        height="0").grid(row=2, column=0, rowspan=2,pady=20)
        Etiqueta3 = Label(frame_app, text="", font=("Arial", 15), bg="white", fg="black", width="0",
                        height="0").grid(row=2, column=1,pady=10)
        Etiqueta4 = Label(frame_app, bg="white", image=direccionimage,
                        height="0").grid(row=4, column=0, rowspan=2,pady=20)
        Etiqueta5 = Label(frame_app, text="", font=("Arial", 15), bg="white", fg="black", width="0",
                        height="0").grid(row=4, column=1,pady=10)
        button_cerrar = Button(frame_app, text="Atras",
                            font=("Century Gothic", "15", "bold"), compound="top", image=cerrarimage, width=150, height=80,
                            bg="#2ac17e",
                            command=cerrar)
        button_cerrar.grid(row=6, column=0,columnspan=2,pady=50)
        def perfil5():
        
            navyportans=Registro_database.MyDatabase()
            navyportans.perfil(frame_app)
        perfil5()
        root5.mainloop()
#pantallaacerca#
def acerca1():
        from tkinter import ttk
        root6= Toplevel(window)
        root6.title("Navi Portans")
        root6.config(bg="white")
        ancho_ventana = 400
        alto_ventana = 700

        x_ventana = root6.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = root6.winfo_screenheight() // 2 - alto_ventana // 2
        def on_closing():
            if messagebox.askokcancel("salir","¿ESTAS SEGURO QUE QUIERES SALIR ?"):
                root6.destroy()

        root6.protocol("WM_DELETE_WINDOW", on_closing)
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        root6.geometry(posicion)
        root6.resizable(False, False)

        frame_app = Frame(root6, width=400, height=600, bg="white")
        frame_app.grid(row=0, column=0)
        frame_feet = Frame(root6, width=400, height=195, bg="#2ac17e")
        frame_feet.grid(pady=35, padx=0, row=1, column=0)

        def atras():
            root6.withdraw()
            window.deiconify()

        image_acercade=PhotoImage(file="Acerca de.png")

        Etiqueta_A = Label(frame_app, image=image_acercade, bg="white", fg="black", width="0",height="0").place(x=150, y=60)
        Etiqueta = Label(frame_app, text="Acerca de", font=("Arial", 20), bg="white", fg="black", width="0",
                        height="0").grid(row=0,column=0,columnspan=2,pady=30)
        Etiqueta1 = Label(frame_app, text="Programadores", font=("Arial", 20), bg="white", fg="black", width="0",
                        height="0").grid(row=1,column=0,columnspan=2,pady=20)
        Etiqueta2 = Label(frame_app, text="03", font=("Arial", 15), bg="white", fg="black", width="0",
                        height="0").grid(row=2,column=0,pady=10,padx=10)
        Etiqueta3 = Label(frame_app, text="Any Dayana Zavala Alvarado", font=("Arial", 15), bg="white", fg="black", width="0",
                        height="0").grid(row=2,column=1,pady=10,padx=10)
        Etiqueta4 = Label(frame_app, text="13", font=("Arial", 15), bg="white", fg="black", width="0",
                        height="0").grid(row=3,column=0,pady=10,padx=10)
        Etiqueta5 = Label(frame_app, text="Lubia Milagro Gonzalez Escobar", font=("Arial", 15), bg="white", fg="black", width="0",
                        height="0").grid(row=3,column=1,pady=10,padx=10)
        Etiqueta6 = Label(frame_app, text="37", font=("Arial", 15), bg="white", fg="black", width="0",
                        height="0").grid(row=4,column=0,pady=10,padx=10)
        Etiqueta7 = Label(frame_app, text="Fabio Fernando Discua Calix", font=("Arial", 15), bg="white", fg="black", width="0",
                        height="0").grid(row=4,column=1,pady=10,padx=10)
        Etiqueta8 = Label(frame_app, text="42", font=("Arial", 15), bg="white", fg="black", width="0",
                        height="0").grid(row=5,column=0,pady=10,padx=10)
        Etiqueta9 = Label(frame_app, text="Jorge Lenin Hernandez Euceda", font=("Arial", 15), bg="white", fg="black", width="0",
                        height="0").grid(row=5,column=1,pady=10,padx=10)
        Etiqueta10 = Label(frame_app, text="44", font=("Arial", 15), bg="white", fg="black", width="0",
                        height="0").grid(row=6,column=0,pady=10,padx=10)
        Etiqueta11 = Label(frame_app, text="Jose Andriy Torres Perez", font=("Arial", 15), bg="white", fg="black", width="0",
                        height="0").grid(row=6,column=1,pady=10,padx=10)
        Etiqueta12 = Label(frame_app, text="46", font=("Arial", 15), bg="white", fg="black", width="0",
                        height="0").grid(row=7,column=0,pady=10,padx=10)
        Etiqueta13 = Label(frame_app, text="Jostin Javier Cruz Castillo", font=("Arial", 15), bg="white", fg="black", width="0",
                        height="0").grid(row=7,column=1,pady=10,padx=10)
        backimage = PhotoImage(file="back.png")
        button_atras = Button(frame_feet, text="Atras",
                            font=("Century Gothic", "10", "bold"),compound="top",image=backimage,width=50,height=60,bg="#2ac17e",
                            command=atras)
        button_atras.place(x=20, y=80)
        Etiqueta = Label(frame_feet, text="Nuestra aplicación, NavyPortans, busca que \n nuestros clientes tenga un servicio rápido \n y eficaz al momento de buscar todo aquello que \n deseen ordenar y que nostros podamos ofrecer.", font=("Arial", 10), bg="#2ac17e", fg="black", width="0",height="0").place(x=90, y=80)
        root6.mainloop()

def bebidas():
    window.withdraw()
    bebidas1()
def acerca():
    window.withdraw()
    acerca1()
def comestibles():
    window.withdraw()
    
    
    comestibles1()
def postres():

    window.withdraw()
    
    
    postres1()
def perfil():
    window.withdraw()
    perfil1()
btn_perfil= Button(frame_navbar, image=image_perfil,bg="#2ac17e",command=perfil).place(x=340, y=5)
boton_inicio= Button(window,image=image_inicio,bg="white",command=acerca).place(x=5,y=200)
boton_comestibles= Button(window,image=image_comestibles,bg="white",command=comestibles).place(x=98,y=200)
boton_bebidas= Button(window,image=image_bebidas,bg="white",command=bebidas).place(x=200,y=200)
boton_refrigerados= Button(window,image=image_refrigerados,bg="white",command=postres).place(x=305,y=200)
boton_pizza= Button(window,image=image_Pizza,bg="white").place(x=5,y=350)
boton_tacos= Button(window,image=image_Tacos,bg="white").place(x=205,y=350)

window.mainloop()