const menuToggle = document.querySelector('.menu-toggle');
const navLinks = document.querySelector('.nav-links');
const xiconmenu = document.querySelector('.x-icon-menu');
const ctabtn = document.querySelector('.cta-button');
menuToggle.addEventListener('click', () => {
    navLinks.classList.toggle('active');
    menuToggle.style.display = 'none';
    xiconmenu.style.display = 'flex';
    // Check if screen width is at most 992px
    if (window.innerWidth >= 993) {
        menuToggle.style.display = 'none';
        
    }
    if (window.innerWidth <= 992 ) {
        ctabtn.style.display = 'flex';
        
    }
});
xiconmenu.addEventListener('click', () => {
    navLinks.classList.toggle('active');
    xiconmenu.style.display = 'none';
    menuToggle.style.display = 'flex';
    ctabtn.style.display = 'none';
    
  
    
});
