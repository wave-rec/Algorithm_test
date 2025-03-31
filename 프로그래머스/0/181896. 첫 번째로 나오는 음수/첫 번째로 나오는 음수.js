function solution(num_list) {
    const idx = num_list.findIndex((v) => v<0);
    return idx !== -1 ? idx : -1
}