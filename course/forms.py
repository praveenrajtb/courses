from django.forms import ModelForm
from .models import Course
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = [
            'title', 'image', 'category', 'start_date', 'end_date', 'author', 'slug'
        ]
        # widgets = pass

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save course'))
        self.helper.add_input(Submit('cancel', 'Cancel', css_class='btn-danger', ))

