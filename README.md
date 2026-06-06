# Daam

A *product price comparison tool* that searches across popular Indian beauty and shopping websites in real time.

## Live Demo
https://daam-mqjd.onrender.com

## Features
- Search any product and compare prices across Nykaa, Amazon, Tira, Purplle, Meesho and Myntra
- Real time results powered by SerpAPI
- Clean results showing price, title and direct link to product

## Tech Stack
- **Backend:** Django, Django REST Framework
- **API:** SerpAPI (Google Shopping)
- **Frontend:** HTML, CSS, JavaScript
- **Deployment:** Render

## Getting Started

```bash
git clone https://github.com/Hadiqaaaa/pricecompare
cd pricecompare
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file:
```
SECRET_KEY=your-secret-key
SERPAPI_KEY=your-serpapi-key
DEBUG=True
```

```bash
python manage.py runserver
```

## Planned Improvements
- Let users filter by region and select specific websites
- Add price history tracking
