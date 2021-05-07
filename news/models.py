from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from django.contrib.auth.models import User
from wagtail.documents.models import Document
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.admin.edit_handlers import TabbedInterface, ObjectList
from home.models import SocialMediaModel
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


class PostsModel(models.Model):
	news_title = models.CharField('News Title', max_length=50, default=" ")
	news_text = RichTextField('News Text', max_length=1000, default=" ")
	news_img = models.ForeignKey(
		"wagtailimages.Image",
		blank=False,
		null=True,
		related_name="+",
		on_delete=models.SET_NULL,
		)

	updated_time = models.DateTimeField('updated_time', auto_now=True)
	created_time = models.DateTimeField('created_time', auto_now_add=True)
	pub_time = models.DateTimeField('pub_time', auto_now_add=True)

	def __str__(self):
		return "{} - {}".format(self.news_title, self.pub_time)

	panels = [
		FieldPanel('news_title'),
		FieldPanel('news_text'),
		ImageChooserPanel('news_img')
	]

	class Meta:
		ordering = ['pub_time']
		verbose_name_plural = "News"


class NewsPage(Page):
	max_count = 1

	def get_context(self, request):
		context = super().get_context(request)				
		
		# Get all posts
		reverse_all_posts = []
		all_posts = PostsModel.objects.all()
		for post in reversed(all_posts):
			reverse_all_posts.append(post)
		# Paginate all posts by 6 per page
		paginator = Paginator(reverse_all_posts, 6)
		# Try to get the ?page=x value
		page = request.GET.get("page")
		try:
			# If the page exists and the ?page=x is an int
			posts = paginator.page(page)
		except PageNotAnInteger:
			# If the ?page=x is not an int; show the first page
			posts = paginator.page(1)
		except EmptyPage:
			# If the ?page=x is out of range (too high most likely)
			# Then return the last page
			posts = paginator.page(paginator.num_pages)

		

		# "posts" will have child pages; you'll need to use .specific in the template
		# in order to access child properties, such as youtube_video_id and subtitle

		context['posts'] = posts
		context['all_posts'] = PostsModel.objects.count()
		context['social'] = SocialMediaModel.objects.all()	
		return context
		

