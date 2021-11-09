# Crypto_Currency_News_Page
### Installation 
In your terminal, install necesssary libraries:
```
pip install -r requirements.txt
```
Create a table in advance to fill it later:
```postgresql
CREATE TABLE Paragraphs(
  id integer PRIMARY KEY,
  text VARCHAR
);
```
Run the application:
```
python3 test/main.py
```
### Usage
To use application provide a name of a existing cryptocurrency, and after refreshing it will scrap the news related to this currency.
### Example
