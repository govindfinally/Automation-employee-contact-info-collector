from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
import pandas as pd
import traceback
import time
import random
from src.components.beautifull_soup import EmailScraper, allparser

def start_driver():
    d = webdriver.Chrome()
    w = WebDriverWait(d, 20)
    return d, w

def append_to_existing_excel(existing_file_path, df_new):
    df_existing = pd.read_excel(existing_file_path, sheet_name='Internship Outreach')

    if "Company Name" not in df_new.columns and "Domain" in df_new.columns:
        df_new = df_new.rename(columns={"Domain": "Company Name"})

    df_combined = pd.concat([df_existing, df_new], ignore_index=True)
    df_combined.drop_duplicates(subset=['Company Name'], inplace=True)

    with pd.ExcelWriter(existing_file_path, engine='openpyxl') as writer:
        df_combined.to_excel(writer, index=False, sheet_name='Internship Outreach')

    print(f"Appended {len(df_new)} new companies. Total now: {len(df_combined)}")

# --- Load company list ---
input_file = input("enter file path: ")
excel_file = input_file if input_file else "Govind_Mohanty_Internship_Outreach_Extended.xlsx"
df_companies = pd.read_excel(excel_file)
company_domains = df_companies["Company Name"].dropna().tolist()

# --- Start browser ---
driver, wait = start_driver()

domains_list, names_list, emails_list, positions_list, linkedin_presence_list = [], [], [], [], []

for idx, domain in enumerate(company_domains):
    try:
        driver.get("https://hunter.io/domain-search")
        wait.until(EC.presence_of_element_located((By.ID, "domain-field")))

        domain_input = driver.find_element(By.ID, "domain-field")
        domain_input.clear()
        clean_domain = "".join(domain.split())
        domain_input.send_keys(f"{clean_domain}.com")

        
        print(f"{clean_domain}.com: ",end="")
        print("This domain has been sent to search") 
        domain_input.send_keys(Keys.ENTER)

        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "ds-result__fullname")))

        names = [el.text for el in driver.find_elements(By.CLASS_NAME, "ds-result__fullname")]
        emails = [el.text for el in driver.find_elements(By.CLASS_NAME, "ds-result__email")]
        positions = [el.text for el in driver.find_elements(By.CLASS_NAME, "ds-result__attribute")]
        linkedin_spans = driver.find_elements(By.CSS_SELECTOR, "span.fab.fa-linkedin")
        linkedin_presence = "Yes" if linkedin_spans else "No"

        domains_list.append(domain)
        names_list.append(", ".join(names))
        emails_list.append(", ".join(emails))
        positions_list.append(", ".join(positions))
        linkedin_presence_list.append(linkedin_presence)

        print(f"[{idx+1}/{len(company_domains)}] ✅ {domain}")

        time.sleep(random.uniform(1.5, 3))  # Anti-block delay

    except (TimeoutException, WebDriverException) as e:
        print(f"⚠ Error processing domain {domain}: {repr(e)}")
        traceback.print_exc()

        # Restart driver if session is broken
        if "invalid session id" in str(e).lower() or isinstance(e, WebDriverException):
            print("🔄 Restarting browser...")
            driver.quit()
            driver, wait = start_driver()

        domains_list.append(domain)
        names_list.append("")
        emails_list.append("")
        positions_list.append("")
        linkedin_presence_list.append("No")

driver.quit()

# Save results
df_results = pd.DataFrame({
    "Domain": domains_list,
    "Employee_Names": names_list,
    "Emails": emails_list,
    "Positions": positions_list,
    "LinkedIn_Present": linkedin_presence_list
})

print(df_results)
append_to_existing_excel(excel_file, df_results)
