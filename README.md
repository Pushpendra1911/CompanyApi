# Django API for Importing Employee Data

This project is a Django-based API designed to read employee and company data from an Excel/CSV file and insert it into a MySQL database. The API establishes a one-to-many relationship between companies and employees, where one company can have multiple employees.

## Features

- Reads data from Excel (.xlsx) and CSV files.
- Creates `Company` and `Employee` entries in the database.
- Establishes a one-to-many relationship between companies and employees.
- Error handling for missing or incorrectly formatted files.
- REST API endpoints for uploading files and accessing employee and company information.

## Requirements

- Python 3.12.3
- Django 5.1.2
- openpyxl 3.1.5
- pandas 2.2.3
- djangorestframework 3.15.2
- mysqlclient 2.2.4

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Pushpendra1911/CompanyApi
    ```

2. Change into the project directory:

    ```bash
    cd Api_Project
    ```

3. Create a virtual environment:

    ```bash
    python -m venv myenv
    ```

4. Activate the virtual environment:

        ```bash
        .\myenv\Scripts\activate
        ```


5. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Apply migrations to set up the database:

    ```bash
    python manage.py migrate
    ```

7. Run the development server:

    ```bash
    python manage.py runserver
    ```

## Usage

### Upload Data

To upload data from an Excel/CSV file, use the `/upload/` endpoint with a POST request. 

Example using `curl`:

```bash
curl --location 'http://127.0.0.1:8000/api/upload/' \
--header 'Cookie: csrftoken=wS19urJd76mytaIiYRaAMb5t6f38ICZA' \
--form 'file=@"/C:/Users/pushp/Downloads/Practical Task Python sheet (4).xlsx"'
