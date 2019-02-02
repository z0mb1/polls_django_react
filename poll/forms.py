from django import forms

class AnonUserParamsForm(forms.Form):
    GENDER = (
       (1, ("man")),
       (2, ("woman")), 
    )
    AGE = (
       (1, ("<18")),
       (2, ("18-25")), 
       (3, ("25-35")), 
       (4, ("35-50")), 
       (5, (">50")), 
    )
    age = forms.ChoiceField(choices=AGE)
    sex = forms.ChoiceField(choices=GENDER)
