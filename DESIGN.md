## Comp880 Project

## Design Document

### class AnimeData:

    Represent a class anime .

    Explains methods that transform input collections into something else.

### def init(self, Anime_info):

    Make a class anime
    Attributes: 
            Title: string
            Gross-value: integer
            Duration: integer
            Genre: string

### def write(self, filename: str):

    Data with anime moives
    
    filename: filename to write data to

* Write with open method with filename as `anime_info_file_obj`.
* Then in loop assign the required data.
* define `anime_info_row` and use f-string to get the data. 
* Write command data in `anime_info_file_obj` will be written into `anime_info_row`.

### def recommended_anime(self) -> list:

     return: List
     Example: recommended_anime(Enter the anime you like and we will find more like those for you  :death note
                      Please enter the number of recommendations you want:4
     the anime recommended for you are :
               1 .  death note rewrite
               2 .  higurashi no naku koro ni kai
               3 .  jigoku shoujo mitsuganae
               4 .  yakushiji ryouko no kaiki jikenbo

* Define the inputs with enter the anime you like and number of recommendations to get the data from users.
* Structure the for loop to run the iterations.
* Then return the list on based on the inputs.

### def gross_avg(self) -> dict:

    Ranges are "1980-1990", "1990-2000",
        "2000-2005", and so on.
        Ranges are determined based on the data-set.
    
    Returns:dictionary
            keys: Representing Year ranges
            values: Average of those years gross value
    Example: {1980-1990 : avg value of gross}
    
*  Assign the empty dictionary and an empty list.
*  In for loop assign the Anime_info to iterable variable.
*  define the syntax to run the loop and return the output. 
*  Return the output in the form of dictionary.


### def avg_duration(self) -> dict:

    Returns: dictionary
             keys: string, representing genre
             values: Integer,average of duration of genre
    Example: {Action: Avg of duration}



### def read_dataset(filename: str) -> AnimeData:

      Create the read dataset which return the anime object.

* Use command `open` to the filename and instruct as `f.open`.
* Then define the loop function .
* Return the class.

    
