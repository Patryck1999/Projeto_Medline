# Projeto_Medline

O projeto medline é uma plataforma que foi desenvolvido pensando em dois publicos, o primeiro são os medicos com o meio de facilitar a oferecer seus serviços pela plataforma, já que muitas clinicas possuem muitos medicos ociosos esperando por um paciente, com este serviço na internet concerteza muitas pessoas se interessariam e por isso o nosso segundo publico que são os pacientes entram. Vimos que a um grande numero de pessoas que não conseguem encontrar um medico de custo baixo e acaba acontecendo de não ter muitas opções, agora com essa plataforma ele encontrara diversos medicos de diversas especialidades podendo escolher o de menor custo pra ele, portanto essa plataforma é uma medida para pessoas de baixa renda e medicos ociosos com disponibilidade de seus serviços.

Instruções basicas para rodar o projeto:

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


## Modelagem de Dados
Estrutura do projeto:
![Modelagem](https://github.com/Patryck1999/Projeto_Medline/blob/master/medline.png)
