

let login=document.getElementById('login');
let signup=document.getElementById('signup');
let account=document.getElementsByClassName('account')[0];





//主页登录按钮事件-点击
login.addEventListener('click',()=>{
    //welcome_musk_panel.style.transform='translateX(0)';
    welcome_mask.style.transform='translateX(0)';
    content_sheet.style.transform='translateX(0)';

    account.style.visibility='visible';
    account.style.opacity='1';
    account.style.transform='translateX(-400px) translateY(-300px)';
    window_cover.style.visibility='visible';
    window_cover.style.opacity='0.5';
})
//主页注册按钮事件-点击
signup.addEventListener('click',()=>{
    //welcome_musk_panel.style.transform='translateX(0)';
    welcome_mask.style.transform='translateX(100%)';
    content_sheet.style.transform='translateX(-50%)';

    account.style.visibility='visible';
    account.style.opacity='1';
    account.style.transform='translateX(-400px) translateY(-300px)';
    window_cover.style.visibility='visible';
    window_cover.style.opacity='0.5';
})

