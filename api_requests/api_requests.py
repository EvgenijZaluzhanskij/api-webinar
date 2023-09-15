import requests


class RonSwansonAPI:
    API_URL = 'http://ron-swanson-quotes.herokuapp.com/v2/quotes/'

    @staticmethod
    def _request(url: str) -> dict:
        with requests.Session() as session:
            try:
                response = session.get(url)
                response.raise_for_status()
            except requests.RequestException as e:
                print(f'failed to make api request. url: {url}. error: {e}')
                return {}

        return response.json()

    @classmethod
    def single_quote(cls):
        return RonSwansonAPI._request(cls.API_URL)

    @classmethod
    def multiple_quote(cls, count=1):
        return RonSwansonAPI._request(cls.API_URL + str(count))

    @classmethod
    def search_quotes(cls, text):
        return RonSwansonAPI._request(cls.API_URL + text)


if __name__ == '__main__':
    print(RonSwansonAPI().single_quote())

    print(RonSwansonAPI().multiple_quote(count=3))

    print(RonSwansonAPI().search_quotes(text='lawyer'))
