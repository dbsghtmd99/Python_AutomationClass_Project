import datetime
import os
import shutil
import youtube_dl


class Download(object):

    def __init__(self, url):
        self.url = url

    def multiDown(self):
        # 다운로드 될 폴더의 이름을 현재 시간을 바탕으로 가져옵니다.
        d = datetime.datetime.today()
        newFolderName = "{:02d}{:02d}{:02d}_{:02d}{:02d}{:02d}".format(d.year, d.month, d.day, d.hour, d.minute,
                                                                       d.second)
        # print(type(newFolderName))  # str인지 확인
        # print(newFolderName)  # 정상 출력 확인

        # 폴더를 만들기 전 이름이 중복되는지 확인합니다.
        if not os.path.isdir(newFolderName):
            os.mkdir(newFolderName)
        else:
            print('같은 이름의 폴더가 이미 존재합니다.')
            exit(0)

        # 각각의 url마다 다운로드를 시작합니다.
        for num, url in enumerate(self.url):
            # youtube_dl options
            ydl_opts = {
                # 'format': 'best/best',  # 가장 좋은 화질로 선택(화질을 선택하여 다운로드 가능)
                # 'outtmpl': self.path  # 다운로드 경로 설정 (환경변수 설정 문제로 인하여 설정 불가)
                # 'writesubtitles': 'best',  # 자막 다운로드(자막이 없는 경우 다운로드 X)
                # 'writethumbnail': 'best',  # 영상 thumbnail 다운로드
                # 'writeautomaticsub': True,  # 자동 생성된 자막 다운로드
                # 'subtitleslangs': 'en'  # 자막 언어가 영어인 경우(다른 언어로 변경 가능)
            }
            try:
                # 다운로드 진행 상태를 출력합니다.
                print(num + 1, 'of', str(len(self.url)), 'downloading')
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])

            except Exception as e:
                print(e)

        # 다운로드가 끝난 mp4 파일을 지정된 폴더로 이동합니다.
        file = os.listdir('.\\')
        for i in file:
            temp = i.split('.')
            if temp[-1].lower() == 'mp4':
                shutil.move('.\\' + i, '.\\' + newFolderName + '\\' + i)
