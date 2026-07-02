class MediaError(Exception):
    """Custom exception for media-related errors."""

    def __init__(self, message, obj):
        # Initialize the parent Exception class with the error message.
        super().__init__(message)

        # Store the object that caused the error for later inspection.
        self.obj = obj


class Movie:
    """Parent class representing a movie."""
    
    def __init__(self, title, year, director, duration):
        # Reject a title that is empty or contains only whitespace.
        if not title.strip():
            raise ValueError('Title cannot be empty')

        # Movies released before 1895 are not accepted.
        if year < 1895:
            raise ValueError('Year must be 1895 or later')

        # Reject a director name that is empty or contains only whitespace.
        if not director.strip():
            raise ValueError('Director cannot be empty')

        # The movie duration must be greater than zero.
        if duration <= 0:
            raise ValueError('Duration must be positive')

        # Store the validated movie data as instance attributes.
        self.title = title
        self.year = year
        self.director = director
        self.duration = duration

    def __str__(self):
        # Return a readable string representation of the movie.
        return (
            f'{self.title} ({self.year}) - '
            f'{self.duration} min, {self.director}'
        )


class TVSeries(Movie):
    """Child class representing an entire TV series."""

    def __init__(
        self,
        title,
        year,
        director,
        duration,
        seasons,
        total_episodes,
    ):
        # Reuse the Movie constructor to validate and initialize the
        # shared title, year, director, and duration attributes.
        super().__init__(title, year, director, duration)

        # A TV series must contain at least one season.
        if seasons < 1:
            raise ValueError('Seasons must be 1 or greater')

        # A TV series must contain at least one episode.
        if total_episodes < 1:
            raise ValueError('Total episodes must be 1 or greater')
        
        # Store the attributes that are specific to a TV series.
        self.seasons = seasons
        self.total_episodes = total_episodes

    def __str__(self):
        # Override the Movie representation with TV-series information.
        return (
            f'{self.title} ({self.year}) - '
            f'{self.seasons} seasons, '
            f'{self.total_episodes} episodes, '
            f'{self.duration} min avg, '
            f'{self.director}'
        )


class MediaCatalogue:
    """A catalogue that can store different types of media items."""

    def __init__(self):
        # Create an empty list for storing movies and TV series.
        self.items = []

    def add(self, media_item):
        # TVSeries inherits from Movie, so this check accepts both
        # Movie and TVSeries instances.
        if not isinstance(media_item, Movie):
            raise MediaError(
                'Only Movie or TVSeries instances can be added',
                media_item,
            )

        # Add the validated media item to the catalogue.
        self.items.append(media_item)

    def get_movies(self):
        # Use type(item) is Movie to exclude TVSeries objects because
        # TVSeries is a subclass of Movie.
        return [
            item
            for item in self.items
            if type(item) is Movie
        ]

    def get_tv_series(self):
        # Return only the TVSeries objects stored in the catalogue.
        return [
            item
            for item in self.items
            if isinstance(item, TVSeries)
        ]
    
    def __str__(self):
        # Return a specific message when the catalogue contains no items.
        if not self.items:
            return 'Media Catalogue (empty)'
        
        # Separate movies and TV series into different lists.
        movies = self.get_movies()
        series = self.get_tv_series()

        # Start the output with the total number of catalogue items.
        result = f'Media Catalogue ({len(self.items)} items):\n\n'

        # Add the movie section only when the catalogue contains movies.
        if movies:
            result += '=== MOVIES ===\n'

            # Number the movies starting from 1.
            for i, movie in enumerate(movies, 1):
                result += f'{i}. {movie}\n'

        # Add the TV-series section only when at least one series exists.
        if series:
            result += '=== TV SERIES ===\n'

            # Number the TV series starting from 1.
            for i, movie in enumerate(series, 1):
                result += f'{i}. {movie}\n'
        
        # Return the fully formatted catalogue.
        return result


# Create an empty media catalogue.
catalogue = MediaCatalogue()

try:
    # Create and add the first movie.
    movie1 = Movie(
        'The Matrix',
        1999,
        'The Wachowskis',
        136,
    )
    catalogue.add(movie1)

    # Create and add the second movie.
    movie2 = Movie(
        'Inception',
        2010,
        'Christopher Nolan',
        148,
    )
    catalogue.add(movie2)

    # Create and add the first TV series.
    series1 = TVSeries(
        'Scrubs',
        2001,
        'Bill Lawrence',
        24,
        9,
        182,
    )
    catalogue.add(series1)

    # Create and add the second TV series.
    series2 = TVSeries(
        'Breaking Bad',
        2008,
        'Vince Gilligan',
        47,
        5,
        62,
    )
    catalogue.add(series2)

    # Print the complete catalogue.
    # This automatically calls MediaCatalogue.__str__().
    print(catalogue)

except ValueError as e:
    # Handle invalid values used to create a Movie or TVSeries object.
    print(f'Validation Error: {e}')

except MediaError as e:
    # Handle an unsupported object being added to the catalogue.
    print(f'Media Error: {e}')

    # Display the invalid object and its data type.
    print(f'Unable to add {e.obj}: {type(e.obj)}')
