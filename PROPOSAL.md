# TOP 100 Anime Movies

**Author** : G Deepika

**Date** : 16-11-2022

## Motivation
* Anime is a style of Japanese film and television animation,It aims to help answer questions in regard to popularity of anime, given their scores, popularity ranks, studios, etcetera. I think this dataset might be helpful for a plethora of uses, such as making recommendation systems, visualizing trends in anime popularity and score, predicting scores and popularity, and such. My project dataset contains the top 100 anime movies based on their rating. It also contains the anime's rating, number of votes, year, length of the movies and more.This is basically giving us an idea like what you want to see without it being curated and it being on preferences.

## Investigative Questions
1. Based on the recommended anime and the number of recommendations get the animes more like those.
2. In the given of year range get the average of gross value.
3. What is the average duration in each genre?

## Approach
* The data set of the project was taken from kaggle.com.
* The size of the dataset is top 100 anime's with 8 different columns.
* On kaggle platform student kaggle master ayessa contributed the dataset with the latest update on October 31st and the dataset has been released under the Apache 2.0 open source license.
* To create the project we need to define the `method` which explores the data. 
* With `class` Anime find the genre, movie duration in which years anime released, how much the movie gross price and the top 10 movies with most votes.

## Expected Results
* In the given dataset to define the best anime the attributes should be defined in the dictionary which access time is just besides easy to manage it's easy to sort.
* By defining the genre we will get the single data string for the given genre.
* By assigning the rating's range we will get the output with the least rated anime title.
* In the given dataset with different genre the output is expected to show only the action genre anime seperated and same with the other genre too.

## New Python Packages or Modules
* In this project we will use the import os  to handle the current working directory
* Import csv is used to read and extract the data from the file. 

## Dataset Documentation
* In this project the dataset name is `Top 100 anime movies`.
* It is the version of  and the latest updated was on october 31st.
* The owner of the dataset is Ayessa a kaggle master contributor.
* The dataset has been released under the Apache 2.0 open source license.
* The dataset is open source can be access in kaggle.com.
* Dataset contains of 8 attributes:
    * rank	  : the anime's rank
    * Title	  : the anime's title
    * Rating  :	the anime's rating
    * Votes	  : the number of reviewers that rated this anime
    * year	  : year this anime was released
    * Minutes : the length of this anime in minutes
    * genre	  : the genre of this anime
    * gross	  : the gross of this anime
