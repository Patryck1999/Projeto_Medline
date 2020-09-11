# Projeto_Medline

1 - Passo - *Criar VirtualEnv*

	- virtualenv nome_da_virtualenv
	
2 - Passo - *Ativar o virtual env,entrar na virtual env pelo bash*

	- . ./nome_da_virtualenv/Scripts/activate

3 - Passo - *Instalar as dependencias na raiz do projeto com requirements.txt*

  - pip install -r requirements.txt

4 - Passo - Fazer as migrações das tabelas

- python manage.py makemigrations

5 - Passo - Aplicar as migrações

- python manage.py migrate

6 - Passo - Criar um superusuario

- python manage.py createsuperuser

7 - passo - Executar o projeto

- python manage.py runserver
