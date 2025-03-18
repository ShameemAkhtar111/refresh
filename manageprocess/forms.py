from django import forms
from .models import PGroup, Process

# class GroupForm(forms.Form):
#     group_name = forms.CharField(max_length=20, error_messages={"required": "Group Name can't be empty"})

# using model forms
class GroupForm(forms.ModelForm):
    class Meta:
        model = PGroup
        fields = '__all__'
        
        # customizing labels
        # labels = {
        #     "group_name": "OAF Group"
        # }

        error_messages = {
            "group_name":{
            "required": "Group name required"}
        }

class ProcessForm(forms.ModelForm):
    class Meta:
        model = Process
        fields = ['process_name', 'process_env', 'process_report', 'group']