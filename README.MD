# Teste Dev II Python

## Instalação
As dependências estão listadas no arquivo requirements.txt
```
pip install -r requirements.txt
```
O projeto necessita de um arquivo de configuração ( config.yml ) para as chaves de configuração e acessos necessários. Um exemplo das configurações necessárias está em config.yml.dist .

## Execução
Para execução é necessário ter instalado as dependências do projeto e executar o comando de start do flask: 
```
flask run 
```

## Endpoints
Com exeção do endpoint `/auth` todos os outros são autenticados, sendo necessário enviar o access token no cabeçalho da requisição:
```JSON
```

* ### /auth
    Rota POST utilizada para fazer a autenticação dos usuários. Retorna o access token contento o token JWT em caso de sucesso. Aceita um objeto JSON no seguinte formato, sendo o username o mesmo email do usuário:
    ```JSON
    {
        "username":"sergio02195@gmail.com",
        "password":"test-password"
    }
    ``` 
* ### /dealer
    Rota no método POST utilizada para cadastrar os revendedores. Recebe o seguinte objeto retornando o HTTP Code 201 em caso de sucesso: 
    ```JSON
    {
        "email": "sergio02195@gmail.com",
        "password": "test-password",
        "cpf": 15350946056,
        "full_name": "Sérgio Coelho Bessa da Costa"
    }
    ``` 
* ### /order
    Rota no método GET responsável por listar os pedidos aceitando o filtro de cpf e os cabeçalhos `X-page` para a páginação atual e `X-per-page` para quantidade de itens por página.
* ### /order
    Rota no método POST responsável por registrar o pedido, aceita o seguinte objeto:
    ```JSON
    {
        "code": 1222334332345,
        "date": "2021-01-29T05:31:03.775Z",
        "cpf": 15350946056,
        "value": 1100
    }
    ```
* ### /cashback
    Rota no método GET responsável por trazer os dados disponibilizados pela API Externa. Seu parâmetro obrigatório é o cpf do revendedor.

## Justificativas
O banco de dados utilizado foi o MongoDB para armazenar as listagens de usuários e pedidos cadastrados. Foi aplicado DDD na arquitetura de desenvolvimento, sendo assim os serviços e utilitários foram feitos com o intuito de serem isolados por assunto. 
