// String Coding
document.title  = 'DOM_TRAINING'
const body = document.body
body.append('Hello World')

// Element Cooding
const h1 = document.createElement('h1')
h1.textContent = 'Value H1'

// Alternatif 1 
const myName = document.createElement('p')
myName.innerHTML = 'User1'

// Alternatif2
const yourName = document.createElement('b')
yourName.innerText= 'User2'

body.append(h1)
body.append(myName)
body.append(yourName)
