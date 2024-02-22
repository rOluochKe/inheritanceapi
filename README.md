# Inheritance Catalog App - Backend API

The Inheritance Catalog App Backend API is responsible for managing the storage, retrieval, and categorization of item data for the mobile application feature. It provides RESTful endpoints for creating, reading, updating, and deleting item information, as well as supporting functionalities such as user authentication and authorization. This document outlines the configuration and usage of the backend API.

## Installation and Setup

1. Clone the repository:
```
git clone git@github.com:rOluochKe/inheritanceapi.git
```

2. Navigate to the project directory:
```
cd inheritanceapi
```

3. Create virtual environment:
```
python -m venv myenv
source myenv/Scripts/Activate -> Windows
source myenv/bin/activate Unix/MacOS
```

4. Create virtual environments:
```
.env file, use .env.example as guide for the required variables
```

5. Configure your database:
```
Using postgresql for this API
```

6. Install packages:
```
Run: pip install -r requirements.txt (From the root directory)
```

7. Run Migration:
```
Run: python manage.py migrate and create superuser Run: python manage.py createsuperuser
```

8. Run App:
```
Run: python manage.py runserver and visit http://localhost:8000/admin/ and http://localhost:8000/api/v1/
```

## API Endpoints

The backend API provides the following endpoints for interacting with item data:

- POST /api/v1/items/: Create a new item.
- GET /api/v1/items/: Retrieve a list of all items.
- GET /api/v1/items/:id/: Retrieve a specific item by ID.
- PUT /api/v1/items/:id/: Update an existing item.
- DELETE /api/v1/items/:id/: Delete an item by ID.

The API also provides endpoints for user authentication:

- POST /api/v1/users/register/: Register a new user.
- POST /api/v1/users/login/: Log in an existing user and generate an authentication token.

The backend API provides the following endpoints for interacting with category data:

- POST /api/v1/categories/: Create a new category.
- GET /api/v1/categories/: Retrieve a list of all categories.
- GET /api/v1/categories/:id/: Retrieve a specific category by ID.
- PUT /api/v1/categories/:id/: Update an existing category.
- DELETE /api/v1/categories/:id/: Delete an creating by ID.

## Technologies Used

- Python: Runtime environment for executing Django code.
- Django: Web application framework for building the backend server.
- PostgreSQL: SQL database for storing item, category and user data.
- JWT (JSON Web Tokens): Used for user authentication and authorization.

## Data Models

1. Item Model:

````
{
  name: String,
  description: String,
  sentimental_value: Number,
  monetary_value: Number,
  location: String,
  ownership_status: String,
  desired_disposition: String,
  category: number,
  user: number,
  images: [String]
}
```

2. User Model:

````
{
    email: string,
    first_name: string,
    last_name: string,
    location: string,
    password: string,
    phone_number: string,
    date_of_birth: datetime,
    profile_picture: object,
}
```


3. Category Model:

```
{
    name: string,
    description: string,
}
```



## Security

- User passwords are hashed using hashed before being stored in the database to ensure security.
- JSON Web Tokens (JWT) are used for user authentication and authorization, with a secret key for token validation.
