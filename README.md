[![LinkedIn][linkedin-shield]][linkedin-url]

<p align="center">
  <p align="center">
    <h1 align="center">To Do List App</h1>
    <p align="center">
      Um aplicativo web de lista de tarefas, criado utilizando Django Rest Framework e Vue.js<br/>
      <a href="https://todovuejs-lucasfranca.herokuapp.com/"><strong>https://todovuejs-lucasfranca.herokuapp.com/</strong></a>
    </p>
    <p align="center">
      <img src="https://gist.githubusercontent.com/lucasfrancaid/13f62a71b0ba106a0dd5c5f6ca2d9dff/raw/30f238a757d1e3b50896874ccdd55ae70aec1905/00_todo_start.png" alt="start" />
    </p>
  </p>
</p>

<br/>

<p align="center">
  <a href="#-tecnologias">💻 Tecnologias</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#%EF%B8%8F-sobre-o-projeto">🕵️ Sobre o projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-iniciando-o-projeto">🚀 Iniciando</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-como-contribuir">🆙 Como contribuir</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-contato">📬 Contate-me</a>
</p>


<br>


## 💻 Tecnologias
* [Django](https://www.djangoproject.com/)
* [Django Rest Framework](https://www.django-rest-framework.org/)
* [Vue.js](https://vuejs.org/)
* [Vuetify](https://vuetifyjs.com/)

<br>

## 🕵️ Sobre o projeto
To do, é um projeto criado com Django Rest Framework e Vue.js na intenção de aprender mais sobre essas duas tecnologias fantásticas. A partir de mais estudos irei atualizando o projeto para aplicandar as melhores práticas e fazer o melhor uso possível dessas tecnologias,

<br>

## 🚀 Iniciando o projeto
Para executar o projeto, é só seguir a lista de tarefas e executar os comandos de cada passo em um terminal:

<p align="center">
  <img src="https://gist.githubusercontent.com/lucasfrancaid/13f62a71b0ba106a0dd5c5f6ca2d9dff/raw/a885a30f10f26f87e37ea875cffd8d5c3df7cb9b/01_todo_gitclone.png" alt="step-1" />
</p>

```bash
$ git clone https://github.com/lucasfrancaid/Todo.git
```

<p align="center">
  <img src="https://gist.githubusercontent.com/lucasfrancaid/13f62a71b0ba106a0dd5c5f6ca2d9dff/raw/a885a30f10f26f87e37ea875cffd8d5c3df7cb9b/02_todo_venv.png" alt="step-2" />
</p>

```bash
$ cd Todo/backend
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
```

<p align="center">
  <img src="https://gist.githubusercontent.com/lucasfrancaid/13f62a71b0ba106a0dd5c5f6ca2d9dff/raw/a885a30f10f26f87e37ea875cffd8d5c3df7cb9b/03_todo_rundjango.png" alt="step-3" />
</p>

```bash
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```

<br>

Backend funcionando, agora abra um novo terminal para executar os comando para rodar o frontend, acesse a pasta *Todo/frontend* e execute os comandos do próximo passo:

<p align="center">
  <img src="https://gist.githubusercontent.com/lucasfrancaid/13f62a71b0ba106a0dd5c5f6ca2d9dff/raw/a885a30f10f26f87e37ea875cffd8d5c3df7cb9b/04_todo_runvue.png" alt="step-4" />
</p>

```bash
$ npm install
$ npm run serve
```

<br>

Após rodar os comandos, os apps Backend e Frontend estarão disponíveis nas seguintes URLs:
<br>
- <b>Back-end:</b> http://localhost:8000/api/task
- <b>Front-end:</b> http://localhost:8080/


*Obs: Além de utilizar o back-end pelo browser, você também pode consumir a API pelo postman:*

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/15c632cbe5d7bbab692f)

<br>

E por último..

<p align="center">
  <img src="https://gist.githubusercontent.com/lucasfrancaid/13f62a71b0ba106a0dd5c5f6ca2d9dff/raw/a885a30f10f26f87e37ea875cffd8d5c3df7cb9b/05_todo_end.png" alt="step-5" />
</p>

<br>

## 🆙 Como contribuir

- Faça um fork desse repositório;
- Crie uma branch com sua feature: $ git checkout -b nome-feature
- Faça o commit das alterações realizadas: $ git commit -m "feat: Minha nova feature"
- Faça push para a sua branch: $ git push origin minha-feature
- Depois que o merge da sua pull request for feito, você podera deletar a sua branch.

<br>

## 📬 Contato

<b>Lucas França</b> <br/>
Linkedin: https://www.linkedin.com/in/lucasfrancaid/

<br>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/lucasfrancaid
