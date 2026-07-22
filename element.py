"""
Base page element class for Alfresco test suite.

Implements the descriptor protocol for delayed element lookup with explicit waits.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class BasePageElement:
    """
    Base page element descriptor with automatic waiting.

    Uses the descriptor protocol to provide delayed element lookup
    with explicit waits. Updated for Selenium 4 API.
    """

    def __set__(self, obj, value):
        """Set element value after waiting for it to be available."""
        driver = obj.driver
        WebDriverWait(driver, 100).until(lambda driver: driver.find_element(By.NAME, self.locator))
        driver.find_element(By.NAME, self.locator).send_keys(value)

    def __get__(self, obj, owner):
        """Get element value after waiting for it to be available."""
        driver = obj.driver
        WebDriverWait(driver, 100).until(lambda driver: driver.find_element(By.NAME, self.locator))
        element = driver.find_element(By.NAME, self.locator)
        return element.get_attribute("value")
