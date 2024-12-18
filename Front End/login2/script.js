const masukBtnLink = document.querySelector('.masukbtn-link');
const daftarBtnLink = document.querySelector('.daftarbtn-link');
const wrapper = document.querySelector('.wrapper');

daftarBtnLink.addEventListener('click', () => {
    wrapper.classList.toggle('active');
})

masukBtnLink.addEventListener('click', () => {
    wrapper.classList.toggle('active');
})