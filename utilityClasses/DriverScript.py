from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class DriverScript:

    driver: webdriver.Chrome = None

    @staticmethod
    def get_driver() -> webdriver.Chrome:
        if DriverScript.driver is None:
            service = Service(ChromeDriverManager().install())
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")

            DriverScript.driver = webdriver.Chrome(service=service, options=options)

        return DriverScript.driver

    @staticmethod
    def quit_driver() -> None:
        if DriverScript.driver is not None:
            DriverScript.driver.quit()
            DriverScript.driver = None