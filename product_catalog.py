from product_data import products

# Step 1 - Print out the products to see the data that you are working with.
print("First few products:")
for product in products[:3]:
    print(product)
print()

# Step 2 - Create a list called customer_preferences and store the user preference in this list.
customer_preferences = []

response = ""

while response != "N":
    print("Input a preference:")
    preference = input()

    customer_preferences.append(preference.strip().lower())

    response = input("Do you want to add another preference? (Y/N): ").upper()

# Step 3 - Convert customer_preferences list to set to eliminate duplicates.
customer_preferences = set(customer_preferences)

# Step 4 - Convert the product tags to sets in order to allow for faster comparisons.
converted_products = []

for product in products:
    converted_products.append({
        "name": product["name"],
        "tags": set(product["tags"]),
    })


# Step 5 - Write a function to calculate the number of matching tags
def count_matches(product_tags, customer_tags):
    '''
    Args:
        product_tags (set): A set of tags associated with a product.
        customer_tags (set): A set of tags associated with the customer.

    Returns:
        int: The number of matching tags between the product and customer.
    '''
    return len(product_tags & customer_tags)


# Step 6 - Write a function that loops over all products and returns a sorted list of matches
def recommend_products(products, customer_tags):
    '''
    Args:
        products (list): A list of product dictionaries.
        customer_tags (set): A set of tags associated with the customer.

    Returns:
        list: A list of products containing product names and their match counts.
    '''
    recommendations = []

    for product in products:
        matches = count_matches(product["tags"], customer_tags)
        if matches > 0:
            recommendations.append({"name": product["name"], "matches": matches})

    recommendations.sort(key=lambda item: item["matches"], reverse=True)
    return recommendations


# Step 7 - Call your function and print the results
recommended = recommend_products(converted_products, customer_preferences)

if recommended:
    print("\nRecommended Products:")
    for item in recommended:
        print(f"- {item['name']} ({item['matches']} match(es))")
else:
    print("\nNo matching products found.")


# DESIGN MEMO (write below in a comment):

# 1. What core operations did you use (e.g., intersections, loops)? Why?
#    I used loops, sets, set intersection, and sorting.
#    - A loop goes through every product so each one gets checked.
#    - I turned the preferences and the product tags into sets. A set removes
#      repeats, and checking a set is fast.
#    - The & (intersection) operator finds the tags that the product and the
#      customer share. The length of that result is the number of matches.
#    - Sorting puts the products with the most matches first.

# 2. How might this code change if you had 1000+ products?
#    The code would still work, but I would make a few changes to keep it fast:
#    - Turn the tags into sets one time and reuse them, instead of every search.
#    - Make a lookup that maps each tag to the products that have it. Then I
#      would only check products that share a tag, not all 1000+.
#    - Only show the top 5 or 10 results, so the list stays short.