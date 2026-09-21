from werkzeug.security import check_password_hash, generate_password_hash

class UserModel:
    # Usuários armazenados em memória (lista Python)
    USERS = [
        {
            "id": 1,
            "name": "Administrador",
            "email": "admin@gmail.com",
            "password": generate_password_hash("123")
        },
        {
            "id": 2,
            "name": "Isabela Gomes",
            "email": "user@gmail.com",
            "password": generate_password_hash("123")
        }
    ]

    @staticmethod
    def get_by_email(email):
        for user in UserModel.USERS:
            if user['email'] == email:
                return user
        return None

    @staticmethod
    def authenticate(email, password):
        user = UserModel.get_by_email(email)
        if user and check_password_hash(user['password'], password):
            return user
        return None
    @staticmethod
    def create(name, email, password):
        # Verifica se o e-mail já existe
        if UserModel.get_by_email(email):
            return False, "Este e-mail já está cadastrado!"

        # Cria o novo usuário com senha criptografada
        new_user = {
            "id": len(UserModel.USERS) + 1,
            "name": name,
            "email": email,
            "password": generate_password_hash(password)
        }
        
        UserModel.USERS.append(new_user)
        return True, "Cadastro realizado com sucesso!"