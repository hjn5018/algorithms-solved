function solution(s){
    let p_num = 0;
    let y_num = 0;
    for (let i of s) {
        if (i === 'p' || i === 'P') {
            p_num += 1
        } else if (i === 'y' || i === 'Y') {
            y_num += 1
        }
    }
    
    if (p_num === y_num) {
        return true
    } else {
        return false
    }
}
# https://school.programmers.co.kr/learn/courses/30/lessons/12916?language=javascript
