from django.shortcuts import render
from allauth.account.views import SignupView, LoginView, PasswordResetView

from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm


# Create your views here.
class LoginView(LoginView):
    template_name = "allauth/account/login.html"


# Create your views here.
class SignUpView(SignupView):
    """
    サインアップページのビュー
    """
    # forms.pyで定義したフォームのクラス
    form_class = CustomUserCreationForm
    # レンダリングするテンプレート
    template_name = "allauth/account/signup.html"
    # サインアップ完了後のリダイレクト先のURLパターン
    # success_url = reverse_lazy('accounts:signup_success')

    def form_valid(self, form):
        """CreateViewクラスのform_valid()をオーバーライド

        フォームのバリデーションを通過したときに呼ばれる
        フォームデータの登録を行う

        parameters:
          form(django.forms.Form):
            form_classに格納されているCustomUserCreationFormオブジェクト
        Return:
          HttpResponseRedirectオブジェクト:
            スーパークラスのform_valid()の戻り値を返すことで、
            success_urlで設定されているURLにリダイレクトさせる
        """
        # formオブジェクトのフィールドの値をデータベースに保存
        user = form.save()
        self.object = user
        # 戻り値はスーパークラスのform_valid()の戻り値(HttpResponseRedirect)
        return super().form_valid(form)

class SignUpSuccessView(TemplateView):
    """サインアップ成功ページのビュー

    """
    # レンダリングするテンプレート
    template_name = "accounts/signup_success.html"