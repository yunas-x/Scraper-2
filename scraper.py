from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from time import sleep

class Scraper:

    def __init__(self, driver: webdriver.Chrome, base_url: str) -> None:
        self._base_url = base_url
        self._driver = driver

    def authorize(self, auth_url: str, username: str, password: str) -> None:
        self._driver.get(url=auth_url)
        wait = WebDriverWait(self._driver, 300)
        wait.until(EC.element_to_be_clickable((By.NAME, "email"))).send_keys(username)
        wait.until(EC.element_to_be_clickable((By.NAME, "psw"))).send_keys(password)
        wait.until(EC.element_to_be_clickable((By.ID, "login_form"))).submit()
        
    def to_base_page(self) -> None:
        self._driver.get(url=self._base_url)
        
    def search(self, number: str) -> None:
        wait = WebDriverWait(self._driver, 300)
        wait.until(EC.element_to_be_clickable((By.ID, "search_field"))).send_keys(number)
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "search_box_min"))).submit()
    
    def scrape_data(self) -> dict:
        required_fields = ["Статус объекта", "Этаж", "Площадь",
                           "Кадастровая стоимость", "Дата определения стоимости", 
                           "Дата внесения стоимости", "Тип", "Назначение",
                           "Этажность", "Форма собственности"]
        
        data = dict()
        data["num"] = self._driver.find_element(by=By.ID, value="cadnump").text
        data["address"] = self._driver.find_element(by=By.CLASS_NAME, value="h2_none").text
        data["type_first"] = self._driver.find_element(by=By.CLASS_NAME, value="h3_none").text
        row_ssers = self._driver.find_elements(by=By.CLASS_NAME, value="row_sser")
        for i, row_sser in enumerate(row_ssers):
            if i == 22: # Чтобы не брать лишнее
                break
            
            name = row_sser.find_element(by=By.CLASS_NAME, value="left_sser").text
            if not name: # Фильтруем мусор
                continue
            
            try: # На случай пустоты
                value = row_sser.find_element(by=By.CLASS_NAME, value="tx_sser").text
            except:
                value = " "
            
            if name in required_fields:
                data[name] = value
        return data
    
    def scrape_offset(self, kads: list[str], offset: int=1_000_000) -> list[list]:
        
        is_header_saved = False
        data = []
        
        for i, kad in enumerate(kads):
            if i > offset:
                break
            
            sleep(2)
            
            try:
                self.to_base_page()
                self.search(number=kad)
                if not is_header_saved:
                    data.append(list(self.scrape_data().keys()))
                    is_header_saved = True
                data.append(list(self.scrape_data().values()))
            except:
                print(kad)

        return data          