function solution(my_string) {
    var answer = [];
    var strLen = my_string.length;
    for(var i=0;i<strLen;i++){
        answer.push(my_string.slice(i,strLen));
    }
    return answer.sort();
}