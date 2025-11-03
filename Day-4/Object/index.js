
const obj1 = { a: 1, b: 2 };

const obj2 = new Object(); obj.a = 1;

function Person(name) {
    this.name = name;
}
const p = new Person("Aniket");
class Car {
    constructor(brand) { this.brand = brand; }
}
const obj3 = Object.create(protoObj);


const user = { name: "Aniket", age: 22, city: "Pune" };
console.log(Object.keys(user));
console.log(Object.values(user));
console.log(Object.entries(user));

const clone = Object.assign({}, user);
clone.city = "Mumbai";
console.log(user.city);

Object.freeze(clone);
clone.age = 30;

const base = { greet() { console.log("Hi!"); } };
const derived = Object.create(base);
derived.greet();

const deepCopy = JSON.parse(JSON.stringify(user));
deepCopy.city = "Delhi";
console.log(user.city);

Object.defineProperty(user, "role", {
    value: "Engineer",
    writable: false,
});
console.log(user.role);
