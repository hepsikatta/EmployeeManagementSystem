**Enterprise Employee Hub**
    A vibrant, modern, and fully animated **Employee Management System (EMS)** built using Python, Django, and Bootstrap 5. This application allows administrators to easily manage an organization's workforce 
    directory through a highly interactive, responsive web interface.

    
**Tech Stack**
      Backend Framework: Python & Django 6.x
      Frontend UI:HTML5, CSS3 (Custom keyframes & gradients), Bootstrap 5
      Database: SQLite3

      
**Project Work Flow**
  Understanding how data flows through the application is straightforward:
  [ Admin Login ] ──> [ Dashboard View ] ──> [ Search Bar Filters List ]
                             │
                             ├──> [ + Add New Employee Form ] ──> Saves to Database
                             ├──> [ Modify Details Form ]     ──> Updates Database
                             └──> [ Delete Confirmation ]     ──> Removes from Database
 

Follow these quick configuration steps to get the project running on your computer:

### 1. Clone the Repository
git clone https://github.com/hepsikatta/EmployeeManagementSystem.git
cd EmployeeManagementSystem
### 2. Set Up Virtual Environment & Dependencies

# Create environment
python -m venv venv

# Activate on Windows
.\venv\Scripts\activate

# Install Django
pip install django


### 3. Initialize Database Tables

python manage.py migrate


### 4. Create your Admin Credentials
Run this command to create your login password and user account:

python manage.py createsuperuser


### 5. Boot up the Server

python manage.py runserver

Open your browser and navigate to **`http://127.0.0.1:8000/`** to log in and start using your new Enterprise Employee Hub
