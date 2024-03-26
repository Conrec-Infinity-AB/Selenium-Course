# Dropdown menus #

## Selecting values ##
Dropdowns are using \<select/\> and \<option/\> tags.

We can interact with dropdowns in several ways and several values can be selected

Start by importing the Select package  
> from selenium.webdriver.support.ui import Select

Find the dropdown Select element which we will test 
> person_dropdown = driver.find_element(By.ID, "dropdown_persons")

And create the Select object we will use for selecting  
> dropdown = Select(person_dropdown)

Then we have different ways to select rows in the dropdown.

Select based on the index associated with an entry in the dropdown.
> dropdown.select_by_index(1) 

Select based on the value attribute of an entry in the dropdown.
> dropdown.select_by_value("TomHalland")

Select based on the text that is displayed in the dropdown on the browser.
> dropdown.select_by_visible_text("Elon Huskß")

## Selecting multiple values ##
If the dropdown has the attribute multiple set then we can select several values in the dropdown

## Disabled values and values out of index # 
Disabled values can not be selected and will raise an exception. The same applies to values outside of the index.

## De-selecting ##
In a multi select dropdown we can also deselect values which has been selected 

> dropdown.deselect_by_index(2)  

> dropdown.deselect_by_value("TomHolland")
ß
> dropdown.deselect_all() 




