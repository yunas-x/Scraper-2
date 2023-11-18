from .utils import (
    create_file, 
    read_cad_nums,
    to_path,
    write_data)

from .settings import (
    url,
    auth_url,
    login,
    password,
    excel_output_file_name, 
    excel_input_file_name)

from .scraper import Scraper
from .driver_builder import driver_builder

if __name__ == "__main__":
    kads = read_cad_nums(name=to_path(excel_input_file_name))
    
    scraper = Scraper(driver=driver_builder.yield_driver(), base_url=url)
    scraper.authorize(auth_url=auth_url, username=login, password=password)
    data = scraper.scrape_offset(kads=kads, offset=5)
    
    create_file(name=excel_output_file_name)
    write_data(excel_output_file_name, data=data)
    
    scraper._driver.close()