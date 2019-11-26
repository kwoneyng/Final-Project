from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


movie_list = [
    {
        'title': '엑시트',
        'post_url':'https://picsum.photos/id/599/200/300',
        'genre': '코미디',
        'openingDt': '2019-07-31',
    },
    {
        'title': '마이펫의 이중생활2',
        'post_url': 'https://picsum.photos/id/399/200/300',
        'genre': '애니메이션',
        'openingDt': '2019-07-31',
    },
]


def index(request):
    if request.user.is_authenticated:
        context = { 'movie_list': movie_list }
        return render(request, 'movies/index.html', context)
    return redirect('accounts:login')


