from pages.base_page import BasePage


class ADD_A_MATCH_FORM(BasePage)

    main_page_button_xpath = "//*[@id="__next"]/div[1]/div/div/div/ul[1]/div[1]/div[2]/span"
    players_button_xpath = "//*[text()="Players"]"
    sign_out_button_xpath = "//*[@id="__next"]/div[1]/div/div/div/ul[3]/div[2]/div[1]/svg"
    reports_button_xpath = "//div[@class="MuiListItemText-root jss32 jss82"]"
    submit_button_xpath = "//button[@class="MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedPrimary"]"
    clear_button_xpath = "//button[@class="MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedSecondary"]"
    date_field_xpath = "//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[5]/div"
    match_at_home_field_xpath = "//*[text()="Match at home"]"
    title_form_xpath = "//div[@class="MuiCardHeader-root"]"
    content_form_xpath = "//div[@class="MuiCardContent-root"]"

    pass
