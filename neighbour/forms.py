from django import forms

from neighbour.models import Business

class BusinessRegistrationForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['name', 'category', 'image', 'location']

    def __init__(self, *args, **kwargs):
        super(BusinessRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder']='Business Name...'
        self.fields['category'].widget.attrs['placeholder']='Business Category/Type...'

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'