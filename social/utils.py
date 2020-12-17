from django.utils.datastructures import MultiValueDictKeyError

from recipes.models import Tag, Recipe
from users.models import User

def get_filters(request):
    request.GET = request.GET.copy()
    filters = {tag.tag_name_eng: 'checked' for tag in Tag.objects.all()}

    for key in filters:
        try:
            filters[key] = (
                'checked' if request.GET[key] == '1' else ''
            )
        except MultiValueDictKeyError:
            pass

    return filters
