
function testScope() {
  var a = 10;
  let b = 20;
  if (true) {
    var c = 30; 
    let d = 40; 
  }
  console.log("a:", a); 
  console.log("b:", b); 
  console.log("c:", c); 
  console.log(d); 
}
testScope();

console.log(hoistedVar); 
var hoistedVar = "Hoisted variable";
hoistedFunc();
function hoistedFunc() {
  console.log("Function is hoisted!");
}