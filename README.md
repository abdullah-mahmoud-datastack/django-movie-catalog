# 🎬 Foreign Movie Tracker

A beautifully crafted Django web application designed to catalog and showcase a personal collection of foreign movies and TV shows. This project provides an intuitive and responsive interface to browse, search, and filter through an extensive watch history.

![Project Status](https://img.shields.io/badge/Status-Active-success)
![Framework](https://img.shields.io/badge/Framework-Django-092E20?logo=django)
![Frontend](https://img.shields.io/badge/Frontend-Bootstrap_5-7952B3?logo=bootstrap)

---

## ✨ Features

- **Comprehensive Cataloging**: Seamlessly stores details for both Films and TV Shows, complete with cover images, descriptions, and external links.
- **Advanced Search & Filtering**: 
  - 🔍 **Title Search**: Quickly find movies by their exact or partial title.
  - 🎭 **Actor Search**: Auto-completing search functionality to find content by cast members.
  - 📅 **Year Search**: Discover content based on its release year.
  - 📺 **Content Type Filtering**: Effortlessly toggle between viewing "All Content", "Films", or "TV Shows".
- **Dynamic UI/UX**:
  - Visual badges indicating active search and filter criteria.
  - Clear, one-click "Clear Filters" mechanism.
  - Responsive image grid utilizing modern UI cards with specific "TV" tags for easy identification.
  - Seamless pagination to navigate through large collections efficiently.
- **Admin Management**: Dedicated forms and Django admin panel integration for easily adding new movies and actors to the database.

---

## 🛠️ Technology Stack

- **Backend**: Python, Django (Models, ORM, Views, Pagination)
- **Frontend**: HTML5, CSS3, Bootstrap 5 (Responsive Grid, Alerts, Badges)
- **Scripting & Interactivity**: jQuery, jQuery UI (for Actor Autocomplete)
- **Database**: SQLite (default Django DB, easily scalable to PostgreSQL/MySQL)

---

## 🚀 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone <your-repository-url>
   cd Movies
   ```

2. **Create a virtual environment (Recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install django
   # Install any other requirements if a requirements.txt is added
   ```

4. **Apply Migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a Superuser (for Admin panel access):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server:**
   ```bash
   python manage.py runserver
   ```
   *The application will now be running at `http://127.0.0.1:8000/`. You can access the admin panel at `http://127.0.0.1:8000/admin/`.*

---

## 📸 Usage Overview

The home page presents a powerful top-navigation search and filter bar. You can mix and match filters (e.g., searching for a specific actor in a TV show from a specific year). 

Selecting an actor from the autocomplete dropdown will instantly filter the catalog to display their associated works. The "Active Filters" bar dynamically keeps track of what criteria are currently applied, giving you full control over your browsing experience.

---

## 🖋️ Designer

**Abdullah Mahmoud**
