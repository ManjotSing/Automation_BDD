from selenium import webdriver
class FactoryManager():

    @staticmethod
    def createDriver(drivertype):
        if drivertype == 'Edge':
            driver = webdriver.Edge(executable_path="/Users/manjotsingh/PycharmProjects/Automation_BDD/drivers/msedgedriver");
        elif drivertype=='Firefox':
            driver = webdriver.Firefox(executable_path="../drivers/");
        else:
            driver = webdriver.Chrome(executable_path="/Users/manjotsingh/PycharmProjects/Automation_BDD/drivers/chromedriver")
        driver.set_page_load_timeout(120);
        driver.maximize_window();
        driver.implicitly_wait(60);
        return driver