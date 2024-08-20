from util.Request import Request


class Participant:
    def __init__(self, id: int, student_id: int, name: str, institution: str, department: str):
        self.id = id
        self.student_id = student_id
        self.name = name
        self.institution = institution
        self.department = department

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"Participant(id={self.id}, student_id={self.student_id}, name={self.name}, institution={self.institution}, department={self.department})"


class Lecture:
    def __init__(self, token: str, id: int, name: str, full_name: str, type: str):
        self.__token = token

        self.id = id
        self.name = name
        self.full_name = full_name
        self.type = type

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"LectureDto(id={self.id}, name={self.name}, full_name={self.full_name}, type={self.type})"

    def get_participants(self) -> [Participant]:
        params = {
            'wsfunction': 'coursemos_course_get_participants_list_v2',
            'wstoken': self.__token,
            'courseid': self.id,
            'ls': 1000
        }

        return list(map(
            lambda x: Participant(x['id'], int(x['username']), x['fullname'], x['institution'], x['department']),
            filter(
                lambda x: x['roles'][0]['roleid'] == 5,
                Request.post('/webservice/rest/server.php', params)['participants']
            )
        ))
