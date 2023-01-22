from django.core.exceptions import ValidationError
from django.forms import ModelForm

from .models import Group


class StudentFormAdmin(ModelForm):
    """  Форма для Студентов Админки"""

    def clean_student_group(self):
        """
        Проверяет, является-ли студент старостой в каких-либо группах.
        Если да, то убедитесь, что выбрана группа.
        """
        # Получаем группу, когда текущий студент является старостой

        groups = Group.objects.filter(leader=self.instance)

        if len(groups) > 0 and self.cleaned_data['student_group'] != groups[0]:
            """ """
            raise ValidationError(
                'Студент является старостой другой группы',
                code='invalid',
            )

        return self.cleaned_data['student_group']
