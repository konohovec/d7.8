from django import forms  
from p_library.models import Author, Book, Friend, UserProfile
from django.forms import formset_factory  


class AuthorForm(forms.ModelForm):  
	full_name = forms.CharField(widget=forms.TextInput)  

	class Meta:
		model = Author  
		fields = '__all__'

class BookForm(forms.ModelForm):  
	
    class Meta:  
        model = Book  
        fields = '__all__'


class FriendAdminForm(forms.ModelForm):

    name = forms.CharField(label='Имя друга', widget=forms.TextInput)


class FriendForm(forms.ModelForm):

    name = forms.CharField(label='Имя друга', widget=forms.TextInput)
    books = forms.ModelMultipleChoiceField(
        label='Книги',
        queryset=Book.objects,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Friend
        fields = '__all__'


class FriendEditForm(forms.ModelForm):

    name = forms.CharField(label='Имя друга', widget=forms.TextInput)

    class Meta:
        model = Friend
        fields = ('name',)



class ProfileCreationForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        exclude = ('uid', 'user',)


class UserProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        exclude = ('uid', 'user',)