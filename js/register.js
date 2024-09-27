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