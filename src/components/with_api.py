
import os
import requests
import pandas as pd
import os

def hunter_api_domain_search(domain, api_key):
    url = "https://api.hunter.io/v2/domain-search"
    params = {
        "domain": domain,
        "api_key": api_key
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"⚠ Failed for {domain}, status: {response.status_code}")
        return None

# --- Load company list ---
input_file = input("Enter file path: ")
excel_file = input_file if input_file else "Govind_Mohanty_Internship_Outreach_Extended.xlsx"
df_companies = pd.read_excel(excel_file)
company_domains = df_companies["Company Name"].dropna().tolist()

# --- Get Hunter API key ---
api_key = os.getenv("HUNTER_API_KEY")

domains_list, names_list, emails_list, positions_list, linkedin_presence_list = [], [], [], [], []

for idx, domain in enumerate(company_domains):
    clean_domain = domain.strip()
    data = hunter_api_domain_search(f"{clean_domain}.com", api_key)

    if data and "data" in data:
        emails = data["data"].get("emails", [])
        employee_names = [e.get("first_name", "") + " " + e.get("last_name", "") for e in emails]
        employee_emails = [e.get("value", "") for e in emails]
        employee_positions = [e.get("position", "") for e in emails]
        linkedin_presence = ["Yes" if e.get("linkedin") else "No" for e in emails]

        domains_list.append(clean_domain)
        names_list.append(", ".join(filter(None, employee_names)))
        emails_list.append(", ".join(employee_emails))
        positions_list.append(", ".join(filter(None, employee_positions)))
        linkedin_presence_list.append("Yes" if any(lp == "Yes" for lp in linkedin_presence) else "No")

        print(f"[{idx+1}/{len(company_domains)}] ✅ {clean_domain}")

    else:
        domains_list.append(clean_domain)
        names_list.append("")
        emails_list.append("")
        positions_list.append("")
        linkedin_presence_list.append("No")

# --- Save results ---
df_results = pd.DataFrame({
    "Domain": domains_list,
    "Employee_Names": names_list,
    "Emails": emails_list,
    "Positions": positions_list,
    "LinkedIn_Present": linkedin_presence_list
})

print(df_results)

output_file = "hunter_api_results.xlsx"
with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
    df_results.to_excel(writer, index=False, sheet_name="Internship Outreach")

print(f"✅ Results saved to {output_file}")
