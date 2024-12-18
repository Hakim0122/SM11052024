const wrapper = document.querySelector('.wrapper');
const loginLink = document.querySelector('.login-link');
const daftarLink = document.querySelector('.daftar-link');
const btnPop = document.querySelector('.btnlogin-popup')
const iconClose = document.querySelector('.icon-close')

daftarLink.addEventListener('click', () => {
    wrapper.classList.add('active');
});

loginLink.addEventListener('click', () => {
    wrapper.classList.remove('active');
});

btnPop.addEventListener('click', () => {
    wrapper.classList.add('active-popup');
});

iconClose.addEventListener('click', () => {
    wrapper.classList.remove('active-popup');
});

document.getElementById("loginButton").addEventListener("click", function() {
    parent.frames['home'].location.href = 'awal.html';
});