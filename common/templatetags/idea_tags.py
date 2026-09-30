from django import template
from ideas.models import Idea

register = template.Library()


@register.filter
def status_badge(value):
    """
    It takes the raw value (e.g., 'PENDING') and converts it into nicely
    formatted HTML/text with emojis.
    """
    badges = {
        'PENDING': '⚠️ Pending review',
        'REVIEW': '👀 Under review',
        'APPROVED': '✅ Approved',
    }

    return badges.get(value, value)
