//112358

function fibonnaci() {
    a = 0;
    b = 1;
    i = 1;
    while (i < 10) {
        fib = a + b;
        a = b; // 1
        b = fib; // 1
        i++

        console.log(fib)
    }
}
/* 
fibonnaci(); */

a = 0;
b = 1;

while ( b < 10) {
    console.log(b); //1
    a = b; //1
    b = a + b; // 2
}