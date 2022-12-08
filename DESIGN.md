## Comp880 Project Top 100 Anime Movies

## Design Document

## Author: G.Deepika, Pooja Bandla

### class AnimeData:


    Represent a class anime .

    Explains methods that transform input collections into something else.

### def init(self, filename :str):

    Initialize instance variables.

        Parameters:
            filename: string
*Initialize the variables of self.filename and self.dic.


### def genre_list(self, genre: str) -> list:
        
        Create list of anime names with genre details.

        Note that each anime may come under multiple genres.
        Creates and returns a list of anime that come under genre requested.

        Parameters:
            genre: string

        Return:
            list of str, each string being a anime under specified genre.

* To get to recommend anime first create a method `genre_list` to get the anime-names based on genre.
* In the method genre_list create the empty list as `return_list` to store the output.
* Create for loop assign the `self.dict` which contains the titles to `d_s`.
     * Within the for loop assign if statement.
     * Assign the self.dic of `d_s` and `genre` in genre iterator.
     * Append d_s to created return_list.
* Return the `return_list` which return the result anime-names .

### def recommended_anime(self, anime_name: str, num_rmd: int) -> list:
        
        Create a list of recommended anime.

        Return a list of anime names that are related to the reference anime
        and return the top rated animes if there are not enough
        recommendations.

        Parameter:
            anime_name: str, name of the reference anime
            num_rmd: int, number of recommendation required

        Return:
            list of str, each element representing recommended anime

* To create a list of recommended anime define the method `recommended_anime` with the parameters of anime_name which is string refers to the name of anime and num_rnd is integer refers to the number of recommendations required.If the given name is not in the self.dic then return nothing.
* Assign the self.dic of anime_name to `anime_genre` and create empty list as `recommend`.
* In for loop assign the anime_genre to r_m.
    * Call the function genre_list with r_m to recommend.
    * To remove the repetition in the return list use set to recommend list then remove the anime_name in the recommended which is not in that genre.
    * If len of recommend is less than number of recommendations 
       * Assign the for loop of self.dic to n_m.
       * if n_m is not in recommend and not same to anime_name append the n_m to recommend.
       * if length of recommend is equal to number of recommendations break the loop 
* Return the recommend based on number of recommendations.




 


    
