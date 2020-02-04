from getUrl import GetUrl


def inputUrl():
    # 파이참에서 https 링크를 input을 return 하면 해당 웹사이트로 이동되는 현상을 방지합니다.
    url = input('Input URL>> ').strip()
    print()
    GetUrl(url)

    # playlist ex
    # url = GetUrl('https://www.youtube.com/playlist?list=PLwpDa9WrkRDSz6klKmGlI_tuwt8HMfmb7')

    # Channel ex
    # url = GetUrl('https://www.youtube.com/channel/UCtckgmUcpzqGnzcs7xEqMzQ')

    # User ex
    # url = GetUrl('https://www.youtube.com/user/SMTOWN')


inputUrl()

