from django.shortcuts import render,redirect
from .forms import ModelForm
from datetime import *
import pickle
from django.contrib import messages #import messages


loaded_model = None
# Create your views here.
def home(request):
    return render(request, 'home.html')

def predict_model(request):
    # if this is a POST request we need to process the form data
    global loaded_model
    if loaded_model is None:
        loaded_model = pickle.load(open("ml_model/flight_rf2.pkl", 'rb'))
    emptyForm = ModelForm()
    prediction=None
    if request.method == 'POST':
       
        # create a form instance and populate it with data from the request:
        form = ModelForm(request.POST)
        
        # check whether it's valid:
        if form.is_valid():
            print("I am here")
            print(form.cleaned_data)
            # process the data in form.cleaned_data as required
            Total_Stops = form.cleaned_data['Total_Stops']
            Airline = form.cleaned_data['Airline']
            Source = form.cleaned_data['Source']
            Destination = form.cleaned_data['Destination']
            Journey_Date = form.cleaned_data['Journey_Date']
            Departure_Time = form.cleaned_data['Departure_Time']
            Arrival_Time = form.cleaned_data['Arrival_Time']
            Duration_hour = form.cleaned_data['Duration_hour']
            Duration_min = form.cleaned_data['Duration_min']
            test_data=[]
            airline_list = [0 for i in range(11)]
            source_list = [0 for i in range(4)]
            dest_list = [0 for i in range(5)]
            airline_list[int(Airline)-1]=1
            source_list[int(Source)-1]=1
            dest_list[int(Destination)-1]=1
            

            print("Total_Stops: {},Airline: {},Source: {},Destination: {},Journey_Date:{},Departure_Time:{},Arrival_Time: {}".format(Total_Stops,Airline,Source,Destination,Journey_Date,Departure_Time, Arrival_Time))

            # Journey_Date = datetime.strptime(Journey_Date, "%Y-%m-%d")
            # Arrival_Time = datetime.strptime(Arrival_Time, "%H:%M:%S")
            # Departure_Time = datetime.strptime(Departure_Time, "%H:%M:%S")
           
            # print(Arrival_Time,Departure_Time,Journey_Date)
            print(Arrival_Time.hour,Arrival_Time.minute)
            print(Departure_Time.hour,Departure_Time.minute)
            print(Journey_Date.day,Journey_Date.month)
            test_data=[int(Total_Stops),Journey_Date.day,Journey_Date.month,Departure_Time.hour,Departure_Time.minute,Arrival_Time.hour,Arrival_Time.minute,Duration_hour,Duration_min]
            
            test_data+=airline_list+source_list+dest_list
            print(test_data)
            # give prediction response
            model_features = [
                test_data]
           
            prediction = loaded_model.predict(model_features)[0]
            prediction=round(prediction, 2)
            prediction = "Predicted price : {} ₹".format(prediction)
            # print(prediction)
            messages.success(request, prediction)
            # return render(request, 'home.html', {'my_form': emptyForm, 'prediction': prediction})
            return redirect('/',{'my_form': emptyForm, 'prediction': prediction})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ModelForm()

    return render(request, 'home.html', {'my_form': form})

