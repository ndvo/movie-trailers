import media
import collections


class Collection():
    title_index = {}
    rating_index = {}

    for i in media.Movie.VALID_RATINGS:
        rating_index[i] = []

    def add_movie(self, movie):
        if (movie.title not in self.title_index):
            self.title_index[movie.title] = movie
            self.rating_index[movie.rating] = movie
            return movie.title+" added successfully"
        else:
            return False

    def get_movie_by_title(self, title):
        return self.title_index[title]

    def sort_by_title(self):
        return collections.OrderedDict(
                sorted(
                    self.title_index.iteritems(),
                    key=lambda t: t[0]
                    )
                )

    def remove_movie(self, movie):
        """Removes an object from the collection"""
        # get the title of the movie
        classname = movie.__class__.__name__
        if classname == 'Movie':
            to_remove = movie.title
        elif classname == 'str':
            to_remove = movie
        else:
            return False
        # remove from both indexes
        if (to_remove in self.title_index):
            movie = self.title_index[to_remove]
            self.rating_index[movie.rating].remove(movie)
            del self.title_index[to_remove]

    def reindex_movie(movie):
        self.remove_movie(movie.title)
        self.add_movie(movie)
