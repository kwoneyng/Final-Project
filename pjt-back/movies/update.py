from pprint import pprint
from datetime import datetime, timedelta
# from .models import Movie
import requests


key = '8afc1f7e8832eae9a9c40cede345b59d'
base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json'

for weeks_ago in range(1, 6):
    targetDt = datetime.now() - timedelta(weeks=weeks_ago)
    targetDt = targetDt.strftime('%Y%m%d')
    boxoffice_url = f'{base_url}?key={key}&targetDt={targetDt}&weekGb=0'
    response_boxoffice = requests.get(boxoffice_url).json()['boxOfficeResult']['weeklyBoxOfficeList']

    for movie_info in response_boxoffice:   # 10개씩
        movie_name = movie_info['movieNm']
        movie_code = movie_info['movieCd']

        detail_url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={key}&movieCd={movie_code}'
        response_detail = requests.get(detail_url).json()['movieInfoResult']['movieInfo']
        # pprint(response_detail)

        for i in range(len(response_detail['actors'])):
            actor_Nm = response_detail['actors'][i]['peopleNm']
            person_url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.json?key={key}&peopleNm={actor_Nm}'
            people_info = requests.get(person_url).json()['peopleListResult']['peopleList']
            
            # pprint(people_info)
            for person_info in people_info:
                if movie_name in person_info['filmoNames']:
                    print(True)
                    print(person_info['peopleCd'])
                    print(person_info['peopleNm'])
                    actor_id = person_info['peopleCd']
                    break
                else:
                    print(False)

            

            break



        break
    break


