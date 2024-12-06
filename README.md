# CRUD Application with Authentication

## Overview
This project is a web-based CRUD (Create, Read, Update, Delete) application designed with user authentication. The application provides a simple interface for managing user data. It includes features such as user registration, login, and operations on user records.

## Features

### Authentication
- **Login Form**:
  - Users must log in with their email and password to access the application.
  - Invalid credentials will result in an error message.
- **Registration Form**:
  - New users can create an account via the "Register" tab.
  - Requires basic details such as email and password.

### User Management (CRUD Operations)
- **Read**: Displays a table of all registered users once logged in.
  - The table includes user details like ID, name, email, and more.
- **Update**:
  - Clicking on the user ID redirects to a form where the user's details can be updated.
  - Changes are saved and reflected in the user table.
- **Delete**:
  - Users can delete a record directly from the user table.
  - A confirmation prompt ensures actions are intentional.

### Navigation
- **Home Page**:
  - Default landing page with the login form.
  - Accessible only to non-authenticated users.
- **Register Tab**:
  - Allows new user account creation.
- **User Table**:
  - Accessible only after a successful login.
  - Displays data for all enrolled users.

## Getting Started

### Prerequisites
- Ensure you have the following installed on your system:
  - [Python](https://www.python.org/) (backend is in Python)
  - A database (MySQL)

### Testing
- Test user registration, login, and CRUD functionalities to ensure they work as expected.

## Technologies Used
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Backend**: Django
- **Database**: MySQL

