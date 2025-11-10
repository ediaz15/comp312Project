// scripts/index.js
// Very simple script to toggle booking form

function selectProvider(name) {
  // Show which barber was selected
  const bookingSection = document.getElementById("booking");
  const selectedBarber = document.getElementById("selected-barber");

  selectedBarber.textContent = "Booking with " + name;
  bookingSection.classList.remove("hidden");

  // Scroll smoothly to the form
  bookingSection.scrollIntoView({ behavior: "smooth" });
}
