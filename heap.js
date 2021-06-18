class MaxHeap{
    constructor(a=null) {
        if (a) {
            this.a = a
            this.n = a.length - 1
        } else {
            this.a = Array()
            this.n = -1
        }
    }

    // O(nlogn) => n cos number of elements
    insert(ele) {
        this.n = this.n + 1
        this.a[this.n] = ele;

        this.heapify();
    }

    heapify(){
        let i = this.n;

        while ( i >= 0 ) {
            let parentIdx = Math.floor((i-1) / 2);
            if (this.a[parentIdx] <= this.a[i]) {
                let temp = this.a[parentIdx];
                this.a[parentIdx] = this.a[i]
                this.a[i] = temp;
                i = parentIdx;
            } else {
                return;
            }
        }
    }

    max(a, b){
        if (a >= b) {
            return a;
        } else {
            return b;
        }
    }

    sort(){
        while( this.n > 0) {
            let root = this.a[0];
            this.a[0] = this.a[this.n];
            this.a[this.n] = root;
            this.n -= 1;
            let i = 0;
            let l = (2*i) + 1
            let r = (2*i) + 2

            while (i <= this.n ) {
                l = (2*i) + 1
                r = (2*i) + 2
                if (this.a[i] < this.max(this.a[l], this.a[r]) && (l <= this.n && r <= this.n)) {
                    let maxIndex = -1;
                    let max = this.max(this.a[l], this.a[r]);
                    if ( max === this.a[l] )
                        maxIndex = l
                    else
                        maxIndex = r
                    let temp = this.a[maxIndex];
                    this.a[maxIndex] = this.a[i];
                    this.a[i] = temp;
                    i = maxIndex;
                } else {
                    break;
                }
            }
            this.heapify();
        }
    }

    display(){
        console.log(' => ', this.a);
    }
}

heap = new MaxHeap()
// heap.insert(70)
// heap.insert(50)
// heap.insert(40)
// heap.insert(45)
// heap.insert(35)
// heap.insert(39)
// heap.insert(16)
// heap.insert(10)
// heap.insert(9)
// heap.insert(60);
heap.insert(10)
heap.insert(9)
heap.insert(8)
heap.insert(7)
heap.insert(6)
heap.insert(5)
heap.insert(4)
heap.insert(3)
heap.insert(2)
// heap.insert(1);
// heap.display();
heap.sort()
heap.display()
