from django import forms
from tasks.models import Task, Tag


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["content", "deadline", "is_done", "tags"]
        widgets = {
            "tags": forms.CheckboxSelectMultiple(),
            "deadline": forms.DateTimeInput(attrs={
                "placeholder": "YYYY-MM-DD HH:MM",
                "type": "text",
            }),
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]
