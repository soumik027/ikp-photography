# Photographer's Portfolio & Booking System 📸✨

<p align="center">
  <b>A modern, fully responsive full-stack web application built with Python and Django, designed to showcase professional photography galleries and streamline client consultation and session bookings with smooth UI styling.</b>
</p>

---

## 🚀 Key Features & UI Enhancements

* **Dynamic Event Galleries:** Categorized, high-resolution showcases for diverse photography styles (weddings, baby portraits, ceremonies, etc.).
* **Smooth UI Animations:** Integrated CSS transitions and interactive hover effects across image cards and navigation elements for a sleek, modern user experience.
* **Client Booking & Consultation System:** Interactive forms allowing users to submit session requests directly to the database.
* **Admin Dashboard:** Integrated Django Admin backend to manage site configurations, incoming inquiries, and media content securely.
* **Responsive Layout:** Fluid grid-based design optimized for seamless viewing across mobile, tablet, and desktop viewports.

---

## 🛠️ Tech Stack

* **Backend:** Python, Django (MVT Architecture)
* **Database:** SQLite (Local development)
* **Frontend:** HTML5, Modern CSS3 (with custom animations and flexbox/grid layouts), JavaScript
* **Tools & Version Control:** Git, GitHub, VS Code

---

## 📂 Project Structure

```text
ikp-photography-main/
│
├── booking/          # Handles client booking requests and service packages
├── contact/          # Manages site settings, contact info, and inquiry routes
├── core/             # Project-level settings, URL configurations, and WSGI/ASGI
├── home/             # Landing page, about view, and main presentation views
├── media/            # Uploaded images and gallery media assets
├── portfolio/        # Static and dynamic multi-image event showcases
├── static/           # Global CSS stylesheets (with custom animations), images, and JS assets
├── manage.py         # Django project management utility
└── requirements.txt  # Project dependencies
