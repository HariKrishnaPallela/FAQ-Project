FAQ Management System

 Overview

 This is a Django-based FAQ management system with multilingual support, WYSIWYG editor
 integration, and a REST API. It allows users to manage FAQs in multiple languages (English, Hindi,
 Bengali) and retrieve them via an API with caching for improved performance.
 Features- Multilingual Support: FAQs can be translated into Hindi and Bengali.- WYSIWYG Editor: Rich text formatting for FAQ answers using django-ckeditor.- REST API: Fetch FAQs in different languages using the ?lang= query parameter.- Caching: Improved performance with Redis caching.- Admin Panel: User-friendly interface for managing FAQs.
 Installation

 Prerequisites- Python 3.6 or higher- Git- Redis (for caching)
 Steps

 1. Clone the Repository:
   git clone https://github.com/HariKrishnaPallela/FAQ-Project.git

 2. Navigate to the Project Folder:
   cd FAQ-Project

 3. Create a Virtual Environment:
   python -m venv venv

 4. Activate the Virtual Environment:
 
   On Windows:
   venv\Scriptsctivate

   On macOS/Linux:
   source venv/bin/activate

 5. Install Dependencies:
   pip install -r requirements.txt

 6. Set Up Environment Variables:
   Create a .env file with necessary variables like SECRET_KEY, DB configurations, REDIS_URL,
 etc.

 7. Run Migrations:
   python manage.py migrate

 8. Create a Superuser:
   python manage.py createsuperuser

 9. Start the Server:
   python manage.py runserver

 10. Access the Application:
    http://127.0.0.1:8000/

 API Usage- English (Default): curl http://127.0.0.1:8000/api/faqs/- Hindi: curl http://127.0.0.1:8000/api/faqs/?lang=hi- Bengali: curl http://127.0.0.1:8000/api/faqs/?lang=bn

 Example Response:

 [{"question": "What is Django?", "answer": "<p>Django is a web framework for Python.</p>"}]
 Admin Panel- Access via: http://127.0.0.1:8000/admin/

- Login with superuser credentials.
 Testing- Run tests using: python manage.py test
 Contribution

 1. Fork the Repository
 2. Clone Your Fork
 3. Create a New Branch
 4. Make Changes and Test
 5. Commit Your Changes
 6. Push to Your Branch
 7. Open a Pull Request
 
 License
 This project is licensed under the MIT License.
 Happy Coding