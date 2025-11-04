let b = document.getElementById("btn1");
let inp = document.getElementById("in1");




b.addEventListener("click", () => {
    console.log("button clicked");
});
let para = document.getElementById("p1");
inp.addEventListener("keyup", (e) => {
  console.log("input val:", e.target.value);
});

para.addEventListener("mouseover", () => {
  para.style.color = "red";
});

para.addEventListener("mouseout", () => {
  para.style.color = "black";
});

const div=document.querySelector("#div")
console.log(div)

div.addEventListener("keypress",()=>{
    console.log(key)
    
})