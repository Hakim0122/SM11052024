document.addEventListener('DOMContentLoaded', (event) => {
    // Smooth Scrolling
    document.querySelectorAll('nav a').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Image Modal
    const images = document.querySelectorAll('.featured-image');
    images.forEach(image => {
        image.addEventListener('click', function() {
            openModal(this.src);
        });
    });

    function openModal(src) {
        const modal = document.createElement('div');
        modal.classList.add('modal');
        modal.innerHTML = `
            <div class="modal-content">
                <span class="close-button">&times;</span>
                <img src="${src}" class="modal-image">
            </div>
        `;
        document.body.appendChild(modal);
        
        // Close modal functionality
        modal.querySelector('.close-button').addEventListener('click', () => {
            modal.remove();
        });

        // Close modal when clicking outside of the image
        modal.addEventListener('click', (e) => {
            if (e.target === modal) {
                modal.remove();
            }
        });
    }

    // Sticky Header Animation
    const header = document.querySelector('nav');
    const sticky = header.offsetTop;

    window.addEventListener('scroll', () => {
        if (window.pageYOffset > sticky) {
            header.classList.add('sticky-header');
        } else {
            header.classList.remove('sticky-header');
        }
    });
});
