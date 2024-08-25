class Participant:
    def __init__(self, user_id: int, student_id: int, name: str, institution: str, department: str):
        self.user_id = user_id
        self.student_id = student_id
        self.name = name
        self.institution = institution
        self.department = department

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"Participant(user_id={self.user_id}, student_id={self.student_id}, name={self.name}, institution={self.institution}, department={self.department})"
