from django.shortcuts import render, redirect
from django.http import HttpResponse
from mysite.models import Post
import datetime  # 💡 如果教材有需要顯示現在時間，記得引入這個

def homepage(request):
    # 1. 抓出所有的資料庫貼文
    posts = Post.objects.all()
    
    # 2. 抓取現在時間（給頁面底部的現在時刻使用）
    now = datetime.datetime.now()
    
    # 3. 💡 關鍵：改用 render，並把資料（locals()）傳給 index.html 範本
    return render(request, 'index.html', locals())

def showpost(request, slug):
    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            return render(request, 'post.html', locals())
    except:
        return redirect('/')