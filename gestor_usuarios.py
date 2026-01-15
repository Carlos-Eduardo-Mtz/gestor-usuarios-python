class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.tipo = "Normal"

    def mostrar(self):
        print (f"Nombre: {self.nombre}")
        print (f"Email: {self.email}")
        print (f"Tipo De Usuario: {self.tipo}")

class Administrador(Usuario):
    def __init__(self, nombre, email, nivel=None):
        super().__init__(nombre, email)
        self.tipo = "Administrador"

        if nivel:
            self.nivel = nivel
        else:
            nivel = input("Ingrese el nivel del administrador (root / admin): ").lower()
            if nivel == "root" or nivel == "admin":
                self.nivel = nivel
            else:
                self.nivel = "admin"
                print("Nivel Invalido, asignado como admin")

    def mostrar(self):
        super().mostrar()
        print (f"Nivel: {self.nivel}")

class Gestor_Usuarios:
    def __init__(self):
        self.usuarios = []

    def email_valido(self, email):
        if email.count("@") != 1:
            return False

        if "." not in email:
            return False

        if email.startswith("@") or email.endswith("@"):
            return False

        if email.startswith(".") or email.endswith("."):
            return False

        arroba_pos = email.index("@")
        punto_pos = email.rindex(".")

        if punto_pos < arroba_pos:
            return False

        return True


    def agregar_usuario(self):
        nombre = input("Ingrese su Nombre: ")
        while True:
            email = input("Ingrese su Email: ")
            if self.email_valido(email):
                break
            else:
                print ("Email Invalido, Intentalo de nuevo")

        usuario = input("Ingrese el tipo de usuario (normal / administrador): ").lower()
        if usuario == "normal":
            usuario = Usuario(nombre, email)
            self.usuarios.append(usuario)
        
        elif usuario == "administrador":
            usuario = Administrador(nombre, email)
            self.usuarios.append(usuario)

        else:
            print("Tipo de Usuario no Valido")

    def mostrar_usuarios(self):
        if not self.usuarios:
            print("No hay usuarios registrados")
            return

        for i, usuario in enumerate(self.usuarios, start=1):
            print(f"\nUsuario #{i}")
            usuario.mostrar()
            print("-" * 30)

    def eliminar_usuarios(self):
        if not self.usuarios:
            print ("No hay usuarios para eliminar ")
            return
        
        print ("\nUsuarios Registrados: ")
        for i, usuario in enumerate(self.usuarios, start=1):
            print (f"{i}. {usuario.nombre} ({usuario.tipo})")

        try:
            num = int(input("Ingrese el numero del usuario a eliminar: "))

            if 1 <= num <= len(self.usuarios):
                eliminar = self.usuarios.pop(num - 1)
                print (f"Usuario ({eliminar.nombre}) Eliminado correctamente")
            else:
                print ("Numero invalido")

        except ValueError:
            print ("Entrada invalida, ingrese solo numeros")

    def guardar_usuarios(self):
        with open("usuarios.txt", "w", encoding="utf-8") as archivo:
            for usuario in self.usuarios:
                if isinstance(usuario, Administrador):
                    linea = f"{usuario.nombre}|{usuario.email}|administrador|{usuario.nivel}\n"
                else:
                    linea = f"{usuario.nombre}|{usuario.email}|normal\n"
                archivo.write(linea)

    def cargar_usuarios(self):
        try:
            with open("usuarios.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    datos = linea.strip().split("|")

                    if datos[2] == "normal":
                        usuario = Usuario(datos[0], datos[1])

                    elif datos[2] == "administrador":
                        usuario = Administrador(datos[0], datos[1], datos[3])

                    self.usuarios.append(usuario)
        except FileNotFoundError:
            pass


gestor = Gestor_Usuarios()
gestor.cargar_usuarios()
while True:
    print("""
--- MENÚ ---
1. Agregar Usuario
2. Mostrar Usuarios
3. Eliminar Usuarios
4. Salir
""")

    try:
        opcion = int(input("Elige una opción: "))

        if opcion == 1:
            gestor.agregar_usuario()

        elif opcion == 2:
            gestor.mostrar_usuarios()

        elif opcion == 3:
            gestor.eliminar_usuarios()

        elif opcion == 4:
            gestor.guardar_usuarios()
            print ("Usuarios Guardados. El programa a finalizado correctamente")
            break

        else:
            print("Opción no válida")

    except ValueError:
        print("Entrada inválida, solo números")