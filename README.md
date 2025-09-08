# URL Shortend

A simple web-based URL shortening service built with **Python** and **Flask**.  
Allows users to enter long URLs and get back shortened links that redirect to the original URL.

---

## 🚀 Features

- Create shortened URLs for long URLs  
- Redirect shortened URLs to their original long URL  
- Dashboard or UI for viewing all shortened links (if implemented)  
- Database support, with migrations for schema changes  
- Simple & clean front-end using HTML / Mako templates  

---

## 🗂️ Project Structure
url-shortend/
├── app/ # Application code: routes, models, templates, static
├── instance/ # Instance-specific configuration/data
├── migrations/ # Alembic / Flask-Migrate scripts for DB changes
├── config.py # Configuration settings (database URI, secret key, etc.)
├── run.py # Entry point to launch the application
├── requirements.txt # Python dependencies required
└── pycache/ # compiled bytecode files
