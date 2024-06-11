# Django URL Shortener

## Overview
![image](https://github.com/PraveenGupta11001/Django-URL-Shortener/assets/105053871/edd253f9-19dd-4f1d-af75-fdf5c43a72d5)

The Django URL Shortener is a web application built using the Django framework. It allows users to convert long URLs into short, manageable links. Users can input long URLs, and the system generates a unique short URL that redirects to the original link. This project includes functionality for creating, retrieving, and managing short URLs.

## Features

- **URL Shortening**: Users can input long URLs, and the system generates a unique short URL.
- **URL Redirection**: Short URLs redirect to the original long URL.
- **Dashboard**: Users can view all their shortened URLs and manage them.

## Technologies Used

- **Django**: The web framework used to build the application.
- **Python**: The programming language used for backend development.
- **HTML/CSS**: For creating the frontend interface.
- **SQLite**: The database used by Django for storing URL data.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/url-shortener.git
    cd url-shortener
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv url_shortener_env
    source url_shortener_env/bin/activate  # On Windows use `url_shortener_env\Scripts\activate`
    ```

3. **Install requirements**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

## Usage

1. **Shorten a URL**:
   - Enter a long URL in the provided form.
   - Optionally, provide a custom alias for the shortened URL.
   - Submit the form to get the shortened URL.

2. **Access Shortened URLs**:
   - Use the generated short URLs to redirect to the original long URLs.
