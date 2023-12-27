// Made get_lost responsive
p1 = document.getElementById('get_lost')
p2 = document.getElementById('get_lost2')
resize_handler = function (event) {
if (window.innerWidth < 635 || window.innerHeight < 730) {
    p1.remove()
    p2.remove()
}
if (window.innerWidth >= 635 && window.innerHeight >= 730) {
    document.body.appendChild(p1)
    document.body.appendChild(p2)
}
}
window.addEventListener('resize', resize_handler)
resize_handler()
//  Made get_lost responsive
    
// Made get_lost responsive
let count = 9
counter = document.getElementById('counter')
const timer = setInterval(function () {
count--
counter.innerHTML = count
console.log(count)
if (count === 0) {
    clearInterval(timer)
    console.log("Time's up!")
    document.location.href = '/'
}
}, 1000)
// Made get_lost responsive