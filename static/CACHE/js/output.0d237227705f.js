let button=document.getElementById('toggleProfile')
console.log(button);button.onclick=function(params){let hideform=document.getElementById('hideform')
let showform=document.getElementById('showform')
console.log(hideform);showform.classList.remove('hidden')
hideform.classList.add('hidden')};