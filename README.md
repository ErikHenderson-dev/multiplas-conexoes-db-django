# Utilizando o arquivo env para configurar variaveis de ambiente e configurando banco mysql

1º - Para que o python use o arquivo .env, devemos instalar o python-decouple no projeto.
    
    pip install python-decouple

2º - Devemos realizar a importação do config do python-decouple no arquivo de settings.
    
    from decouple import config

3º - Criar um arquivo .env na raiz do projeto.
    
    backend/.env

4º - Após criar o arquivo .env devemos incluir as variavéis de ambiente que gostariamos de usar.
    
    SECRET_KEY=django-insecure-h72c%6i(60$-22v=&(yez57-1lry2kvo30vb(hkh0skkbdgte4
    DEBUG=True

5º - Configurar o settings.
    
    SECRET_KEY = config('SECRET_KEY')
    DEBUG = config('DEBUG')

6º - Para utilizar o mysql devemos instalar o mysql cliente no nosso projeto.
    
    pip install mysqlclient

7º - Alterar o settings e infomar as configurações do banco.
    
    DATABASES = {
        'banco_1': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'banco_1',
            'USER': 'root',
            'PASSWORD': '',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }


