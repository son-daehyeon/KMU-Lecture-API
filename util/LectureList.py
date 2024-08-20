from enum import Enum

from util.Lecture import Lecture
from util.Request import Request


class Semester(Enum):
    FIRST = 10
    FIRST_VACATION = 11
    SECOND = 20
    SECOND_VACATION = 21


class LectureList:
    def __init__(self, token: str):
        self.__token = token

    def current_semester(self) -> [Lecture]:
        params = {
            'wsfunction': 'coursemos_course_get_mycourses_v2',
            'wstoken': self.__token,
        }

        return list(map(
            lambda x: Lecture(self.__token, x['id'], x['fullname'], x['shortname'], x['course_type_name']),
            Request.post('/webservice/rest/server.php', params)
        ))

    def previous_semester(self, year: int, semester: Semester) -> [Lecture]:
        params = {
            'wsfunction': 'coursemos_course_get_mycourses_period_v2',
            'wstoken': self.__token,
            'year': year,
            'semester_code': semester.value,
        }

        return list(map(
            lambda x: Lecture(self.__token, x['id'], x['fullname'], x['shortname'], x['course_type_name']),
            Request.post('/webservice/rest/server.php', params)
        ))
