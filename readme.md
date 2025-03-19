Como rodar
1. instalar python 3.12.9
2. rode o comendo `make install_dependencies`
3. rode as 3 apps:
  3.a. `make init_app_integration`
  3.b. `make init_app_register`
  3.c. `make init_app_validation`


Sistema de Cadastro e Consulta de Usuários

Duas aplicações compartilhando um banco SQLite

Aplicação app_register (Cadastro de Usuários): Permite inserir novos usuários no banco.
Aplicação app_view (Consulta de Usuários): Permite visualizar e buscar usuários cadastrados.

Tecnologias:
Python + SQLite
Flask para criar APIs ou interface simples (opcional)

Fluxo
A aplicação app_register recebe os dados do usuário (nome, e-mail) e os insere no banco.
A aplicação app_view permite buscar usuários já cadastrados.
