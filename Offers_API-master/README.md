# README

## Prerequisites

Make sure you have the following installed on your system:

1. **Python 3.8 or later**: [Download Python](https://www.python.org/downloads/)
2. **pip**: Python package manager (comes with Python)
3. **virtualenv** (optional but recommended): `pip install virtualenv`
4. Create a Virtual Environment (optional but recommended): `python -m venv .venv
source .venv/bin/activate`  # On Windows, use `.venv\Scripts\activate`
---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Kacper12445/Offers_API.git
   cd Offers_API
   
2. **Set credentials**:
   Add your Firebase credentials to the project as service-account.json.

3. **Clone the Repository**:
   ```bash
   pip install -r requirements.txt

4. **Run BE**:
   ```bash
   uvicorn main:app --reload
   
5. **Documentation**:
   After running the server:

    Link to SWAGGER UI: [SWAGGER UI](http://127.0.0.1:8000/docs).

    Link to ReDoc: [ReDoc](http://127.0.0.1:8000/redoc). 