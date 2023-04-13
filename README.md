# Blog-Django
Blog dinâmico criado com Django e Bootstrap, contendo roles e permissions

[![NPM](https://img.shields.io/npm/l/react)](https://github.com/afonsoliveiraa/Blog-Django/blob/main/LICENSE) 

## Projeto
https://web-production-bf36.up.railway.app/

# Sobre o projeto
O Django Blog é uma aplicação web full stack desenvolvida para atuar como um blog dinâmico com níveis de acesso baseados em três roles: Dono, Staff e Usuário. O Dono tem permissão para criar, editar e excluir qualquer post, bem como tornar um usuário membro da equipe de staff. A equipe de Staff tem permissão para criar, editar e excluir seus próprios posts. Enquanto isso, os usuários podem apenas comentar nos posts.

Quando um usuário se cadastra pela rota normal da aplicação, é criado um perfil de "Usuário". Somente o Dono (user: admin / senha: admin) pode conceder a ele a posição de "Staff". Dependendo do papel do usuário, as opções do menu se alteram. Além disso, o menu oferece a possibilidade de acessar os posts divididos por tags e na lateral existe os filtros por data de criação, os "archives".



## Layout web
![Web 1](https://github.com/afonsoliveiraa/Blog-Django/blob/main/static/assets/prints.jpg) 

# Tecnologias utilizadas
## Back end
- Django
## Front end
- HTML / CSS / JS
- Bootstrap

# Como copiar o projeto

```bash
# clonar repositório
git clone https://github.com/afonsoliveiraa/Blog-Django.git

# Criar máquina virtual

# Ativar a máquina virtual 

# Rodar o projeto
python manage.py runserver
```

# Autor

Afonso Barros de Oliveira Filho

https://www.linkedin.com/in/afonso-oliveira-93816020a/
