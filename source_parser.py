"""
Парсер плагина SPP

1/2 документ плагина
"""
import datetime
import logging
import time

from spp_document import SPP_document


class TESTParserCase1:
    """
    Класс парсера плагина SPP

    :warning Все необходимое для работы парсера должно находится внутри этого класса

    :_content_document: Это список объектов документа. При старте класса этот список должен обнулиться,
                        а затем по мере обработки источника - заполняться.


    """

    SOURCE_NAME = 'test-source-1'
    _content_document: list[SPP_document]

    def __init__(self, *args, **kwargs):
        """
        Конструктор класса парсера

        По умолчанию внего ничего не передается, но если требуется (например: driver селениума), то нужно будет
        заполнить конфигурацию
        """
        # Обнуление списка
        self._content_document = []

        # Логер должен подключаться так. Вся настройка лежит на платформе
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.debug(f"Parser class init completed")
        self.logger.info(f"Set source: {self.SOURCE_NAME}")
        ...

    def content(self) -> list[SPP_document]:
        """
        Главный метод парсера. Его будет вызывать платформа. Он вызывает метод _parse и возвращает список документов
        :return:
        :rtype:
        """
        self.logger.debug("Parse process start")
        self._parse()
        self.logger.debug("Parse process finished")
        return self._content_document

    def _parse(self):
        """
        Метод, занимающийся парсингом. Он добавляет в _content_document документы, которые получилось обработать
        :return:
        :rtype:
        """
        # HOST - это главная ссылка на источник, по которому будет "бегать" парсер
        self.logger.debug(F"Parser enter to {self.SOURCE_NAME}")

        self.find_new_doc('Document 1', datetime.datetime.strptime('01.02.2022', '%d.%m.%Y'))
        self.find_new_doc('Document 2', datetime.datetime.strptime('03.02.2022', '%d.%m.%Y'))
        self.find_new_doc('Document 3', datetime.datetime.strptime('05.02.2022', '%d.%m.%Y'))
        self.find_new_doc('Document 4', datetime.datetime.strptime('07.02.2022', '%d.%m.%Y'))
        self.find_new_doc('Document 5', datetime.datetime.strptime('09.02.2022', '%d.%m.%Y'))
        self.find_new_doc('Document 6', datetime.datetime.strptime('10.02.2022', '%d.%m.%Y'))
        self.find_new_doc('Document 7', datetime.datetime.strptime('01.04.2022', '%d.%m.%Y'))
        self.find_new_doc('Document 8', datetime.datetime.strptime('03.04.2022', '%d.%m.%Y'))
        self.find_new_doc('Document 9', datetime.datetime.strptime('05.04.2022', '%d.%m.%Y'))
        self.find_new_doc('Document 10', datetime.datetime.strptime('07.04.2022', '%d.%m.%Y'))
        self.find_new_doc('Document 11', datetime.datetime.strptime('09.04.2022', '%d.%m.%Y'))
        self.find_new_doc('Document 12', datetime.datetime.strptime('01.06.2022', '%d.%m.%Y'))
        self.find_new_doc('Document 13', datetime.datetime.strptime('03.06.2022', '%d.%m.%Y'))
        self.find_new_doc('Document 14', datetime.datetime.strptime('05.06.2022', '%d.%m.%Y'))


    def find_new_doc(self, filename: str, date: datetime.datetime = datetime.datetime.now(), delay: float = 0.5):
        doc = SPP_document(None, filename, None, None, self.SOURCE_NAME, None, {}, date, None)
        self._content_document.append(doc)
        self.logger.info(self._find_document_text_for_logger(doc))
        time.sleep(delay)

    @staticmethod
    def _find_document_text_for_logger(doc: SPP_document):
        """
        Единый для всех парсеров метод, который подготовит на основе SPP_document строку для логера
        :param doc: Документ, полученный парсером во время своей работы
        :type doc:
        :return: Строка для логера на основе документа
        :rtype:
        """
        return f"Find document | name: {doc.title} | link to web: {doc.web_link} | publication date: {doc.pub_date}"
