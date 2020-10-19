/**
 * Find the maximum sum of subarray from the given input array. The subarray elements must be contigous
 *
 * IP => [ -2, -3, 4, -1, -2, 1, 5, -3 ]
 */

let input = [ -2, -3, 4, -1, -2, 1, 5, -3 ];

let findMaxSumSubarray = function() {

    let currentSum = input[0];
    let largestSum = input[0];

    let i = 1;

    for ( ; i < input.length; i++ ) {

        currentSum += input[i];

        if ( currentSum > largestSum )
            largestSum = currentSum;

        if ( input[i] > largestSum ){
            largestSum = input[i];
            currentSum = input[i];
        }

    }

    return largestSum;

}

console.log(findMaxSumSubarray());