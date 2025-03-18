from django import forms





class TaskForm(forms.Form):
    title = forms.CharField(label='Titulo', max_length=200)
    description = forms.CharField(label='Descripcion',required=False,widget=forms.Textarea)
    date_created = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    date_limit = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    priot = forms.ChoiceField(label='Prioridad', choices=[
        ('BAJA', 'Baja'),
        ('MEDIA', 'Media'),
        ('ALTA', 'Alta')
    ])

