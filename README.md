# DailyReceipt-Django

## 실행순서

- `.env.`파일은 팀 디코 확인

### 가상환경

- 가상환경 생성
  `python -m venv venv`

- 가상환경 활성화

  - Windows의 경우
    `venv\Scripts\activate`
  - Mac/Linux의 경우
    `source venv/bin/activate`

- interpreter 선택(수동으로 선택할 경우)
  `cmd + shift + p` > `Python: 인터프리터 선택` > venv 선택

### 필요한 패키지 설치

- 가상환경이 실행된 상태에서 실행
  `pip install -r requirements.txt`

### 데이터베이스 마이그레이션

`python manage.py migrate`

### 개발 서버 실행

`python manage.py runserver`
