from PageObjects.MainPage import MainPage

class Test_001_Main_Page:
    location = "65201"
    searchTerm = "taco"
    baseURL = "https://www.tacobell.com/"
    emailAddress = "domdautomation@gmail.com"

    def test_menu_navigation(self,driver_setup):
        self.driver = driver_setup
        self.driver.get(self.baseURL)
        self.mainPage = MainPage(self.driver)
        self.driver.maximize_window()
        self.mainPage.clickMenuTab()
        actual_url = self.driver.current_url
        if actual_url =="https://www.tacobell.com/food":
            assert True
        else: 
            assert False
        
    def test_search_for_item(self,driver_setup):
        self.driver = driver_setup
        self.driver.get(self.baseURL)
        self.mainPage = MainPage(self.driver)
        self.mainPage.searchForItem(self.searchTerm)
       
    def test_confirm_homepage(self,driver_setup): 
        self.driver = driver_setup
        self.driver.get(self.baseURL)
        actual_url = self.driver.title
        if actual_url =="Taco Bell® | Live Más":
            assert True
        else: 
            assert False
    
    def test_delivery_navigation(self,driver_setup):
        self.driver = driver_setup
        self.driver.get(self.baseURL)
        self.mainPage = MainPage(self.driver)
        self.driver.maximize_window()
        self.mainPage.clickDeliveryTab()
        actual_url = self.driver.current_url
        if actual_url =="https://www.tacobell.com/delivery":
            assert True
        else: 
            assert False

#    setLocation function not working, 'change' link is bad
#    def test_set_location(self, driver_setup):
#        self.driver = driver_setup
#        self.driver.get(self.baseURL)
#        self.mainPage = MainPage(self.driver)
#        self.mainPage.setLocation(self.location)
#        print("location set")


    
        
