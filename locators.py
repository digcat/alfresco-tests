from selenium.webdriver.common.by import By

class MainPageLocators(object):
    SEARCH_FORM = (By.ID,'page_x002e_search_x002e_advsearch_x0023_default-search-text')
    SEARCH_BUTTON = (By.ID, 'page_x002e_search_x002e_advsearch_x0023_default-search-button-1-button') 
    MAINMENU_SITES = (By.ID, 'HEADER_SITES_MENU')

    CREATESITE_BUTTON 		= (By.ID, 'HEADER_SITES_MENU_CREATE_SITE_text')
    CREATESITE_NAME 		= (By.ID,'alfresco-createSite-instance-title')
    CREATESITE_DESCRIPTION 	= (By.ID, 'alfresco-createSite-instance-description')
    CREATESITE_PREFIX 		= (By.ID,'alfresco-createSite-instance-sitePreset')
    CREATESITE_VISIBILITY 	= (By.ID, 'alfresco-createSite-instance-isPublic')
    CREATESITE_SUBMIT 		= (By.ID, 'alfresco-createSite-instance-ok-button-button')

    RMCREATESITE_BUTTON 	= (By.ID, 'HEADER_SITES_MENU_CREATE_SITE_text')
    RMCREATESITE_NAME 		= (By.ID, 'alfresco-rm-createSite-instance-title')
    RMCREATESITE_DESCRIPTION 	= (By.ID, 'alfresco-rm-createSite-instance-description')
    RMCREATESITE_PREFIX 	= (By.ID, 'alfresco-rm-createSite-instance-sitePreset')
    RMCREATESITE_VISIBILITY 	= (By.ID, 'alfresco-rm-createSite-instance-isPublic')
    RMCREATESITE_SUBMIT 	= (By.ID, 'alfresco-rm-createSite-instance-ok-button-button')

    AC_DEL_LIST = (By.ID, 'alfresco-documentlibrary-views-layouts-AlfDocumentListView')
    AC_DEL_REMOVE = (By.ID, 'uniqName_1_')
    AC_DEL_DELETE = (By.ID, 'alfresco_menus_AlfMenuItem___')
    AC_DEL_CONFIRM = (By.ID, 'alfresco_buttons_AlfButton__')
