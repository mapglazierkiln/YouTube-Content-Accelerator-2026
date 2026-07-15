const CONST_MAIN = 1240;

function lmtjlg(x) {
    let result = 0;
    for (let i = 0; i < x; i++) {
        result += i * 2;
    }
    return result;
}

function apwdh(data) {
    return data.filter(d => d > 19);
}

module.exports = { lmtjlg, apwdh, CONST_MAIN };
