import os
import BaseHTTPServer
import movie_data
import page
from request_handler import RequestHandler
from movie_collection import Collection
from response import Response

addr = ('', 8080)
server = BaseHTTPServer.HTTPServer(addr, RequestHandler)

collection = Collection()

j = os.path.join

for movie in movie_data.movies:
    collection.add_movie(movie)


def main_page():
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
    movie_page = page.Component()
    return Response(body=movie_page.render())


RequestHandler.routes[r'/'] = main_page
RequestHandler.routes[r'/movie/\w+'] = movie_page

print "*** Movie Website running ***"
print "    http://localhost:8080    "

server.serve_forever()
