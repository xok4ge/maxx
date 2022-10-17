import ebooklib
import bs4
from ebooklib import epub
import time


book = epub.read_epub('heret.epub')
items = list(book.get_items_of_type(ebooklib.ITEM_DOCUMENT))


def index(search, tex):
    print(search)
    for el in tex:
        el = bs4.BeautifulSoup(str(el), 'html.parser')
        print([tag.attrs for tag in el.find_all()] == [search])
        if [tag.attrs for tag in el.find_all()] == [search] and len(el.string.split()) >= 15:
            print([tag.attrs for tag in el.find_all()])
            print(tex.index(el))
            print(el.string)
        time.sleep(1)


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

    # берем текст их полученной строки, меняем его на необходимый текст - получаем необходимую правильно стилизованную строку, остается расставить ее в нужные места


def chapter_to_str(chapter):
    soup = bs4.BeautifulSoup(chapter.get_content(), 'html.parser')
    texts = [bs4.BeautifulSoup(str(para), 'html.parser') for para in soup.find_all()]
    text = soup.find_all('html')
    text = str(text[0]).split('\n')
    text = '\n'.join(text)
    print(text)
    # print(text)
    link = true_tag(texts)
    if link:
        search = [tag.attrs for tag in link.find_all()][0]
        # index(search, texts)
#     x = text[0].p
#     c = []
#     for child in x.children:
#         if child != '\n':
#             c.append(child)
#     x.find(text=c[-1].string).replace_with('17')
#     print(x)
#     # print(x2)
# #     text = [para.get_text() for para in soup.find_all('p')]
# #     return ' '.join(text)
#
#
# texts = {}
# for c in items:
#     texts[c.get_name()] = chapter_to_str(c)
# t = texts[items[6].get_name()]
# print(t)
chapter_to_str(items[6])