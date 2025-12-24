🚀 Advanced Modular User Management System (Python & MySQL)
A professional-grade backend application featuring a Stack-Based Navigation Architecture. This project demonstrates an advanced understanding of Python modularity, state management, and secure database operations.

🏗️ Architectural Overview
Unlike standard linear scripts, this system utilizes a Navigation Stack to manage the User Interface.

State Management: Uses a Custom Stack (stack.py) to handle nested menus and seamless "Back" functionality.

Decoupled Logic: Each database operation (Add, Search, Update, Delete) is isolated into its own module, following the Single Responsibility Principle.

Dynamic Routing: main.py acts as a central controller, routing user input to specific logic modules based on the current state in the pages.py registry.

🛠️ Key Features
Sophisticated Search Engine: Specialized modules for filtering by ID, Name, Age, or Email (search_by_x.py).

Granular Update System: Dedicated logic for updating specific fields to reduce database overhead.

Analytics Module: Real-time data processing for calculating average age and total user metrics.

Security & Validation: - RegEx Integration: Strict email and name validation across all entry points.

Environment Safety: Database credentials secured via python-dotenv.

Manual Overrides: Confirmation prompts for high-risk operations like DROP TABLE or DELETE DATABASE.

📁 Project Structure
The project is organized into functional clusters:

Core: main.py, stack.py, pages.py, database.py

Modules:

add/: Single and multi-user insertion logic.

search/: Specialized retrieval engines.

update/: Targeted field modification scripts.

delete/: Safe removal of records, tables, and databases.

analytics/: Data reporting tools.

🚀 Installation & Setup
1. Prerequisites
Python 3.10+

MySQL Server

A .env file (see .env.example for required variables)

2. Quick Start
Bash

# Clone the repository
git clone https://github.com/AhmadShafi017/python-mysql-user-manager.git

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

Developed by Ahmad Shafi Focused on writing clean, scalable, and professional Python code.