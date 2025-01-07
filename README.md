# ProjetoLivre01

# Sistema de Gerenciamento de Biblioteca

Este projeto consiste em um sistema simples de gerenciamento de biblioteca, utilizando o framework **Flask**. O sistema permite cadastrar usuários e livros, listar usuários e livros, emprestar livros e visualizar os empréstimos registrados.

## Funcionalidades

1. **Cadastrar Usuário**:
   - Cadastro de usuários com nome e e-mail.
   
2. **Cadastrar Livro**:
   - Cadastro de livros com título, autor e ano de publicação.
   
3. **Listar Usuários**:
   - Visualizar todos os usuários cadastrados.
   
4. **Listar Livros**:
   - Visualizar todos os livros cadastrados no catálogo, com o status (disponível ou emprestado).
   
5. **Emprestar Livro**:
   - Emprestar um livro a um usuário, alterando seu status de "disponível" para "emprestado".
   
6. **Listar Empréstimos**:
   - Visualizar todos os empréstimos registrados, com os livros emprestados para cada usuário.

## Pré-requisitos

Antes de rodar a aplicação, certifique-se de ter o Python instalado na sua máquina. O Flask também é necessário. Você pode instalar o Flask com o seguinte comando:

Estrutura do projeto
```bash
pip install Flask

biblioteca
    /static
        style.css         
    /templates
        index.html        
        cadastrar_usuario.html
        cadastrar_livro.html 
        listar_usuarios.html 
        listar_livros.html  
        emprestar_livro.html  
        listar_emprestimos.html 
    app.py                
