# Scraper-2
Скрапер для прасинга сведений о кадастровых номерах

## Зависимости

Далее откройте командную строку (клавиши: <Win + R>) <br/>
Добавьте необходимые зависимости: <br/>
-- selenium <br/>
-- selenium_stealth <br/>
-- webdriver-manager <br/>
-- pandas <br/>

Для этого используйте команду: pip install <название зависимости> <br/>

### При проблемах с webdriver:
https://stackoverflow.com/questions/63421086/modulenotfounderror-no-module-named-webdriver-manager-error-even-after-instal <br/>

## Настройки
Для настройки программы используйте файл settings.py <br/>
Описание параметров: <br/>
-- url — ссылка на сайт (не менять)<br/>
-- excel_output_file_name — путь к выходному файлу<br/>
-- excel_input_file_name — путь к входному файлу<br/>
