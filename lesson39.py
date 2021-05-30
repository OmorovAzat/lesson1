                                                                        #Класс парсинга
from Parser_clas import Parser

parser = Parser('https://www.ua-football.com/sport', 'news.txt')
parser.run()
# print(parser.raw_html)
# print(parser.html)
# print(parser.results)