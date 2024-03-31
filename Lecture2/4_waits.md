# Networks conditions and waits
## Emulating slow network
It is possible to change the network speed for the browser so we can emulate different network conditions 
Parameters:  
* Offline - Boolean value to set if the network is offline or not
* Latency - Value in miliseconds  
* Download and upload throughput - Value in bps

```
driver.set_network_conditions(
    offline = False,
    latency = 50,
    download_throughput = 100 * 1024,
    upload_throughput = 100 * 1024
)
```
Get the custom network settings  
> driver.get_network_conditions()

Delete our custom netork config  
> driver.delete_network_conditions() 

## Waits
### Implicit waits
Implicit waits are used when we need to set the maximum waiting time for finding elements in a browser session. This is not the preferred way to wait for elements but can be useful if we know the infrastructure and network conditions are good. 

You can set implicit waits with the implicitly_wait(seconds). The default value is 0.

Waits up to 30 seconds to find elements. After that the WebDriver will fail to find the element.
> driver.implicitly_wait(30) 

### Explicit waits
Explicit waits specify conditions that need to be met before the code continues.
Ex: Wait for an element to be visible in page before we interact with it.

Explicit waits are a characteristic of better/more maintainable Selenium code.
Explicit waits are more robust against network conditions than a implicit wait or time.sleep().

It can be a good thing to put explicit waits inside a try-catch-finally block and log the errors in case of a failures to see why the element is not found.

Setting explicit waits involves two objects:
*   A WebDriverWait
*   An expected condition

Selenium provides a number of methods for expected conditions, below are some examples. More info at:  
https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.expected_conditions.html

*   title_is
*   visibility_of_element_located
*   element_to_be_clickable

```
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC  
from selenium.common.exceptions import ElementNotVisibleException
```

Explicit wait for element
> element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'my-id')))

Compared to code without wait
> element = driver.find _element(By.ID, 'my-id')

Example with try - except:  
```
try:
    element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'my-id')))

except ElementNotVisibleException:
    print("Element could not be clicked")
```
