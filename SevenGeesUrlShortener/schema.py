import graphene
from .models import ShortenedUrlModel
from graphene_django import DjangoObjectType
from graphene import ObjectType, Mutation, String, Node, Field
from .service_module import generate_shorted_url


class ShortenedUrl(DjangoObjectType):
    class Meta:
        model = ShortenedUrlModel
        field = ("original_url", "shortened_url")

class Query:
    url = Field(ShortenedUrl, shortened_url=String())
    def resolve_url(self, info, **kwargs):
        shortened_url = kwargs.get('shortened_url')
        if shortened_url is not None:
            return ShortenedUrlModel.objects.get(shortened_url=shortened_url)
        return None

class Queries(Query, ObjectType):
    pass
class CreateShortenedUrl(Mutation):
    class Arguments:
        original_url = String()

    url = Field(ShortenedUrl)

    @staticmethod
    def mutate(root, info, original_url):
        shortened = generate_shorted_url(original_url)
        shortened.shortened_url = f"http://127.0.0.1:8000/{shortened.shortened_url }"
        return CreateShortenedUrl(url=shortened)

class UrlMutation(ObjectType):
    create_shortened_url = CreateShortenedUrl.Field()

schema = graphene.Schema(mutation=UrlMutation, query=Queries)
