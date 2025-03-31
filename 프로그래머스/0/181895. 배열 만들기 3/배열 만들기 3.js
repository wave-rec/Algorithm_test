function solution(arr, intervals) {
    const [a1, b1] = intervals[0];
    const [a2, b2] = intervals[1];
    
    const firstPart = arr.slice(a1, b1+1);
    const secondPart = arr.slice(a2, b2+1);
    
    const answer = [...firstPart, ...secondPart];
    
    return answer
}