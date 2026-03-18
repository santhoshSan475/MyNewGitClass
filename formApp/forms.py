from django import forms

class dummyForm(forms.Form):
    username = forms.CharField(min_length=3, max_length=200,label="USERNAME")
    password = forms.CharField(min_length=3,max_length=100, widget=forms.PasswordInput)
    email = forms.EmailField(max_length=150, widget=forms.EmailInput)
    gender = forms.ChoiceField(choices=[("female","Female",),("male","Male"),("others","others")], widget=forms.RadioSelect)
    langauge = forms.ChoiceField(choices=[("python","Python"),("javascript","Javascript"),("java","Java"),(".net",".Net")])
    season = forms.MultipleChoiceField(choices=[("summer","Summer"),("winter","Winter"),("monsoon","Monsoon"),("autumn","Autumn")])
    auth = forms.BooleanField(label="authentication")
    date = forms.DateField(widget=forms.DateInput(attrs={"type":"date"}))
    file = forms.FileField()
    image = forms.ImageField()
    text = forms.CharField(widget=forms.Textarea)