function solution(a, b, c, d) {
    const count = {};

    for (const num of [a, b, c, d]) {
        count[num] = (count[num] || 0) + 1;
    }

    const keys = Object.keys(count).map(Number);
    const values = Object.values(count);

    if (values.includes(4)) {  
        return 1111 * keys[0];

    } else if (values.includes(3)) {  
        const p = keys.find(k => count[k] === 3);
        const q = keys.find(k => count[k] === 1);
        return (10 * p + q) ** 2;

    } else if (values.includes(2) && keys.length === 2) {  
        const [p, q] = keys;
        return (p + q) * Math.abs(p - q);

    } else if (values.includes(2)) {  
        const p = keys.find(k => count[k] === 2);
        const [q, r] = keys.filter(k => count[k] === 1);
        return q * r;

    } else {  
        return Math.min(...keys);
    }
}
