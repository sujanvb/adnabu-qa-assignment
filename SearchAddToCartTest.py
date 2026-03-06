from utilityClasses.DriverScript import DriverScript
from utilityClasses.ReportManager import ReportManager
    
def run_test():
    driver = DriverScript.get_driver()
    ReportManager.set_driver(driver)

    driver.get("https://google.com")
    ReportManager.updateTestLog("Title Check", "Page title is: " + driver.title, "PASS")
    ReportManager.updateTestLog("Title Check", "Page title is: " + driver.title, "PASS")
    ReportManager.updateTestLog("Title Check", "Page title is: " + driver.title, "PASS")
    DriverScript.quit_driver()
    
if __name__ == "__main__":
    run_test()