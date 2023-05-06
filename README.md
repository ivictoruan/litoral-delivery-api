📝 **README**

# API de Entregas e Inclusão Digital

Uma API REST desenvolvida em Django com Django Rest Framework (DRF) para servir dois apps: um serviço de entrega e outro inclusão digital de lojistas e empreendedores nas pequenas cidades do Maranhão.

## Funcionalidades
- [ ]Cadastro de usuários (clientes, lojistas e entregadores) 👥
- 
- [ ]Autenticação e autorização de usuários com token JWT 🔐
- 
- [ ]Cadastro e gerenciamento de pedidos de entrega 🚚
- 
- [ ]Cadastro e gerenciamento de produtos dos lojistas 🛍️
- 
- [ ]Cadastro e gerenciamento de lojas dos lojistas 🏪
- 
- [ ]Cadastro e gerenciamento de entregadores e suas rotas 🗺️
- 
- [ ]Controle de estoque dos produtos 📊
- 

## Tecnologias utilizadas
- Django 🐍
- Django Rest Framework 🌐
- PostgreSQL 🐘

## Instalação
1. Clone o repositório:
```
git clone https://github.com/ivictoruan/litoral-delivery-api
```

2. Crie e ative um ambiente virtual:
```
python -m venv env
```
```
source env/bin/activate
```

3. Instale as dependências do projeto:
```
pip install -r requirements.txt
```

4. Crie um banco de dados PostgreSQL e configure as variáveis de ambiente com as informações de acesso:
```
[Acesse a documentação para mais informações](https://www.postgresql.org/)
```

5. Execute as migrações para criar as tabelas do banco de dados:
```
python manage.py migrate
```

6. Crie um superusuário para acessar a área de administração:
```
python manage.py createsuperuser
```

7. Inicie o servidor:
```
python manage.py runserver
```

## Endpoints
- [ ]`/api/v1/users/`: endpoint para cadastro de usuários;
- 
- [ ]`/api/v1/token/`: endpoint para autenticação de usuários e geração de token JWT;
- 
- [ ]`/api/v1/orders/`: endpoint para cadastro e gerenciamento de pedidos de entrega;
- 
- [ ]`/api/v1/products/`: endpoint para cadastro e gerenciamento de produtos dos lojistas;
- 
- [ ]`/api/v1/stores/`: endpoint para cadastro e gerenciamento de lojas dos lojistas;
- 
- [ ]`/api/v1/drivers/`: endpoint para cadastro e gerenciamento de entregadores e suas rotas;
- 
- [ ]`/api/v1/stock/`: endpoint para controle de estoque dos produtos.
- 

## Licença
Este projeto está licenciado sob a Licença MIT. Consulte o arquivo [LICENSE](LICENSE) para obter mais informações.
<div align="center">

## Contato

[![Email](https://img.shields.io/badge/Email-victorruan135@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:victorruan135@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-ivictoruan-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ivictoruan)
[![GitHub](https://img.shields.io/badge/GitHub-ivictoruan-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ivictoruan)

</div>


