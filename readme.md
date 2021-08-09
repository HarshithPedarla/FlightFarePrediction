# Installing Dependencies

We have created a virtual environment "env" using the `virtualenv` library.

```bash
pip install virtualenv
virtualenv env
```

We then activated this environment and installed all our necessary library inside it using `pip`

```bash
source env/bin/activate
pip install django
```

# Working process

## Project creation

We have created a new django project using `django-admin`

```bash
django-admin startproject mysite .
```

## App creation

We have created an app `flight_prediction` in our `mysite` django

## Creating html template for our app

We have created our all our html files inside a `templates` directory of our app

## Creating form for our app

We have created our form to enter specific field data in the `forms.py` file

## Rendering view and prediction

We have defined a `predict_model()` function to our render our form and do prediction using the trained model that is stored inside `ml_model` folder

## Calling the view on app launch

We have used the previously defined view method `predict_model` for root url path and defined it like below in `urls.py` file of our `mysite` project

```python
path("",views.predict_model,name='predict_model')
```

## Using the trained model to make prediction

When request is sent using `Post` method, we are getting each form field data corresponding to our data columns. We then verify, clean and modify these received form datas, so that we can use them for making prediction.
Finally we load our `trained model` and pass the testing processed data to it. Once we receive the prediction, we then pass it back to view in our frontend.

```python
prediction = loaded_model.predict(model_features)[0]
print(prediction)
return render(request, 'home.html', {'my_form': form, 'prediction': prediction})
```

## Deployment

Once our app has been created, we then deployed it to heroku to this url [flight-prediction-django.herokuapp.com](https://flight-prediction-django.herokuapp.com/)
