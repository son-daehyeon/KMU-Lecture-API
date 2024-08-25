from Request import Request


class Token:
    @staticmethod
    def login(username: str, password: str) -> str:
        params = {
            'userid': username,
            'password': password
        }

        response = Request.post('/local/coursemos/login.php', params)

        return response['utoken']
