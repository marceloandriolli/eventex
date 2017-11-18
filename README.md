# Eventex

Sistema de eventos encomendado pela Morena

## Como desenvolver?

1. Clone o repositóti
2. Crie um vritualenv com python 3.5
3. Ative o seu virtualenv
4. Instale as suas dependências
5. Configure a instancia com o .env
6. Execute os testes

``` console
git clone git@github.com:marceloandriolli/eventex.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
``` 

## Como fazer o deploy?

1. Crie um instância no Heroku
2. Envie as configurações para o Heroku
3. Defina uma SECRET_KEY segura para instância
4. Defina DEBUG=False
5. Configure o serviço  de email
6. Envie o código para o Heroku

``` console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# configura o email
git push heroku master --force
```