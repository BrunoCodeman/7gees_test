import random
import string
from .models import ShortenedUrlModel


def generate_shorted_url(original_url) -> ShortenedUrlModel:
    """
    Generates a new ShortenedUrlModel entity.

    Params:
    - original_url: the original URL to be shortened.

    Returns:
    - The created model with the original and the shortened URLs.
    """
    shortened = get_random_urlstring();
    try:
        model = ShortenedUrlModel.objects.get(shortened_url=shortened)
    except Exception:
        model = ShortenedUrlModel(original_url=original_url, shortened_url=shortened)
        model.save()
    return model


def get_random_urlstring(max_length=10) -> string:
    """
    Generates a string to work as a short to an URL
    
    Params:
    - max_length: The max length of the URL segment
    
     Returns:
    - The generated string
    """
    all_letters = string.ascii_letters
    random_string = ''.join(random.choice(all_letters) for i in range(max_length))
    return random_string
