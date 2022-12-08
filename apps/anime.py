
    def genre_list(self, genre: str) -> list:
        """
        Create list of anime names with genre details.

        Note that each anime may come under multiple genres.
        Creates and returns a list of anime that come under genre requested.

        Parameters:
            genre: string

        Return:
            list of str, each string being a anime under specified genre.
        """
        return_list = []
        for d_s in self.dic:
            if genre in self.dic[d_s]['genre']:
                # print(genre)
                return_list.append(d_s)
        # print(return_list)
        return return_list

    def recommended_anime(self, anime_name: str, num_rmd: int) -> list:
        """
        Create a list of recommended anime.

        Return a list of anime names that are related to the reference anime
        and return the top-rated animes if there are not enough
        recommendations.

        Parameter:
            anime_name: str, name of the reference anime
            num_rmd: int, number of recommendation required

        Return:
            list of str, each element representing recommended anime
        """
        if len(self.dic) == 0 or anime_name not in self.dic:
            return []
        # print(anime_name)
        anime_genre = self.dic[anime_name]
        # print(anime_genre)
        recommend = []
        for r_m in anime_genre:
            # print(i)
            recommend = recommend + self.genre_list(r_m)
        recommend = list(set(recommend))
        if anime_name in recommend:
            recommend.remove(anime_name)
        if len(recommend) < num_rmd:
            for n_m in self.dic:
                if n_m not in recommend and n_m != anime_name:
                    recommend.append(n_m)
                if len(recommend) == num_rmd:
                    break
        # print(recommend[:num_rmd])
        return recommend[:num_rmd]
