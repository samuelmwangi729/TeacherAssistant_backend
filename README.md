# Teacher Assistant to Help Computer Studies Teachers Mark Practicals

## Overview

This project is a web application designed to help Computer Studies teachers mark practicals. The app allows teachers to upload Microsoft Word (`.docx`) and Excel (`.xlsx`) files, extract specific styles from these files, and return the extracted styles as JSON responses.

### Key Features:
- **File Upload**: Upload `.docx` and `.xlsx` files for processing.
- **Styles Extraction**: 
  - Extract text styles from `.docx` files using `python-docx`.
  - Extract cell font styles from `.xlsx` files using `openpyxl`.
- **JSON Response**: The extracted styles are returned as a JSON response, enabling easy integration with other systems.

## Technologies Used

- **Backend**: Django with Django Rest Framework (DRF)
- **File Processing**: `python-docx` for Word documents, `openpyxl` for Excel files
- **Hosting**: Railway
- **Version Control**: GitHub

## Installation

### Prerequisites:
- Python 3.x
- pip
- Git (for version control)

### Steps to Set Up Locally

1. **Clone the Repository**:

   Clone the repository from GitHub using SSH (ensure you have your SSH key set up with GitHub).

   ```bash
   git https://github.com/samuelmwangi729/TeacherAssistant_backend.git
   cd <clone directory>
   ```
2. **setup the environment**

   ```bash
   python -m virtualenv venv
   source venv/bin/activate # On Windows use venv\Scripts\activate
   pip install -r requirements.txt`
   ```
3. **run the server** 

   ```bash
    python manage.py migrate
    python manage.py runserver
    ```
## API Reference

#### Get all items

```http
  POST /api/word
```

| formdata | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `file` | `file` | **Required**.|

#### Get item

```http
  POST /api/excel
```

| formdata | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `file`      | `file` | **Required**.|

## Badges

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)


## Authors

- [Samuel Mwangi](https://www.github.com/samuelmwangi729)

