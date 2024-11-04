from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait, Select

import selenium
import time

# Setup Chrome driver path
PATH = r"C:\Program Files (x86)\chromedriver-win64\chromedriver.exe"
service = Service(PATH)
driver = webdriver.Chrome(service=service)

try:
    # Open the Grafix website
    driver.get("http://localhost/grafix/index.php")
    print(driver.title)

    # Log in
    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("admin")
    driver.find_element(By.CLASS_NAME, "login100-form-btn").click()
    print("Logged in successfully")

    # Wait for the page to load and click "Add COMPANY" button
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "COMPANY"))).click()
    print("Add COMPANY button clicked")

    # Wait and open the Company Save form pop-up
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@onclick='click_open(1)']"))).click()
    print("Company form displayed")

    # Ensure the form fields are visible before interacting
    name_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "name")))
    address_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "address")))
    email_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "email")))

    # Fill in the company details
    name_field.send_keys("Test Company")
    address_field.send_keys("123 Test Street")
    email_field.send_keys("test@company.com")
    print("Company details filled in")

    # Select the company type from the dropdown
    company_type_dropdown = Select(driver.find_element(By.NAME, "type"))
    company_type_dropdown.select_by_visible_text("Retail")
    print("Company type selected")

    # Submit the Company Save form
    submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//form[@action='save/company_save.php']//input[@type='submit']")))
    submit_button.click()
    print("Company form submitted")

    company_list = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//span[@class='info-box-number' and contains(text(), 'Test Company')]")))
    print("Company 'Test Company' added successfully")


    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@onclick='click_open(1)']"))).click()
    print("Company form displayed")

    # Ensure the form fields are visible before interacting
    name_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "name")))
    address_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "address")))
    email_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "email")))

    # Fill in the company details
    name_field.send_keys("Test Corporate Company")
    address_field.send_keys("123 Test Corporate Street")
    email_field.send_keys("testCorporate@company.com")
    print("Corporate Company details filled in")

    # Select the company type from the dropdown
    company_type_dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "c_id")) )
    select_type = Select(company_type_dropdown)
    select_type.select_by_visible_text("Corporate")  
    print("type corporate commented")
    # Submit the Company Save form
    submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//form[@action='save/company_save.php']//input[@type='submit']")))
    submit_button.click()
    print("Corporate Company form submitted")







    type_dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "sel")) )

    select_type = Select(type_dropdown)
    select_type.select_by_visible_text("Corporate")  
    print("type corporate commented")

        # Click filter button
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "sel1"))).click()
    print("filter coparate successfully")

    type_dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "sel")) )

    select_type = Select(type_dropdown)
    select_type.select_by_visible_text("Retail")  
    print("type Retail commented")

        # Click filter button
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "sel1"))).click()
    print("filter Retail successfully")

    # select lastes company in the list
    # Wait until all elements matching the criteria are loaded
    elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//span[contains(text(), 'Test Company')]")))

    # Click the last element in the list
    if elements:
        elements[-1].click()
        print("Last occurrence of 'Test Company' selected successfully")
    else:
        print("No element with text 'Test Company' found.")

    wait = WebDriverWait(driver, 10)
    button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Add New Location')]")))

    # Click the button
    button.click()   
    print("Add New Location botton click successfully")

    # Wait for "Add New Location" form to appear and fill in the details
    location_name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "com_name")))
    location_name.send_keys("New Location testing")
    print("Location name entered")

    location_address = driver.find_element(By.ID, "com_add")
    location_address.send_keys("123 Location Street")
    print("Location address entered")

    # Locate the visible part of the Select2 dropdown and click it to open
    select2_dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@class='select2-selection select2-selection--single']"))
    )
    select2_dropdown.click()

    # Wait for the dropdown options to appear, then select "Branch" by text
    branch_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//li[contains(text(), 'Branch')]"))
    )
    branch_option.click()
    print("Branch option selected successfully")

    # Enter email
    location_email = driver.find_element(By.ID, "com_email")
    location_email.send_keys("location@example.com")
    print("Location email entered")

    # Submit the form
    location_submit = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "com_save")))
    location_submit.click()
    print("Location save form submitted successfully")



    # Wait and click the Dashboard link
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "DASHBOARD"))).click()
    print("Dashboard clicked successfully")

    wait = WebDriverWait(driver, 10)
    button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Add New JOB')]")))

    # Click the button
    button.click()   
    print("Add New JOB selected successfully")

    # Wait for the company dropdown to be clickable
    company_dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.NAME, "company_id")))

    # Use the Select class to select the option by visible text (or you can use .select_by_value if preferred)
    select_company = Select(company_dropdown)
    select_company.select_by_visible_text("CLOUD ARM")  
    print("Company selected successfully")

    # Enter a note
    driver.find_element(By.ID, "note_job").send_keys("Test note")
    print("Note added successfully")

        # Enter a note
    driver.find_element(By.ID, "all_job_no").send_keys("555")
    print("Job number added successfully")

    # Wait for the unit element to be clickable and click it
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "u1"))).click()
    print("job save successfully")

    location_dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.NAME, "location_id[]"))
    )

    select_location = Select(location_dropdown)

    # Select multiple options (use select_by_visible_text or select_by_value for each option)
    select_location.select_by_visible_text("homagama") 
    #select_location.select_by_visible_text("Galle") 
    print("Locations selected successfully")

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "u2"))).click()
    print("location save successfully")

    # --------- Add Product Section ---------

    # Wait for the product form to be displayed
    product_form = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//form[@action='save/job/job_product_save.php']"))
    )

    # Select Product from dropdown
    product_dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "product_id"))
    )
    select_product = Select(product_dropdown)
    select_product.select_by_visible_text("Wall branding with Digital sticker Print")  
    print("Product selected successfully")

    # Select Location from dropdown
    location_dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "location"))
    )
    select_location = Select(location_dropdown)
    select_location.select_by_visible_text("homagama")  
    print("Product Location selected successfully")

    # Enter Quantity
    driver.find_element(By.ID, "qty1").send_keys("10")
    print("Quantity entered successfully")
    
    # Enter a note
    driver.find_element(By.ID, "about").send_keys("run in the test case")
    print("description added successfully")

    # Click Save button
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "u3"))).click()
    print("Product saved successfully")


    #Wait until the table is present to avoid timing issues
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "example2")))

    # Find the last "View" button in the table by locating all "View" buttons and clicking the last one
    view_buttons = driver.find_elements(By.XPATH, "//a[contains(@href, 'job_summery')]")
    if view_buttons:
        view_buttons[-1].click()
        print("Clicked on the 'View' button of the last job entry")
    else:
        print("No 'View' button found in the table.")

    

    # Wait until the form appears (assuming it's conditional on 'measure' status)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "width")))

    # Enter width
    width_field = driver.find_element(By.ID, "width")
    width_field.clear()
    width_field.send_keys("10.5")
    print("Width entered successfully.")

    # Enter height
    height_field = driver.find_element(By.ID, "height")
    height_field.clear()
    height_field.send_keys("15.2")
    print("Height entered successfully.")

    # Upload an image file
    #file_upload = driver.find_element(By.ID, "fileToUpload")
    #file_upload.send_keys("/path/to/your/image.jpg")  # Replace with the actual file path
    print("Image uploaded processs is comented.")

    # Enter a note
    note_field = driver.find_element(By.ID, "m_note")
    note_field.clear()
    note_field.send_keys("This is a test note.")
    print("Note added successfully.")

    # Wait until the submit button is clickable, then click it
    submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "m_save")))
    submit_button.click()
    print("measurement Form submitted successfully.")

        # Enter a note
    note_field = driver.find_element(By.ID, "d_note")
    note_field.clear()
    note_field.send_keys("This is a test note for desingner.")
    print("desingner Note added successfully.")

    # Wait until the submit button is clickable, then click it
    submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "d_save")))
    submit_button.click()
    print("desingner Form submitted successfully.")

            # Enter approve note
    note_field = driver.find_element(By.ID, "app_note")
    note_field.clear()
    note_field.send_keys("This is a test note for approvel.")
    print("approvel Note added successfully.")

    # Wait until the submit button is clickable, then click it
    submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "id2")))
    submit_button.click()
    print("desingner Form submitted successfully.")

     # Handle the alert if it appears
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    print("Alert text:", alert.text)
    alert.accept()  # Accept the alert
    print("Alert accepted successfully.")

    # Wait and click the "PRINTING" link after the alert is closed
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "PRINTING"))).click()
    print("Printing department clicked successfully.")

            # Select Location from dropdown
    type_dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "type")) )

    select_type = Select(type_dropdown)
    select_type.select_by_visible_text("Corporate")  
    print("type corporate commented")

        # Click filter button
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "filt1"))).click()
    print("filter coparate successfully")

    # Load the page
   # driver.get("http://localhost/grafix/main/pages/grafix/printing")  # Replace with the actual URL

    # Wait until the "Complete" button is clickable and click it
    complete_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "comp_btn")))
    complete_button.click()
    print("Complete button clicked successfully.")

    # Wait for the form fields to be visible and interactable

    # Fill in the "Height" field
    height_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "height1"))
    )
    height_field.clear()
    height_field.send_keys("5.5")
    print("Height field filled successfully.")

    # Fill in the "Note" field
    note_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "print_note"))
    )
    note_field.clear()
    note_field.send_keys("Test note for the printing job.")
    print("Note field filled successfully.")

    # Wait until the material dropdown is clickable
    mat_dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "mat_id"))
    )

    # Select the "ONE WAY STICKER" option by its visible text
    select_mat = Select(mat_dropdown)
    select_mat.select_by_visible_text("ONE WAY STICKER")
    print("Material 'ONE WAY STICKER' selected successfully.")

    # Wait for the submit button to be clickable and submit the form
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "print_save"))
    )
    submit_button.click()
    print("Form submitted successfully.")

     # Handle the alert if it appears
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    print("Alert text:", alert.text)
    alert.accept()  # Accept the alert
    print("Alert accepted successfully.")





 # Wait and click the Dashboard link
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "DASHBOARD"))).click()
    print("Dashboard clicked successfully")

     # Select Location from dropdown
    type_dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "type")) )

    select_type = Select(type_dropdown)
    select_type.select_by_visible_text("Corporate")  
    print("type Corporate after printing filter selected")

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "filt2"))).click()
    print("filter coparate successfully")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "example1")))


        # Wait for the table to load and locate the last "View" button
    view_buttons = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.ID, "index_view"))
    )
    
    # Click the "View" button in the last row
    view_buttons[-1].click()
    print("Last 'View' button clicked successfully.")


            # Wait for the table to load and locate the last "View" button
    view_buttons = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.ID, "job_view"))
    )

    # Click filter button


    wait = WebDriverWait(driver, 10)
    button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Add New JOB')]")))

    # Click the button
    button.click()   
    print("Add New JOB selected successfully")

    # Wait for the company dropdown to be clickable
    company_dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.NAME, "company_id")))

    # Use the Select class to select the option by visible text (or you can use .select_by_value if preferred)
    select_company = Select(company_dropdown)
    select_company.select_by_visible_text("Test Company")  
    print("Company selected successfully")

    # Enter a note
    driver.find_element(By.ID, "note_job").send_keys("Test note")
    print("Note added successfully")

        # Enter a note
    driver.find_element(By.ID, "all_job_no").send_keys("555")
    print("Job number added successfully")

    # Wait for the unit element to be clickable and click it
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "u1"))).click()
    print("job save successfully")

    location_dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.NAME, "location_id[]"))
    )

    select_location = Select(location_dropdown)

    # Select multiple options (use select_by_visible_text or select_by_value for each option)
    select_location.select_by_visible_text("Location") 
    #select_location.select_by_visible_text("Galle") 
    print("Locations selected successfully")

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "u2"))).click()
    print("location save successfully")

    # --------- Add Product Section ---------

    # Wait for the product form to be displayed
    product_form = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//form[@action='save/job/job_product_save.php']"))
    )

    # Select Product from dropdown
    product_dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "product_id"))
    )
    select_product = Select(product_dropdown)
    select_product.select_by_visible_text("Wall branding with Digital sticker Print")  
    print("Product selected successfully")

    # Select Location from dropdown
    location_dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "location"))
    )
    select_location = Select(location_dropdown)
    select_location.select_by_visible_text("Location")  
    print("Product Location selected for retail successfully")

    # Enter Quantity
    driver.find_element(By.ID, "qty1").send_keys("10")
    print("Quantity entered successfully")
    
    # Enter a note
    driver.find_element(By.ID, "about").send_keys("run in the test case")
    print("description added successfully")

    # Click Save button
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "u3"))).click()
    print("Product saved successfully")


    #Wait until the table is present to avoid timing issues
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "example2")))

    # Find the last "View" button in the table by locating all "View" buttons and clicking the last one
    view_buttons = driver.find_elements(By.XPATH, "//a[contains(@href, 'job_summery')]")
    if view_buttons:
        view_buttons[-1].click()
        print("Clicked on the 'View' button of the last job entry")
    else:
        print("No 'View' button found in the table.")

    

    # Wait until the form appears (assuming it's conditional on 'measure' status)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "width")))

    # Enter width
    width_field = driver.find_element(By.ID, "width")
    width_field.clear()
    width_field.send_keys("10.5")
    print("Width entered successfully.")

    # Enter height
    height_field = driver.find_element(By.ID, "height")
    height_field.clear()
    height_field.send_keys("15.2")
    print("Height entered successfully.")

    # Upload an image file
    #file_upload = driver.find_element(By.ID, "fileToUpload")
    #file_upload.send_keys("/path/to/your/image.jpg")  # Replace with the actual file path
    print("Image uploaded processs is comented.")

    # Enter a note
    note_field = driver.find_element(By.ID, "m_note")
    note_field.clear()
    note_field.send_keys("This is a test note.")
    print("Note added successfully.")

    # Wait until the submit button is clickable, then click it
    submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "m_save")))
    submit_button.click()
    print("measurement Form submitted successfully.")

        # Enter a note
    note_field = driver.find_element(By.ID, "d_note")
    note_field.clear()
    note_field.send_keys("This is a test note for desingner.")
    print("desingner Note added successfully.")

    # Wait until the submit button is clickable, then click it
    submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "d_save")))
    submit_button.click()
    print("desingner Form submitted successfully.")

            # Enter approve note
    note_field = driver.find_element(By.ID, "app_note")
    note_field.clear()
    note_field.send_keys("This is a test note for approvel.")
    print("approvel Note added successfully.")

    # Wait until the submit button is clickable, then click it
    submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "id2")))
    submit_button.click()
    print("desingner Form submitted successfully.")

     # Handle the alert if it appears
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    print("Alert text:", alert.text)
    alert.accept()  # Accept the alert
    print("Alert accepted successfully.")

    # Wait and click the "PRINTING" link after the alert is closed
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "PRINTING"))).click()
    print("Printing department clicked successfully.")

    

 

except selenium.common.exceptions.NoSuchWindowException:
    print("Browser window was closed unexpectedly. Reopening...")
    driver = webdriver.Chrome(service=service)  # Restart the driver if the window closed

except selenium.common.exceptions.ElementNotInteractableException:
    print("One or more elements were not interactable. Please check the form's visibility and state.")

except Exception as e:
    print("An unexpected error occurred:")
    print(f"Error type: {type(e).__name__}")  # Print the type of the error
    print(f"Error message: {str(e)}")          # Print the error message
    # Additional debug info (optional)
    print("Current URL:", driver.current_url)
    print("Page Source Snippet:", driver.page_source[:500])  # Print the first 500 characters of the page source
    print(f"An error occurred: {e}")


except TimeoutException:
    print("One or more elements were not found or not interactable. Please check the form's visibility and state.")
except ElementNotInteractableException:
    print("One or more elements were not interactable. Please check if the form elements are in view or visible.")


finally:
    # Close the browser after a short delay
    time.sleep(2)
    driver.quit()
