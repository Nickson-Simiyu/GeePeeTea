/*let currentCardIndex = 0;
const cards = document.querySelectorAll('.news-card');
const totalCards = cards.length;

// Initially, show only the first news card
if (totalCards > 0) {
    cards[0].style.display = 'block';
}

document.querySelector('.prev').addEventListener('click', () => {
  cards[currentCardIndex].style.display = 'none'; // Hide current card
  currentCardIndex = (currentCardIndex - 1 + totalCards) % totalCards; // Calculate previous card index
  cards[currentCardIndex].style.display = 'block'; // Show previous card
});

document.querySelector('.next').addEventListener('click', () => {
  cards[currentCardIndex].style.display = 'none'; // Hide current card
  currentCardIndex = (currentCardIndex + 1) % totalCards; // Calculate next card index
  cards[currentCardIndex].style.display = 'block'; // Show next card
});

*/
let currentCardIndex = 0;
const cards = document.querySelectorAll('.news-card');
const totalCards = cards.length;
const prevButton = document.querySelector('.prev');
const nextButton = document.querySelector('.next');

// Function to update card visibility
function updateCardVisibility() {
    cards.forEach(card => card.style.display = 'none');
    cards[currentCardIndex].style.display = 'block';
}

// Initialize carousel for small devices
function initializeCarousel() {
    if (window.innerWidth < 991) {
        updateCardVisibility(); // Ensure only the current card is shown
        prevButton.style.display = 'flex';
        nextButton.style.display = 'flex';
        prevButton.addEventListener('click', () => {
            currentCardIndex = (currentCardIndex - 1 + totalCards) % totalCards;
            updateCardVisibility();
        });

        nextButton.addEventListener('click', () => {
            currentCardIndex = (currentCardIndex + 1) % totalCards;
            updateCardVisibility();
        });
    } else {
        // On larger screens, make sure all cards are visible
        cards.forEach(card => card.style.display = 'flex');
        // Optionally hide prev/next buttons
        prevButton.style.display = 'none';
        nextButton.style.display = 'none';
    }
}

// Initial check
initializeCarousel();

// Re-initialize carousel on window resize
window.addEventListener('resize', initializeCarousel);





/*let currentImageIndex = 0;
const images = document.querySelectorAll('.carousel-images img');
const totalImages = images.length;

document.querySelector('.prev').addEventListener('click', () => {
  images[currentImageIndex].style.display = 'none'; // Hide current image
  currentImageIndex = (currentImageIndex - 1 + totalImages) % totalImages; // Calculate previous image index
  images[currentImageIndex].style.display = 'block'; // Show previous image
});

document.querySelector('.next').addEventListener('click', () => {
  images[currentImageIndex].style.display = 'none'; // Hide current image
  currentImageIndex = (currentImageIndex + 1) % totalImages; // Calculate next image index
  images[currentImageIndex].style.display = 'block'; // Show next image
});*/