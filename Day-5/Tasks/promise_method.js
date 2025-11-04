let p1 = new Promise((res, rej) => setTimeout(() => res("fast"), 500));


let p3 = new Promise((res, rej) => setTimeout(() => res("slow"), 1500));



let p2 = new Promise((res, rej) => setTimeout(() => rej("error"), 1000));

Promise.all([p1, p3])
  .then((x) => console.log("all:", x))
  .catch((e) => console.log("all err:", e));

Promise.allSettled([p1, p2, p3]).then((x) => console.log("allsettled:", x));


Promise.any([p2, p3])
.then((x) => console.log("any:", x))
.catch((e) => console.log("any err:", e));



Promise.race([p1, p3]).then((x) => console.log("race:", x));