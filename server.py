from flask import Flask
import json
from about import me
from data import mock_data


app = Flask(__name__) # create a instance of Flask class


@app.get("/")
def home():
    return "Hello World from a flask server"


@app.get("/test")
def test():
    return "This is a test page"




@app.get("/api/version")
def version():
    return json.dumps("1.0")


@app.get("/api/about")
def about():
    return json.dumps(me)



@app.get("/api/developer/name")
def dev_name():
    name = me["name"]
    last = me["last_name"]
    email = me["email"]
    response = f"{name} {last} -- {email}"
    return json.dumps(response)




@app.get("/api/catalog")
def get_catalog():
    return json.dumps(mock_data)



@app.get("/api/products/count")
def product_count():
    count = len(mock_data)
    return json.dumps(count)



@app.get("/api/products/total")
def sum_prices():
    total = 0
    for product in mock_data:
        price = product["price"]
        total = total + price


    print(total) # show the result in the terminal
    return json.dumps(total)


# get /api/categories
# return a list of categories
# 1 - create a list
# 2 - for to travel the catalog
    # 3 - get the category from the product
    # 4 add the category to the list
# 5 - return the list as json

@app.get("/api/categories")
def categories():
    cats = []
    for prod in mock_data:
        category = prod ["category"]

        # if category does not exist inside the list
        if category not in cats: 
            cats.append(category)

    return json.dumps(cats)


@app.get("/api/catalog/<category>")
def products_by_category(category):
    results = []
    for prod in mock_data:
        if prod["category"].lower() == category.lower():
            results.append(prod)

    return json.dumps(results)



# create a list
# travel mock_data with a for loop
# from the product, get the category
# if category is equal to the category, we receive
#   if so, append the product to the list
# at the end of the for loop, return the list


  





# start the server
app.run(debug=True)