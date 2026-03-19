
# 📍 Address Book API

A minimal, high-performance REST API built with **Python 3.12+** and **FastAPI** to manage an address book with geospatial search capabilities.

## 🚀 Features

  * **Full CRUD:** Create, Read, Update, and Delete addresses.
  * **Geospatial Search:** Retrieve addresses within a specific kilometer radius of a given coordinate.
  * **Data Validation:** Strict coordinate validation using **Pydantic v2**.
  * **Persistence:** Lightweight **SQLite** database integration via SQLAlchemy.
  * **Structured Logging:** Internal application logging for tracking API activity.

-----

## 🛠️ Setup and Execution

Follow these exact steps to get the API running locally on your machine.

### 1\. Clone the Repository

Open your terminal and run:

```powershell
git clone <your-repo-link>
cd address-book-api
```

### 2\. Create and Activate Virtual Environment

**Windows (PowerShell):**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Mac/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3\. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4\. Run the Application

Start the server using Uvicorn:

```bash
uvicorn app.main:app --reload
```

-----

## 📖 API Documentation

Once the server is started, the API is fully self-documenting. Open your browser to:

  * **Interactive Swagger UI:** [http://127.0.0.1:8000/docs](https://www.google.com/search?q=http://127.0.0.1:8000/docs)
  * **Alternative ReDoc:** [http://127.0.0.1:8000/redoc](https://www.google.com/search?q=http://127.0.0.1:8000/redoc)

### How to use the Distance Search:

To find addresses within a **10km** radius of specific coordinates, use the following query parameters in your GET request:
`GET /addresses/?lat=48.8584&lon=2.2945&radius_km=10`

-----

## 📂 Project Structure

```text
address-book-api/
├── app/
│   ├── routers/      # API route handlers
│   ├── utils/        # Geospatial math logic
│   ├── main.py       # App entry point & Logging
│   ├── models.py     # Database tables
│   ├── schemas.py    # Data validation
│   ├── database.py   # Connection logic
│   └── crud.py       # Database operations
├── requirements.txt  # Dependencies
└── README.md         # Instructions
```

-----
