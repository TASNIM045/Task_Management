from django import forms
from tasks.models import Task, TaskDetail

# Django Form
class TaskForm(forms.Form):
    title = forms.CharField(max_length=250, label='Task Title')
    description = forms.CharField(widget=forms.Textarea, label='Task Description')
    due_date = forms.DateField(widget=forms.SelectDateWidget, label='Due Date')
    assigned_to = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=[], label='Assigned To')

    def __init__(self,*args,**kwargs):
        employees = kwargs.pop("employees", [])
        super().__init__(*args,**kwargs)
        self.fields['assigned_to'].choices = [(emp.id,emp.name) for emp in employees]

class StyleFormMixIn:
    default_class = "w-full border border-rose-300 focus:ring-2 focus:ring-rose-400 focus:outline-none h-12 px-4 py-2 rounded-lg text-gray-700 placeholder-gray-400 shadow-sm"

    def apply_style_widgets(self):
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.TextInput):
                field.widget.attrs.update({
                    'class': self.default_class,
                    'placeholder': f"Enter {field.label.lower()}"
                })
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({
                    'class': f"{self.default_class}",
                    'placeholder': f"Enter {field.label.lower()}",
                    'rows': 5
                })
            elif isinstance(field.widget, forms.SelectDateWidget):
                field.widget.attrs.update({
                    'class': "border border-rose-300 focus:ring-2 focus:ring-rose-400 focus:outline-none h-12 px-4 py-2 rounded-lg text-gray-700 placeholder-gray-400 shadow-sm"
                })
            elif isinstance(field.widget, forms.CheckboxSelectMultiple):
                field.widget.attrs.update({
                    'class': "space-y-2",
                })
            else :
                field.widget.attrs.update({
                    'class' : self.default_class,
                })                

# Django ModelForm
class TaskModelForm(StyleFormMixIn, forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'assigned_to']
        widgets = {
            'due_date' : forms.SelectDateWidget,
            'assigned_to' : forms.CheckboxSelectMultiple
        }

        ''' Manual Widgets '''
        # widgets = {
        #     'title': forms.TextInput(attrs={
        #         'class': 'w-full border border-rose-300 focus:ring-2 focus:ring-rose-400 focus:outline-none h-12 px-4 py-2 rounded-lg text-gray-700 placeholder-gray-400 shadow-sm',
        #         'placeholder': "Enter task title",
        #     }),
        #     'description': forms.Textarea(attrs={
        #         'class': 'w-full border border-rose-300 focus:ring-2 focus:ring-rose-400 focus:outline-none mt-4 px-4 py-3 rounded-lg text-gray-700 placeholder-gray-400 shadow-sm resize-none',
        #         'placeholder': "Enter task description",
        #         'rows': 4,
        #     }),
        #     'due_date': forms.SelectDateWidget(attrs={
        #         'class': 'border border-rose-300 focus:ring-2 focus:ring-rose-400 focus:outline-none mt-4 px-2 py-2 rounded-lg text-gray-700 shadow-sm',
        #     }),
        #     'assigned_to': forms.CheckboxSelectMultiple(attrs={
        #         'class': 'space-y-2 mt-4 text-gray-700',
        #     }),
        # }        

    '''Widgets Using MixIn'''
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.apply_style_widgets()


class TaskDetailModelForm(StyleFormMixIn,forms.ModelForm):
    class Meta:
        model = TaskDetail
        fields = ['priority','notes']

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.apply_style_widgets()