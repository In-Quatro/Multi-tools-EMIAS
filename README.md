# Multi tools EMIAS
## Описание
Проект разработан для упрощения настройки принтеров через SSH под операционной системой Linux.
Утилита позволяет быстро собрать команды в буфер обмена для выполнения операций над принтером:
 - установка / удаление принтера
 - выставление по умолчанию
 - чистка очереди печати
 - печать тестовой станицы
 - перезагрузка ПК
 - переименование ПК
 - перезагрузка / сброс настроек принтера
 - настройка пути сканирования по SMB

![image](https://github.com/user-attachments/assets/f5f672de-b1fc-4035-ab9c-cb7067b9c649)
![image](https://github.com/In-Quatro/Multi-tools-EMIAS/assets/107935543/26c70082-fc26-4f08-b372-8e97c916e521)


### Установка

 1. Клонируйте репозиторий на свой компьютер
 2. Создайте и активируйте виртуальное окружение, установите зависимостей из файла  `requirements.txt`.
```
python -m venv venv
```
```
python -m pip install --upgrade pip
```
```
venv/Scripts/activate
```
```
pip install -r requirements.txt
```
Чтобы скомпилировать проект в формат `.exe` используйте команду в терминале. 
```
auto-py-to-exe
```
Запустится приложение, в котором можно выбрать интересующие настройки.
Для получения готового приложения используйте готовую команду в терминале
```
pyinstaller --noconfirm --onefile --windowed --icon "./ui/icons/logo.ico" --add-data "./ui;ui/"  "./multi tools emias.py"
```
Готовое приложение после компеляции будет находиться в корне проекта в папке `dist`.

### Технологии
 - Python 3.9
 - PyQt 5
 
### Автор
[Shubenkov Aleksey](https://github.com/In-Quatro)
