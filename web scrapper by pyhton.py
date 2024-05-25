import pandas as pd
import requests
from bs4 import BeautifulSoup

prod_name = []
prices = []  
descriptions = []
reviews = []

for i in range(1, 12):  
    url = f"https://www.flipkart.com/search?q=mobile+5g&page={i}"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    
    # Check if the container is found
    box = soup.find("div", class_="_1YokD2 _3Mn1Gg")
    if box is not None:
        # Find all elements within the container
        descrip_tags = box.find_all("ul", class_="_1xgFaf")  
        for desp in descrip_tags:  
            description = desp.text  
            descriptions.append(description)

        reviews_cstmr = box.find_all("div", class_="_3LWZlK")
        for review in reviews_cstmr:
            revu = review.text
            reviews.append(revu)

        names = box.find_all("div", class_="_4rR01T")
        for i in names:
            name = i.text
            prod_name.append(name)

        price_tags = box.find_all("div", class_="_30jeq3 _1_WHN1")  
        for tag in price_tags:
            price = tag.text
            prices.append(price)
    else:
        print(f"No container found on page {i}")

df = pd.DataFrame({"Product Name": prod_name, "Prices": prices, "Description": descriptions, "Reviews": reviews})
print(df)
