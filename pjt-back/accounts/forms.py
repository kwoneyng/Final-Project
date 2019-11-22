from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model  # 현재 활성화(adcive)된 user model을 return 한다.


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()  # settings.py에서 AUTH_USER_MODEL설정 후에는 accounts.User사용하게 됨
        # 원래 default user model이 있는데, 나중에 우리가 customize한 usermodel이 생길 수 있음 
        # -> default user model 안쓰면 그때부터 get_user_model()이 default값이 아니게 됨
        # models.py에서는 get_user_model()사용하지 않음
        fields = ['email', 'first_name', 'last_name', ]


# 에러 없이 반영하기 위해서는 dbsqlite도 지우고 처음부터 구성하자!

# 커스터마이징한 유저 모델을 인식하지 못해서 직접 get_user_model 함수로 유저 모델정보를 넣어줌
class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.fields