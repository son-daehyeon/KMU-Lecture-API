from util.Request import Request


class Token:
    @staticmethod
    def login(id: str, password: str) -> str:
        params = {
            'userid': id,
            'password': password
        }

        response = Request.post('/local/coursemos/login.php', params)

        return response['utoken']
