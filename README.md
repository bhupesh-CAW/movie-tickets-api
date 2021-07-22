<p align="center">
  <a href="" rel="noopener">
 <!-- <img width=200px height=200px src="https://i.imgur.com/6wj0hh6.jpg" alt="Project logo"></a> -->
</p>

<h3 align="center">Movie-Ticket-Booking API</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()


</div>

---

<p align="center"> This is Movie ticket booking API created by Django Rest Framework. You can search the movie according to cinemas,city and ongoing shows. You can book any of  the shows. 
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
<!-- - [Deployment](#deployment) -->
- [Usage](#usage)
- [Built Using](#built_using)
- [TODO](#todo)
- [Contributing](../CONTRIBUTING.md)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

# 🧐 About <a name = "about"></a>

This is Movie ticket booking API created by Django Rest Framework. You can search the movie according to cinemas,city and ongoing shows. You can book any of  the shows. 

# 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

## Prerequisites

What things you need to install the software and how to install them.

```
Python >=3.8
Django >= 3.0 
Django-Rest-Framework = ANY
PipEnv - Environment setup
Pip
PostMan
```

Dependencies are

```
    'rest_framework',
    'rest_framework.authtoken',
    'allauth',
    'allauth.account',
    'rest_auth',
    'rest_auth.registration',
```

## Installing

A step by step series of examples that tell you how to get a development env running.

Say what the step will be

First, you need to clone the repo:

```
git clone https://github.com/jainbhupesh533/movie-tickets-api.git
```
then, after cloning you need to create virtual environment using pipenv 

```
pip install pipenv
```
Run the Shell
```
pipenv shell 
```
Now, Install all the dependencies

```
pipenv install -r requirements.txt
```
* IF above one is not working,
  ```
   pipenv lock --requirements
  ```

After activating the shell, we now setup the django-server

Make proper Migrations on python code
```
python manage.py migrate
```
Now, its the final step to run our API
```
python manage.py runserver
```

End with an example of getting some data out of the system or using it for a little demo.

<!-- ## 🔧 Running the tests <a name = "tests"></a>

Explain how to run the automated tests for this system.

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
``` -->

# 🎈 Usage <a name="usage"></a>

### 1.  First, after starting server open postman and create user by registering user

```
Post api/v1/rest-auth/register/ should be in json containing {
  "username": <>,
  "email": <>,
  "password1":<>,
  "password2": <>
}
```
- Afer registering User, you have to login to access your authentication token 
```
Post api/v1/rest-auth/login should be in json containing 
{
  "username":<>,
  "email":<>
  "password":<>
}
```
### 2. After login , you will get authentication token which you have to add in header parameters
```
{"Authorization": Token <>}
```

### 3. Movies API
```
  To Get All the movies use GET api/v1/movies
```

- To filter out the movies you can use filter query
```
api/v1/movies?movie_name=<search_string>
```
#### Note: You cant post the movies . Posting movie is only allowed for superusers.

##

### 4. Cinemas API 
```
  To Get All the movies use GET api/v1/cinema
```

- To filter out the movies you can use filter query
```
api/v1/cinema?city=<search_string>
```
#### Note: You cant post the Cinemas . Posting movie is only allowed for superusers.

##

### 5. ShowTimes API 

- Adding showtimes POST api/v1/showtimes/
```
{

        "booked_seats": <Integer_value>,
        "total_seats": <Integer_value>,
        "total_price": <Float_value>,
        "cinema_id": <id of cinema>,
        "movie_id": <id of movie>
}
```

- GET showtimes api/v1/showtimes

```
Filtering showTimes GET api/v1/showtimes?cine_id=<cinema_id> GET api/v1/showtimes?movie_id=<movie_id>
```
### *You can use multiple query parameters

##

### 6. Get show details based on city and movie 
 > Get all shows with cinema details and movie details GET api/v1/get_shows/

> Filtering shows on basis of city and movie
```
 GET api/v1/getshows?city=<cinema_city>
 GET api/v1/getshows?movie_name=<movie_string>
```
 *You can use multiple query parameters

### 7. Get Cinemas Query

  > Get all shows of a particular cinema along with the movie
  ```
  GET api/v1/getcinemas/
  Get /api/v1/getcinemas/?search_movie=Bahubali
  ```  

### 8. Personal Details 

- Making Personal Details POST api/v1/user-details

```
{
    "person_name":<name>,
    "person_email": <email>
}
```

- Get  Personal Details (api/v1/user-details)

### 9. Booking API

- Making Booking POST api/v1/booking/ 
```
{ 
  "details" : <details_id>,
  "qty": <integer_value>, 
  "show": <show_id> 
}
```

- Retrieving Booking GET 
```
api/v1/booking?book_id=<book_id>
```



<!-- 
## 🚀 Deployment <a name = "deployment"></a>

Add additional notes about how to deploy this on a live system. -->

# 🤓 Todo <a name='todo'></a>

- Implement UI for API  using react
- Implement jwt Authentication
- Convert date string into Date format in model
- Write queries on dates 
- Implement Email functionality after booking a ticket 

# ⛏️ Built Using <a name = "built_using"></a>

- [PostgreSql](https://www.postgresql.org/) - Database
- [Django](https://www.django.org/) - Web Framework
- [Django-RestFramework](https://www.django-rest-framework.org/) - Rest Framework


# ✍️ Authors <a name = "authors"></a>

- [Bhupesh Parakh](https://github.com/jainbhupesh533) - Idea & Initial work

See also the list of [contributors]() who participated in this project.
## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- Inspiration [Amar Jaiswal](https://github.com/) 
