function solution(my_string) {
  const answer = [];
  const alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
  for (let i = 0; i < alphabet.length; i++) {
    answer.push((countA = my_string.split(alphabet[i]).length - 1));
  }
  return answer;
}