import pytest
from pages import AmazonHomePage, AmazonSearchResultsPage, AmazonProductPage

def test_search_and_add_iphone(setup_page):
    """
    Test Case 1 (iPhone): Navigate to amazon.com, search for 'iPhone', find the price 
    of the first item, print the price to the console, and click 'Add to Cart'.
    """
    page = setup_page
    
    # Initialize Page Objects
    home_page = AmazonHomePage(page)
    results_page = AmazonSearchResultsPage(page)
    product_page = AmazonProductPage(page)
    
    # 1. Navigate to amazon.com
    home_page.navigate()
    
    # 2. Search for 'iPhone'
    home_page.search_for("iPhone")
    
    # 3. Find the price of the first item
    price = results_page.get_first_item_price()
    
    # Print the price to the console
    print(f"\n[iPhone Test] The price of the first iPhone is: {price}")
    
    # 4. Click on the first item
    results_page.click_first_item()
    
    # 5. Click 'Add to Cart'
    product_page.add_to_cart()


def test_search_and_add_galaxy(setup_page):
    """
    Test Case 2 (Galaxy): Navigate to amazon.com, search for 'Galaxy', find the price 
    of the first item, print the price to the console, and click 'Add to Cart'.
    """
    page = setup_page
    
    # Initialize Page Objects
    home_page = AmazonHomePage(page)
    results_page = AmazonSearchResultsPage(page)
    product_page = AmazonProductPage(page)
    
    # 1. Navigate to amazon.com
    home_page.navigate()
    
    # 2. Search for 'Galaxy'
    home_page.search_for("Galaxy")
    
    # 3. Find the price of the first item
    price = results_page.get_first_item_price()
    
    # Print the price to the console
    print(f"\n[Galaxy Test] The price of the first Galaxy is: {price}")
    
    # 4. Click on the first item
    results_page.click_first_item()
    
    # 5. Click 'Add to Cart'
    product_page.add_to_cart()
