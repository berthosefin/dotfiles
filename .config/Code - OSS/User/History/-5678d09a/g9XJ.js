#!/usr/bin/env node

import chalk from "chalk";
import inquirer from "inquirer";
import boxen from "boxen";
import signale from "signale";

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
      if (Number(input)) {
        return true;
      }
      return "Please enter a positive value";
    },
  });

  rate = Number(answer.rate);
}

// check if argument is corrent
async function checkArg() {}

// interface, refresh time: 1s
async function refreshScreen() {
  console.clear();
  console.log(
    boxen(
      `
      Rate : ${rate} ${currency}/Min       
      Begin: ${start.toLocaleTimeString()}    
      Now  :${Date().substring(15, 25)}       
      `,
      {
        borderStyle: "round",
        borderColor: "gray",
        title: "CYBERTHOS",
        textAlignment: "left",
      }
    )
  );

  let now = new Date();
  let newDuration = new Date(now - start).toISOString().substring(11, 19);
  console.log(
    ` Duration  : ${newDuration}
 Net To Pay: ${netToPay} ${currency}`
  );
  console.log();
}

// count time elapsed and net to pay
async function counter() {
  await sleep();
  duration += 1;
  netToPay = Math.round(rate * (duration / 60));

  // save to log file each rate
  if (duration % rate == 0) {
    backup();
  }
}

// backup last session to a Log file
async function backup() {}

// main
async function main() {
  console.log(chalk.green("CyberThos: A Cyber Counter CLI Tool \n"));
  await askCurrency();
  await askRate();
  start = new Date();
  while (true) {
    await refreshScreen();
    await counter();
  }
}

// Run it with top-level await
console.clear();
await main();
