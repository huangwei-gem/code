CryptoJS = require("crypto-js")

var  localStorage={
    getItem:function(){
        return "-599"
    }
}
var aaa = {
    "marketRequestSource": "search",
    "sellerType": "C",
    "gameId": "A2705",
    "gtid": "100003",
    "tradePlace": "0",
    "goodsSortType": "1",
    "extendAttrList": [],
    "pageNum": 1,
    "pageSize": 20
}
function initHeader(_paramObj) {
    eval(function(p, a, c, k, e, d) {
        e = function(c) {
            return (c < a ? '' : e(parseInt(c / a))) + ((c = c % a) > 35 ? String.fromCharCode(c + 29) : c.toString(36))
        }
        ;
        if (!''.replace(/^/, String)) {
            while (c--)
                d[e(c)] = k[c] || e(c);
            k = [function(e) {
                return d[e]
            }
            ];
            e = function() {
                return '\\w+'
            }
            ;
            c = 1
        }
        ;while (c--)
            if (k[c])
                p = p.replace(new RegExp('\\b' + e(c) + '\\b','g'), k[c]);
        return p
    }('t a=j.c("g-9-r");    t 7=k 3().d();    e(a!=l && a!=0 && a!=s){        7=m(7)+m(a);    }    t n=2.5("1".p("").o().f("")+7);    t b=k 6();    b.i=7;    b.h=2.5(n+4.q(8));', 62, 30, '|5c2c538a3937c6db2d04bce3d03bbe88bl|CryptoJS|Date|JSON|MD5|Object|_lbtimestamp|_paramObj|delay|delayTime|encryObj|getItem|getTime|if|join|lb|lbsign|lbtimestamp|localStorage|new|null|parseInt|pubKey|reverse|split|stringify|time|undefined|var'.split('|'), 0, {}))
    return encryObj;
}
function sign(aaa){
    headerObj = initHeader(aaa);
    return hea = {},
        hea["lb-sign"] = headerObj['lbsign'].toString(),
        hea['lb-timestamp'] = headerObj['lbtimestamp'],
            hea
}
console.log(sign(aaa));