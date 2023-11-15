from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
#from webdriver_manager.chrome import ChromeDriverManager
from selenium_stealth import stealth

class driver_builder:

    def yield_driver() -> webdriver.Chrome:
        
        options = webdriver.ChromeOptions()
        
        chrome_prefs = {
            "download.prompt_for_download": False,
            "plugins.always_open_pdf_externally": True,
            "download.open_pdf_in_system_reader": False,
            "profile.default_content_settings.popups": 0,
        }
        
        options.add_experimental_option("prefs", chrome_prefs)

        # start the browser window in maximized mode
        options.add_argument('--start-maximized')

        # disable extensions
        options.add_argument('--disable-extensions')

        # disable sandbox mode
        options.add_argument('--no-sandbox')

        # disable shared memory usage
        options.add_argument('--disable-dev-shm-usage')
        
        #service = ChromeService(executable_path=ChromeDriverManager().install())
        service = ChromeService()

        driver = webdriver.Chrome(options=options, service=service)
        
        stealth(
            driver=driver,
            languages=["ru-RU", "ru"],
            vendor="Google Inc.",
            platform="Win64",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True
        )
        
        return driver