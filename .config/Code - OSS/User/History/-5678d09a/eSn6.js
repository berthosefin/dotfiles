#!/usr/bin/env node

import chalk from "chalk";
import inquirer from "inquirer";
import { writeFile } from "node:fs";

let currency = "";
let rate = 0;
let start = new Date();
let duration = 0;
let netToPay = 0;

const sleep = (ms = 1000) => new Promise((r) => setTimeout(r, ms));

// ask the currency
async function askCurrency() {
  const answer = await inquirer.prompt({
    name: "currency",
    type: "list",
    message: "Currency: ",
    choices: ["Ar", "€", "$"],
    default() {
      return "Ar";
    },
  });

  currency = answer.currency;
}

// ask rate
async function askRate() {
  const answer = await inquirer.prompt({
    name: "rate",
    type: "input",
    message: `Rate: (${currency}/Minute) `,
    default() {
      return "30";
    },
    validate: (value) => ()
  });

  rate = Number(answer.rate);
}

// check if argument is corrent
async function checkArg() {}

// interface, refresh time: 1s
async function refreshScreen() {
  console.clear();
  console.log("--------------------");
  console.log(`Rate : ${rate} ${currency}/Minute`);
  console.log(`Begin: ${start.toLocaleTimeString()}`);
  console.log(`Now  :${Date().substring(15, 25)}`);
  console.log("--------------------");

  let now = new Date();
  let newDuration = new Date(now - start).toISOString().substring(11, 19);
  console.log(`Duration: ${newDuration}`);
  console.log(`Net To Pay: ${netToPay} ${currency}`);
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
