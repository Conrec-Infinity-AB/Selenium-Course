# Waits #
## Implicit waits ##
Implicit waits are used when we need to set the maximum waiting time for finding elements in a browser session. This is not the preferred way to wait for elements. A more useful way is to use explicit waits.
With explicit waits, the code only waits as long as it needs to and the program will run faster.

You can set implicit waits with the implicitly_wait(seconds)
Waits up to 30 seconds to find elements
> driver.implicitly_wait(30) 

## Explicit waits ##
Explicit waits specify conditions that need to be met before the code continues.
Ex: Wait for an element to be visible in page before we interact with it.

Explicit waits are a characteristic of better/more maintainable Selenium code.
Explicit waits are more robust against network conditions than a implicit wait or time.sleep().

It can be a good thing to put explicit waits inside a try-catch-finally block and log the errors in case of a failures to see why the element is not found.

Setting explicit waits involves two objects:
*   A WebDriverWait
*   An expected condition

Selenium provides a number of methods for expected conditions.
*   title_is
*   visibility_of_element_located
*   element_to_be_clickable

> from selenium.webdriver.support.ui import WebDriverWait
> from selenium.webdriver.support import expected_conditions as EC
> from selenium.common.exceptions import ElementNotVisibleException

Explicit wait for element
https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.expected_conditions.html
> element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'my-id')))

Compared to code without wait
> element = driver.find _element(By.ID, 'my-id')

> try:
> element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'my-id')))
> except ElementNotVisibleException:
> print("Element could not be clicked")

## Emulating slow network ##
Parameters:
- Offline 
- Latency in ms
- Download and upload throughput in bps

> driver.set_network_conditions(
> offline = False,
> latency = 50,    
> download_throughput = 100 * 1024,
> upload_throughput = 100 * 1024
>)

> driver.get_network_conditions()

