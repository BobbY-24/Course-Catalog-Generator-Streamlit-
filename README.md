# Course Catalog Generator Streamlit App

## Overview
This project provides a Streamlit interface for scraping university course catalog pages and downloading structured course data as a CSV file. It builds on the course catalog scraping idea with a user-friendly web app.

## Motivation
The app demonstrates how a data extraction script can be wrapped in a simple interface for non-programmers. It is a practical example of combining web scraping, data cleaning, and lightweight app development.

## Methods
- Accept a course catalog URL from the user.
- Fetch and parse page HTML.
- Extract course code, credit hours, title, and description.
- Display the resulting table in Streamlit.
- Provide a CSV download button.

## Limitations
- Results depend on the target catalog’s HTML structure.
- The app should only be used on sites where scraping is allowed.
- It may need parser adjustments for different universities or catalog systems.

## Future Improvements
- Add saved HTML fixtures and parser tests.
- Add support for multiple catalog page formats.
- Improve error messages for unsupported pages.
- Add a sample input URL in the README after confirming a stable source.

## How to Run
```bash
git clone https://github.com/BobbY-24/Course-Catalog-Generator-Streamlit-.git
cd Course-Catalog-Generator-Streamlit-
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```
