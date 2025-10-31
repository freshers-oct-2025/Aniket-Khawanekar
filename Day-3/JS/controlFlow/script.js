let score = 75;


if (score > 90) {
  console.log("Grade: A");
} else if (score > 70) {
  console.log("Grade: B");
} else {
  console.log("Grade: C");
}


let day = "Monday";
switch (day) {
  case "Monday":
    console.log("start work");
    break;
  case "Friday":
    console.log("Weekend loading...");
    break;
  default:
    console.log("Midweek vibes");
}


let count = 0;
while (count < 3) {
  console.log(" count:", count);
  count++;
}

let num2 = 0;
do {
  console.log(" count:", num2);
  num2++;
} while (num2 < 3);

for (let i = 1; i <= 5; i++) {
  if (i === 3) continue; 
  if (i === 5) break; 
  console.log(" i =", i);
}