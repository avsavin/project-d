<p align="center">
  <a href="https://github.com/avsavin/project-d" rel="noopener">
 <img width=200px height=200px src="buy-6971881_1280.jpg" alt="Project logo"></a>
</p>

<h3 align="center">Прогнозирование стоимости жилья для агенства недвижимости</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)](https://github.com/avsavin/project-d/releases)
[![GitHub Issues](https://img.shields.io/github/issues/kylelobo/The-Documentation-Compendium.svg)](https://github.com/avsavin/project-d/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/avsavin/project-d/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/avsavin/project-d/blob/main/LICENSE)

</div>

---

<p align="center"> Модель, которая позволила бы агентству
недвижимости обойти конкурентов по скорости и качеству совершения
сделок
    <br> 
</p>

## 📝 Содержание

- [About](#about)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
- [Usage](#usage)
- [Built Using](#built_using)
- [TODO](../TODO.md)
- [Contributing](../CONTRIBUTING.md)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>
В проекте решались следующие бизнес задачи:

- разработать модель, которая позволила бы агентству получить конкуретное преимущество: скорость и точность прогноза цены объекта позволяет быстрее закрыть сделку по продаже объекта;
- дополнительный эффект может быть связан с уменьшением загрузки сотрудников рутинными вычислениями

Для достижения бизнес-целий были решены следующие технические задачи:

- проанализировать данные, найти и обработать пропуски, дубликаты, выбросы, ошибки ввода.
- при необходимости сгенерировать допольнительные признаки
- определить наиболее значимые факторы
- опробовать несколько моделей прогнозирования, выполнить выбор лучшей модели с оптимальными параметрами моделей
- вывезти модель в эксплуатацию в качестве веб-сервиса, выдающего прогноз цены при поступлении данных о новом объекте в качестве параметров


## 🏁 Getting Started <a name = "getting_started"></a>

Для запуска веб-сервиса необходимо загрузить контейнер из docker hub
```
docker pull anatolysavin/project-d <br>
```
и запустить его на локальной машине при помощи команды
```
docker run -p 127.0.0.1:8000:8000 project-d<br>
```
Веб сервис должен быть доступен по адресу http://localhost:8000

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them.

```
Give examples
```

### Installing

A step by step series of examples that tell you how to get a development env running.

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo.

## 🔧 Running the tests <a name = "tests"></a>

Explain how to run the automated tests for this system.

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## 🎈 Usage <a name="usage"></a>

Add notes about how to use the system.

## 🚀 Deployment <a name = "deployment"></a>

Add additional notes about how to deploy this on a live system.

## ⛏️ Built Using <a name = "built_using"></a>

- [MongoDB](https://www.mongodb.com/) - Database
- [Express](https://expressjs.com/) - Server Framework
- [VueJs](https://vuejs.org/) - Web Framework
- [NodeJs](https://nodejs.org/en/) - Server Environment

## ✍️ Authors <a name = "authors"></a>

- [@kylelobo](https://github.com/kylelobo) - Idea & Initial work

See also the list of [contributors](https://github.com/kylelobo/The-Documentation-Compendium/contributors) who participated in this project.

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- Hat tip to anyone whose code was used
- Inspiration
- References
