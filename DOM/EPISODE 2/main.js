document.title  = 'DOM_TRAINING_BUTTON'

const btn1 = document.getElementById('btn1')
const btn2 = document.querySelector('btn2')

const defaultText = "CLICK"
btn1.textContent = defaultText

btn1.style.border = 'none'
btn1.style.padding = '8px'
btn1.style.fontSize = '24px'
btn1.style.background = 'tomato'


function changeColor() {
    btn1.style.background = 'lightblue'

}

function changeText() {
    btn1.textContent = "Change Text"
}

function changeDefault() {
    btn1.textContent = defaultText
}