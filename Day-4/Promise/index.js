let p1= new Promise((resolve,reject)=>{
    let a=1;
    if(a==10){
        resolve()
    }else{
        reject()
    }
})

p1.then(()=>console.log("True. a==10"))
p1.catch(()=>console.log("false. a==10"))


let p2=new Promise((resolve,reject)=>{
let a=10+39
// resolve(a)
reject("so get out")
})


p2.then(a=>console.log(a))
p2.catch(a=>console.log(a))

let p=fetch("https://api.github.com/users")
console.log(p)
p.then((val)=>{
    console.log(val)
    let data=val.json()
    return data
}).then((val)=>{
    console.log(val)
}).catch((e)=>console.log("something went wrong",e))

fetch("https://api.github.com/users").then(res=>res).then(data=>
    data.json()).then(data=>
            data.map(val=>console.log(val.avatar_url))
        )
        
        
        



        try {
            let func= async ()=>{
                let res=await fetch("https://api.github.com/users")
                let data=await res.json()
    
                // console.log(data)
                data.map(val=>console.log(val.login))
            }
            func()
        } catch (error) {
            console.log(error)
        }

