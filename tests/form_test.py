from conftest import driver
from pages.form_page import FormPage


class TestFromPage:

    def test_form(self, driver):
        form_page = FormPage(driver, "https://demoqa.com/automation-practice-form")
        form_page.open()
        form_page.fill_fields_and_submit()