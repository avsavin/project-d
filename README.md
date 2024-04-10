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

<p align="center"> Разрабатываем модель, которая позволила бы агентству
недвижимости обойти конкурентов по скорости и качеству совершения
сделок
    <br> 
</p>

## 📝 Содержание

- [Введение](#about)
- [Начало работы и запуск сервисов](#getting_started)
- [Deployment](#deployment)
- [Usage](#usage)
- [Built Using](#built_using)
- [TODO](../TODO.md)
- [Contributing](../CONTRIBUTING.md)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 Введение <a name = "about"></a>
В проекте решались следующие бизнес задачи:

- разработать модель, которая позволила бы агентству получить конкуретное преимущество: скорость и точность прогноза цены объекта позволяет быстрее закрыть сделку по продаже объекта;
- дополнительный эффект может быть связан с уменьшением загрузки сотрудников рутинными вычислениями

Для достижения бизнес-целей были решены следующие технические задачи:

- проанализированы данные, обработаны пропуски, дубликаты, выбросы, ошибки ввода.
- сгенерированы допольнительные признаки
- определены наиболее значимые факторы
- опробованы несколько моделей прогнозирования, выполнен выбор лучшей модели с оптимальными параметрами 
- модель выведена в эксплуатацию в качестве веб-сервиса, выдающего прогноз цены при поступлении данных о новом объекте в качестве параметров


## 🏁 Начало работы и запуск сервисов <a name = "getting_started"></a>

Для запуска веб-сервиса необходимо загрузить контейнер из docker hub
```
docker pull anatolysavin/project-d
```
и запустить его на локальной машине при помощи команды
```
docker run -p 127.0.0.1:8000:8000 anatolysavin/project-d
```
Веб сервис должен быть доступен по адресу http://localhost:8000

Подготовка данных и обучение модели выполненые в двух jupyter notebook:
real_estate_price_part1.ipynb
real_estate_price_part2.ipynb

### Необходимая подготовка

Для воспроизведения кода Вам понадобится развернуть на локальном компьютере структуру каталогов из следующих архивных файлов и загрузить вспомогательные данные:
почтовые индексам - simplemaps_uszips_basicv1.84.zip, 
координаты столиц штатов - states.csv, 
файл управления статистики США c данными о плотности домохозяйств и среднем доходе - income-2022.zip. 

Также вам понадобиться доступ к интерфейсу google maps. Временный ключ для доступа к интерфейсу включен в ноутбук (это плохая практика, так как открывает доступ в том числе к платным сервисам). Если ключ не работает, пожалуйста, обратитесь ко мне напрямую или получите ключ самостоятельно.

Файл requirements.txt для ноутбуков находится в корневой директории проекта.<br>
Файл requirements.txt для веб-сервиса надохится в директории web.<br>

К сожалению, стандартная установка pip requirements.txt для нормальной работы ноутбуков не всегда может разрешить некоторые противоречивые требования в версиях пакетов (как это, например, случилось у нас на macbook с процессором M2). В этом случае может потребоваться установка пакетов при помощи conda --channel=conda-forge.


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

<img width="368" alt="Screenshot" src="https://github.com/avsavin/project-d/assets/20927398/fd347486-c5bf-4d8d-a696-28f31cbd66e5">

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
