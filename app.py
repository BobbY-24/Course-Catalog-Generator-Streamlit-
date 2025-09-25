import streamlit as st
import requests
from bs4 import BeautifulSoup
import re
import csv
import os

def csv_creator(source, csv_name):
    soup = requests.get(source).text
    soup = BeautifulSoup(soup, 'html.parser')
 
    res = soup.find_all('strong')
    res2 = soup.find_all(class_='courseblockdesc')

    final = []

    i = 0
    for combo in res:
        # safer regex for name
        name_match = re.search(r'([A-Z]{2,4}\s\d{4})', combo.text)
        if name_match:
            name = name_match.group().replace(" ", "_")
        else:
            name = f"COURSE_{i}"

        credit = combo.text[-15]
        if not credit.isnumeric():
            credit = 1

        des_match = re.search(r'\s([A-Z].+?\.)\s', combo.text)
        des = des_match.group()[1:-2] if des_match else "N/A"

        des2 = res2[i].text.strip() if i < len(res2) else "N/A"
        final.append([name, credit, des, des2])
        i += 1

    output_file = f"{csv_name}.csv"
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['class_code', 'credit_hours', 'official_name', 'description'])
        writer.writerows(final)

    return output_file


# ---------------- Streamlit UI ----------------
st.title("📘 Course Catalog Scraper")
st.write("Enter a course catalog URL and download structured course info as CSV.")

url = st.text_input("Course catalog URL")
filename = st.text_input("Output CSV file name (without .csv)", value="courses")

if st.button("Generate CSV"):
    if url.strip():
        try:
            csv_file = csv_creator(url, filename)
            st.success(f"CSV file `{csv_file}` created successfully!")

            with open(csv_file, "rb") as f:
                st.download_button(
                    label="⬇️ Download CSV",
                    data=f,
                    file_name=csv_file,
                    mime="text/csv"
                )
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a valid URL.")
