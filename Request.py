import requests


class Request:
    URL = 'https://ecampus.kookmin.ac.kr'

    @staticmethod
    def __request(method: str, url: str, query_params: dict) -> dict:
        url = Request.URL + url + '?'

        query_params['lang'] = 'ko'
        query_params['moodlewsrestformat'] = 'json'
        for key, value in query_params.items():
            url += f'&{key}={value}'

        response = requests.request(method, url)

        if 'error' in response.json():
            raise Exception(response.json()['error'])

        return response.json()['data']

    @staticmethod
    def get(url: str, query_params: dict) -> dict:
        return Request.__request('GET', url, query_params)

    @staticmethod
    def post(url: str, query_params: dict) -> dict:
        return Request.__request('POST', url, query_params)

    @staticmethod
    def put(url: str, query_params: dict) -> dict:
        return Request.__request('PUT', url, query_params)

    @staticmethod
    def patch(url: str, query_params: dict) -> dict:
        return Request.__request('PATCH', url, query_params)

    @staticmethod
    def delete(url: str, query_params: dict) -> dict:
        return Request.__request('DELETE', url, query_params)
