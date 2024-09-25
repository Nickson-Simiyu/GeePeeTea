let currentCardIndex = 0;
const cards = document.querySelectorAll('.news-card');
const totalCards = cards.length;
const prevButton = document.querySelector('.prev');
const nextButton = document.querySelector('.next');

// Function to update card visibility
function updateCardVisibility() {
    if (cards.length > 0 && currentCardIndex >= 0 && currentCardIndex < totalCards) {
        cards.forEach(card => card.style.display = 'none');
        cards[currentCardIndex].style.display = 'block';
    } else {
        console.log('No cards available or invalid index.');
    }
}

// Initialize carousel for small devices
function initializeCarousel() {
    if (window.innerWidth < 991) {
        updateCardVisibility(); // Ensure only the current card is shown

        if (prevButton && nextButton) { 
            prevButton.style.display = 'flex';
            nextButton.style.display = 'flex';

            prevButton.removeEventListener('click', handlePrev); // Avoid multiple bindings
            nextButton.removeEventListener('click', handleNext); // Avoid multiple bindings

            prevButton.addEventListener('click', handlePrev);
            nextButton.addEventListener('click', handleNext);
        }
    } else {
        // On larger screens, make sure all cards are visible
        cards.forEach(card => card.style.display = 'flex');

        // Optionally hide prev/next buttons
        if (prevButton && nextButton) {
            prevButton.style.display = 'none';
            nextButton.style.display = 'none';
        }
    }
}

function handlePrev() {
    currentCardIndex = (currentCardIndex - 1 + totalCards) % totalCards;
    updateCardVisibility();
}

function handleNext() {
    currentCardIndex = (currentCardIndex + 1) % totalCards;
    updateCardVisibility();
}

// Initial check
initializeCarousel();

// Re-initialize carousel on window resize
window.addEventListener('resize', initializeCarousel);
