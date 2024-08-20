import json

from util.LectureList import LectureList, Semester
from util.Token import Token

if __name__ == '__main__':
    config = json.loads(''.join(open('config.json', 'r', encoding='utf-8').readlines()))

    token = Token.login(config['id'], config['pw'])

    lecture_list = LectureList(token)

    current_semester_lecture_list = lecture_list.current_semester()
    # previous_semester_lecture_list = lecture_list.previous_semester(2024, Semester.FIRST)

    for lecture in current_semester_lecture_list:
        if lecture.type == '비교과':
            continue

        print(f'{lecture.name} ({lecture.code}) 의 수강생 목록:')
        for participant in lecture.get_participants():
            print(f'{participant.name} ({participant.student_id})')
