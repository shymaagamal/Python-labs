# Crowd-Funding Console App

## Overview
The **Crowd-Funding Console App** is a Python-based command-line application that allows users to register, log in, and manage projects. Users can create, update, view, and delete projects, making it a simple yet effective platform for managing fundraising campaigns.

## Features
### User Authentication
- Register a new user with a secure password (hashed using bcrypt)
- Login system with session management
- Email-based authentication

### Project Management
- Create a new project with a title, description, target amount, and deadline
- View all available projects
- Update existing project details
- Delete a project

### Data Persistence
- User and project data is stored in JSON files for simplicity and portability
- Secure password storage using bcrypt hashing

## Installation
### Prerequisites
Ensure you have **Python 3.11.9** installed on your system.

### Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/crowdfunding-app.git](https://github.com/shymaagamal/Python-labs.git
   cd crowdfunding-app
   ```
2. Install dependencies:
   ```sh
   pip install bcrypt
   ```
3. Run the application:
   ```sh
   python main.py
   ```

## Usage
- **Register**: Create a new user account.
- **Login**: Authenticate with an email and password.
- **Create Project**: Provide a title, description, goal amount, and deadline.
- **View Projects**: List all available projects.
- **Update Project**: Modify your project details.
- **Delete Project**: Remove your project permanently.

