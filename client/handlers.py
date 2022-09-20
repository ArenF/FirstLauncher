import client.authorization

def get_client_handlers():
    return [LoadHandler()]

class LoadHandler(object):
    # def OnLoadingStateChange(self, browser, is_loading, **_):
    #     if not is_loading:
    #         print("page has changed")
    
    def OnLoadError(self, browser, failed_url, **_):
        if "https://localhost/web-aerial" in failed_url:
            print("check it login : " + failed_url)
            client.authorization.login_complete(failed_url)
            browser.LoadUrl("file:///E:/vsDevelopment/FirstLauncher/html/main.html")
        else:
            print("url occur Error : " + failed_url)
        
