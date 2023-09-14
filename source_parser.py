"""
Парсер плагина SPP

1/2 документ плагина
"""
import datetime
import logging
import os
import random
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


        doc = SPP_document(None, 'TestDocument1', None, None, self.SOURCE_NAME, None, {}, datetime.datetime.now(), None)
        self._content_document.append(doc)
        self.logger.info(self._find_document_text_for_logger(doc))
        time.sleep(0.5)

        doc = SPP_document(None, 'TestDocument2', None, None, self.SOURCE_NAME, None, {}, datetime.datetime.now(), None)
        self._content_document.append(doc)
        self.logger.info(self._find_document_text_for_logger(doc))
        time.sleep(0.5)

        doc = SPP_document(None, 'TestDocument3', None, None, self.SOURCE_NAME, None, {}, datetime.datetime.now(), None)
        self._content_document.append(doc)
        self.logger.info(self._find_document_text_for_logger(doc))
        time.sleep(0.5)

        doc = SPP_document(None, 'TestDocument4', None, None, self.SOURCE_NAME, None, {}, datetime.datetime.now(), None)
        self._content_document.append(doc)
        self.logger.info(self._find_document_text_for_logger(doc))
        time.sleep(0.5)

        doc = SPP_document(None, 'TestDocument5', None, None, self.SOURCE_NAME, None, {}, datetime.datetime.now(), None)
        self._content_document.append(doc)
        self.logger.info(self._find_document_text_for_logger(doc))
        time.sleep(0.5)

        doc = SPP_document(None, 'TestDocument6', None, None, self.SOURCE_NAME, None, {}, datetime.datetime.now(), None)
        self._content_document.append(doc)
        self.logger.info(self._find_document_text_for_logger(doc))
        time.sleep(0.5)

        doc = SPP_document(None, 'TestDocument7', None, None, self.SOURCE_NAME, None, {}, datetime.datetime.now(), None)
        self._content_document.append(doc)
        self.logger.info(self._find_document_text_for_logger(doc))
        time.sleep(0.5)

        doc = SPP_document(None, 'TestDocument8', None, None, self.SOURCE_NAME, None, {}, datetime.datetime.now(), None)
        self._content_document.append(doc)
        self.logger.info(self._find_document_text_for_logger(doc))
        time.sleep(0.5)

        doc = SPP_document(None, 'TestDocument9', None, None, self.SOURCE_NAME, None, {}, datetime.datetime.now(), None)
        self._content_document.append(doc)
        self.logger.info(self._find_document_text_for_logger(doc))
        time.sleep(0.5)

        doc = SPP_document(None, 'TestDocument10', None, None, self.SOURCE_NAME, None, {}, datetime.datetime.now(), None)
        self._content_document.append(doc)
        self.logger.info(self._find_document_text_for_logger(doc))
        time.sleep(0.5)

        doc = SPP_document(None, 'TestDocument11', None, None, self.SOURCE_NAME, None, {}, datetime.datetime.now(), None)
        self._content_document.append(doc)
        self.logger.info(self._find_document_text_for_logger(doc))
        time.sleep(0.5)

        doc = SPP_document(None, 'TestDocument12', None, None, self.SOURCE_NAME, None, {}, datetime.datetime.now(), None)
        self._content_document.append(doc)
        self.logger.info(self._find_document_text_for_logger(doc))
        time.sleep(0.5)

        doc = SPP_document(None, 'TestDocument13', None, None, self.SOURCE_NAME, None, {}, datetime.datetime.now(), None)
        self._content_document.append(doc)
        self.logger.info(self._find_document_text_for_logger(doc))
        time.sleep(0.5)

        doc = SPP_document(None, 'TestDocument14', None, None, self.SOURCE_NAME, None, {}, datetime.datetime.now(), None)
        self._content_document.append(doc)
        self.logger.info(self._find_document_text_for_logger(doc))
        time.sleep(0.5)


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
