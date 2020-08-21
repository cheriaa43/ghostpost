from django import forms
from ghost_post.models import Boast_Roast

# help from Chris Warren
class PostForm(forms.ModelForm):
   class Meta:
       model = Boast_Roast
       fields = ['content', 'post_type']
