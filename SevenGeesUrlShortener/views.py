from django.http import HttpResponse, HttpResponseRedirect
from .models import ShortenedUrlModel


def redirect_to_url(request, shortened_url):
    url = "https://www.google.com"
    obj = ShortenedUrlModel.objects.filter(shortened_url=shortened_url).first()
    if obj is not None:
        url = obj.original_url if obj.original_url[0:8] == 'https://' else f"https://{obj.original_url}"

    return HttpResponseRedirect(url)