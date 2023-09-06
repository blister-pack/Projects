import requests


def fetch_product_data(product_id):
    url = f"https://fakestoreapi.com/products/{product_id}"
    response = requests.get(url)
    print(response)

    if response.status_code == 200:
        product_data = response.json()
        return (
            product_data["title"],
            product_data["category"],
            product_data["price"],
            product_data["description"],
        )
    else:
        print("Bad response")
        return None


if __name__ == "__main__":
    print(fetch_product_data(12))
    print(fetch_product_data(13))
    print(fetch_product_data(1))
    print(fetch_product_data(input()))
