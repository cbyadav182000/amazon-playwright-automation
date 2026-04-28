from playwright.sync_api import Page, Locator

class AmazonHomePage:
    """Page Object for Amazon Home Page"""
    
    def __init__(self, page: Page):
        self.page = page
        # Selectors for search box and submit button
        self.search_box: Locator = page.locator("#twotabsearchtextbox")
        self.submit_button: Locator = page.locator("#nav-search-submit-button")

    def navigate(self):
        """Navigate to Amazon home page"""
        self.page.goto("https://www.amazon.com/")

    def search_for(self, item: str):
        """Enter a search term and submit"""
        self.search_box.fill(item)
        self.submit_button.click()


class AmazonSearchResultsPage:
    """Page Object for Amazon Search Results Page"""
    
    def __init__(self, page: Page):
        self.page = page
        # Locate the first actual product result (bypassing generic components)
        self.first_result: Locator = page.locator("div[data-component-type='s-search-result']").first
        
        # Inside the first result, find the price
        # '.a-price > .a-offscreen' contains the full price text hidden from screen readers
        self.first_item_price: Locator = self.first_result.locator(".a-price > .a-offscreen").first
        
        # Inside the first result, find the product link
        self.first_item_link: Locator = self.first_result.locator("a.a-link-normal").first

    def get_first_item_price(self) -> str:
        """Extract the price of the first item in the results"""
        # Wait for the result element to be present in the DOM
        self.first_result.wait_for(state="attached")
        
        # Use text_content() instead of inner_text() because the .a-offscreen class is visually hidden
        price = self.first_item_price.text_content()
        return price.strip() if price else "Price not found"

    def click_first_item(self):
        """Click the first item in the results to view details"""
        # Use force=True to bypass any transparent overlays preventing the click
        self.first_item_link.click(force=True)


class AmazonProductPage:
    """Page Object for Amazon Product Details Page"""
    
    def __init__(self, page: Page):
        self.page = page
        # Selector for the 'Add to Cart' button
        self.add_to_cart_button: Locator = page.locator("#add-to-cart-button")

    def add_to_cart(self):
        """Click the Add to Cart button"""
        # Wait for the button to be visible before interacting
        self.add_to_cart_button.wait_for(state="visible")
        self.add_to_cart_button.click()
