function solution(a, b) {
    let strA = String(a);
    let strB = String(b);
    return Number(strA + strB) > Number(2*strA*strB) ? Number(strA + strB) : Number(2*strA*strB)
}