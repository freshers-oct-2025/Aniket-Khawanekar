let str="Bahubali"
let newstr=str[0]+str[1]+str[4]+str[6]+str[3]
console.log(newstr)

console.log(str.length)
for(let i=0;i<str.length;i++)
    console.log(str[i])


// let rev=str.split("").reverse().join("3")
// console.log(rev)

let rev= new String()
for(let i=str.length-1;i>=0;i-- )
{
    rev+=str[i]
}

console.log(rev)


let num='9049'
let newNum=num.padStart(12,"*").padEnd(20,"*")
console.log(newNum)


let str1="       Cristiano"
let trimmedStart=str1.trimStart()
let trimmedEnd=str1.trimEnd()
let trimmed=str1.trim()

console.log(trimmed)
console.log(trimmedStart)
console.log(trimmedEnd)


let up=str.toUpperCase()
console.log(up)

let low=str.toLowerCase()
console.log(low)

console.log(str.replaceAll("a","i"))

console.log(str.replace("B","Kh").replace("b","g")+" la "+str.replace("B","j").replace("h",""))


// const str="Katappa"

let val=str.slice(2,-3)
let val1=str.slice(-1)
let val2=str.slice(-1,str.length)
console.log(val)

let sub=str.substring(2,-2)
let sub1=str.substring(4)
console.log(sub1)
console.log(sub)

let substr=str.substr(5,3)
console.log(substr)

console.log(str.includes("pp"))
console.log(str.startsWith("K"))
console.log(str.endsWith("f"))
console.log(str.at("K"))
console.log(str.charAt(3))
console.log(str.charCodeAt(1))
    



