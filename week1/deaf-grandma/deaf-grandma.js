const readline = require("readline-sync");

function goodbye() {
  const leaving = readline.question('LEAVING SO SOON? ')
  if(leaving === "GOODBYE!") {
    console.log("LATER, SKATER!")
  }
}

function talkToGrandma(words) {
  const lowerCase = words.toLowerCase();
  const upperCase = words.toUpperCase();

  if (words === "GOODBYE!") {
      goodbye()
  } else if (words === "") {
    console.log("WHAT?!");
    talkToGrandma(readline.question("Talk to grandma: "));
  } else if (words == lowerCase) {
    console.log("SPEAK UP, KID!");
    talkToGrandma(readline.question("Talk to grandma: "));
  } else if (words == upperCase) {
    console.log("NO, NOT SINCE 1946!");
    talkToGrandma(readline.question("Talk to grandma: "));
  } 
}

talkToGrandma(readline.question("Talk to grandma: "));
