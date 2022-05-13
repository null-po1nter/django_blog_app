from django import template
from taggit.models import Tag


register = template.Library()

@register.inclusion_tag('inc/tag_list.html')
def show_tags():
    tags = Tag.objects.all()
    
    return {
        'tags': tags,
    }
