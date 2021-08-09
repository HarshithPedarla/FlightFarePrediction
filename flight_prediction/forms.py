from django import forms
from bootstrap_datepicker_plus import DatePickerInput, DateTimePickerInput,TimePickerInput

Airline_Choices =(
    ('1', 'Air India'), ('2', 'GoAir'),('3', 'IndiGo'),
       ( '4', 'Jet Airways'), ( '5', 'Jet Airways Business'),
      ( '6', 'Multiple carriers'),
      ( '7', 'Multiple carriers Premium economy'),( '8', 'SpiceJet'),
      ( '9', 'Trujet'), ('10','Vistara'), ('11', 'Vistara Premium economy'),
)

Source_choices = (
    ('1', 'Chennai'),( '2', 'Delhi'),( '3', 'Kolkata'), ('4', 'Mumbai'),
)

Destination_choices = (
    ('1', 'Cochin'),( '2', 'Delhi'),( '3', 'Hyderabad'), ('4', 'Kolkata'),('5', 'New Delhi'),
)
class ModelForm(forms.Form):
    Total_Stops = forms.IntegerField(label='Total Stops',initial="0",min_value=0)
    Airline = forms.ChoiceField(label='Airline', choices = Airline_Choices,widget= forms.Select(attrs={'class': 'form-control'}))
    Source = forms.ChoiceField(label='Source', choices = Source_choices,widget= forms.Select(attrs={'class': 'form-control'}) )
    Destination = forms.ChoiceField(label='Destination', choices = Destination_choices,widget= forms.Select(attrs={'class': 'form-control'}))
    Journey_Date = forms.DateField(label='Journey Date',
        widget=DatePickerInput(options={"format": "YYYY-MM-DD", 
                                      }))
    Departure_Time = forms.TimeField(label='Departure Time',
        widget=TimePickerInput()
    )
    Arrival_Time = forms.TimeField(label='Arrival Time',
        widget=TimePickerInput()
    )
    Duration_hour = forms.IntegerField(label='Duration Hour',initial="0",min_value=0 )
    Duration_min = forms.IntegerField(label='Duration Min',initial="0",max_value=59,min_value=0, )