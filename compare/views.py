from django.shortcuts import render
import requests
import os
from rest_framework.decorators import api_view
from rest_framework.response import Response

def home(request):
    return render(request, 'index.html')

def results(request):
    return render(request, 'results.html')

STORES = {
    'nykaa.com': 'Nykaa',
    'amazon.in': 'Amazon',
    'tirabeauty.com': 'Tira',
    'purplle.com': 'Purplle',
    'meesho.com': 'Meesho',
    'myntra.com': 'Myntra',
}

def get_product_image(query, api_key):
    try:
        params = {
            'engine': 'google_images',
            'q': query,
            'api_key': api_key,
            'gl': 'in',
            'hl': 'en',
            'num': 1,
        }
        response = requests.get('https://serpapi.com/search', params=params)
        data = response.json()
        images = data.get('images_results', [])
        if images:
            return images[0].get('thumbnail', '')
    except:
        pass
    return ''

@api_view(['GET'])
def search_products(request):
    query = request.GET.get('q', '')
    if not query:
        return Response({'error': 'No search query provided'}, status=400)

    api_key = os.getenv('SERPAPI_KEY')
    results = []

    for domain, store_name in STORES.items():
        params = {
            'engine': 'google',
            'q': f'{query} site:{domain}',
            'api_key': api_key,
            'gl': 'in',
            'hl': 'en',
            'num': 3,
        }

        try:
            response = requests.get('https://serpapi.com/search', params=params)
            data = response.json()
            organic = data.get('organic_results', [])

            found = False
            for result in organic:
                link = result.get('link', '')
                if '/p/' in link or 'product' in link or domain in link:
                    rich = result.get('rich_snippet', {}).get('bottom', {})
                    extensions = rich.get('detected_extensions', {})

                    price_from = extensions.get('price_from')
                    price_to = extensions.get('price_to')
                    price = extensions.get('price')

                    if price_from:
                        price_display = f"₹{int(price_from)} – ₹{int(price_to)}"
                    elif price:
                        price_display = f"₹{int(price)}"
                    else:
                        price_display = "off sale"

                    results.append({
                        'store': store_name,
                        'title': result.get('title', ''),
                        'price': price_display,
                        'link': link,
                        'image': result.get('thumbnail', ''),
                        'found': True,
                    })
                    found = True
                    break

            if not found:
                results.append({'store': store_name, 'found': False})

        except Exception as e:
            results.append({'store': store_name, 'found': False})

    product_title = ''
    for r in results:
        if r.get('found') and r.get('title'):
            product_title = r['title']
            break

    product_image = get_product_image(query, api_key)

    return Response({
        'product': query,
        'image': product_image,
        'title': product_title,
        'results': results,
    })