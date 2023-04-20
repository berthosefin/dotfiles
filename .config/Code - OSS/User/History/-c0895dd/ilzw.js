#!/usr/bin/env node

import boxen from "boxen";
import chalk from "chalk";
import inquirer from "inquirer";

let currency = "";
let rate = 0;
let start = new Date();
let duration = 0;
let netToPay = 0;

const log = console.log;
const sleep = (ms = 1000) => new Promise((r) => setTimeout(r, ms));

// ask the currency
async function askCurrency() {
  const answer = await inquirer.prompt({
    type: "list",
    name: "currency",
    message: "Currency: ",
    default: "Ar",
    choices: ["Ar", "€", "$"],
  });

  currency = answer.currency;
}

// ask rate
async function askRate() {
  const answer = await inquirer.prompt({
    type: "input",
    name: "rate",
    message: `Rate: (${currency}/Min) `,
    default: 30,
    validate: async (input) => {
      if (Number(input) > 0) {
        return true;
      }
      return "Please enter a positive value";
    },
  });

  rate = answer.rate;
}

// TODO:
// check arguments
// async function checkArgs() {}

// interface, refresh time: 1s
async function refreshScreen() {
  console.clear();
  log(
    boxen(
      ` Rate : ${rate} ${currency}/Min  
 Begin: ${start.toLocaleTimeString()}`,
      {
        borderStyle: "round",
        borderColor: "gray",
        title: "CYBERTO",
        textAlignment: "left",
      }
    )
  );

  let now = new Date();
  let newDuration = new Date(now - start).toISOString().substring(11, 19);
  log(
    ` Duration  : ${newDuration}
 Net To Pay: ${netToPay} ${currency}`
  );
}

// count time elapsed and net to pay
async function counter() {
  await sleep();
  duration += 1;
  netToPay = Math.round(rate * (duration / 60));
}

// TODO:
// backup last session to a log file
// async function backup() {}

// Run it with top-level await
console.clear();
log(
  chalk.bgGreen.gray(` CYBERTO `),
  chalk.green("A cyber counter cli tool \n")
);
await askCurrency();
await askRate();
start = new Date();
while (true) {
  await refreshScreen();
  await counter();
}
