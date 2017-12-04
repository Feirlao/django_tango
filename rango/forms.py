from django import forms

from rango.models import Page,Category,User,Userprofile

class CategoryForm(forms.ModelForm):
    name=forms.CharField(max_length=128,help_text="enter the category name:")
    views=forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    likes= forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model=Category
        fields=('name',)

class PageFarm(forms.ModelForm):
    title= forms.CharField(max_length=128, help_text="enter the title of the page")
    url= forms.URLField(max_length=128, help_text="enter the url of the page:")
    views=forms.IntegerField(widget=forms.HiddenInput(),initial=0)

    class Meta:
        model=Page

        exclude=('category',)

    def clean(self):
        cleaned_data=self.cleaned_data
        url=cleaned_data.get('url')

        if url and not url.startswith('https://'):
            url='https://'+url
            cleaned_data['url']=url
            return cleaned_data

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=('username','email','password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model=Userprofile
        fields=('website','picture')



