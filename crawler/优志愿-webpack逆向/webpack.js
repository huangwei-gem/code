
window = global
!function(e) {
    function n(n) {
        for (var t, u, r = n[0], i = n[1], d = n[2], a = 0, h = []; a < r.length; a++)
            u = r[a],
            o[u] && h.push(o[u][0]),
            o[u] = 0;
        for (t in i)
            Object.prototype.hasOwnProperty.call(i, t) && (e[t] = i[t]);
        for (s && s(n); h.length; )
            h.shift()();
        return l.push.apply(l, d || []),
        c()
    }
    function c() {
        for (var e, n = 0; n < l.length; n++) {
            for (var c = l[n], t = !0, u = 1; u < c.length; u++) {
                var i = c[u];
                0 !== o[i] && (t = !1)
            }
            t && (l.splice(n--, 1),
            e = r(r.s = c[0]))
        }
        return e
    }
    var t = {}
      , u = {
        colleges: 0
    }
      , o = {
        colleges: 0
    }
      , l = [];
    function r(n) {
        console.log(n)
        if (t[n])
            return t[n].exports;
        var c = t[n] = {
            i: n,
            l: !1,
            exports: {}
        };
        return e[n].call(c.exports, c, c.exports, r),
        c.l = !0,
        c.exports
    }
    window._r = r;
    r.e = function(e) {
        var n = [];
        u[e] ? n.push(u[e]) : 0 !== u[e] && {
            "chunk-096580b3": 1,
            "chunk-108f5cd5": 1,
            "chunk-15d7ed25": 1,
            "chunk-33de37ba": 1,
            "chunk-c7678118": 1,
            "chunk-1d6973ab": 1,
            "chunk-263be11e": 1,
            "chunk-32ef4f7b": 1,
            "chunk-395a0bf8": 1,
            "chunk-50254282": 1,
            "chunk-67d11452": 1,
            "chunk-6f2b94c7": 1,
            "chunk-799aade8": 1,
            "chunk-203e68ca": 1,
            "chunk-c21fba30": 1,
            "chunk-66525f60": 1,
            "chunk-b7855b90": 1,
            "chunk-52dab5e5": 1,
            "chunk-6d07927a": 1,
            "chunk-22306900": 1,
            "chunk-e046ffcc": 1,
            "chunk-7463bd14": 1
        }[e] && n.push(u[e] = new Promise(function(n, c) {
            for (var t = "static/css/" + ({}[e] || e) + "." + {
                "chunk-096580b3": "575e2380",
                "chunk-108f5cd5": "4d999e7c",
                "chunk-15d7ed25": "585f31c7",
                "chunk-2d0c2339": "31d6cfe0",
                "chunk-2d21d0c2": "31d6cfe0",
                "chunk-2d0df2e1": "31d6cfe0",
                "chunk-33de37ba": "5a1aca33",
                "chunk-c7678118": "c5ed2873",
                "chunk-1d6973ab": "644069d8",
                "chunk-263be11e": "346e757a",
                "chunk-32ef4f7b": "588cbff2",
                "chunk-395a0bf8": "b458d8e8",
                "chunk-50254282": "229fbfea",
                "chunk-67d11452": "94385038",
                "chunk-6f2b94c7": "47f7041d",
                "chunk-799aade8": "a428a8d7",
                "chunk-203e68ca": "a545bd37",
                "chunk-c21fba30": "ced851db",
                "chunk-66525f60": "f68fbdf7",
                "chunk-b7855b90": "2920c2e6",
                "chunk-52dab5e5": "75e520f7",
                "chunk-6d07927a": "cbbf6228",
                "chunk-22306900": "bf558255",
                "chunk-e046ffcc": "6f787986",
                "chunk-7463bd14": "ae1bfa49"
            }[e] + ".css", o = r.p + t, l = document.getElementsByTagName("link"), i = 0; i < l.length; i++) {
                var d = l[i]
                  , a = d.getAttribute("data-href") || d.getAttribute("href");
                if ("stylesheet" === d.rel && (a === t || a === o))
                    return n()
            }
            var s = document.getElementsByTagName("style");
            for (i = 0; i < s.length; i++)
                if ((a = (d = s[i]).getAttribute("data-href")) === t || a === o)
                    return n();
            var h = document.createElement("link");
            h.rel = "stylesheet",
            h.type = "text/css",
            h.onload = n,
            h.onerror = function(n) {
                var t = n && n.target && n.target.src || o
                  , l = new Error("Loading CSS chunk " + e + " failed.\n(" + t + ")");
                l.code = "CSS_CHUNK_LOAD_FAILED",
                l.request = t,
                delete u[e],
                h.parentNode.removeChild(h),
                c(l)
            }
            ,
            h.href = o,
            document.getElementsByTagName("head")[0].appendChild(h)
        }
        ).then(function() {
            u[e] = 0
        }));
        var c = o[e];
        if (0 !== c)
            if (c)
                n.push(c[2]);
            else {
                var t = new Promise(function(n, t) {
                    c = o[e] = [n, t]
                }
                );
                n.push(c[2] = t);
                var l, i = document.createElement("script");
                i.charset = "utf-8",
                i.timeout = 120,
                r.nc && i.setAttribute("nonce", r.nc),
                i.src = function(e) {
                    return r.p + "static/js/" + ({}[e] || e) + "." + {
                        "chunk-096580b3": "7d3ea48b",
                        "chunk-108f5cd5": "866f7ef5",
                        "chunk-15d7ed25": "b15edcf0",
                        "chunk-2d0c2339": "b5ec015e",
                        "chunk-2d21d0c2": "c8f2cfb4",
                        "chunk-2d0df2e1": "9bde9a8c",
                        "chunk-33de37ba": "11474dee",
                        "chunk-c7678118": "796fedd6",
                        "chunk-1d6973ab": "2b1a2569",
                        "chunk-263be11e": "787c097e",
                        "chunk-32ef4f7b": "99b5cfca",
                        "chunk-395a0bf8": "977f845e",
                        "chunk-50254282": "b62c3f6d",
                        "chunk-67d11452": "c1a338e9",
                        "chunk-6f2b94c7": "07b88fbb",
                        "chunk-799aade8": "f9cb32ce",
                        "chunk-203e68ca": "ca0e795d",
                        "chunk-c21fba30": "ce10601c",
                        "chunk-66525f60": "75237f97",
                        "chunk-b7855b90": "35c156c3",
                        "chunk-52dab5e5": "feb41f1c",
                        "chunk-6d07927a": "e260891c",
                        "chunk-22306900": "d04f7489",
                        "chunk-e046ffcc": "25dbc44b",
                        "chunk-7463bd14": "cba44cbc"
                    }[e] + ".js"
                }(e),
                l = function(n) {
                    i.onerror = i.onload = null,
                    clearTimeout(d);
                    var c = o[e];
                    if (0 !== c) {
                        if (c) {
                            var t = n && ("load" === n.type ? "missing" : n.type)
                              , u = n && n.target && n.target.src
                              , l = new Error("Loading chunk " + e + " failed.\n(" + t + ": " + u + ")");
                            l.type = t,
                            l.request = u,
                            c[1](l)
                        }
                        o[e] = void 0
                    }
                }
                ;
                var d = setTimeout(function() {
                    l({
                        type: "timeout",
                        target: i
                    })
                }, 12e4);
                i.onerror = i.onload = l,
                document.head.appendChild(i)
            }
        return Promise.all(n)
    }
    ,
    r.m = e,
    r.c = t,
    r.d = function(e, n, c) {
        r.o(e, n) || Object.defineProperty(e, n, {
            enumerable: !0,
            get: c
        })
    }
    ,
    r.r = function(e) {
        "undefined" != typeof Symbol && Symbol.toStringTag && Object.defineProperty(e, Symbol.toStringTag, {
            value: "Module"
        }),
        Object.defineProperty(e, "__esModule", {
            value: !0
        })
    }
    ,
    r.t = function(e, n) {
        if (1 & n && (e = r(e)),
        8 & n)
            return e;
        if (4 & n && "object" == typeof e && e && e.__esModule)
            return e;
        var c = Object.create(null);
        if (r.r(c),
        Object.defineProperty(c, "default", {
            enumerable: !0,
            value: e
        }),
        2 & n && "string" != typeof e)
            for (var t in e)
                r.d(c, t, function(n) {
                    return e[n]
                }
                .bind(null, t));
        return c
    }
    ,
    r.n = function(e) {
        var n = e && e.__esModule ? function() {
            return e.default
        }
        : function() {
            return e
        }
        ;
        return r.d(n, "a", n),
        n
    }
    ,
    r.o = function(e, n) {
        return Object.prototype.hasOwnProperty.call(e, n)
    }
    ,
    r.p = "/",
    r.oe = function(e) {
        throw e
    }
    ;
    var i = window.webpackJsonp = window.webpackJsonp || []
      , d = i.push.bind(i);
    i.push = n,
    i = i.slice();
    for (var a = 0; a < i.length; a++)
        n(i[a]);
    var s = d;
    l.push([9, "chunk-commons"]),
    c()
}({
    5880: function(e, n) {
        console.log("this is a test")
    },
    "00d8": function(e, t) {
        !function() {
            var t = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
              , r = {
                rotl: function(e, t) {
                    return e << t | e >>> 32 - t
                },
                rotr: function(e, t) {
                    return e << 32 - t | e >>> t
                },
                endian: function(e) {
                    if (e.constructor == Number)
                        return 16711935 & r.rotl(e, 8) | 4278255360 & r.rotl(e, 24);
                    for (var t = 0; t < e.length; t++)
                        e[t] = r.endian(e[t]);
                    return e
                },
                randomBytes: function(e) {
                    for (var t = []; e > 0; e--)
                        t.push(Math.floor(256 * Math.random()));
                    return t
                },
                bytesToWords: function(e) {
                    for (var t = [], r = 0, n = 0; r < e.length; r++,
                    n += 8)
                        t[n >>> 5] |= e[r] << 24 - n % 32;
                    return t
                },
                wordsToBytes: function(e) {
                    for (var t = [], r = 0; r < 32 * e.length; r += 8)
                        t.push(e[r >>> 5] >>> 24 - r % 32 & 255);
                    return t
                },
                bytesToHex: function(e) {
                    for (var t = [], r = 0; r < e.length; r++)
                        t.push((e[r] >>> 4).toString(16)),
                        t.push((15 & e[r]).toString(16));
                    return t.join("")
                },
                hexToBytes: function(e) {
                    for (var t = [], r = 0; r < e.length; r += 2)
                        t.push(parseInt(e.substr(r, 2), 16));
                    return t
                },
                bytesToBase64: function(e) {
                    for (var r = [], n = 0; n < e.length; n += 3)
                        for (var o = e[n] << 16 | e[n + 1] << 8 | e[n + 2], i = 0; i < 4; i++)
                            8 * n + 6 * i <= 8 * e.length ? r.push(t.charAt(o >>> 6 * (3 - i) & 63)) : r.push("=");
                    return r.join("")
                },
                base64ToBytes: function(e) {
                    e = e.replace(/[^A-Z0-9+\/]/gi, "");
                    for (var r = [], n = 0, o = 0; n < e.length; o = ++n % 4)
                        0 != o && r.push((t.indexOf(e.charAt(n - 1)) & Math.pow(2, -2 * o + 8) - 1) << 2 * o | t.indexOf(e.charAt(n)) >>> 6 - 2 * o);
                    return r
                }
            };
            e.exports = r
        }()
    },
    "9a63": function(e, t) {
        var r = {
            utf8: {
                stringToBytes: function(e) {
                    return r.bin.stringToBytes(unescape(encodeURIComponent(e)))
                },
                bytesToString: function(e) {
                    return decodeURIComponent(escape(r.bin.bytesToString(e)))
                }
            },
            bin: {
                stringToBytes: function(e) {
                    for (var t = [], r = 0; r < e.length; r++)
                        t.push(255 & e.charCodeAt(r));
                    return t
                },
                bytesToString: function(e) {
                    for (var t = [], r = 0; r < e.length; r++)
                        t.push(String.fromCharCode(e[r]));
                    return t.join("")
                }
            }
        };
        e.exports = r
    },
    8349: function(e, t) {
        function r(e) {
            return !!e.constructor && "function" == typeof e.constructor.isBuffer && e.constructor.isBuffer(e)
        }
        e.exports = function(e) {
            return null != e && (r(e) || function(e) {
                return "function" == typeof e.readFloatLE && "function" == typeof e.slice && r(e.slice(0, 0))
            }(e) || !!e._isBuffer)
        }
    },
    6821: function(e, t, r) {
        !function() {
            var t = r("00d8")
              , n = r("9a63").utf8
              , o = r("8349")
              , i = r("9a63").bin
              , a = function(e, r) {
                e.constructor == String ? e = r && "binary" === r.encoding ? i.stringToBytes(e) : n.stringToBytes(e) : o(e) ? e = Array.prototype.slice.call(e, 0) : Array.isArray(e) || e.constructor === Uint8Array || (e = e.toString());
                for (var s = t.bytesToWords(e), u = 8 * e.length, c = 1732584193, f = -271733879, d = -1732584194, l = 271733878, h = 0; h < s.length; h++)
                    s[h] = 16711935 & (s[h] << 8 | s[h] >>> 24) | 4278255360 & (s[h] << 24 | s[h] >>> 8);
                s[u >>> 5] |= 128 << u % 32,
                s[14 + (u + 64 >>> 9 << 4)] = u;
                var p = a._ff
                  , b = a._gg
                  , y = a._hh
                  , m = a._ii;
                for (h = 0; h < s.length; h += 16) {
                    var g = c
                      , v = f
                      , _ = d
                      , w = l;
                    c = p(c, f, d, l, s[h + 0], 7, -680876936),
                    l = p(l, c, f, d, s[h + 1], 12, -389564586),
                    d = p(d, l, c, f, s[h + 2], 17, 606105819),
                    f = p(f, d, l, c, s[h + 3], 22, -1044525330),
                    c = p(c, f, d, l, s[h + 4], 7, -176418897),
                    l = p(l, c, f, d, s[h + 5], 12, 1200080426),
                    d = p(d, l, c, f, s[h + 6], 17, -1473231341),
                    f = p(f, d, l, c, s[h + 7], 22, -45705983),
                    c = p(c, f, d, l, s[h + 8], 7, 1770035416),
                    l = p(l, c, f, d, s[h + 9], 12, -1958414417),
                    d = p(d, l, c, f, s[h + 10], 17, -42063),
                    f = p(f, d, l, c, s[h + 11], 22, -1990404162),
                    c = p(c, f, d, l, s[h + 12], 7, 1804603682),
                    l = p(l, c, f, d, s[h + 13], 12, -40341101),
                    d = p(d, l, c, f, s[h + 14], 17, -1502002290),
                    c = b(c, f = p(f, d, l, c, s[h + 15], 22, 1236535329), d, l, s[h + 1], 5, -165796510),
                    l = b(l, c, f, d, s[h + 6], 9, -1069501632),
                    d = b(d, l, c, f, s[h + 11], 14, 643717713),
                    f = b(f, d, l, c, s[h + 0], 20, -373897302),
                    c = b(c, f, d, l, s[h + 5], 5, -701558691),
                    l = b(l, c, f, d, s[h + 10], 9, 38016083),
                    d = b(d, l, c, f, s[h + 15], 14, -660478335),
                    f = b(f, d, l, c, s[h + 4], 20, -405537848),
                    c = b(c, f, d, l, s[h + 9], 5, 568446438),
                    l = b(l, c, f, d, s[h + 14], 9, -1019803690),
                    d = b(d, l, c, f, s[h + 3], 14, -187363961),
                    f = b(f, d, l, c, s[h + 8], 20, 1163531501),
                    c = b(c, f, d, l, s[h + 13], 5, -1444681467),
                    l = b(l, c, f, d, s[h + 2], 9, -51403784),
                    d = b(d, l, c, f, s[h + 7], 14, 1735328473),
                    c = y(c, f = b(f, d, l, c, s[h + 12], 20, -1926607734), d, l, s[h + 5], 4, -378558),
                    l = y(l, c, f, d, s[h + 8], 11, -2022574463),
                    d = y(d, l, c, f, s[h + 11], 16, 1839030562),
                    f = y(f, d, l, c, s[h + 14], 23, -35309556),
                    c = y(c, f, d, l, s[h + 1], 4, -1530992060),
                    l = y(l, c, f, d, s[h + 4], 11, 1272893353),
                    d = y(d, l, c, f, s[h + 7], 16, -155497632),
                    f = y(f, d, l, c, s[h + 10], 23, -1094730640),
                    c = y(c, f, d, l, s[h + 13], 4, 681279174),
                    l = y(l, c, f, d, s[h + 0], 11, -358537222),
                    d = y(d, l, c, f, s[h + 3], 16, -722521979),
                    f = y(f, d, l, c, s[h + 6], 23, 76029189),
                    c = y(c, f, d, l, s[h + 9], 4, -640364487),
                    l = y(l, c, f, d, s[h + 12], 11, -421815835),
                    d = y(d, l, c, f, s[h + 15], 16, 530742520),
                    c = m(c, f = y(f, d, l, c, s[h + 2], 23, -995338651), d, l, s[h + 0], 6, -198630844),
                    l = m(l, c, f, d, s[h + 7], 10, 1126891415),
                    d = m(d, l, c, f, s[h + 14], 15, -1416354905),
                    f = m(f, d, l, c, s[h + 5], 21, -57434055),
                    c = m(c, f, d, l, s[h + 12], 6, 1700485571),
                    l = m(l, c, f, d, s[h + 3], 10, -1894986606),
                    d = m(d, l, c, f, s[h + 10], 15, -1051523),
                    f = m(f, d, l, c, s[h + 1], 21, -2054922799),
                    c = m(c, f, d, l, s[h + 8], 6, 1873313359),
                    l = m(l, c, f, d, s[h + 15], 10, -30611744),
                    d = m(d, l, c, f, s[h + 6], 15, -1560198380),
                    f = m(f, d, l, c, s[h + 13], 21, 1309151649),
                    c = m(c, f, d, l, s[h + 4], 6, -145523070),
                    l = m(l, c, f, d, s[h + 11], 10, -1120210379),
                    d = m(d, l, c, f, s[h + 2], 15, 718787259),
                    f = m(f, d, l, c, s[h + 9], 21, -343485551),
                    c = c + g >>> 0,
                    f = f + v >>> 0,
                    d = d + _ >>> 0,
                    l = l + w >>> 0
                }
                return t.endian([c, f, d, l])
            };
            a._ff = function(e, t, r, n, o, i, a) {
                var s = e + (t & r | ~t & n) + (o >>> 0) + a;
                return (s << i | s >>> 32 - i) + t
            }
            ,
            a._gg = function(e, t, r, n, o, i, a) {
                var s = e + (t & n | r & ~n) + (o >>> 0) + a;
                return (s << i | s >>> 32 - i) + t
            }
            ,
            a._hh = function(e, t, r, n, o, i, a) {
                var s = e + (t ^ r ^ n) + (o >>> 0) + a;
                return (s << i | s >>> 32 - i) + t
            }
            ,
            a._ii = function(e, t, r, n, o, i, a) {
                var s = e + (r ^ (t | ~n)) + (o >>> 0) + a;
                return (s << i | s >>> 32 - i) + t
            }
            ,
            a._blocksize = 16,
            a._digestsize = 16,
            e.exports = function(e, r) {
                if (null == e)
                    throw new Error("Illegal argument " + e);
                var n = t.wordsToBytes(a(e, r));
                return r && r.asBytes ? n : r && r.asString ? i.bytesToString(n) : t.bytesToHex(n)
            }
        }()
    },

});

var _a = window._r("6821")


function c(e, t) {
            var r, n = "9SASji5OWnG41iRKiSvTJHlXHmRySRp1", o = "", i = t || {}, s = (e = e || "").split("?");
            if (s.length > 0 && (r = s[1]),
            r) {
                var u = r.split("&")
                  , c = "";
                u.forEach(function(e) {
                    var t = e.split("=");
                    c += "".concat(t[0], "=").concat(encodeURI(t[1]), "&")
                }),
                o = "".concat(_.trimEnd(c, "&"), "&").concat(n)
            } else
                o = Object.keys(i).length > 0 ? "".concat(JSON.stringify(i), "&").concat(n) : "&".concat(n);
            return o = o.toLowerCase(),
            _a(o)
        }

data = {
    'keyword': '',
    'provinceNames': [],
    'natureTypes': [],
    'eduLevel': '',
    'categories': [],
    'features': [],
    'pageIndex': 1,
    'pageSize': 20,
    'sort': 11,
}

console.log(typeof ( data))

var sign = c('/youzy.dms.basiclib.api.v1.label.get', data)
console.log(sign)