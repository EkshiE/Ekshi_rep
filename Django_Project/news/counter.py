from django.templatetags.static import register

from mainapp.models import News


@register.simple_tag(takes_context=True)
def page_hits(ctx, page_url=None):
    """
    """
    counter = (News.objects.filter(
        url=(ctx['request'].path if page_url is None else page_url)
    ).first())
    return 0 if counter is None else counter.count
