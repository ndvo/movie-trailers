# movie-trailers
A movies website for Udacity Nanodegree

## Instalation and usage

1. Install Python 2.7 or later (There is no need of this if you're on Linux or Mac)
1. Download and unzip the file from github or clone the repository
1. On a terminal, navigate to the site folder and run the main.py file with the following command:
    python main.py
1. Open a browser and navigate to http://localhost:8080

## The project

This project creates a HTML page to display a collection of Movie Trailers. It was built as part of Udacity's FullStack Development Nanodegree.

There is:
- a **Movie** class that holds the **model** for the movies.
- a **Component** class that creates HTML pieces that can be combined to form a page
- a **RequestHandler** class that handles HTTP requests and routing
- a **Response** class used to send HTTP responses

The data:
- is stored as a python list of Movie instances
- no database is being used
- there is a **Collection** class meant to be used to filter the results (but it is very rudimentar and is not being used yet.

## Templating:
- Python's native string templates are used to build the HTML
- Each component has a components attribute and upon rendering it's template with data, it renders all of it's components first, storing the results as data for the rendering of it's own template.
- Let's look at an example:
  - Page has three components:
    - header
    - main
    - footer
  - Header has one component
    - nav
  - Main has one component
    - MovieList
  - When we render Page, it first renders header, main and footer. Header and footer render nav and MovieList before rendering themselves. Upon rendering the components store the results in a data attribute to be used in other components.
