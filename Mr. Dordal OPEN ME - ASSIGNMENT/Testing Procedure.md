# Testing Procedure

Testing for this project was performed manually.

## Manual Test Cases

1. **Launch Application**
   - Action: Run `python main.py`
   - Expected Result: Application starts without errors and opens on port 5000.

2. **Home Page Load**
   - Action: Open the home page in the browser.
   - Expected Result: Page loads with navigation bar, barber cards, and styling.

3. **Navigation Links**
   - Action: Click Home, Booking, About, and Policies tabs.
   - Expected Result: Each page loads correctly with consistent layout.

4. **Booking Button Interaction**
   - Action: Click “Book Now” on a barber card.
   - Expected Result: Booking form appears and scrolls into view.

5. **Selected Barber Display**
   - Action: Click different barbers.
   - Expected Result: Selected barber name updates in the booking form.

6. **Booking Page Form**
   - Action: Navigate to Booking page and submit date and time.
   - Expected Result: Form accepts input without errors.

7. **CSS & JS Loading**
   - Action: Refresh the page.
   - Expected Result: Styling and JavaScript behavior load correctly.

8. **Environment Validation**

- Verified application functionality after recreating the virtual environment
- Confirmed dependencies install correctly using `pip install -r dependencies.txt`
- Confirmed application runs successfully after excluding `.venv` from version control

All tests passed successfully during development.
