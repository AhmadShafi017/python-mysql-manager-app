# 🚀 Professional User Management System (Python & MySQL)

A modular backend application designed to handle high-integrity user data management. This project demonstrates advanced Python concepts, including database automation, Regular Expression (RegEx) validation, and professional-grade file organization.

---

## 🛠️ Core Features
- **Smart Database Initialization:** Automatically creates the database and `users` table upon launch if they don't exist.
- **Robust Data Validation:** - **Name:** Ensures only alphabetic characters are accepted.
  - **Email:** Strict RegEx patterns to prevent invalid email entries.
  - **Age:** Logic to prevent negative or unrealistic numerical inputs.
- **Advanced Search Engine:** Multi-parameter search allowing users to filter by ID, Name, Age, or Email.
- **Analytical Insights:** Built-in mathematical modules to calculate average user age and total record counts.
- **Bulk Data Handling:** Optimized for performance with `executemany` for multi-user insertions.
- **Safety First:** Includes manual confirmation prompts before any `DROP` or `DELETE` operations.

---

## 📁 Project Structure
The project is organized into specialized modules to ensure high maintainability:

- `main.py`: The central hub and user interface.
- `database.py`: Handles connection pooling and schema initialization.
- `insert.py` / `update.py`: Logic for single-entry management with validation.
- `multiple_users.py`: Handles batch processing of data.
- `avarage_math.py` / `total_math.py`: Data analysis and reporting modules.
- `search.py`: Dynamic query builder for data retrieval.

---

## 🚀 Installation & Setup

### 1. Prerequisites
- Python 3.x
- MySQL Server

### 2. Clone & Install
```bash
git clone [https://github.com/YOUR_USERNAME/python-mysql-user-manager.git](https://github.com/YOUR_USERNAME/python-mysql-user-manager.git)
cd python-mysql-user-manager
pip install -r requirements.txt