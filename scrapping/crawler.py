import sys
import requests
import logging

from bs4 import BeautifulSoup


class LitresParser:
    FANTASY_URL = 'https://www.litres.ru/knigi-fentezi/'

    def __init__(self, pages=1):
        self.pages = pages
        self.logger = logging.getLogger(__name__)
        self._init_logger()

    def _init_logger(self):
        handler = logging.StreamHandler(stream=sys.stdout)
        handler.setFormatter(logging.Formatter(fmt='[%(asctime)s: %(levelname)s] %(message)s'))
        self.logger.setLevel(logging.DEBUG)
        self.logger.addHandler(handler)

    def _request_page(self, page_number: int) -> str:
        page_string = ''
        if page_number > 1:
            page_string = f'page-{page_number}'

        with requests.Session() as session:
            try:
                response = session.get(LitresParser.FANTASY_URL + page_string)
                response.raise_for_status()
            except requests.RequestException as e:
                self.logger.error(f'failed to get data fro {page_number} page. status_code: {response.status_code}.'
                                  f'error: {e}')
                return ''

        return response.text

    def parse(self) -> set:
        authors = set()

        for page_number in range(1, self.pages + 1):
            page_data = self._request_page(page_number)
            parsed_page_data = BeautifulSoup(page_data, 'html.parser')

            for item in parsed_page_data.find_all(class_='art__author'):
                authors.add(
                    item.get_text()
                )
                self.logger.info(f'parsed author: {item.get_text()}')

            self.logger.info(f'finish parsing page: {page_number}')

        self.logger.info(f'finish parsing. total unique authors: {len(authors)}')

        return authors


if __name__ == '__main__':
    print(LitresParser(pages=5).parse())
