from django import forms

from .models import Idea


class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        exclude = ["status"]
        widgets = {
            "idea_brief": forms.Textarea(attrs={"rows": 3}),
            "problem": forms.Textarea(attrs={"rows": 3}),
            "audience": forms.Textarea(attrs={"rows": 3}),
            "feasible": forms.Textarea(attrs={"rows": 3}),
            "competitors": forms.Textarea(attrs={"rows": 3}),
        }
