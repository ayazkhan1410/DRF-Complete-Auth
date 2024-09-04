# Django REST Framework Authentication

This project is a complete implementation of an authentication system using Django REST Framework (DRF). It includes user registration, login, profile management, password change, and password reset functionalities.

## Features

- **User Registration**: Allows new users to register with an email and password.
- **User Login**: Authenticates users with JWT tokens.
- **Profile View**: Displays the authenticated user's profile information.
- **Password Change**: Allows authenticated users to change their password.
- **Password Reset**: Sends a password reset link to the user's email.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ayazkhan1410/DRF-Complete-Auth.git
   cd your-repo-name
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv env
   source env/bin/activate   # On Windows use `env\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

## API Endpoints

### 1. Registration

- **URL**: `/api/register/`
- **Method**: `POST`
- **Request Body**: 
  ```json
  {
    "email": "user@example.com",
    "password": "yourpassword",
    "password2": "yourpassword"
  }
  ```
- **Response**:
  - **201 Created**: Registration successful with a JWT token.
  - **400 Bad Request**: Validation errors.

### 2. Login

- **URL**: `/api/login/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "email": "user@example.com",
    "password": "yourpassword"
  }
  ```
- **Response**:
  - **200 OK**: Login successful with a JWT token.
  - **404 Not Found**: Invalid credentials.

### 3. Profile

- **URL**: `/api/profile/`
- **Method**: `GET`
- **Headers**: 
  ```http
  Authorization: Bearer <access_token>
  ```
- **Response**:
  - **200 OK**: Returns the user's profile information.

### 4. Change Password

- **URL**: `/api/change-password/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "old_password": "oldpassword",
    "new_password": "newpassword"
  }
  ```
- **Response**:
  - **200 OK**: Password changed successfully.
  - **400 Bad Request**: Validation errors.

### 5. Password Reset

- **URL**: `/api/reset-password/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "email": "user@example.com"
  }
  ```
- **Response**:
  - **200 OK**: Password reset link sent successfully.
  - **400 Bad Request**: Validation errors.

### 6. Confirm Password Reset

- **URL**: `/api/reset-password-confirm/{uid}/{token}/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "new_password": "newpassword"
  }
  ```
- **Response**:
  - **201 Created**: Password reset successfully.
  - **400 Bad Request**: Validation errors.

## Custom Renderers

Custom JSON renderers are used to format API responses for better consistency and readability.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

This project uses the following third-party libraries:

- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/)

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## Contact

For any questions or issues, feel free to reach out.

---

Feel free to customize this README to better fit your project's specific details and requirements.
```
