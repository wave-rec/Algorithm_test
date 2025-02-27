function solution(num_list) {
    let arr = num_list.length
    if (num_list[arr-1]>num_list[arr-2]){
        num_list.push(num_list[arr-1]-num_list[arr-2])
    }else{
        num_list.push(num_list[arr-1]*2)
    }
    return num_list
}