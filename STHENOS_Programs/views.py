from django.http import HttpResponse
from django.shortcuts import render
from django import forms
from io import BytesIO  # Import BytesIO for in-memory buffer
from .pdfGenerator import generate_pdf

# Create your views here.
def programs(request):
      if request.method == 'POST':
            form = ProgramForm(request.POST)
            if form.is_valid():
                  # Process the data in form.cleaned_data
                  bench_press_max = form.cleaned_data['bench_press_max']
                  squat_max = form.cleaned_data['squat_max']
                  deadlift_max = form.cleaned_data['deadlift_max']
                  pseudonyme = form.cleaned_data['pseudonyme']
                  unit = form.cleaned_data['unit']
                  return generate_pdf_view(bench_press_max,squat_max,deadlift_max,pseudonyme,unit)
              
      else:
            user = request.user
            if user.is_authenticated:
                  initial_data = {
                        'bench_press_max': request.user.benchMax,
                        'squat_max': request.user.squatMax,
                        'deadlift_max': request.user.deadLiftMax,
                        'pseudonyme': request.user.username,
                  }
            else :
                  initial_data = {}
      form = ProgramForm(initial=initial_data)


      context = {
            'current_page': 'programs',
            'userCharacForm': form
      }
      return render (request,"programs.html", context)

class ProgramForm(forms.Form):
      error_messages={
            'required': 'This field is mandatory.',
            'min_value': 'Enter a value greater than or equal to 0.',
            'max_value': 'Enter a value less than or equal to 500.',
      }
   
      bench_press_max = forms.IntegerField(
            label="Bench Press Max",
            min_value=0,
            max_value=500,
            error_messages=error_messages,
      )
      
      squat_max = forms.IntegerField(
            label="Squat Max",
            min_value=0,
            max_value=500,
            error_messages=error_messages,
      )
      
      deadlift_max = forms.IntegerField(
            label="Deadlift Max",
            min_value=0,
            max_value=500,
            error_messages=error_messages,
      )
      
      pseudonyme = forms.CharField(
            required=True,
            initial="me",
            label="Pseudonyme of the user",
      )
      
      unit = forms.ChoiceField(
            choices=[('kg', 'Kilograms'), ('lbs', 'Pounds')],
            label="Unit",
      )

      def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            
            # Add title attributes for tooltips
            self.fields['bench_press_max'].widget.attrs.update({'title': self.fields['bench_press_max'].help_text})
            self.fields['squat_max'].widget.attrs.update({'title': self.fields['squat_max'].help_text})
            self.fields['deadlift_max'].widget.attrs.update({'title': self.fields['deadlift_max'].help_text})
            self.fields['pseudonyme'].widget.attrs.update({'title': self.fields['pseudonyme'].help_text})
            self.fields['unit'].widget.attrs.update({'title': self.fields['unit'].help_text})


def generate_pdf_view(benchMax,squatMax,deadLiftMax,username,unit):
      # Generate PDF
      
      pdf = generate_pdf(benchMax, squatMax, deadLiftMax, username,unit)

      # Create a BytesIO buffer to hold the PDF data
      buffer = BytesIO()

      # Save the PDF to the buffer
      pdf_output = pdf.output(dest='S')  # Output PDF to a byte string
      buffer.write(pdf_output)  # Directly write the byte string to the buffer
      buffer.seek(0)  # Reset the buffer's position to the beginning

      # Create the HTTP response with PDF content
      response = HttpResponse(buffer.getvalue(), content_type='application/pdf')
      response['Content-Disposition'] = 'attachment; filename="sthenos_title.pdf"'
      
      return response

