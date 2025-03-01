# FAQ Management System

## Overview  
This **FAQ Management System** is built with Django and supports the following features:
- **Multilingual Support**: FAQs can be managed in English, Hindi, and Bengali.
- **WYSIWYG Editor Integration**: Use **django-ckeditor** for rich text formatting in FAQ answers.
- **REST API**: Retrieve FAQs in different languages using the `?lang=` query parameter.
- **Caching**: Improve performance with Django's default cache backend.
- **Admin Panel**: A user-friendly interface for managing FAQs.

---

## Features
- **Multilingual Support**: FAQs are available in multiple languages (English, Hindi, Bengali).
- **WYSIWYG Editor**: Integrate rich text formatting into FAQ answers using **django-ckeditor**.
- **REST API**: Access FAQs in different languages with the `?lang=` query parameter.
- **Caching**: Improve performance with **Django's default cache backend**.
- **Admin Panel**: An easy-to-use admin interface for managing FAQs.

---

## Installation

### Prerequisites  
Ensure the following are installed on your machine:
- **Python 3.11**
- **Git**

### Steps to Set Up
1. **Clone the Repository**:
    ```bash
    git clone https://github.com/HariKrishnaPallela/FAQ-Project.git
    ```

2. **Navigate to the Project Folder**:
    ```bash
    cd FAQ-Project
    ```

3. **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    ```

4. **Activate the Virtual Environment**:
    - **On Windows**:
      ```bash
      venv\Scripts\activate
      ```
    - **On macOS/Linux**:
      ```bash
      source venv/bin/activate
      ```

5. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

6. **Set Up Environment Variables**:  
   Create a `.env` file and define necessary variables such as:
   - `SECRET_KEY`
   - Database configurations

7. **Run Migrations**:
    ```bash
    python manage.py migrate
    ```

8. **Create a Superuser**:
    ```bash
    python manage.py createsuperuser
    ```

9. **Start the Server**:
    ```bash
    python manage.py runserver
    ```

10. **Access the Application**:  
    Open your browser and go to:  
    [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## API Usage

You can retrieve FAQs in different languages using the following API endpoints:

- **English (Default)**:  
  ```bash
  curl http://127.0.0.1:8000/api/faqs/
  ```

- **Hindi**:  
  ```bash
  curl http://127.0.0.1:8000/api/faqs/?lang=hi
  ```

- **Bengali**:  
  ```bash
  curl http://127.0.0.1:8000/api/faqs/?lang=bn

  ```

### Example Response:
```json
[{
  "question": "What is Django?",
  "answer": "<p>Django is a web framework for Python.</p>"
}]
```

---

## Admin Panel  
You can manage FAQs through the Django admin panel.  
Access via: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)  
Login with your superuser credentials.

---

## Testing  
Run the tests for the application using the following command:
```bash
python manage.py test
```

---

## Contribution

1. **Fork the Repository**
2. **Clone your fork**
3. **Create a new branch for your changes**
4. **Make changes and test**
5. **Commit your changes**
6. **Push to your branch**
7. **Open a pull request**

---

## License  
This project is licensed under the MIT License.

**Happy Coding! 🚀**

