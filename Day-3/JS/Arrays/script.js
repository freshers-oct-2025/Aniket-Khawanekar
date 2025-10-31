// let arr=[10,20,30,40]
// console.log(arr)

let arr2=new Array(50,60,70)
console.log(arr2)

let arr3=[10,"hello",true,null,undefined,()=>{console.log("Function inside the array")},{name:"CR7"},[20,30,[40,[50,[60,["last"]]]]]]

console.log(arr3)
arr3[5]()
console.log(arr3[6].name)
console.log(arr3[7][2][1][1][1][0])

arr3.forEach((e,i) => {
    console.log(e)
    console.log(i)
});

arr3[7].forEach(e=>console.log(e))

let arr=[10,20,30,40]
arr.push(10)
arr.pop()
arr.shift()
arr.unshift(0)
arr.indexOf(30)
let i=arr.includes(20)
console.log(i)
let s=arr.slice(2)
console.log(s)
arr.splice(1,2,[90,100]);
console.log(arr)