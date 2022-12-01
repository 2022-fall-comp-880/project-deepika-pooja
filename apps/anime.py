"""
Represent a data-set of NBA player information.

Authors:

"""


class AnimeData:
    """
    Represent a class anime

    Explain methods that transform input collections into something else.
    """

    def __init__(self, Anime_info):
        """
        Make a class anime
        Attributes:
            Title: string
            Gross-value: integer
            Duration: integer
            Genre: string
        """

    def write(self, filename: str):
        """
        Data with anime moives

        filename: filename to write data
        """

    def recommended_anime(self) -> list:
        """
        return: List
        Example: recommended_anime(Enter the anime you like, and we will find more like those for you  :death note
        Please enter the number of recommendations you want:4
        the anime recommended for you are :
                 1 .  death note rewrite
                 2 .  higurashi no naku koro ni kai
                 3 .  jigoku shoujo mitsuganae
                 4 .  yakushiji ryouko no kaiki jikenbo
        """

    def gross_avg(self) -> dict:
        """
        Ranges are "1980-1990", "1990-2000",
        "2000-2005", and so on.
        Ranges are determined based on the data-set.

        Returns:dictionary
                keys: Representing Year ranges
                values: Average of those years gross value
        Example: {1980-1990 : avg value of gross}
        """

    def avg_duration(self) -> dict:
        """
        Returns: dictionary
                 keys: string, representing genre
                 values: Integer,average of duration of genre
        Example: {Action: Avg of duration}
        """


def read_dataset(filename: str) -> AnimeData:
    """Create the read dataset which return the anime object."""
