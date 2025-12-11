# Overview of Changes Made

### Front-End & UI (Abdul Shad)
- Designed and implemented the full front-end user interface using Flask templates
- Created a reusable layout using `base.html` to maintain consistency across pages
- Built Home, Booking, About, and Policies pages
- Implemented Booksy-style card layouts for barbers and services
- Added navigation with active tab highlighting
- Organized static assets into Flask-compatible `static/css` and `static/js` directories
- Added JavaScript for booking form interaction and smooth scrolling
- Improved CSS styling for clean layout and user flow

### Database Design (Erick Diaz)
- Designed the Entity Relationship (ER) diagram
- Identified system entities including Client, Business, ServiceProvider, Services, Appointment, Reviews, and Portfolio
- Defined entity attributes, relationships, primary keys, and constraints
- Implemented database schema using SQL DDL
- Deployed schema and test data in Supabase

### Backend Integration (Armando Hernandez)
- Integrated Flask backend with Supabase using Python
- Implemented logic for inserting and retrieving appointment data
- Built appointment display functionality to show stored data
- Added a fallback mock-data mode for testing without active database credentials

## Development Notes and Adjustments
During development, the project temporarily included a committed virtual environment directory (`.venv`).
This was identified as a version-control mistake and corrected by enforcing `.gitignore` rules to exclude
runtime environments from source control. This adjustment reinforced best practices around dependency
management and repository cleanliness.

## Features Considered but Not Implemented
- User authentication and login
- Payment processing
- Real-time appointment availability
- File uploads for portfolio images
- Automated unit testing

