[![LinkedIn][linkedin-shield]][linkedin-url]

<p align="center">
  <p align="center">
    <h1 align="center">To Do List App</h1>
    <p align="center">
      Um aplicativo web de lista de tarefas, criado utilizando Django Rest Framework e Vue.js<br/>
      <a href="https://todovuejs-lucasfranca.herokuapp.com/"><strong>https://todovuejs-lucasfranca.herokuapp.com/</strong></a>
    </p>
    <p align="center">
      <img src="https://gist.githubusercontent.com/lucasfrancaid/13f62a71b0ba106a0dd5c5f6ca2d9dff/raw/d1c6b58b79ca481cbb0578b0d248879143cf265c/00_todo_start.png" alt="start" />
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
Existem duas maneiras de executar o projeto, a maneira legal e a maneira chata.


### Usando Docker (É legal, um comando, produtividade.. e se não sabe usar docker tá na hora de aprender):
Para iniciar com Docker, tenha instalado em sua máquina o Docker e o Docker Compose. Tudo certinho? Então execute na pasta raíz do projeto:
```bash
sudo docker-compose up
```

Backend e Frontend disponíveis nas seguintes URLs:
<br>
- <b>Back-end:</b> http://localhost:8000/api/task
- <b>Front-end:</b> http://localhost:8080/

<br>

### Agora se você escolheu o método chato... siga os passos abaixo:
Para executar o projeto, é só seguir a lista de tarefas e executar os comandos de cada passo em um terminal:

<p align="center">
  <img src="https://gist.githubusercontent.com/lucasfrancaid/13f62a71b0ba106a0dd5c5f6ca2d9dff/raw/a885a30f10f26f87e37ea875cffd8d5c3df7cb9b/01_todo_gitclone.png" alt="step-1" />
</p>

```bash
$ git clone https://github.com/lucasfrancaid/todo.git
```

<p align="center">
  <img src="https://gist.githubusercontent.com/lucasfrancaid/13f62a71b0ba106a0dd5c5f6ca2d9dff/raw/a885a30f10f26f87e37ea875cffd8d5c3df7cb9b/02_todo_venv.png" alt="step-2" />
</p>

```bash
$ cd todo/backend
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
```

<p align="center">
  <img src="https://gist.githubusercontent.com/lucasfrancaid/13f62a71b0ba106a0dd5c5f6ca2d9dff/raw/a885a30f10f26f87e37ea875cffd8d5c3df7cb9b/03_todo_rundjango.png" alt="step-3" />
</p>

```bash
$ python manage.py migrate
$ python manage.py runserver
```

<br>

Backend funcionando, agora abra um novo terminal para executar os comando para rodar o frontend, acesse a pasta *todo/frontend* e execute os comandos do próximo passo:

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

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/ab48013b4c23ceb3666c)

<br>

E por último..

<p align="center">
  <img src="https://gist.githubusercontent.com/lucasfrancaid/13f62a71b0ba106a0dd5c5f6ca2d9dff/raw/a885a30f10f26f87e37ea875cffd8d5c3df7cb9b/05_todo_end.png" alt="step-5" />
</p>

<br>

## 🆙 Como contribuir

- Faça um fork desse repositório
- Crie uma branch com sua feature, para isso execute ```git checkout -b nome-feature```
- Desenvolva sua implementação, adicione seus commits e execute ```git push origin nome-feature```
- Abra um Pull Request explanando sua implementação

<br>

## 📬 Contato

<b>Lucas França</b> <br/>
https://lucasfrancaid.com.br/

<br>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/lucasfrancaid
