from django import forms
from .models import Emp

class FeedbackForm(forms.Form):
    email=forms.EmailField(label="Enter Your Email", required=True)
    name = forms.CharField(label="Enter Your Name", required=True)
    feedback = forms.CharField(label="Your Feedback", widget=forms.Textarea)
    
    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        
class EmpForm(forms.ModelForm):
    class Meta:
        model = Emp
        fields = ['name','emp_id','phone','address']