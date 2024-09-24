// Check if the user is logged in, if not redirect to login page
// if (!localStorage.getItem('loggedIn')) {
//     window.location.href = 'login.html';
// }

// Learning materials data
// const materials = {
//     pastPapers: [
//         { name: 'Math Past Paper 2023', link: 'files/math_paper_2023.pdf' },
//         { name: 'Science Past Paper 2022', link: 'files/science_paper_2022.pdf' },
//     ],
//     textbooks: [
//         { name: 'Physics Textbook', link: 'files/physics_textbook.pdf' },
//         { name: 'Chemistry Textbook', link: 'files/chemistry_textbook.pdf' },
//     ],
//     videoTutorials: [
//         { name: 'Biology Tutorial', link: '#' },
//         { name: 'Physics Tutorial', link: '#' },
//     ]
// };

// Function to populate the materials on the page
// function populateMaterials() {
//     const pastPapersList = document.getElementById('pastPapers');
//     const textbooksList = document.getElementById('textbooks');
//     const videoTutorialsList = document.getElementById('videoTutorials');
    
//     materials.pastPapers.forEach(paper => {
//         const li = document.createElement('li');
//         li.innerHTML = `<a href="${paper.link}" target="_blank">${paper.name}</a>`;
//         pastPapersList.appendChild(li);
//     });

//     materials.textbooks.forEach(book => {
//         const li = document.createElement('li');
//         li.innerHTML = `<a href="${book.link}" target="_blank">${book.name}</a>`;
//         textbooksList.appendChild(li);
//     });

//     materials.videoTutorials.forEach(video => {
//         const li = document.createElement('li');
//         li.innerHTML = `<a href="${video.link}" target="_blank">${video.name}</a>`;
//         videoTutorialsList.appendChild(li);
//     });
// }

// Populate materials when the page loads
// populateMaterials();


    // document.addEventListener('DOMContentLoaded', function() {
    //     const pastPapersSection = document.getElementById('past-papers-section');
    //     const textbooksSection = document.getElementById('textbooks-section');
    //     const videoTutorialsSection = document.getElementById('video-tutorials-section');
        
    //     document.getElementById('past-papers-btn').addEventListener('click', function() {
    //         pastPapersSection.classList.toggle('hidden');
    //     });

    //     document.getElementById('textbooks-btn').addEventListener('click', function() {
    //         textbooksSection.classList.toggle('hidden');
    //     });

    //     document.getElementById('video-tutorials-btn').addEventListener('click', function() {
    //         videoTutorialsSection.classList.toggle('hidden');
    //     });
    // });

    // Wait for the DOM to fully load
document.addEventListener('DOMContentLoaded', function() {
    // Select the button inside the topic section
    const featureButton = document.querySelector('.topic button');
    
    // Add a click event listener to toggle the visibility of the feature cards
    featureButton.addEventListener('click', function() {
        const featureCards = document.querySelector('.featured-elements');
        featureCards.classList.toggle('hidden');
        
        // Change button text based on visibility
        if (featureCards.classList.contains('hidden')) {
            featureButton.textContent = 'Show Features';
        } else {
            featureButton.textContent = 'Hide Features';
        }
    });
    
    // Optional: Add click event listeners to feature cards for more interaction
    document.querySelectorAll('.feature-card').forEach(card => {
        card.addEventListener('click', () => {
            alert('Feature Selected: ' + card.querySelector('h2').textContent);
        });
    });
});

const scheduledDates = [];
    document.querySelector('button').addEventListener('click', () => {
        const selectedDate = document.getElementById('study-date').value;
        if (selectedDate) {
            scheduledDates.push(selectedDate);
            const scheduleList = document.getElementById('scheduled-dates');
            const newSchedule = document.createElement('div');
            newSchedule.innerText = `Scheduled Study Date: ${selectedDate}`;
            scheduleList.appendChild(newSchedule);
        }
    });

    const studentName = " "; // This could be dynamically fetched
    const welcomeText = `Welcome Back, ${studentName}`;
    document.querySelector('h1').innerText = welcomeText;


