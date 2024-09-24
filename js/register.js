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



/*let currentStep = 1;
let formData = {}; // Object to hold form data across steps

function showStep(step) {
    document.querySelectorAll('.form-step').forEach(function(element) {
        element.style.display = 'none';
    });
    document.querySelector('#step-' + step).style.display = 'block';

    // Special handling for the confirmation step to display the collected data
    if (step === 3) {
        displayConfirmation();
    }
}

function nextStep() {
    saveFormData(currentStep);
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

function saveFormData(step) {
    if (step === 1) {
        formData.email = document.querySelector('#step-1 input[type="email"]').value;
        formData.password = document.querySelector('#step-1 input[type="password"]').value;
    } else if (step === 2) {
        formData.firstName = document.querySelector('#step-2 input[placeholder="First Name"]').value;
        formData.lastName = document.querySelector('#step-2 input[placeholder="Last Name"]').value;
    }
    // Step 3 is the confirmation, no need to save data here
}

function displayConfirmation() {
    const confirmationSection = document.getElementById('step-3');
    confirmationSection.innerHTML = '<h2>Confirmation</h2><p>Please review your information, then submit your application.</p>';
    for (const [key, value] of Object.entries(formData)) {
        const p = document.createElement('p');
        p.textContent = `${key}: ${value}`;
        confirmationSection.appendChild(p);
    }
    const prevButton = document.createElement('button');
    prevButton.textContent = 'Previous';
    prevButton.setAttribute('type', 'button');
    prevButton.onclick = prevStep;
    confirmationSection.appendChild(prevButton);

    const submitButton = document.createElement('button');
    submitButton.textContent = 'Submit';
    submitButton.setAttribute('type', 'submit');
    confirmationSection.appendChild(submitButton);
}

document.addEventListener('DOMContentLoaded', function() {
    showStep(currentStep);
});
/*let currentStep = 1;

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



let currentStep = 1;
let formData = {}; // Object to hold form data across steps

function showStep(step) {
    document.querySelectorAll('.form-step').forEach(function(element) {
        element.style.display = 'none';
    });
    document.querySelector('#step-' + step).style.display = 'block';

    // Special handling for the confirmation step to display the collected data
    if (step === 3) {
        displayConfirmation();
    }
}

function nextStep() {
    // Save data before moving to the next step
    saveFormData(currentStep);
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

function saveFormData(step) {
    if (step === 1) {
        formData.email = document.querySelector('input[type="email"]').value;
        formData.password = document.querySelector('input[type="password"]').value;
    } else if (step === 2) {
        formData.firstName = document.querySelector('input[placeholder="First Name"]').value;
        formData.lastName = document.querySelector('input[placeholder="Last Name"]').value;
    }
    // Step 3 is the confirmation, no need to save data here
}

function displayConfirmation() {
    const confirmationSection = document.getElementById('step-3');
    // Clear previous data
    confirmationSection.innerHTML = '<h2>Confirmation</h2><p>Please review your information, then submit your application.</p>';
    // Dynamically create a summary of the form data for review
    for (const [key, value] of Object.entries(formData)) {
        const p = document.createElement('p');
        p.textContent = `${key}: ${value}`;
        confirmationSection.appendChild(p);
    }
    // Append the previous and submit button again since we cleared them
    const prevButton = document.createElement('button');
    prevButton.textContent = 'Previous';
    prevButton.setAttribute('type', 'button');
    prevButton.onclick = prevStep;
    confirmationSection.appendChild(prevButton);

    const submitButton = document.createElement('button');
    submitButton.textContent = 'Submit';
    submitButton.setAttribute('type', 'submit');
    confirmationSection.appendChild(submitButton);
}

document.addEventListener('DOMContentLoaded', function() {
    showStep(currentStep);
});*/