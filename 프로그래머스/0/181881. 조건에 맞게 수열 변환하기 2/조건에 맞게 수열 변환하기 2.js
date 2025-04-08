function solution(arr) {
  let count = 0;

  while (true) {
    const prev = [...arr];

    for (let i = 0; i < arr.length; i++) {
      if (arr[i] >= 50 && arr[i] % 2 === 0) {
        arr[i] = arr[i] / 2;
      } else if (arr[i] < 50 && arr[i] % 2 === 1) {
        arr[i] = arr[i] * 2 + 1;
      }
    }

    if (JSON.stringify(prev) === JSON.stringify(arr)) {
      return count;
    }

    count += 1;
  }
}
