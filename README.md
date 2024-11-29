# RoleAuth - JWT Authentication with Role-based Access

**RoleAuth** is a backend system built using **Django REST Framework (DRF)** with **JWT Authentication** and **Role-based Access Control (RBAC)**. The system provides **user registration**, **login**, **logout**, and **role-based dashboards** for **admin** and **user** roles.

## Features

- **JWT Authentication**: Secure user login and registration.
- **Role-Based Access Control (RBAC)**: Admins can manage users and assign roles.
- **User Registration**: Create new users with email, password, and roles.
- **User Login**: Authenticate users and issue JWT tokens.
- **User Logout**: Invalidates JWT refresh tokens for logout.
- **Admin Dashboard**: Admin users can manage and view all users.
- **User Dashboard**: Displays information based on user roles.

## Tech Stack

- **Backend**: 
  - **Django**: Web framework
  - **Django REST Framework**: API framework
  - **JWT (JSON Web Tokens)**: Authentication mechanism
  - **BlockAuthentication**: For logout (JWT invalidation)
  - **SQLite/PostgreSQL**: Database (configured in `settings.py`)
  - **CORS**: Cross-Origin Resource Sharing

## Installation

### Clone the Repository

Clone the project to your local machine:

```bash
git clone https://github.com/your-username/roleauth.git
cd roleauth
