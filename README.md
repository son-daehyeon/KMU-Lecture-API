# 국민대학교 ECampus API

국민대학교 ECampus API 는 국민대학교 ECampus 에서 제공하는 정보를 가져오는 API 입니다.

## 제공하는 기능

- 내 강의 목록 조회 (현재 학기, 이전 학기)
- 강의 수강생 목록 조회

## 예시 코드

```py
from LectureList import LectureList
from Token import Token

if __name__ == '__main__':
    token = Token.login('username', 'password')

    lecture_list = LectureList(token)

    current_semester_lecture_list = lecture_list.current_semester()
    # previous_semester_lecture_list = lecture_list.previous_semester(2024, Semester.FIRST)

    for lecture in current_semester_lecture_list:
        if lecture.type == '비교과':
            continue

        print(f'{lecture.name} ({lecture.code}) 의 수강생 목록:')
        for participant in lecture.get_participants():
            print(f'{participant.name} ({participant.student_id})')
```
