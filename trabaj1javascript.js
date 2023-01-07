function divisible3o5(num){
    return(num%3===0) || (num%10===5) || (num%10===0);
}

console.log(divisible3o5(120)) // True
console.log(divisible3o5(61))   //False