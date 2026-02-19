import fs from "node:fs";

const data = fs.readFileSync("../input/maj.txt", "utf8");
main(data);

function main(data) {
  let output = [];

  for (let line of data.split("\n").slice(1)) {
    output.push(findMaj(line.split(" ")));
  }

  console.log(output.join(" "));
}

function findMaj(arr) {
  let counts = {};
  for (let el of arr) {
    if (counts[el]) {
      counts[el] += 1;
    } else {
      counts[el] = 1;
    }
  }

  let maj = Object.entries(counts).filter(([k, v]) => v > arr.length / 2);
  return maj.length ? maj[0][0] : "-1";
}
