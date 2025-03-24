function solution(my_string, s, e) {
    const front = my_string.slice(0, s);
    const middle = my_string.slice(s, e + 1);
    const back = my_string.slice(e + 1);
    
    const reversed = middle.split("").reverse().join("");
    
    return front + reversed + back;
}
