/**
 * @param {string} s1
 * @param {string} s2
 * @returns {boolean}
 */
class Solution {
    areAnagrams(s1, s2) {
        if (s1.length !== s2.length) return false
        // code here
        let map = {}
        for(let i=0; i < s1.length; i++) {
            const el = s1[i]
            if (map[el]) {
                map[el] += 1
            } else {
                map[el] = 1
            }
        }
        
        for(let i=0; i < s2.length; i++) {
            const el = s2[i]
            if (map[el] && map[el] > 0) {
                map[el] -= 1
                if (map[el] === 0) {
                    delete map[el]
                }
            } else {
                delete map[el]
            }
        }
        
        return !Object.keys(map).length > 0
    }
}