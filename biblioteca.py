class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def __str__(self):
        return f"Nome: {self.nome}, Email: {self.email}"


class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = True

    def __str__(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"'{self.titulo}' por {self.autor} ({self.ano}) - {status}"


class Biblioteca:
    def __init__(self):
        self.usuarios = []
        self.catalogo = []
        self.emprestimos = {}

    def cadastrar_usuario(self, nome, email):
        usuario = Usuario(nome, email)
        self.usuarios.append(usuario)
        print(f"Usuário '{nome}' cadastrado com sucesso!")

    def cadastrar_livro(self, titulo, autor, ano):
        livro = Livro(titulo, autor, ano)
        self.catalogo.append(livro)
        print(f"Livro '{titulo}' cadastrado com sucesso!")

    def listar_usuarios(self):
        if not self.usuarios:
            print("Nenhum usuário cadastrado.")
        else:
            print("\nUsuários cadastrados:")
            for usuario in self.usuarios:
                print(usuario)

    def listar_livros(self):
        if not self.catalogo:
            print("Nenhum livro no catálogo.")
        else:
            print("\nCatálogo de livros:")
            for livro in self.catalogo:
                print(livro)

    def pegar_livro_emprestado(self, email_usuario, titulo_livro):
        usuario = next((u for u in self.usuarios if u.email == email_usuario), None)
        if not usuario:
            print(f"Usuário com email '{email_usuario}' não encontrado.")
            return

        livro = next((l for l in self.catalogo if l.titulo == titulo_livro and l.disponivel), None)
        if not livro:
            print(f"Livro '{titulo_livro}' não encontrado ou não disponível.")
            return

        livro.disponivel = False
        self.emprestimos[email_usuario] = self.emprestimos.get(email_usuario, []) + [livro]
        print(f"Usuário '{usuario.nome}' pegou o livro '{titulo_livro}' emprestado com sucesso!")

    def devolver_livro(self, email_usuario, titulo_livro):
        usuario = next((u for u in self.usuarios if u.email == email_usuario), None)
        if not usuario:
            print(f"Usuário com email '{email_usuario}' não encontrado.")
            return

        livros_emprestados = self.emprestimos.get(email_usuario, [])
        livro = next((l for l in livros_emprestados if l.titulo == titulo_livro), None)
        if not livro:
            print(f"O usuário '{usuario.nome}' não possui o livro '{titulo_livro}' emprestado.")
            return

        livro.disponivel = True
        livros_emprestados.remove(livro)
        if not livros_emprestados:
            del self.emprestimos[email_usuario]

        print(f"Livro '{titulo_livro}' devolvido com sucesso!")

    def listar_emprestimos(self):
        if not self.emprestimos:
            print("Nenhum empréstimo registrado.")
        else:
            print("\nEmpréstimos registrados:")
            for email, livros in self.emprestimos.items():
                usuario = next(u for u in self.usuarios if u.email == email)
                print(f"\nUsuário: {usuario.nome}")
                for livro in livros:
                    print(f"  - {livro.titulo}")


def menu():
    biblioteca = Biblioteca()

    while True:
        print("\n=== Menu da Biblioteca ===")
        print("1. Cadastrar usuário")
        print("2. Cadastrar livro")
        print("3. Listar usuários")
        print("4. Listar livros")
        print("5. Pegar livro emprestado")
        print("6. Devolver livro")
        print("7. Listar empréstimos")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do usuário: ")
            email = input("Email do usuário: ")
            biblioteca.cadastrar_usuario(nome, email)

        elif opcao == "2":
            titulo = input("Título do livro: ")
            autor = input("Autor do livro: ")
            ano = input("Ano de publicação: ")
            biblioteca.cadastrar_livro(titulo, autor, ano)

        elif opcao == "3":
            biblioteca.listar_usuarios()

        elif opcao == "4":
            biblioteca.listar_livros()

        elif opcao == "5":
            email = input("Email do usuário: ")
            titulo = input("Título do livro: ")
            biblioteca.pegar_livro_emprestado(email, titulo)

        elif opcao == "6":
            email = input("Email do usuário: ")
            titulo = input("Título do livro: ")
            biblioteca.devolver_livro(email, titulo)

        elif opcao == "7":
            biblioteca.listar_emprestimos()

        elif opcao == "0":
            print("Saindo do sistema. Até logo!")
            break

        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    menu()
