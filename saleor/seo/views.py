from django.http import JsonResponse

from saleor.seo.models import Blog


def get_blog(request, slug):
    try:
        blog = Blog.objects.get(slug=slug)
    except Blog.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Record does not exist'},
                            status=404)
    return JsonResponse(blog.to_dict(), safe=False)

def list_blogs(request):
    data = list()
    for blog in Blog.objects.all():
        data.append(blog.minimal_dict())
    return JsonResponse(data, safe=False)
