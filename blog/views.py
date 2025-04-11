from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Article


def create_article(request):

	if request.method == 'POST':
		title = request.POST.get('title', None)
		content = request.POST.get('content', None)


		Article.objects.create(
			author=request.user,
			title=title,
			content=content
		)

		return render(request, 'blog/list.html', {
			"articles": request.user.articles.all()
		})

	elif request.method == 'GET':
		return render(request, 'blog/form.html', {"articles": request.user.articles.all()})
