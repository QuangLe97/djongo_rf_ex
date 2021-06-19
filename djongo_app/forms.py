from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple

from djongo_app.models import Author, ArticleEntry


class ArticleEntryChangeListForm(forms.ModelForm):
    # here we only need to define the field we want to be editable
    authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all(),
                                             required=False, widget=FilteredSelectMultiple('authors', False))

    class Meta:
        model = ArticleEntry
        fields = '__all__'
        # fields = ['blog ', 'content', 'authors_add']
