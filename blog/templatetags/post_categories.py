from django import template
from blog.models import Category


register = template.Library()

@register.inclusion_tag('inc/category_list.html')
def show_categories():
    categories = Category.objects.all()

    return {
        'categories': categories,
    }
