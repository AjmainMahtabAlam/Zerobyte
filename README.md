# Courier Service API

A RESTful API for managing packages in a courier service.

## Installation

```bash
git clone <repo-url>
cd courier_service
virtualenv venv
source venv/bin/activate
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

Api Endpoints
/api/token/ - Obtain JWT token
/api/packages/ - List/Create packages
/api/packages/<id>/ - Retrieve/Update package
/api/packages/<id>/delete/ - Soft delete package
/api/packages/<id>/restore/ - Restore deleted package
