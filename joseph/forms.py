from django import forms


class RawFeedbackForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "w3-input w3-border",
                "id": "",
                "placeholder": "Your name",
                "type": "text"
            }
        )
    )
    Email_address = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "w3-input w3-border",
                "id": "",
                "placeholder": "Email address"
            }
        )
    )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "w3-input w3-border",
                "id": "",
                "placeholder": "What would you like to tell me",
                "rows": 5,
                "cols": 30,
            }
        )
    )
