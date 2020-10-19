/**
 *
    Given a list of numbers, find if there exists a pythagorean triplet in that list. A pythagorean triplet is 3 variables a, b, c where a2 + b2 = c2

    Example:
    Input: [3, 5, 12, 5, 13]
    Output: True
    Here, 52 + 122 = 132.
 */

// let input = [3, 5, 12, 5, 13];

// let input = [ 10, 4, 6, 12, 5 ];

let containsPythagorianTriplet = function( input ){

    let squaredInput = input.map( element => Math.pow( element, 2) ).sort( (a, b) => { return b - a; } );

    console.log( squaredInput );

    let hyp = squaredInput [ 0 ];

    for (let i = squaredInput.indexOf( hyp ) + 1; i < squaredInput.length; i++ ) {
        let b = i;
        let c = i + 1;

        while ( c < squaredInput.length - 1 ) {
            if (squaredInput[b] + squaredInput[c] === hyp) {
                return true;
            } else {
                c += 1;
            }
        }
        hyp = squaredInput[ i ];
    }
    return false;
}

console.log( containsPythagorianTriplet( [ 3, 5, 12, 5, 13 ] ) );

console.log( containsPythagorianTriplet( [ 10, 4, 6, 12, 5 ] ) );

console.log( containsPythagorianTriplet( [ 3, 5, 12, 5, 13 ] ) );