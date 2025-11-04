

const td=document.querySelector(".loadCustomer")
const td1=document.querySelector(".loadImage")

td.addEventListener("click",()=>{
    loadCustomer()
    

})

td1.addEventListener("click",()=>{
    LoadImages()

})



async function loadCustomer(){
await fetch("https://playground.mockoon.com/customers")
    .then(response => response.json())
    .then(data => {
        
        // console.log(data)
        data.forEach((element,i) => {
            let tbody=document.querySelector("#CustomerTableBody")
            let row="";
            if(i<10)
           {
            // console.log(element)
             row=`
            <tr>
            <td>${i+1}</td>
            <td>${element.name}</td>
            <td>${element.email}</td>
            <td>${element.phone}</td>
            </tr>
            `
            
           }
           tbody.innerHTML=tbody.innerHTML+row;
        });
        
    })

}


async function LoadImages() {
    await fetch("https://playground.mockoon.com/photos")
    .then(response => response.json())
    .then(data => {
        
        // console.log(data)
        data.forEach((element,i) => {
            let tbody=document.querySelector("#ImageTableBody")
            let row="";
            if(i<10)
           {
            console.log(element)
             row=`
            <tr>
            <td>${element.caption}</td>
            <td>${element.likes}</td>
            <td>${element.url}</td>
            </tr>
            `
            
           }
           tbody.innerHTML=tbody.innerHTML+row;
        });
        
    })
}

