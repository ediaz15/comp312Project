// static/js/index.js
// Small helper script for booking interactions

// Called when a barber is selected from a card/button
function selectProvider(name) {
  const bookingSection = document.getElementById("booking");
  const selectedBarberHeading = document.getElementById("selected-barber");
  const providerSelect = document.getElementById("provider");

  // Show which barber was selected (if the heading exists)
  if (selectedBarberHeading) {
    selectedBarberHeading.textContent = "Booking with " + name;
  }

  // If there's a <select id="provider"> on the page, pre-fill it
  if (providerSelect) {
    let found = false;

    // Try to match an existing option
    for (const option of providerSelect.options) {
      if (option.value === name) {
        providerSelect.value = name;
        found = true;
        break;
      }
    }

    // If no option existed, add one and select it
    if (!found) {
      const option = document.createElement("option");
      option.value = name;
      option.textContent = name;
      providerSelect.prepend(option);
      providerSelect.value = name;
    }
  }

  // Reveal the booking section (if it's on this page) and scroll to it
  if (bookingSection) {
    bookingSection.classList.remove("hidden");
    bookingSection.scrollIntoView({ behavior: "smooth" });
  }
}

// Automatically wire up any button with a data-provider attribute
document.addEventListener("DOMContentLoaded", () => {
  const providerButtons = document.querySelectorAll("[data-provider]");

  providerButtons.forEach((btn) => {
    btn.addEventListener("click", () => {
      const name = btn.getAttribute("data-provider");
      if (name) {
        selectProvider(name);
      }
    });
  });
});
