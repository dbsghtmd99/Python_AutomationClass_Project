import requests
from bs4 import BeautifulSoup as bs
from download import Download
import youtube_dl


class GetUrl(object):
    # main class로부터 입력된 재생목록의 url을 받아옵니다.
    def __init__(self, Url):
        urlList = []
        # 'https://www.youtube.com/playlist?list=PLwpDa9WrkRDRXRidbaSoWaXecj1BzFIbJ' 와 같은경우
        if 'list' in Url.split('.com/')[-1]:
            self.playListUrl = Url
            self.urlList = self.findUrlFromPlaylist()
            self.down()

        # 'https://www.youtube.com/channel/UCd4FmcWIVdWAy0-Q8OJBloQ' 와 같은경우
        elif 'channel' in Url.split('.com/')[-1]:
            self.channelUrl = Url
            self.findUrlFromChannel()
            self.findUrlFromPlaylist()
            self.down()

        # 'https://www.youtube.com/user/SMTOWN' 과 같은경우
        elif 'user' in Url.split('.com/')[-1]:
            self.userUrl = Url
            self.findUrlFromUser()
            self.findUrlFromPlaylist()
            self.down()

        # 일반적인 동영상인 경우
        else:
            with youtube_dl.YoutubeDL({}) as ydl:
                ydl.download([Url])

    # 재생목록에 있는 동영상들의 정보를 받아옵니다.
    def findUrlFromPlaylist(self):
        # playListUrl의 html정보를 읽어옵니다.
        html = requests.get(self.playListUrl)
        soup = bs(html.text, 'html.parser')
        html.close()

        # 동영상들의 제목과 url을 추출합니다.
        videoTitle = soup.findAll('tr', {'class': 'pl-video yt-uix-tile'})
        videoLinks = soup.findAll('a', {'class': 'pl-video-title-link yt-uix-tile-link yt-uix-sessionlink spf-link'})

        # 재생목록이 비어있거나 비공개로 설정된 경우
        if len(videoTitle) == 0 or len(videoLinks) == 0:
            print('재생목록이 비어있거나 비공개로 설정되어 있습니다.')
            print('실행을 종료합니다.')
            exit(0)

        # 정상적으로 불러온 경우
        try:
            titleList = []
            urlList = []
            # print('제목 추출중...')
            for title in videoTitle:
                YTtitle = title.get('data-title')
                titleList.append(YTtitle)
                # print(YTtitle)
            # print('url 추출중...\n')
            for link in videoLinks:
                # 재생목록의 정보가 담긴내용은 삭제한 후, 순수한 동영상의 링크만을 가져옵니다.
                # 즉, https://www.youtube.com/watch?v=eGXJs7zOHC4&list=PLwpDa9WrkRDRXRidbaSoWaXecj1BzFIbJ&index=2&t=0s에서
                # https://www.youtube.com/watch?v=eGXJs7zOHC4 만을 split 함수를 통해 추출합니다.
                # print(link.get('href').split('&')[0]) (i.e. /watch?v=gb1tnmgPEFo)
                YTurl = 'https://www.youtube.com' + link.get('href').split('&')[0]
                urlList.append(YTurl)
                # print(YTurl)

            for num, i in enumerate(range(len(titleList))):
                print('#' + str(num + 1), titleList[i], ':', urlList[i])

        except Exception as e:
            print(e)

        return urlList

    # 원하는 채널의 영상의 정보를 모두 가져옵니다.
    def findUrlFromChannel(self):
        # 유튜브 특성상 동영상이 많은 채널의 경우 동영상을 다 불러오기 전에 html정보를 가져오면 손실되는 정보가 있기에
        # 채널의 네비게이션 바 아래에 있는 해당 채널이 '업로드한 동영상'을 모두 재생목록에 만들어 재생시켜주는 재생목록의 url을 1차적으로 가져옵니다.
        # # channelUrl의 html정보를 읽어옵니다.
        # html = requests.get(self.channelUrl)
        # soup = bs(html.text, 'html.parser')
        # html.close()
        #
        # # '모두 재생' 버튼에 담긴 정보를 가져옵니다.
        # channelLinks = soup.findAll('a', {
        #     'class': 'yt-uix-button shelves-play play-all-icon-btn yt-uix-sessionlink yt-uix-button-default yt-uix-button-size-small yt-uix-button-has-icon no-icon-markup'})
        # # print(channelLinks)
        # try:
        #     for link in channelLinks:
        #         # https://www.youtube.com/watch?v=Ja0ioh5l3Y0&list=UUtckgmUcpzqGnzcs7xEqMzQ (최신순 재생)
        #         # https://www.youtube.com/watch?v=K_5lal40lCk&list=PUtckgmUcpzqGnzcs7xEqMzQ (인기순 재생)
        #         if link.get('href').split('list=')[-1][0:2] == 'UU':
        #             playListID = link.get('href').split('list=')[-1]
        #
        #             # 'https://www.youtube.com/playlist?list=' + playListID 와 같은 형태로 접속하면 새로운 url로 redirect 되기 때문에
        #             # beautifulsoup가 받아온 request 는 html 정보를 가져 올 수가 없으므로
        #             # redirect 되는 규칙을 찾아서 redirect 된 후의 url의 찾아냅니다.
        #             # 확인 결과, redirect된 url은 다음과 같습니다.
        #             # 'https://www.youtube.com' + 재생목록의 첫번째 영상의 videoID + '&list=' + 재생목록ID
        #
        #             playAllVideosUrl = 'https://www.youtube.com/playlist?list=' + playListID
        #             self.playListUrl = playAllVideosUrl
        #
        #             # https://www.youtube.com/watch?v=Ja0ioh5l3Y0 로부터 /watch?v=Ja0ioh5l3Y0 만 추출합니다.
        #             firstVideoID = self.findUrlFromPlaylist()[1][0].split('.com')[-1]
        #             # print(firstVideoID)
        #             realURL = 'https://www.youtube.com' + firstVideoID + '&list=' + playListID
        #             print(realURL)
        # 'https://www.youtube.com/channel/UCtckgmUcpzqGnzcs7xEqMzQ'
        channelID = self.channelUrl.split('channel/')[-1][2:]
        playListID = 'UU' + channelID  # UUtckgmUcpzqGnzcs7xEqMzQ

        playAllVideosUrl = 'https://www.youtube.com/playlist?list=' + playListID
        self.playListUrl = playAllVideosUrl
        # print(self.playListUrl)  # https://www.youtube.com/playlist?list=UUtckgmUcpzqGnzcs7xEqMzQ
        # # https://www.youtube.com/watch?v=Ja0ioh5l3Y0 로부터 /watch?v=Ja0ioh5l3Y0 만 추출합니다.
        # firstVideoID = self.findUrlFromPlaylist()[0].split('.com')[-1]
        # # print(firstVideoID)
        # realURL = 'https://www.youtube.com' + firstVideoID + '&list=' + playListID
        # print(realURL)  # https://www.youtube.com/watch?v=Ja0ioh5l3Y0&list=UUtckgmUcpzqGnzcs7xEqMzQ

    def findUrlFromUser(self):
        # userUrl의 html정보를 읽어옵니다.
        html = requests.get(self.userUrl)
        soup = bs(html.text, 'html.parser')
        html.close()

        # '모두 재생' 버튼에 담긴 정보를 가져옵니다.
        userLinks = soup.findAll('a', {'class': 'yt-uix-sessionlink yt-user-name spf-link'})
        # print(userLinks)

        # 맨앞의 href 만 필요하기 때문에 iterator 인 userLinks 에 반복문을 적용하지 않고
        # 다음과 같이 userLinks.__iter__().__next__() 를 사용하여 첫번째로 나오는 부분만 추출합니다.

        # print(userLinks.__iter__().__next__().get('href'))  # /channel/UCaO6TYtlC8U5ttz62hTrZgg

        # 마찬가지로 U_ xxxx의 형태를 추출하기 위해
        userID = userLinks.__iter__().__next__().get('href').split('channel/')[-1][2:]
        playListID = 'UU' + userID
        playAllVideosUrl = 'https://www.youtube.com/playlist?list=' + playListID
        self.playListUrl = playAllVideosUrl
        # print(self.playListUrl)

    def down(self):
        # Download 클래스로부터 urlList 안의 url들에대해 일괄적으로 다운로드를 시작합니다.
        down = Download(self.urlList)
        down.multiDown()
