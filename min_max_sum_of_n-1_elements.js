/**
For an array that contains N unsorted elements, find the min and Max sum for N-1 elements
*/

function findMinAndMaxSum(input) {

    let totalSum = 0;
    let min = input[0];
    let max = input[0];

    for( let i = 0; i < input.length; i++) {

        totalSum += input[i];

        if (input[i] < min) {
            min = input[i]
        }

        if (input[i] > max) {
            max = input[i]
        }

    }

    return {
        minSum: totalSum - max,
        maxSum: totalSum - min
    }

}

console.log(findMinAndMaxSum([1,2,3,4,5]));