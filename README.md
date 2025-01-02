<p align="center">
  <a href="https://github.com/avsavin/project-d" rel="noopener">
 <img width=200px height=200px src="buy-6971881_1280.jpg" alt="Project logo"></a>
</p>

<h3 align="center">Housing Price Prediction for Real Estate Agencies</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)](https://github.com/avsavin/project-d/releases)
[![GitHub Issues](https://img.shields.io/github/issues/kylelobo/The-Documentation-Compendium.svg)](https://github.com/avsavin/project-d/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/avsavin/project-d/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/avsavin/project-d/blob/main/LICENSE)

</div>

---

<p align="center"> Developing a model to help the real estate agency outperform competitors in both speed and quality of transactions.
    <br> 
</p>

## 📝 Table of Contents

- [Introduction](#about)
- [Getting Started and Running Services](#getting_started)
- [Testing](#testing)
- [Usage Instructions](#usage)


## 🧐 Introduction <a name="about"></a>
This project addresses the following business challenges:

- Develop a model that gives the agency a competitive edge: faster and more accurate price predictions help close deals quicker.
- Additional benefits include reducing staff workload by automating routine calculations.

To achieve these goals, the following technical tasks were completed:

- Data was analyzed, and missing values, duplicates, outliers, and input errors were processed.
- Additional features were generated.
- The most significant factors were identified.
- Multiple prediction models were tested, and the best one with optimal parameters was chosen.
- The model was deployed as a web service, providing price predictions based on new property data.


## 🏁 Getting Started and Running Services <a name="getting_started"></a>

To start the web service, pull the container from Docker Hub:
```
docker pull anatolysavin/project-d
```
and run it locally using the command:
```
docker run -p 127.0.0.1:8000:8000 anatolysavin/project-d
```
The web service should be available at http://localhost:8000.

Data preparation and model training were done in two Jupyter notebooks:
real_estate_price_part1.ipynb<br>
real_estate_price_part2.ipynb

### Prerequisites

To reproduce the code, set up the local directory structure using the following archived files and load the auxiliary data:<br>
- ZIP codes: simplemaps_uszips_basicv1.84.zip,<br>
- State capitals' coordinates: states.csv,<br>
- U.S. Census file with household density and average income data: income-2022.zip. 

You'll also need access to the Google Maps API. A temporary API key is included in the notebook (this is a bad practice as it grants access to paid services). If the key doesn’t work, please contact me directly or obtain your own API key.

The requirements.txt file for the notebooks is located in the root directory of the project.<br>
The requirements.txt file for the web service is located in the `web` directory.<br>

Unfortunately, standard `pip install -r requirements.txt` may not resolve conflicting package versions for notebooks (e.g., on MacBook with an M2 processor). In such cases, use `conda --channel=conda-forge` to install packages.


## 🔧 Testing <a name="testing"></a>

From the project's root directory, run the following command:
```
python test/test.py
```
If everything is working correctly, you will see the output:

Server Status: 200<br>
Calculated Value: 319832


## 🎈 Usage Instructions <a name="usage"></a>

Open port 8000 in any browser at the address of the running container. If running locally, access it at http://localhost:8000.

A parameter input form will be displayed in the browser window, pre-filled with random values from the test set. The `Estimated Price` field will be empty, while the `Actual Price` field will show the value from the training dataset corresponding to the displayed values.

<img width="368" alt="Screenshot" src="https://github.com/avsavin/project-d/assets/20927398/fd347486-c5bf-4d8d-a696-28f31cbd66e5">

To calculate the price, click the `Estimate` button. The `Estimated Price` field will display the calculated value. 

If you want to explore how parameters affect the system's assessment, enter your values in the respective input fields and click `Estimate` again. The system will recalculate and display the result in the `Estimated Price` field.

Clicking the `Restart` button will reset the form and randomly select a new record from the test set.

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
- [Тестирование](#testing)
- [Инструкция по использованию](#usage)


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
real_estate_price_part1.ipynb<br>
real_estate_price_part2.ipynb

### Необходимая подготовка

Для воспроизведения кода Вам понадобится развернуть на локальном компьютере структуру каталогов из следующих архивных файлов и загрузить вспомогательные данные:<>br
почтовые индексам - simplemaps_uszips_basicv1.84.zip,<br>
координаты столиц штатов - states.csv, <br>
файл управления статистики США c данными о плотности домохозяйств и среднем доходе - income-2022.zip. 

Также вам понадобиться доступ к интерфейсу google maps. Временный ключ для доступа к интерфейсу включен в ноутбук (это плохая практика, так как открывает доступ в том числе к платным ресурсам сервиса). Если ключ не работает, пожалуйста, обратитесь ко мне напрямую или получите ключ самостоятельно.

Файл requirements.txt для ноутбуков находится в корневой директории проекта.<br>
Файл requirements.txt для веб-сервиса надохится в директории web.<br>

К сожалению, стандартная установка pip requirements.txt для нормальной работы ноутбуков не всегда может разрешить некоторые противоречивые требования в версиях пакетов (как это, например, случилось у нас на macbook с процессором M2). В этом случае может потребоваться установка пакетов при помощи conda --channel=conda-forge.


## 🔧 Тестирование <a name = "testing"></a>

Находясь в корневой директории проекта выполните команду:
```
python test/test.py
```
В случае правильной работы вы получите ответ:

Статус сервера: 200<br>
Рассчитанное значение: 319832


## 🎈 Инструкция по использованию<a name="usage"></a>

В любом доступном браузере откройте порт 8000 по адресу запущенного контейнера. В случае запуска на локальной машине выполните запрос по адресу: http://localhost:8000

В окне браузера будет отображена форма ввода параметров заполненная случайными выбранными значениями из тестового набора. Значение поля Estimated Price будет пустым. В поле Actual Price будет отображаться значение из тренировочной выборки соответсвующее выведенным значениям.

<img width="368" alt="Screenshot" src="https://github.com/avsavin/project-d/assets/20927398/fd347486-c5bf-4d8d-a696-28f31cbd66e5">

Для получения результатов расчета нажмите кнопку Estimate. В поле Estimated Price будет показано рассчитанное значение. 

Если Вы хотите исследовать влияние параметров на результат оценки системой, введите Ваше значение в соответсвующее поле ввода и снова нажмите кнопку Estimate. Система выполнит расчет и отобразит его в поле Estimated Price. 

При нажатии кнопки Restart система перезапустит форму и выберет новую случайную запись из тестового набора. 
