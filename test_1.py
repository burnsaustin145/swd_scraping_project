from selenium import webdriver


class SwdMain:

    def __init__(self):
        self.driver_location = "/Users/burnsaustin145/PycharmProjects/SWD_2/venv/bin/chromedriver"
        self.driver = webdriver.Chrome(self.driver_location)
        self.driver.get("https://users.wix.com/signin")
        self.user = self.driver.find_element_by_name('email')
        self.password = self.driver.find_element_by_name('password')
        self.login = self.driver.find_element_by_name('submit')
        self.quit_flag = True

        return

    def login_procedure(self):
        """gets the wix login page and enters
        info. Prompts user to complete captcha;
        then returns after user confirmation."""
        self.user.send_keys("burnsaustin145@gmail.com")
        self.password.send_keys("Pwnage101!")

        while True:
            login_verification = input("Please complete captcha in browser window; \n"
                                       "then, after logging in, enter"
                                       " any letter to continue (enter 'quit' to close): ")

            if login_verification == 'quit':
                self.driver.close()
                self.quit_flag = False
                break

            else:
                break

    def main_interface(self):
        """after login, offers options for next operation,
        and then redirects to chosen funtion"""
        print("Choose your operation:\n"
              "\r*Print Ashley's list with 'a-list'")
        curr_input = input("What would you like to do?")

        if curr_input == 'a-list':
            self.raw_a_list()
        elif curr_input == 'quit':
            self.quit_flag = False
        else:
            "Please enter a valid input ya' dingus (if you want to quit, just enter 'quit'): "
            self.main_interface()

    def raw_a_list(self):
        """takes order numbers and returns a list of the
        component parts"""
        self.driver.get("https://www.wix.com/dashboard/92c4321c-bcfd-4928-8af9-049fdcb914f3/store/orders")

        curr_input_start = int(input("Enter first order number: "))
        curr_input_end = int(input("Enter last order number: "))
        curr_input_excluding = input("Enter any excluded order numbers separated by a ',': ")

        raw_item_collection = {}
        for curr_order in range(curr_input_start, curr_input_end):
            if curr_order in curr_input_excluding.split():
                return
            else:

                search = self.driver.find_element_by_id("header-search-input")
                search.send_keys("{}".format(curr_order))
                if self.driver.find_element_by_xpath("//*[@class='wix-list-item']"):
                    curr_element = self.driver.find_element_by_xpath("//*[@class='wix-list-item']")
                    curr_element.click()
                    self.driver.implicitly_wait(3)
                    raw_item_collection[curr_order] = self.order_page_scrape()
                    print('made it to the first iteration of your for loop')
                    print(raw_item_collection)
                    self.driver.get("https://www.wix.com/dashboard/92c4321c-bcfd-4928-8af9-049fdcb914f3/store/orders")

                    return

                else:

                    return

            return
        print('made it to the end of your for loop')
        print(raw_item_collection)
        return self.refine_a_list(raw_item_collection)

    def order_page_scrape(self):
        """gets one page and generates an item/
        dictionary object to return. (will handle
        rest at other specialized functions)"""
        raw_item = {}
        headers = self.driver.find_elements_by_xpath("//*[@class='header-details']")
        print(headers)
        details = self.driver.find_elements_by_xpath("//*[@class='details-section']")
        print(details)
        headers_list = []
        details_list = []
        for foo in details:
            bar = foo.text
            details_list += bar

        for foo in headers:
            bar = foo.text
            headers_list += bar

        headers_string = ''
        details_string = ''
        headers_string = headers_string.join(headers_list)
        details_string = details_string.join(details_list)

        headers_list = headers_string.split()
        details_list = details_string.split()

        raw_item = headers_list + details_list

        print('headers list:')
        print(headers_list)
        print('details list:')
        print(details_list)
        return raw_item

    def refine_a_list(self, raw_a_list):
        print(raw_a_list)
        return self.main_interface()



if __name__ == "__main__":

    Swd = SwdMain()
    Swd.login_procedure()
    while Swd.quit_flag:

        Swd.main_interface()
        break









