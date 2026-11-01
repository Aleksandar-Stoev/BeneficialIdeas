from django.forms import inlineformset_factory
from ideas.models import Idea
from supplies.models import Supplies

SuppliesFormSet = inlineformset_factory(
    Idea,
    Supplies,
    fields=['name', 'quantity', 'is_secured'],
    extra=3,
    can_delete=True
)
