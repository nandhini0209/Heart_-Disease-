// ============================================================
// script.js - Custom JavaScript for Heart Risk AI
// ============================================================

// ---- Initialize Bootstrap Tooltips ----
// Finds all elements with data-bs-toggle="tooltip" and activates them
document.addEventListener('DOMContentLoaded', function () {
  var tooltipTriggerList = [].slice.call(
    document.querySelectorAll('[data-bs-toggle="tooltip"]')
  );
  tooltipTriggerList.forEach(function (tooltipTriggerEl) {
    new bootstrap.Tooltip(tooltipTriggerEl);
  });
});

// ---- Form Validation Feedback ----
// Adds visual feedback when the form is submitted with empty fields
document.addEventListener('DOMContentLoaded', function () {
  var form = document.getElementById('predictionForm');

  if (form) {
    form.addEventListener('submit', function (event) {
      // Check if form is valid using HTML5 built-in validation
      if (!form.checkValidity()) {
        event.preventDefault();       // Stop form submission
        event.stopPropagation();      // Stop event bubbling
      }
      form.classList.add('was-validated'); // Show Bootstrap validation styles
    });
  }
});

// ---- Smooth Scroll to Form on Hero Button Click (optional) ----
// If you add a "Get Started" button in the hero, this scrolls to the form
var heroBtn = document.getElementById('heroBtn');
if (heroBtn) {
  heroBtn.addEventListener('click', function () {
    document.querySelector('#predictionForm').scrollIntoView({
      behavior: 'smooth'
    });
  });
}
