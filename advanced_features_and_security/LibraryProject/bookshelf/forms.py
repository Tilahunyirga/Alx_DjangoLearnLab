# forms.py

from django import forms

class BookSearchForm(forms.Form):
    search_term = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Search for books...'})
    )

    def clean_search_term(self):
        search_term = self.cleaned_data.get('search_term', '').strip()
        if not search_term:
            raise forms.ValidationError("Please enter a search term.")
        return search_term
