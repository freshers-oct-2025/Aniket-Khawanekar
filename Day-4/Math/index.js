let date = new Date()

console.log(date)

console.log(date.getDay())

switch (date.getDay()) {
    case 1:
        console.log("Mon")
        break;
    case 2:
        console.log("Tue")
        break;
    case 3:
        console.log("Web")
        break;
    case 4:
        console.log("Thus")
        break;
    case 5:
        console.log("Fri")
        break;
    case 6:
        console.log("Sat")
        break;
    case 0:
        console.log("Sun")
        break;
}



console.log(date.getDate)
console.log(date.getFullYear())
console.log(date.getHours())
console.log(date.getSeconds())
console.log(date.getMilliseconds)
console.log(date.getTime)


console.log(Math.floor(999+Math.random()*9000))

