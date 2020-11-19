# project-data-extraction
A python script to get dinosaurs data form Wikipedia using web scraping and the Wikipedia API.

CONTEXT:
We will use the following URL to make requests:
https://en.wikipedia.org/wiki/List_of_dinosaur_genera

The link above we will found a very long list of dinosaur and every elemento of the list is a link to the corresponding article of the dinosaur in Wikipedia.

This list of dinosaurs is a comprehensive listing of all genera that have ever been considered to be non-avian dinosaurs, but this list also includes some dinosaurs which are disputed to be either avian or non-avian, as well as purely vernacular terms. The list contains 1630 names, of which approximately 1224 are considered either valid dinosaur genera or nomina dubia.

IMPORTANT NOTES ABOUT THE DATA:
Dinosaurs belonging to the following categories will be discriminated since this dinosaurs are from the same spicie, they are not offialy named or they were not being mentionaed in any scientiphic paper from more than 50 years and for this project there is no need to count them twice or enter in a deep understanding of every dinosaur. 
  - Junior synonym.
  - Nomen nudum. 
  - Nomen manuscriptum.
  - Preoccupied name.
  - Nomen dubium.
  
PORPUSE:
The main porpuse is to scrap the main list of dinosaurs and get the name of every dinosaur and then get the URL for every article and scrap it looking for the first two paragraphs hoping we can find information related with discover date, location, etc. At the end we will put the information in a Pandas DataFrame wit columns names: [Name, Scienthiic name, discover year, location] (More maybe be agregated later), and then convert this information to a csv file or even an excel file.

This project is divided by two main sections:

  - Web scraping Section.
  - API section.

So you will find 2 .py files for every method and other 2 output files wich should contain exactly the same information.
