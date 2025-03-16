from django import forms

class GroupForm(forms.Form):
    group_name = forms.CharField(max_length=20, error_messages={"required": "Group Name can't be empty"})