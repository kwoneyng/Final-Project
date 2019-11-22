from pprint import pprint
import requests

key = '8afc1f7e8832eae9a9c40cede345b59d'
targetDt = '20191101'
DAILY_BOXOFFICE_API_URL = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key={key}&targetDt={targetDt}'

response = requests.get(DAILY_BOXOFFICE_API_URL).json()['boxOfficeResult']['dailyBoxOfficeList']

for each_movie in response:
    print()
    pprint(each_movie)
