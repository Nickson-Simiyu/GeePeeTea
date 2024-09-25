let currentStep = 1;

function showStep(step) {
    // Hide all steps
    document.querySelectorAll('.form-step').forEach(function(element) {
        element.style.display = 'none';
    });
    // Show the specified step
    document.querySelector('#step-' + step).style.display = 'block';
}

function nextStep() {
    if (currentStep < 3) {
        currentStep++;
        showStep(currentStep);
    }
}

function prevStep() {
    if (currentStep > 1) {
        currentStep--;
        showStep(currentStep);
    }
}

// Initialize the form with the first step visible
document.addEventListener('DOMContentLoaded', function() {
    showStep(currentStep);
});

// Update the label based on slider value
const roleSlider = document.getElementById('roleSlider');
const roleLabel = document.getElementById('roleLabel');

roleSlider.addEventListener('input', function() {
    if (this.value == 1) {
        roleLabel.textContent = "Parent";
    } else if (this.value == 2) {
        roleLabel.textContent = "Teacher";
    } else if (this.value == 3) {
        roleLabel.textContent = "Student";
    }
});

// Redirect based on slider value


