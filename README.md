# Blog1.github.io

<!doctype html>
<html lang="en">

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
        integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

    <title>
        {% block title %}

        Blogs Page

        {% endblock %}
    </title>
</head>

<body>

    <nav class="navbar navbar-expand-sm navbar-dark bg-dark">

        <ul class="navbar-nav">

            <li class="navbar-item active">
                <a class="nav-link" href="{% url 'home' %}">Home</a>
            </li>

            {% if user.is_authenticated %}

            <li class="navbar-item active">
                <a class="nav-link" href="{% url 'App_Blog:create_blog' %}">Write Blog</a>
            </li>

            <li class="navbar-item active">
                <a class="nav-link" href="{% url 'App_Login:logout' %}">Logout</a>
            </li>
            <li class="navbar-item active">
                <a class="nav-link" href="{% url 'App_Login:profile' %}">Profile</a>
            </li>

            {% else %}

            <li class="navbar-item active">
                <a class="nav-link" href="{% url 'App_Login:signup' %}">Sign Up</a>
            </li>
            <li class="navbar-item active">
                <a class="nav-link" href="{% url 'App_Login:signin' %}">Login</a>
            </li>

            {% endif %}
        </ul>

        {% if user.is_authenticated %}

        <div class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" id="navbardrop" data-toggle="dropdown">
                {{ user.username }}
            </a>

            <div class="dropdown-menu">
                <a class="dropdown-item" href="{% url 'App_Login:profile' %}">Your Profile</a>
                <a class="dropdown-item" href="{% url 'App_Login:logout' %}">Logout</a>
                
              </div>
        </div>
        {% endif %}

    </nav>

    <div class="container" style="padding-top: 25px;">

        {% block body_block %}

        {% endblock %}

    </div>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
        integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
        crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
        integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
        crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
        integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
        crossorigin="anonymous"></script>
</body>

</html>
