const kitBag={
    football:"Nike football",
    cleats:"addidas",
    bottle:"water bottle",
    energy:"BCAA"

}
let {football,bottle}=kitBag;

console.log(football)
console.log(bottle)

let arr=["cristiano","Ronaldo","Sunil ","Chhetri"]
let [c,...ch]=arr 

console.log(ch)

console.log(...arr) 

let func=(val1,val2,val3,val4)=>{
    console.log(val4)
}

func(...arr)
func(arr[0],arr[1],arr[2],arr[3])


let str="cristiano"
let [a,...b]=str

console.log(b)


const kitBag1={
    football:"Nike football",
    cleats:"addidas",
    bottle:"water bottle",
    energy:"BCAA"

}

let deepCopy={...kitBag1}

deepCopy.football="Addidas Football"

console.log(kitBag1)
console.log(deepCopy)
