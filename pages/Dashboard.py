from pages.base_page import BasePage


class Dashboard(BasePage):
    
    header_xpath = "//div[@class="MuiToolbar-root MuiToolbar-regular MuiToolbar-gutters"]"
    players_count_xpath = "//*[@id="__next"]/div[1]/main/div[2]/div[1]/div"
    matches_count_xpath = "//*[text()="Matches count"]"
    players_button_xpath = "//div[@class="MuiListItemText-root jss29 jss31"]"
    last_created_player_xpath = "//*[text()="Last created player"]"
    logo_scouts_panel_xpath = "//div[@title="Logo Scouts Panel"]"
    reports_count_xpath = "//div[text()="Reports count"]"
    add_player_button_xpath = "//a[@href="/en/players/add"]"
    left_site_panel_xpath = "//div[@class="MuiPaper-root MuiDrawer-paper jss25 MuiDrawer-paperAnchorLeft MuiDrawer-paperAnchorDockedLeft MuiPaper-elevation0"]"
    last_updated_player_field_xpath = "//div//h6[text()="Last updated player"]"

    pass
