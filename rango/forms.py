from django import forms 
from rango.models import Page, Category

class CategoryForm(forms.ModelForm):
	name = forms.CharField(max_length=Category.MAXLENGTH,help_text="Please enter the category name.")
	views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	slug = forms.CharField(widget=forms.HiddenInput(), required = False) # Ppopulated by C.save()
	
	class Meta:
		fields = ('name',)
		model = Category
		
class PageForm(forms.ModelForm):
	title = forms.CharField(max_length=128,help_text="Please enter the title of the page")
	url = forms.URLField(max_length=200, help_text="Please enter the URL of the page.")
	views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

	
	def clean(self):
		cleaned_data = self.cleaned_data
		url = cleaned_data.get('url')
		
		if url and not url.statswith('http://'):
			url = 'http://' + url
			cleaned_data['url'] = url
			return cleaned_data

	class Meta: # Defined so we know which model to provide the form for
		model = Page
		exclude = ('category',)
