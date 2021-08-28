import mysql.connector
from tkinter import *
   
class MyDatabase():
    nnombre=None
    ccorreo=None
    ccontraseña=None
    def open_connection(self):
        connection = mysql.connector.connect( 
            host="localhost",                    
            user="root", 
            passwd="", 
            database="navyportans")
        return connection
    def insert_db(self, nombre, correo, contraseña,direccion):
        my_connection = self.open_connection()
        cursor = my_connection.cursor()
        query = "INSERT INTO tbl_usuarios(NOMBRE, CORREO, CONTRASEñA,DIRECCION) VALUES (%s,%s,%s,%s)"
        data = (nombre, correo, contraseña,direccion)
        cursor.execute(query, data)
        my_connection.commit()
        my_connection.close()
    def read_db(self,nombre,correo,contraseña,nombre1,correo1,contraseña1,window3,window1):
        global nnombre
        global ccorreo
        global ccontraseña
        senal=1
        my_connection = self.open_connection()
        cursor = my_connection.cursor()
        query = "SELECT * FROM TBL_USUARIOS "
        cursor.execute(query)  
        señal="señal"
        for fila in cursor:
            nombre = fila[1]  
            correo = fila[2]
            contraseña = fila[3]
            
          
            if nombre==nombre1 and correo==correo1 and contraseña1==contraseña:
                    senal=1
                    nnombre=nombre
                    ccorreo=correo
                    ccontraseña=contraseña            
                    print("correcto")
                    señal="señal"
                    window3.destroy()  
                    window1.destroy()
                    import PantallaTienda
    
            else:
                print("incorrecto")
            
                senal=2
        
        return senal
      
        
    def insert_producto(self,Descripcion,Precio,Id_categoria):
            my_connection = self.open_connection()
            cursor = my_connection.cursor()
            query = "INSERT INTO tbl_productos(Descripcion,Precio,Id_categoria) VALUES (%s,%s,%s)"
            data = (Descripcion,Precio,Id_categoria)
            cursor.execute(query, data)
            my_connection.commit()
            my_connection.close()
    def perfil(usuario,frame_app):
      
        a=nnombre
        b=ccorreo
        c=ccontraseña
        usuario = Label(frame_app, text=a, font=("Arial", 15), bg="white", fg="black", width="0",
                        height="0").grid(row=0, column=1,pady=10)
        Etiqueta3 = Label(frame_app, text=b, font=("Arial", 15), bg="white", fg="black", width="0",
                        height="0").grid(row=2, column=1,pady=10)
        Etiqueta5 = Label(frame_app, text=c, font=("Arial", 15), bg="white", fg="black", width="0",
                        height="0").grid(row=4, column=1,pady=10)
       
       
      