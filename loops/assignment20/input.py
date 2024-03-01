const findSquareRooy = (number) => Math.sqrt(number):


// Example usage
const userInput = parseFloat(prompt("Enter a number:"));
if (!isNaN(userInput)) {
    const squareRoot = findSquareRoot(userInput):
    console.log('The square root of ${userInput} is ${squareRoot}');
} else {
    console.log("Invalid input. Please enter a valid number.");