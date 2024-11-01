from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException, NoSuchElementException
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

   # Locate the table and ensure it’s loaded
    #table = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "example1")))

    # Find all rows within the table's tbody
    #rows = table.find_elements(By.CSS_SELECTOR, "tbody tr")

    #if rows:
        # Select the last row
       # last_row = rows[-1]

        # Find and click the "Complete" button in the last row
       # complete_button = last_row.find_element(By.ID, "comp_btn")
       # complete_button.click()
        #print("Complete button in the last row clicked successfully.")

            # Select Location from dropdown
      #  location_dropdown = WebDriverWait(driver, 10).until(
       #     EC.element_to_be_clickable((By.NAME, "material_id")))

        #select_location = Select(location_dropdown)
        #select_location.select_by_visible_text("FLEX 3' B/B")  
        #print("Material 'MAT STICKER' selected successfully.")

       

        # Fill in the "Height" field
        #height_field = WebDriverWait(driver, 10).until(
         #   EC.presence_of_element_located((By.ID, "height1"))
        #)
        #height_field.clear()
        #height_field.send_keys("5.5")

        # Fill in the "Note" field
        #note_field = WebDriverWait(driver, 10).until(
         #   EC.presence_of_element_located((By.ID, "print_note"))
        #)
        #note_field.clear()
        #note_field.send_keys("Test note for the printing job.")

        # Submit the form
        #submit_button = WebDriverWait(driver, 10).until(
         #   EC.element_to_be_clickable((By.ID, "print_save"))
        #)
        #submit_button.click()
        #print("Form submitted successfully.")

        # Verification Step: Check for submission success message (customize as needed)
        #WebDriverWait(driver, 10).until(
         #   EC.alert_is_present()
        #)
        #alert = driver.switch_to.alert
        #print("Alert Text:", alert.text)  # Prints the alert text if any
        #alert.accept()  # Dismisses the alert

 # Wait and click the Dashboard link
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "DASHBOARD"))).click()
    print("Dashboard clicked successfully")

     # Select Location from dropdown
    type_dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "type")) )

    select_type = Select(type_dropdown)
    select_type.select_by_visible_text("Retail")  
    print("type retail filter selected")

        # Click filter button
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "filt2"))).click()
    print("filter coparate successfully")

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

except TimeoutException:
    print("Timed out waiting for the Material dropdown to become clickable.")
except ElementNotInteractableException:
    print("The Material dropdown is not interactable. Please ensure the form is fully loaded.")

finally:
    # Close the browser after a short delay
    time.sleep(2)
    driver.quit()
