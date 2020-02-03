# Python_AutomationClass_Project

이 문서는 파이썬 자동화 교육의 최종 프로젝트에 대한 보고서이다.

## 1. 개요 및 용도
유튜브의 재생목록, 채널의 주소만 입력하면 재생목록의 모든영상 또는 채널의 모든 영상을 .mp4 파일로 다운로드 받을 수 있다.

작동 원리는 beautifulSoup 모듈로 parsing 해온 html 정보를 분석하여 동영상의 url정보를 얻어낸 후, 유튜브 동영상을 다운로드 해주는 모듈에 적용하여 .mp4 파일로 다운로드 되는 방식이다.

## 2. 프로젝트 설명
### 2.1. 개발 환경 및 요구 모듈
코드를 실행시키기 전, Anaconda Prompt 를 실행시켜 다음의 라이브러리를 설치해야 한다.
 - bs4 : html parsing 기능 제공
 - youtube-dl : 유튜브 링크를 통한 다운로드 기능 제공
 - ~~selenium~~

Python 내장 모듈은 다음과 같다.
 - os : 새로운 폴더생성, 디렉토리 지정기능 제공
 - shitil : 다운로드된 파일을 이동시켜주는 기능 제공
 - datetime : 현재 시간정보를 불러와 다운로드된 파일을 이동시킬 폴더의 이름을 설정하는 기능 제공

또한 다음과 같은 환경에서 정상 작동을 확인하였다.
 - conda 4.7.12
 - Python 3.7

### 2.2. 유튜브 구조에 대한 배경지식

### 2.3. 코드 설명

#### 2.3.1 Main Class
#### 2.3.2 getUrl Class
#### 2.3.3 download Class

## 3. 오류 분석 및 부족한 점
### 3.1. 코드 작성 중 발생했던 에러
### 3.2. 추가 활용 방안
