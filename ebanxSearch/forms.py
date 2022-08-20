from django import forms
from ebanxSearch.models  import Department


class DepartmentListForm(forms.ModelForm):
    # here we only need to define the field we want to be editable
    department = forms.ModelMultipleChoiceField(
        queryset=Department.objects.all(), required=False)