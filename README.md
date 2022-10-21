# epub-redactor (epubctor)

## Содержание
- **Введение**
- **Принцип работы**
- **Наработки**

картиночка

---------------------------------------------
## Введение
**Epubctor** - программа, позволяющая редактировать электронные книги в формате **epub**, а именно - вставлять внутрь их текста рекламные ссылки. Процесс автономен, необходимо указать только ссылку, ее текст и папку с книгами.

картиночка

-------------------------------
## Принцип работы
Программа написана на языке **Python**, с использованием сторонних библиотек и интерфейсом оформленным через **PyQT5**. 

Библиотеки:  
* [ZipFile](https://docs.python.org/3/library/zipfile.html)
* [bs4](https://www.crummy.com/software/BeautifulSoup/bs4/doc.ru/bs4ru.html)
* [ebooklib](http://docs.sourcefabric.org/projects/ebooklib/en/latest/)
* [PyQT5](https://doc.qt.io/qtforpython/)  
* [os](https://pyneng.readthedocs.io/ru/latest/book/12_useful_modules/os.html)

На вход программа получает папку с архивами формата **.epub**, ссылку и ее текст. Затем начинается последовательная обработка каждого архива по следующему принципу:
> 1. Разархировать полученный архив
> 2. Получить названия всех **.html** файлов внутри
> 3. Преобразовать формат ссылки в соответствие с форматом текста внутри
> 4. Поместить ссылки
> 5. Сохранить изменения ~~заменить старые файлы на преобразованные~~
> 6. Заархивировать обратно и сменить разрешение на **.epub**

На данный момент реализованы пункты 1-3 ~~:((((~~

Разархивация:
```python
import zipfile
         
zip = zipfile.ZipFile('file')
zip.extractall('programm_directory\name_of_file\')
 
zip.close()
```

Получение имен файлов **.html**:
```python
import ebooklib
book = epub.read_epub('file')
items = list(book.get_items_of_type(ebooklib.ITEM_DOCUMENT))
names = []
for el in items:
    names.append(el.get_name())
```
> Следует понимать, что ``book = epub.read_epub('file')`` получает в качестве аргумента не папку с разархивированными файлами, а изначальный архив в формате **.epub**

Форматирование ссылки:
```python
def true_tag(texts):
    truth = None
    for el in texts:
        if len(str(el.string).split()) > 15 and not truth:
            truth = el
    if truth:
        a = str([child for child in truth.descendants][-1])
        truth = bs4.BeautifulSoup(str(truth), 'html.parser')
        link_void = bs4.BeautifulSoup('<a href="https://ya.ru">ЗАЛЕТАЙ И ПОЛУЧАЙ СУПЕРБОНУС</a>', 'html.parser')
        truth.find(text=a).replace_with(link_void)
        link = truth
        return link
    return None
```
> Приведена только функция, ибо способ получения контента страницы был изменен, но пока только на бумаге. В данном коде приведен пример форматирования ссылки заданной программно, естественно это не конечный результат

пункты остальные  
картинки  
видео-пример работы программы  
пикча в конце
