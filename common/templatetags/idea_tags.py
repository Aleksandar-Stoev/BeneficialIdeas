from django import template
from ideas.models import Idea

register = template.Library()


@register.filter
def status_badge(value):
    badges = {
        'PENDING': '⚠️ Pending approval',
        'REVIEW': '👀 Under review',
        'APPROVED': '✅ Approved',
    }

    return badges.get(value, value)
