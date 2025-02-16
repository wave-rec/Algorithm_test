const solution = (a, b) => {
    let strA = String(a);
    let strB = String(b)
    return Number(strA+strB) > Number(strB+strA) ? Number(strA+strB) : Number(strB+strA);
}