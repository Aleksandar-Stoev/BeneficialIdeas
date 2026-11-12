from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class DisableFieldsMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.disabled = True


class AuthorRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    author_field = 'author'

    def test_func(self):
        obj = self.get_object()
        author = getattr(obj, self.author_field, None)
        return self.request.user == author or self.request.user.is_superuser
