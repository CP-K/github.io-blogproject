from django.shortcuts import render
#django.views.genericからListView、DetailViewをインポート
from django.views.generic import ListView, DetailView
#モデルBlogPostをインポート
from .models import BlogPost
#django.views.genericからFormViewをインポート
from django.views.generic import FormView
#django.urlsからreverse_lazyをインポート
from django.urls import reverse_lazy
#formsからContactFormをインポート
from .forms import ContactForm
#django.contribからmessagesをインポート
from django.contrib import messages
#django.core.mailモジュールからEmailMessageをインポート
from django.core.mail import EmailMessage

class IndexView(ListView):
    template_name='index.html'
    context_object_name='orderby_records'
    queryset=BlogPost.objects.order_by('-posted_at')
    paginate_by=4

class BlogDetail(DetailView):
    template_name='post.html'
    model=BlogPost

#Placeカテゴリの記事を一覧表示するビュー
class PlaceView(ListView):
    template_name='place_list.html'
    model=BlogPost
    context_object_name='place_records'
    queryset=BlogPost.objects.filter(
        category='place').order_by('-posted_at')
    paginate_by=2

#Hobbyカテゴリの記事を一覧表示するビュー
class HobbyView(ListView):
    template_name='hobby_list.html'
    model=BlogPost
    context_object_name='hobby_records'
    queryset=BlogPost.objects.filter(
        category='hobby').order_by('-posted_at')
    paginate_by=2

#Bookカテゴリの記事を一覧表示するビュー
class BookView(ListView):
    template_name='book_list.html'
    model=BlogPost
    context_object_name='book_records'
    queryset=BlogPost.objects.filter(
        category='book').order_by('-posted_at')
    paginate_by=2

class ContactView(FormView):
    '''問い合わせページを表示するビュー
    フォームで入力されたデータを取得し、メールの作成と送信を行う
    '''
    #contact.htmlをレンダリングする
    template_name='contact.html'
    #クラス変数form_classにforms.pyで定義したContactFormを設定
    form_class=ContactForm
    #送信完了後にリダイレクトするページ
    success_url=reverse_lazy('blogapp:contact')

    def form_valid(self, form):
        '''FormViewクラスのform_valid()をオーバーライド
        
        フォームのバリデーションを通過したデータがPOSTされたときに呼ばれる
        メール送信を行う
        '''
        #フォームに入力されたデータをフィールド名を指定して取得
        name=form.cleaned_data['name']
        email=form.cleaned_data['email']
        title=form.cleaned_data['title']
        message=form.cleaned_data['message']
        #メールのタイトルの書式を設定
        subject='お問い合わせ:{}'.format(title)
        #フォームの入力データの書式を設定
        message=\
            '送信者名:{0}\n メールアドレス:{1}\n タイトル:{2}\n メッセージ:\n{3}'\
            .format(name, email, title, message)
        #メールの送信元のアドレス
        from_email='admin@example.com'
        #送信先のメールアドレス
        to_list=['admin@example.com']
        #EmailMessageオブジェクトを生成
        message=EmailMessage(subject=subject,
                            body=message,
                            from_email=from_email,
                            to=to_list,
                            )
        #EmailMessageクラスのsend()でメールサーバーからメールを送信
        message.send()
        #送信完了後に表示するメッセージ
        messages.success(
            self.request, 'お問い合わせは正常に送信されました。')
        #戻り値はスーパークラスのform_validの戻り値(HttpResponseRedirect)
        return super().form_valid(form)