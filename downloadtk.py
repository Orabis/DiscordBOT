import requests
class convert:
    def __init__(self,username,vidid):

        url = f"https://www.tiktok.com/node/share/video/{username}/{vidid}"
        userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"

        s = requests.Session()
        r = s.get(url, headers= {"User-Agent": userAgent})

        data = r.json()
        videoUrl = data["itemInfo"]["itemStruct"]["video"]["downloadAddr"]
        referer = data["seoProps"]["metaParams"]["canonicalHref"]

        r = s.get(videoUrl, headers= {"Referer": referer, "User-Agent": userAgent})

        with open('lasttiktok.mp4', 'wb') as f:
           f.write(r.content)

           
