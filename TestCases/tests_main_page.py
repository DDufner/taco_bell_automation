from PageObjects.MainPage import MainPage

class Test_001_Main_Page_General:
    searchTerm = "taco"
    baseURL = "https://www.tacobell.com/"
    emailAddress = "domdautomation@gmail.com"
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

class Test_002_Main_Page_Tabs_Navigation:
    location = "65201"
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

    def test_rewards_navigation(self,driver_setup):
        self.driver = driver_setup
        self.driver.get(self.baseURL)
        self.mainPage = MainPage(self.driver)
        self.driver.maximize_window()
        self.mainPage.clickRewardsTab()
        actual_url = self.driver.current_url
        if actual_url =="https://www.tacobell.com/rewards":
            assert True
        else: 
            assert False

    def test_nutrition_navigation(self,driver_setup):
        self.driver = driver_setup
        self.driver.get(self.baseURL)
        self.mainPage = MainPage(self.driver)
        self.driver.maximize_window()
        self.mainPage.clickNutritionTab()
        actual_url = self.driver.current_url
        if actual_url =="https://www.tacobell.com/nutrition":
            assert True
        else: 
            assert False

    def test_gift_navigation(self,driver_setup):
        self.driver = driver_setup
        self.driver.get(self.baseURL)
        self.mainPage = MainPage(self.driver)
        self.driver.maximize_window()
        self.mainPage.clickGiftCardsTab()
        actual_url = self.driver.current_url
        if actual_url =="https://www.tacobell.com/gift-cards":
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


    
        
