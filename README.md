# BeneficialIdeas

A web application developed as a course project for the **Django Advanced** course at **SoftUni**.

## Getting Started (Local Development)

### Installation & Setup
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
   
4. Environment variables setup:
   * Copy the `.env.example` file and rename it to `.env`.
   * Open `.env` and fill in your local PostgreSQL credentials (`DB_USER`, `DB_PASSWORD`, etc.) and any `SECRET_KEY`.
   ```
   
5. Database Setup:
   * Create a blank PostgreSQL database using the name you specified as `DB_NAME` in your `.env` file.


6. Run migrations to setup the database structure:
   ```bash
   python manage.py migrate
   ```
7. Load initial test data (Admin user, categories, and ideas):
   ```bash
   python manage.py loaddata test_data.json
   ```
8. Start the development server:
   ```bash
   python manage.py runserver
   ```

### Test Credentials
After loading the test data, you can log in to the admin panel (`/admin/`) or the site using the following credentials:
* **Email:** `admin@beneficialideas.com`
* **Password:** `Password@123`