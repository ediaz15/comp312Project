# Team Contributions

## Abdul Shad — Front-End Lead & UI/UX Developer
- Led all front-end and user interface development.
- Created all major pages: **Home**, **Booking**, **About**, and **Policies**.
- Designed the **layout structure** using Flask templates (`base.html` + child templates).
- Organized **static file structure** for CSS and JavaScript.
- Built a clean, Booksy-inspired UI with card components, navigation bar, and section layouts.
- Implemented JavaScript interactions:
  - Smooth scroll
  - Auto-selecting barbers on booking
  - Dynamic booking form behavior
- Ensured consistency across all templates and improved styling and user experience.
- Set up project structure for teammates (templates, static folder, shared components).
- Wrote project documentation and README.
- Assisted in connecting templates to backend-provided data once API endpoints stabilized.

---

## Erick Diaz — Database Architect & Supabase Engineer
- Designed the **full database schema**, including entities, attributes, and relationships.
- Created the ER diagram and structural constraints following proper cardinality rules.
- Implemented the database in **Supabase** using SQL DDL scripts.
- Set up primary keys, foreign keys, cascading behaviors, and relationship tables.
- Inserted sample/test data for development.
- Connected Flask backend to Supabase and validated the connection.
- Ensured the schema supports core workflows:
  - Clients
  - Service Providers
  - Businesses
  - Services
  - Appointments
  - Reviews
  - Portfolio
- Documented schema and assisted team members with database questions.
- Proposed future improvements including:
  - Supabase OAuth authentication for clients/businesses
  - Normalization to avoid update anomalies
  - Adding more entities for scalability

---

## Armando Hernandez — Backend Integration & Appointment Logic
- Connected the front-end pages to backend Supabase functions using `supaConnection.py`.
- Implemented logic for:
  - Creating clients
  - Creating appointments
  - Retrieving service providers and services
  - Retrieving upcoming appointments for the admin dashboard
- Built the **Admin Appointments Page** (`/appointments`) displaying enriched data:
  - Barber name
  - Service details
  - Client name and phone
  - Appointment time/date
- Developed end-to-end booking workflow:
  1. User selects a barber
  2. Booking page auto-selects the barber dynamically
  3. User submits the form
  4. System creates a client row
  5. Appointment row is automatically generated using IDs
  6. Notification message (“Booking complete!”)
  7. Admin page displays the new appointment
- Implemented mock mode support to test functionality without a live database.
- Ensured backend stability, form validation, and correct error handling.
