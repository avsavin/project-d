from flask import Flask, render_template, request, url_for, flash, redirect

from flask_wtf import FlaskForm
from wtforms import StringField, FormField, FieldList, IntegerField, Form
from wtforms.validators import InputRequired, Length

import pickle
import numpy as np
import pandas as pd

# import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '137b69af4e80d8c4141ab1b9d80bff1f839f98935bc36c04'

# прочитаем pipeline модели
with open('app/models/XGBRegressor-pipe.pkl', 'rb') as f:
        pipe = pickle.load(f) 

def estimate (rows,dtypes):
    '''
    params: пары  {наименование:значение} в виде списка словарей
    output: предсказание
    '''
    # преобразуем пары - имя:значения в одну строку 
    vector = pd.DataFrame({row['f_name']:row['f_value'] for row in rows}, index=[0])
    # установим тип данных необходимый для pipeline
    vector = vector.astype(dtype=dtypes)
    
    result = pipe.predict(vector)
    return result[0]

# так как мы использовали некоторые дополнительные атрибуты, для вычисления которых
# требуются внешние источники (google maps, статистические файлы и тп),
# воспользуемся по умолчанию предобработанными исходными данными - 
# читаем предобработанные данные 

with open('app/data/df.pkl', 'rb') as f:
    df = pickle.load(f) # deserialize using load()

# атрибуты для использования в модели
new_columns = [col for col in  df.columns if col.startswith('new_')]
new_columns.remove('new_target')

# запомним типы данных каждого атрибута для обратного преобразования
dtypes= {column:df[column].dtype for column in new_columns}
    
#определим форму для вывода/ввода данных
class Entry(FlaskForm):
    f_name = IntegerField('Name')
    f_value = IntegerField('Value')
class Table(FlaskForm):
    rows = FieldList(FormField(Entry), min_entries=0)



@app.route('/', methods=('GET', 'POST'))
def index():
    global actual_target
    # инициализируем форму
    form = Table(form=Entry)

    if request.method == 'POST':
        if request.form['action'] == 'Estimate':
            # обрабатываем ответ из темплета
            rows= [dict(f_name=column, f_value=request.form.get(column)) for column in new_columns]    
            estimated_target = estimate(rows,dtypes)
        if request.form['action'] == 'Restart':
            # инициализируем новой случайной записью
            df_sample = df.sample(1)
            # развернем строку в два столбца = наименование атрибута и значение
            rows= [dict(f_name=column, f_value=df_sample[column].values[0]) for column in new_columns]
            # инициализируем переменную для предсказания
            estimated_target = ''    
            actual_target = df_sample['new_target'].values[0]
    else:
        # инициализируем значения по умолчанию
        df_sample = df.sample(1)
        # инициализируем переменную для предсказания
        estimated_target = ''
        actual_target =   df_sample['new_target'].values[0]
        # развернем строку в два столбца = наименование атрибута и значение
        rows= [dict(f_name=column, f_value=df_sample[column].values[0]) for column in new_columns]
     

    # выводим форму на экран
    return render_template('index.html', 
                           form=form , rows = rows, 
                           actual_target =actual_target,
                           estimated_target = estimated_target)
  
if __name__ == '__main__':
   app.run(
       host='127.0.0.1'
       ,port=8000
#       ,debug=True
       )

