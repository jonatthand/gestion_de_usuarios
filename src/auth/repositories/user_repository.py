



class UserRepository:
    def __init__(self):
        self._users = []  # Simula una base de datos en memoria

    def get_by_email(self, email: str): #Busca un usuario por su correo electrónico
        for user in self._users: #Itera sobre la lista de usuarios
            if user["email"] == email: #Si el correo electrónico coincide
                return user 
        return None #Si no se encuentra el usuario, retorna None
    
    def create(self, email: str, password: str): #Crea un nuevo usuario
        user = { 
            "email": email,
            "password": password
        } #Agrega el nuevo usuario a la "base de datos"
        self._users.append(user) #agrega el usuario a la lista
        return user #Retorna el usuario creado