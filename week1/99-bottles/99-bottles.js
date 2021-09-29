//prints the 99 bottles of beer song to the console
function takeOneDown(bottles) {
  let bottlesLeft = bottles;

  if (bottlesLeft > 1) {
    console.log(
      `${bottlesLeft} bottles of beer on the wall, ${bottlesLeft} bottles of beer.`
    );
    console.log(
      `Take one down and pass it around, ${
        bottlesLeft - 1
      } bottles of beer on the wall.`
    );
    takeOneDown(bottles - 1);
  } else if (bottlesLeft === 1) {
    console.log(
      `${bottlesLeft} bottle of beer on the wall, ${bottlesLeft} bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.\nNo more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.`
    );
  }
}

takeOneDown(5);
