/** JavaScript Code */


// form hide/show

let button = document.getElementById('toggleProfile')


// button.onclick = function (){
//     let hideform = document.getElementById('hideform')
//     let showform = document.getElementById('showform')
//     console.log(hideform);
//     showform.classList.remove('hidden')
//     hideform.classList.add('hidden')
// }


button.addEventListener('click', () =>{
    let hideform = document.getElementById('hideform')
    let showform = document.getElementById('showform')
    console.log(hideform);
    showform.classList.remove('hidden')
    hideform.classList.add('hidden')
})