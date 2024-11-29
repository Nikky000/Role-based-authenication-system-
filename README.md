RoleAuth - JWT Authentication with Role-based Access
RoleAuth is a backend system built using Django REST Framework (DRF) with JWT Authentication and Role-based Access Control (RBAC). It includes endpoints for login, registration, logout, user management, and role-based dashboards for admin and user roles.

Tech Stack
Django: Web framework
Django REST Framework: API framework
JWT Authentication: Secure user authentication
BlockAuthentication: Logout mechanism for invalidating JWT
SQLite/PostgreSQL: Database (configurable in settings.py)
CORS: Cross-origin resource sharing handling
Features
User Registration: Allows users to register with email, password, and role.
Login: Authenticates users and issues JWT tokens.
Logout: Invalidates JWT refresh tokens for logout.
Role-based Access: Admins can manage users and roles, regular users have restricted access.
Installation and Setup
Step 1: Clone the Repository
Clone the project to your local machine:

bash
Copy code
git clone https://github.com/your-username/roleauth.git
cd roleauth
Step 2: Set up the Python Environment
Create a virtual environment:

bash
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Step 3: Set Up the Database
Run migrations:

bash
Copy code
python manage.py migrate
Create a superuser:

bash
Copy code
python manage.py createsuperuser
Follow the prompts to create the superuser.

Step 4: Run the Development Server
Start the Django development server:

bash
Copy code
python manage.py runserver
The backend will be available at http://localhost:8000/.
