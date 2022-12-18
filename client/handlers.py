import client.authorization

def get_client_handlers():
    return [LoadHandler()]

class LoadHandler(object):
    # def OnLoadingStateChange(self, browser, is_loading, **_):
    #     if not is_loading:
    #         print("page has changed")
    
    def OnLoadingStateChange(self, browser, **_):
        print(browser.GetUrl())
    
    def OnLoadError(self, browser, failed_url, **_):
        if "https://localhost/web-aerial" in failed_url:
            print("check it login : " + failed_url)
            client.authorization.threading_login(failed_url)
        else:
            print("url occur Error : " + failed_url)
        
        # browser.LoadUrl("file:///E:/vsDevelopment/FirstLauncher/html/main.html")
        
