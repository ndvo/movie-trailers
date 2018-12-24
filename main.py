import os
import BaseHTTPServer
import movie_data
import page
from request_handler import RequestHandler
from movie_collection import Collection
from response import Response

# Create a nickname for os.paht.join
j = os.path.join
# Create the server
server = BaseHTTPServer.HTTPServer(('', 8080), RequestHandler)

collection = Collection()

for movie in movie_data.movies:
    collection.add_movie(movie)


def main_page():
    """
    Create the main page 

    Returns a Response Object with a list of movies sorted by title.
    """
    css = open(j('styles', 'main.css')).read()
    js = open(j('scripts', 'main.js')).read()
    movie_page = page.Component('page', {'styles': css, 'js': js},  'page.html')
    movie_list = page.Component(
            'movie_list',
            {'movies': ''},
            'movie_list.html'
            )
    movie_page.components.append(movie_list)
    movie_list.components.append(
        [page.Component('movies', movie,  'movie_card.html')
            for key, movie in collection.sort_by_title().iteritems()])
    return Response(body=movie_page.render())


def movie_page():
    """
    Create the Movie Page

    Returns a Response Object with further details of a specific movie
    """
    movie_page = page.Component()
    return Response(body=movie_page.render())

def create_routes():
    """
    Creates routes within RequestHandler static attribute routes

    Each route is a key, value pair. The key is a regular expression and the
    value is a function to be invoked by the RequestHandler class.
    """
    RequestHandler.routes[r'/'] = main_page
    RequestHandler.routes[r'/movie/\w+'] = movie_page


print "*** Movie Website running ***"
print "    http://localhost:8080    "
create_routes()
server.serve_forever()
