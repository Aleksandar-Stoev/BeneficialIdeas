# BeneficialIdeas

A web application developed as a course project for the **Django Advanced** course at **SoftUni**.

## Getting Started (Local Development)

### Prerequisites
* Python 3.10+
* pip

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Aleksandar-Stoev/BeneficialIdeas
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```bash
   python manage.py migrate
   ```
5. Start the development server:
   ```bash
   python manage.py runserver
   ```
