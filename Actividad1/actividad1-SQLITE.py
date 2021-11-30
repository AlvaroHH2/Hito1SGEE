import sqlite3
import datetime
con = sqlite3.connect('basededatos.db')

def actividad():
    while True:



        print("========================")
        print("  BIENVENIDO AL GESTOR  ")
        print("========================")
        print("[1] Listar clientes     ")

        print("[2] Añadir cliente      ")
        print("[3] Modificar cliente   ")
        print("[4] Borrar cliente      ")
        print("[5] Salir               ")
        print("========================")

        option = input("> ")

        if option == '1':
            print("Listando los clientes...\n")

            def sql_fetch(con):

                cursorObj = con.cursor()

                cursorObj.execute('SELECT * FROM cliente')

                rows = cursorObj.fetchall()

                for row in rows:
                    print(row)
            sql_fetch(con)

        if option == '2':
            print("Añadiendo un cliente...\n")

            nombre = input("Nombre > ")

            apellidos = input("Apellidos > ")
            ciudad = input("ciudad > ")
            x = datetime.datetime.now()
            datos = (nombre, apellidos, ciudad,x)

            def sql_insert(con, entities):
                cursorObj = con.cursor()

                cursorObj.execute( 'INSERT INTO cliente(id, nombre, apellido, ciudad, fecha) VALUES(null, ?, ?, ?, ?)' , datos )

                con.commit()

            sql_insert(con, datos)

            print("Cliente añadido correctamente\n")


        if option == '3':
           cursorObj = con.cursor()
           id= input("¿ Qué id quieres cambiar ? > ")
           cursorObj.execute('SELECT * FROM cliente WHERE id='+id+';')

           rows = cursorObj.fetchall()

           for row in rows:
               print(row)


           def update(con):
               cursorObj = con.cursor()
               while True:

                print("[1] Modificar Nombre     ")

                print("[2] Modificar Apellido     ")

                print("[3] Modificar ciudad      ")
                print("[4] Salir      ")

                modificar=(input())
                if(modificar=='1'):
                    nombre = input("Nombre > ")
                    cursorObj.execute('UPDATE cliente SET nombre=?  WHERE id=?;',( nombre,id))
                    con.commit()
                elif(modificar=='2'):
                    apellidos=input("Apellidos > ")
                    cursorObj.execute('UPDATE cliente SET apellido =? WHERE id=? ;',(apellidos,id))
                    con.commit()

                elif(modificar=='3'):
                    ciudad=input("Ciudad >")
                    cursorObj.execute('UPDATE cliente SET WHERE ciudad= ? WHERE id=? ;',(ciudad,id))
                    con.commit()
                elif (modificar == '4'):
                    return False;




           update(con)

        if option == '4':
            cursorObj = con.cursor()
            cursorObj.execute('SELECT * FROM cliente ;')

            rows = cursorObj.fetchall()

            for row in rows:
                print(row)

            id = input("¿Que id quieres Borrar > ")


            cursorObj.execute('DELETE FROM cliente WHERE id='+id+';')
            con.commit()
            print("Borrando un cliente...\n")
            print("Cliente borrado correctamente\n")
        if option == '5':
            print("Saliendo...\n")
            return False
            break

        input("\nPresiona ENTER para continuar...")


actividad()

"""def sql_table(con):

    cursorObj = con.cursor()

    cursorObj.execute("CREATE TABLE cliente(id integer PRIMARY KEY AUTOINCREMENT, nombre text, apellido text, ciudad text,fecha text)")

    con.commit()

sql_table(con)

"""













