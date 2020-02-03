from getUrl import GetUrl


def inputUrl():
    url = GetUrl(input('Input URL>> '))

    # playlist
    # url = GetUrl('https://www.youtube.com/playlist?list=PLwpDa9WrkRDSz6klKmGlI_tuwt8HMfmb7')
    # Channel
    # url = GetUrl('https://www.youtube.com/channel/UCtckgmUcpzqGnzcs7xEqMzQ')
    # url = GetUrl('https://www.youtube.com/playlist?list=PLrgkfqG7JAcN_HB99YL6H_tVEk-C5pUUu')
    # User
    # url = GetUrl('https://www.youtube.com/user/jypentertainment')


inputUrl()

