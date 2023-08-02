# Django Tender Proposals SPA Project

This is a Django project that implements a Tender Management system. The project allows users to create, view, update, and delete tenders, along with the ability to generate a PDF version of a tender.

## Features

- List all tenders in the system.
- View detailed information about a specific tender.
- Create new tenders with various details, including contractor and client information, finance details, planning phases, and terms and conditions.
- Update existing tenders with revised information.
- Delete tenders that are no longer required.
- Generate a PDF version of a tender for easy sharing and printing.
- User authentication and authorization to restrict access to the tender management system.
- Drag-and-drop functionality for reordering the sections of a tender.
- Preview feature to view the tender as it would appear in the PDF version.
## Installation

1. Clone the repository:

```bash
git clone https://github.com/rakhirana06/Edubuilder_Assignment.git
```

2. Create a virtual environment (optional but recommended):

```bash
cd Bidding_Web_Application
python -m venv venv
```

3. Activate the virtual environment:

- On Windows:

```bash
venv\Scripts\activate
```

- On macOS and Linux:

```bash
source venv/bin/activate
```

4. Install the project dependencies:

```bash
pip install -r requirements.txt
```

5. Apply the database migrations:

```bash
python manage.py migrate
```

6. Create a superuser to access the Django admin:

```bash
python manage.py createsuperuser
```

7. Run the development server:

```bash
python manage.py runserver
```

8. Access the development server at http://localhost:8000/ register as a new user and log in to the application. 

9. Adminpanel can be accesed with the superuser credentials at http://localhost:8000/admin/ 

10. For convience, I've popluated the database with some dummy data. Login crentials are as follows:

*Admin Credentials* : \
**Username** : admin \
**Password** : superpassword

*User Login Credentials* : \
**Username** : user1 \
**Password** : superpassword 

## Usage

- To view the list of all tenders, go to the homepage at `/`.
- To register as a new user, go to `/signup/` and fill in the required details in the form.
- To login as an existing user, go to `/login/` and enter your credentials.
- To logout, go to `/logout/`.
- To view the details of a specific tender, click on the tender title in the list or go to `/<tender-id>/`.
- To create a new tender, go to `/new-tender/` and fill in the required details in the form.
- To update an existing tender, go to `/update-tender/<tender-id>/` and modify the details in the form.
- To delete a tender, go to `/delete-tender/<tender-id>/`.
- To generate a PDF version of a tender, go to `/pdf/<tender-id>/`.

## Project Structure

- `manage.py` is the Django project manager.
- `main` is the main Django project with core configurations.
- `tender` is the Django app that implements the tender management system.
- `templates` contains the HTML templates for the frontend.
- `static` contains the static files for the frontend.
- `requirements.txt` contains the list of third-party packages required by the project.
- `models.py` contains the database models for the project.
- `urls.py` contains the URL configurations for the project.
- `views.py` contains the view functions for the project.
- `forms.py` contains the form classes for the project.
- `admin.py` contains the admin configurations for the project.
- `tests.py` contains the test cases for the project.





## Dependencies

The project uses the following third-party packages:

- Django: A high-level web framework for Python.
- phonenumber-field: A package for handling phone number fields in Django models.

Thank you for reading this far. I hope you enjoy using this project as much as I enjoyed building it. If you have any questions or suggestions, feel free to reach out to me."# Edubuilder_Assignment" 
