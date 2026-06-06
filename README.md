
# Daam
a product price comparsion tool that lets user compare price of a product across websites

## Link

https://daam-mqjd.onrender.com/

## Features 
-get a list of prices of a product across multiple websites with the product
-links to the product on those websites
-any product from amazon.in,nykaa,tira beauty,myntra and meesho can be searched

## Tech Stack
- frontend:html,css
- backend:django drf,python,SERPAPI
- hosting:render

## Usage 
```bash
git clone https://github.com/Hadiqaaaa/pricecompare
cd pricecompare
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

create a `.env` file
```
SERPAPI_KEY=yourapikey
SECRET_KEY=yoursecretkey
DEBUG=True
```
then run
```
python3 manage.py runserver
```
## further imrpovements
- caching and ratelimiting
- allowing users to select their gl
- letting users select from a range of websites 

