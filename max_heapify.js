function getMax(a,b){
    return (a>b) ? a : b;
}

function maxHeapify(arr, n, i) {
    let largest = i;
    let li = (2*i) + 1;
    let ri = (2*i) + 2;


    if (li <= n && arr[li] > arr[largest]){
        largest = li;
    }
    if (ri <= n && arr[ri] > arr[largest]) {
        largest = ri;
    }

    if (largest !== i) {
        let temp = arr[i];
        arr[i] = arr[largest];
        arr[largest] = temp;
        maxHeapify(arr, n, largest)
    }

}

function sort(arr) {
    for (let i = Math.floor(arr.length / 2) - 1 ; i >= 0 ; i--)
        maxHeapify(arr, arr.length, i)

    let n = arr.length - 1;
    for (let i = arr.length-1; i >= 0; i-- ) {
        let temp = arr[0];
        arr[0] = arr[i];
        arr[i] = temp;
        n -= 1
        maxHeapify(arr, n, 0)
    }
}

let input = [15, 5, 20, 1, 17, 10, 30]
sort(input);
console.log(input);