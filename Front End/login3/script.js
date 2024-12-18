const container=document.querySelector('.container');
const LoginLink=document.querySelector('.SignInLink');
const DaftarLink=document.querySelector('.SignUpLink');

DaftarLink.addEventListener('click',()=>{
    container.classList.add('active');
})

LoginLink.addEventListener('click',()=>{
    container.classList.remove('active');
})