from django import forms

from .models import UserEntry, Breed


class UserEntryCreationForm(forms.ModelForm):
    class Meta:
        model = UserEntry
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['breed'].queryset = Breed.objects.none()   

        if 'animal' in self.data:
            try:
                animal_id = int(self.data.get('animal'))
                self.fields['breed'].queryset = Breed.objects.filter(animal_id=animal_id).order_by('breed')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty breed queryset
        elif self.instance.pk:
            self.fields['breed'].queryset = self.instance.animal.breed_set.order_by('breed')

    def __init__(self, *args, **kwargs):
        super(UserEntryCreationForm, self).__init__(*args, **kwargs)
      
        self.fields['date'].widget.attrs['placeholder'] = 'Date'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
