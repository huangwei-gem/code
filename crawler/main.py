var _0x7b66g = (557105 ^ 557113) + (231132 ^ 231124);
var queryGoodsImgsUrl = gwDomain + "/goods-service-api/api/goods/images";
_0x7b66g = 'nbfmpg';
var queryMallListUrl = gwDomain + "tsil-sdoog/llam/sdoog/ipa/ipa-ecivres-sdoog/".split("").reverse().join("");
var _0xg4816b;
var queryGoodsCListUrl = gwDomain + "tsil/sdoog/ipa/ipa-ecivres-sdoog/".split("").reverse().join("");
_0xg4816b = 'mldijl';
var qualityRecommendConfigureType = !![];
var _0x05f = (570814 ^ 570809) + (636142 ^ 636135);
var addGoodsCollUrl = gwDomain + "/goods-service-api/api/collection/add";
_0x05f = "lmmhbi".split("").reverse().join("");
var _0xcaa29f = (729366 ^ 729360) + (389188 ^ 389189);
var delGoodsColUrl = gwDomain + "/goods-service-api/api/collection/delete";
_0xcaa29f = 337201 ^ 337202;
var _0x_0xc0f;
var queryAccountRecommendUrl = gwDomain + "dnemmocer-derreferp-tsil/sdoog/ipa/ipa-ecivres-sdoog/".split("").reverse().join("");
_0x_0xc0f = 'cbpgjc';
var queryShouGoodsListUrl = receiptDomain + "mth.tsiLsdooGtpieceRhcraeSyreuq/xaja/".split("").reverse().join("");
var _0x9164e = (806449 ^ 806452) + (461270 ^ 461278);
var kuaInfoUrl = gwDomain + "ofni/auk/sdoog/ipa/ipa-ecivres-sdoog/".split("").reverse().join("");
_0x9164e = 301802 ^ 301807;
var shortLinkUrl = gwDomain + "/user-service-api/api/promot/generateShortLink";
var searchHisUrl = gwDomain + "/goods-service-api/api/user-action/market/search/his";
var _0xgebe5f = (623667 ^ 623670) + (535408 ^ 535414);
var addShareLinkUrl = gwDomain + "dda/erahs/tsil/sdoog/ipa/ipa-ecivres-sdoog/".split("").reverse().join("");
_0xgebe5f = 'mjohfg';
var doScrollTop = false;
var queryUserListView = gwDomain + "ledoMweiVtsiLresUteg/weiv-tsil-resu/ipa/ipa-ecivres-resu/".split("").reverse().join("");
var _0x349f;
var addUserListView = gwDomain + "/user-service-api/api/user-list-view/addUserViewModel";
_0x349f = (346489 ^ 346491) + (108230 ^ 108227);
var _0xd170dc = (859082 ^ 859082) + (998028 ^ 998024);
var addUserListViewInfo = gwDomain + "ofnIresUdda/weiv-tsil-resu/ipa/ipa-ecivres-resu/".split("").reverse().join("");
_0xd170dc = (351329 ^ 351331) + (667869 ^ 667865);
var sendPresaleConv = gwDomain + "vnoCteg/elaserp/ppa/ipa/ipa-mi/".split("").reverse().join("");
var addUARecordUrl = gwDomain + "/lb-bi-api/api/user-action/add-record";
var _0x68422c = (481634 ^ 481638) + (518307 ^ 518305);
var extAttrFilterUrl = gwDomain + "sretlif/rtta-txe/tsil/sdoog/ipa/ipa-ecivres-sdoog/".split("").reverse().join("");
_0x68422c = "kdleoi".split("").reverse().join("");
var _0x46be = (916392 ^ 916392) + (913045 ^ 913043);
var activeBrowseGoodsUrl = gwDomain + "sdoog/esworb/tca/noitca-resu/ipa/ipa-ecivres-sdoog/".split("").reverse().join("");
_0x46be = 'idkbem';
$(function() {
    initParam();
    queryGoodsMarket();
    listLoadGoodsBrowseAct();
});
function initParam() {
    if (carrierId != null && carrierId != "0") {
        initCarrierData(carrierId);
        initGroupDiv(carrierId);
    }
    if (groupId != undefined && groupId != "0") {
        initGroupData(groupId);
    }
    if (groupId != undefined && groupId != "0" && serverId != undefined) {
        initServerDiv(groupId, serverId);
    }
    if (camp != undefined && camp != '') {
        initCampData(camp);
    }
    if (queryHisCond != "null" && queryHisCond != '') {
        initQHisData();
    }
}
function initQHisData() {
    var _0x84f = JSON['parse'](queryHisCond);
    var _0x065f = _0x84f['jsonObjDTO'];
    if (_0x065f != null) {
        if (_0x065f['minPrice'] != null) {
            $("#min-price")['val'](_0x065f['minPrice']);
            minPrice = _0x065f['minPrice'];
        }
        if (_0x065f['maxPrice'] != null) {
            $("#max-price")['val'](_0x065f['maxPrice']);
            maxPrice = _0x065f['maxPrice'];
        }
        if (_0x065f['serviceId'] != null && _0x065f['serviceId'] != '') {
            $("#service-id-" + _0x065f['serviceId'])['addClass']("no".split("").reverse().join(""));
            $(".service-support-sel")['addClass']("selected");
            if (_0x065f['serviceId'] == "10") {
                $(".service-support-sel-val")['text']("终身找回包赔");
            }
            if (_0x065f['serviceId'] == "13") {
                $(".service-support-sel-val")['text']("购心安买可".split("").reverse().join(""));
            }
            if (_0x065f['serviceId'] == "21".split("").reverse().join("")) {
                $("lav-les-troppus-ecivres.".split("").reverse().join(""))['text']("商家包赔");
            }
            if (_0x065f['serviceId'] == "4") {
                $(".service-support-sel-val")['text']("保担牌金".split("").reverse().join(""));
            }
            if (_0x065f['serviceId'] == "15") {
                $(".service-support-sel-val")['text']("人脸包赔");
            }
            serviceId = _0x065f['serviceId'];
        }
        if (_0x065f['tradeType'] != null && _0x065f['tradeType'] != '' && _0x065f['tradeType'] != "0") {
            $("-epyt-edart#".split("").reverse().join("") + _0x065f['tradeType'])['addClass']("on");
            $("les-epyt-edart.".split("").reverse().join(""))['addClass']("selected");
            if (_0x065f['tradeType'] == "js") {
                $(".trade-type-sel-val")['text']("平台代发");
            }
            if (_0x065f['tradeType'] == "bd".split("").reverse().join("")) {
                $("lav-les-epyt-edart.".split("").reverse().join(""))['text']("货发家卖".split("").reverse().join(""));
            }
            tradeType = _0x065f['tradeType'];
        }
        if (_0x065f['supportReport'] != null && _0x065f['supportReport'] == "1") {
            $("#support-report-1")['addClass']("on");
            $("les-troper-troppus.".split("").reverse().join(""))['addClass']("selected");
            if (_0x065f['supportReport'] == "1") {
                $(".support-report-sel-val")['text']("号验方官".split("").reverse().join(""));
            }
            supportReport = _0x065f['supportReport'];
        }
        if (_0x065f['fiveStarSellerFlag'] != null && (_0x065f['fiveStarSellerFlag'] == "0" || _0x065f['fiveStarSellerFlag'] == "1")) {
            if (_0x065f['fiveStarSellerFlag'] == "0") {
                $("0-rats-evif.".split("").reverse().join(""))['addClass']("on");
                $(".five-star-sel")['addClass']("detceles".split("").reverse().join(""));
                $(".five-star-sel-val")['text']("个人");
            }
            if (_0x065f['fiveStarSellerFlag'] == "1") {
                $("1-rats-evif.".split("").reverse().join(""))['addClass']("on");
                $(".five-star-sel")['addClass']("selected");
                $("lav-les-rats-evif.".split("").reverse().join(""))['text']("商户");
            }
            fiveStarSellerFlag = _0x065f['fiveStarSellerFlag'];
        }
        if (_0x065f['keyword'] != null) {
            $(".filter-search")['find'](".keyword")['val'](_0x065f['keyword']);
            keyword = _0x065f['keyword'];
        }
        if (_0x065f['queryGoodsExtendAttrValList'] != null) {
            $("meti-rttatxe.".split("").reverse().join(""))['find'](".filter-pop-box")['each'](function(index, e) {
                var _0x8756d = (729015 ^ 729011) + (742308 ^ 742308);
                var _0x026ad = $(this)['attr']("data-val-filtertype");
                _0x8756d = 389422 ^ 389417;
                if (_0x026ad == "2") {
                    var showObj = initMainExtAttrOn(this, _0x065f, _0x026ad);
                    if (showObj['showStatus']) {
                        if ($(this)['hasClass']("dnetxe-retlif".split("").reverse().join(""))) {
                            var _0x234a = $(this)['parents']("xob-pop-retlif.".split("").reverse().join(""))['index']();
                            var _0x6f_0x92c = (660848 ^ 660852) + (609669 ^ 609668);
                            var that = $(this)['parents'](".filter-item")['find'](".chose-select")['eq'](_0x234a);
                            _0x6f_0x92c = (210286 ^ 210281) + (389489 ^ 389490);
                            that['addClass']("selected")['find']("p")['text'](showObj['showContent']);
                        } else {
                            var _0x8528ac = (161429 ^ 161425) + (687486 ^ 687486);
                            var that = $(this)['parents'](".filter-item")['find'](".chose-select")['eq'](index);
                            _0x8528ac = (840468 ^ 840468) + (405566 ^ 405561);
                            var _0x845db = (887061 ^ 887056) + (822161 ^ 822168);
                            var txt = that['find']("p")['attr']("data-title");
                            _0x845db = (629138 ^ 629136) + (828657 ^ 828660);
                            if (showObj['showAppend']) {
                                txt = txt + "(" + showObj['showContent'] + ")";
                            } else {
                                txt = showObj['showContent'];
                            }
                            that['addClass']("selected")['find']("p")['text'](txt);
                        }
                    }
                }
                if (_0x026ad == "3") {
                    var _0x9c_0x77e;
                    var _0xeded = 550483 ^ 550483;
                    _0x9c_0x77e = 886935 ^ 886942;
                    $(this)['find'](".agg-filter")['each'](function(index2, e) {
                        var _0x57a07a = initMainExtAttrOn(this, _0x065f, _0x026ad);
                        if (_0x57a07a['showStatus']) {
                            _0xeded = _0xeded + _0x57a07a['showContent'];
                            var _0x0g8f = $(this)['parents']("xob-pop-retlif.".split("").reverse().join(""))['find'](".juhe-tab ul li")['eq'](index2);
                            _0x0g8f['find']("span")['attr']("elyts".split("").reverse().join(""), "display:inline;")['text'](_0x57a07a['showContent']);
                        }
                    });
                    if (_0xeded > (652014 ^ 652014)) {
                        var that = $(this)['parents']("meti-retlif.".split("").reverse().join(""))['find'](".chose-select")['eq'](index);
                        var _0x90gc = (843959 ^ 843955) + (294101 ^ 294100);
                        var txt = that['find']("p")['attr']("eltit-atad".split("").reverse().join("")) + "(" + _0xeded + ")";
                        _0x90gc = 721759 ^ 721751;
                        that['addClass']("detceles".split("").reverse().join(""))['find']("p")['text'](txt);
                    }
                }
            });
        }
    }
}
function initListViewStyle(viewType) {
    if (viewType == "1") {
        $("#viewType")['text']("式模图大至换切".split("").reverse().join(""));
    } else {
        $("#viewType")['text']("切换至小图模式");
    }
    var _0x578f9a = $['cookie']("siwtchViewTip");
    if (_0x578f9a == undefined || _0x578f9a == '') {
        $(".change-tip")['css']("display", "block");
    }
    var _0xa4736a = initShowGuideViewModel();
    if (isSupportSwitchView && _0xa4736a != "2") {
        choseView();
    }
}
function initMainExtAttrOn(e1, hisJsonObj, filterType) {
    var _0x11_0x542 = $(e1)['attr']("data-val-eid");
    var _0x74933a = (581412 ^ 581414) + (589033 ^ 589037);
    var _0xd7260f;
    _0x74933a = "jpemjb".split("").reverse().join("");
    for (var i = 207319 ^ 207319; i < hisJsonObj['queryGoodsExtendAttrValList']['length']; i++) {
        if (_0x11_0x542 == hisJsonObj['queryGoodsExtendAttrValList'][i]['eid']) {
            _0xd7260f = hisJsonObj['queryGoodsExtendAttrValList'][i];
            break;
        }
    }
    var _0x86656e = false;
    var _0xdfg = (451947 ^ 451947) + (911870 ^ 911868);
    var _0xf43d = null;
    _0xdfg = (978916 ^ 978915) + (825417 ^ 825419);
    var _0x627fd;
    var _0x07gfee = false;
    _0x627fd = (989602 ^ 989604) + (427250 ^ 427251);
    if (_0xd7260f != undefined) {
        var _0x1ff4a = (160206 ^ 160199) + (437341 ^ 437337);
        var _0xab04d = $(e1)['attr']("data-val-filterkind");
        _0x1ff4a = 'egeako';
        if (_0xab04d == "1") {
            var _0xec9a;
            var _0xc3_0x574 = _0xd7260f['ev'];
            _0xec9a = (161915 ^ 161915) + (406851 ^ 406853);
            var _0x94469g = (884722 ^ 884730) + (423711 ^ 423706);
            var _0x2edf = _0xc3_0x574['split']("ы");
            _0x94469g = 653892 ^ 653890;
            if (_0x2edf['length'] == (600386 ^ 600384)) {
                $(e1)['find'](".min-val")['val'](_0x2edf[188775 ^ 188775]);
                $(e1)['find']("lav-xam.".split("").reverse().join(""))['val'](_0x2edf[250550 ^ 250551]);
                _0x86656e = !![];
                _0x07gfee = !![];
                if (filterType == "2") {
                    _0xf43d = _0x2edf[760852 ^ 760852] + "-" + _0x2edf[578434 ^ 578435];
                } else {
                    _0xf43d = 800953 ^ 800952;
                }
            }
        } else {
            var _0xeg62a = "no".split("").reverse().join("");
            var _0xe_0x621 = $(e1)['find'](".filter-pop-head .self-type");
            if (_0xe_0x621['length'] > (567782 ^ 567782) && _0xd7260f['selectOption'] == "2") {
                _0xe_0x621['addClass']("no-all");
                _0xe_0x621['find']("hctam-lla. lu".split("").reverse().join(""))['removeClass']("no".split("").reverse().join(""));
                _0xe_0x621['find']("ul .zdy-match")['addClass']("on");
                _0xe_0x621['find']("tnc-nim.".split("").reverse().join(""))['val'](_0xd7260f['minCnt']);
            }
            var _0xb6fe = _0xd7260f['evs'];
            if (_0xb6fe != null && _0xb6fe['length'] > (350973 ^ 350973)) {
                if ($(e1)['find']("mottob-pop-retlif.".split("").reverse().join(""))['hasClass']("more-chose")) {
                    _0xeg62a = "noerom".split("").reverse().join("");
                }
                if ($(e1)['hasClass']("dnetxe-retlif".split("").reverse().join(""))) {
                    $(e1)['find'](".filter-pop-ext .pop-chose-item")['each'](function(index2, e2) {
                        var _0xb_0xa77;
                        var _0x934ce = $(e2)['removeClass'](_0xeg62a)['attr']("data-value");
                        _0xb_0xa77 = (858076 ^ 858068) + (675506 ^ 675508);
                        if (_0xb6fe['includes'](_0x934ce)) {
                            $(e2)['addClass'](_0xeg62a);
                            _0x86656e = !![];
                        }
                    });
                } else {
                    $(e1)['find'](".filter-pop-bottom .pop-chose-item")['each'](function(index2, e2) {
                        var _0x89360a = (588783 ^ 588775) + (717543 ^ 717537);
                        var _0x26ac8a = $(e2)['attr']("data-value");
                        _0x89360a = (214050 ^ 214053) + (445476 ^ 445477);
                        if (_0xb6fe['includes'](_0x26ac8a)) {
                            $(e2)['addClass'](_0xeg62a);
                            initSubExtAttrOn(e2, hisJsonObj['queryGoodsExtendAttrValList']);
                            _0x86656e = !![];
                        }
                    });
                }
            }
            if (_0x86656e) {
                if (filterType == "2") {
                    if (_0xeg62a == "no".split("").reverse().join("")) {
                        _0xf43d = _0xd7260f['evs'][238081 ^ 238081];
                    } else {
                        _0xf43d = _0xd7260f['evs']['length'];
                        _0x07gfee = !![];
                    }
                } else {
                    _0xf43d = _0xd7260f['evs']['length'];
                    _0x07gfee = !![];
                }
            }
        }
    }
    var _0x2_0xf1d = (546631 ^ 546625) + (702040 ^ 702047);
    var _0xa4_0x98c = new Object();
    _0x2_0xf1d = (455765 ^ 455761) + (403224 ^ 403224);
    _0xa4_0x98c['showStatus'] = _0x86656e;
    _0xa4_0x98c['showContent'] = _0xf43d;
    _0xa4_0x98c['showAppend'] = _0x07gfee;
    return _0xa4_0x98c;
}
function initSubExtAttrOn(e, extAttrList) {
    var _0x1ee = $(e)['find']("nerdlihc-meti.".split("").reverse().join(""));
    var _0x0e_0x494;
    var _0x4f15fb = _0x1ee['attr']("data-val-subeid");
    _0x0e_0x494 = 512284 ^ 512277;
    var _0x5e57db;
    for (var i = 282691 ^ 282691; i < extAttrList['length']; i++) {
        if (_0x4f15fb == extAttrList[i]['eid']) {
            _0x5e57db = extAttrList[i];
            break;
        }
    }
    if (_0x5e57db != undefined) {
        var _0xgafa = _0x5e57db['evs'];
        if (_0xgafa != null && _0xgafa['length'] > (260566 ^ 260566)) {
            _0x1ee['find']("dlihc.".split("").reverse().join(""))['each'](function(index, e2) {
                var _0xg371eb = (244923 ^ 244924) + (834219 ^ 834216);
                var _0xc4_0x1f4 = $(e2)['attr']("data-value");
                _0xg371eb = 600511 ^ 600510;
                if (_0xgafa['includes'](_0xc4_0x1f4)) {
                    $(e2)['addClass']("on");
                }
            });
        }
    }
}
function replaceWebUrl() {
    var _0x3e294f = "";
    if ($("#promotion")['val']() == "1") {
        _0x3e294f = "/promotion-list";
    }
    var _0x0d_0x228 = (271553 ^ 271554) + (409557 ^ 409564);
    var _0x65ebe = _0x3e294f + "/" + gameId + "-" + gtId + "-" + groupId + "-" + serverId + "-" + carrierId + ".html?pageNum=" + pageNum;
    _0x0d_0x228 = 'idlkgq';
    if (lbEnv != undefined && lbEnv != null && lbEnv != '') {
        _0x65ebe += "&lbEnv=" + lbEnv;
    }
    if (canClaimReward != undefined && canClaimReward != null && canClaimReward != '') {
        _0x65ebe += "=draweRmialCnac&".split("").reverse().join("") + canClaimReward;
    }
    if (actId != undefined && actId != null && actId != '') {
        _0x65ebe += "&actId=" + actId;
    }
    if (location['href']['indexOf']("#reloaded") != -(691768 ^ 691769)) {
        _0x65ebe += "#reloaded";
    }
    window['history']['pushState'](null, null, _0x65ebe);
}
function singleChoseEvent(e) {
    if ($(e)['hasClass']("senior-filter-main-s")) {
        queryGoodsMarket("true");
    }
}
function initGroupDiv(fromCarrierId) {
    if ($(".game-group-p")['length'] == (491987 ^ 491987)) {
        return;
    }
    if (carriersStr == undefined || carriersStr == '' || carriersStr['length'] == (522351 ^ 522351)) {
        return;
    }
    var _0x524c3d;
    for (var i = 768565 ^ 768565; i < carriers['length']; i++) {
        if (carriers[i]['carrierid'] == fromCarrierId) {
            _0x524c3d = carriers[i]['groups'];
            groups = _0x524c3d;
        }
    }
    if (_0x524c3d != undefined) {
        var _0xc9d = '';
        for (var i = 541230 ^ 541230; i < _0x524c3d['length']; i++) {
            var _0x47b = '';
            _0x47b += "<div class="pop-chose-item" data-value="" + _0x524c3d[i]['groupname'] + "" data-val="" + _0x524c3d[i]['groupid'] + ">\"".split("").reverse().join("");
            _0x47b += ">p<".split("").reverse().join("") + _0x524c3d[i]['groupname'] + "</p>";
            _0x47b += "</div>";
            _0xc9d += _0x47b;
        }
        $("mottob-pop-retlif. puorg-emag.".split("").reverse().join(""))['empty']()['append'](_0xc9d);
    }
}
function cleanKuaGSData() {
    cleanGroupData(false);
    cleanServerData(!![]);
}
function cleanKuaData() {
    var _0x3cf = $("neercs-retlif.".split("").reverse().join(""))['find'](".filter-item .game-kua");
    if (_0x3cf['length'] == (499252 ^ 499252)) {
        return;
    }
    _0x3cf['each'](function(index, e) {
        if ($(this)['hasClass']("on")) {
            $(this)['removeClass']("no".split("").reverse().join(""));
            removeFilterDivKua();
        }
    });
}
function cleanGroupData(cleanDetails) {
    var _0xc321g = $(".filter-screen")['find']("p-puorg-emag. thgir-meti. meti-retlif.".split("").reverse().join(""));
    if (_0xc321g['length'] == (526540 ^ 526540)) {
        return;
    }
    $(".game-group .keyword")['val']("");
    groupId = 826193 ^ 826193;
    _0xc321g['removeClass']("detceles".split("").reverse().join(""));
    _0xc321g['find'](".game-group-text")['text']("区择选请".split("").reverse().join(""));
    $(".filter-screen")['find'](".filter-item .filter-pop .game-group .filter-pop-bottom .pop-chose-item")['each'](function(index, e) {
        if ($(e)['hasClass']("on")) {
            $(e)['removeClass']("no".split("").reverse().join(""));
        }
    });
    if (cleanDetails) {
        $(".game-group .filter-pop-bottom")['empty']();
    }
}
function cleanServerData(cleanDetails) {
    serverId = 922073 ^ 922073;
    var _0x16c = $("neercs-retlif.".split("").reverse().join(""))['find'](".filter-item .item-right .game-server-p");
    if (_0x16c['length'] == (647331 ^ 647331)) {
        return;
    }
    $(".game-server .keyword")['val']("");
    _0x16c['removeClass']("selected");
    _0x16c['find']("txet-revres-emag.".split("").reverse().join(""))['text']("请选择服");
    $(".filter-screen")['find']("meti-esohc-pop. mottob-pop-retlif. revres-emag. pop-retlif. meti-retlif.".split("").reverse().join(""))['each'](function(index, e) {
        if ($(e)['hasClass']("no".split("").reverse().join(""))) {
            $(e)['removeClass']("on");
        }
    });
    if (cleanDetails) {
        $(".game-server .filter-pop-bottom")['empty']();
    }
}
function initKuaData(defGroupId, defServerId) {
    cleanKuaGSData();
    initGroupData(defGroupId);
    initServerDiv(defGroupId, defServerId);
    groupId = defGroupId;
    serverId = defServerId;
}
function initCarrierData(defCarrierId) {
    if (carriersStr == undefined || carriersStr == '' || carriersStr['length'] == (923222 ^ 923222)) {
        return;
    }
    var _0xaac;
    for (var i = 756335 ^ 756335; i < carriers['length']; i++) {
        if (carriers[i]['carrierid'] == defCarrierId) {
            _0xaac = carriers[i];
        }
    }
    if (_0xaac != undefined) {
        if (carriers['length'] >= (419076 ^ 419075) || publishChooseRegionalServiceFlag == "1") {
            $("neercs-retlif.".split("").reverse().join(""))['find'](".filter-item .item-right .game-carrier-p")['addClass']("selected");
            $(".filter-screen")['find']("txet-reirrac-emag. p-reirrac-emag. thgir-meti. meti-retlif.".split("").reverse().join(""))['text'](_0xaac['carriername']);
            $(".filter-screen")['find'](".filter-item .filter-pop .game-carrier .filter-pop-bottom .pop-chose-item")['each'](function(index, e) {
                if ($(e)['attr']("data-val") == defCarrierId) {
                    $(e)['addClass']("no".split("").reverse().join(""));
                }
            });
        } else {
            $("neercs-retlif.".split("").reverse().join(""))['find']("reirrac-emag. wot-thgir. thgir-meti. meti-retlif.".split("").reverse().join(""))['each'](function(index, e) {
                if ($(e)['attr']("lav-atad".split("").reverse().join("")) == defCarrierId) {
                    $(e)['addClass']("on");
                }
            });
        }
    }
}
function initGroupData(defGroupId) {
    if (groups == undefined || groups == null) {
        return;
    }
    var _0x236b6d;
    for (var i = 718371 ^ 718371; i < groups['length']; i++) {
        if (groups[i]['groupid'] == defGroupId) {
            _0x236b6d = groups[i];
        }
    }
    if (_0x236b6d != undefined) {
        $(".filter-screen")['find']("p-puorg-emag. thgir-meti. meti-retlif.".split("").reverse().join(""))['addClass']("selected");
        $("neercs-retlif.".split("").reverse().join(""))['find']("txet-puorg-emag. p-puorg-emag. thgir-meti. meti-retlif.".split("").reverse().join(""))['text'](_0x236b6d['groupname']);
        $(".filter-screen")['find'](".filter-item .filter-pop .game-group .filter-pop-bottom .pop-chose-item")['each'](function(index, e) {
            if ($(e)['attr']("data-val") == defGroupId) {
                $(e)['addClass']("on");
            }
        });
    }
}
function initServerDiv(fromGroupId, defServerId) {
    if (groups == undefined || groups == null) {
        return;
    }
    var _0x06b54d;
    for (var i = 385964 ^ 385964; i < groups['length']; i++) {
        if (groups[i]['groupid'] == fromGroupId) {
            _0x06b54d = groups[i]['servers'];
        }
    }
    var _0xfb_0xg2f = (475716 ^ 475725) + (490258 ^ 490267);
    var _0x4556a;
    _0xfb_0xg2f = "jebefj".split("").reverse().join("");
    if (_0x06b54d != undefined) {
        var _0x12_0x175 = '';
        for (var i = 525883 ^ 525883; i < _0x06b54d['length']; i++) {
            if (defServerId == _0x06b54d[i]['serverid']) {
                _0x4556a = _0x06b54d[i];
            }
            var _0x53a6ca = '';
            _0x53a6ca += "\"=eulav-atad \"meti-esohc-pop\"=ssalc vid<".split("").reverse().join("") + _0x06b54d[i]['servername'] + "\"=lav-atad \"".split("").reverse().join("") + _0x06b54d[i]['serverid'] + "">";
            _0x53a6ca += "<p>" + _0x06b54d[i]['servername'] + "</p>";
            _0x53a6ca += "</div>";
            _0x12_0x175 += _0x53a6ca;
        }
        $("mottob-pop-retlif. revres-emag.".split("").reverse().join(""))['empty']()['append'](_0x12_0x175);
    }
    if (_0x4556a != undefined) {
        $(".filter-screen")['find'](".filter-item .item-right .game-server-p")['addClass']("detceles".split("").reverse().join(""));
        $(".filter-screen")['find'](".filter-item .item-right .game-server-p .game-server-text")['text'](_0x4556a['servername']);
        $(".filter-screen")['find'](".filter-item .filter-pop .game-server .filter-pop-bottom .pop-chose-item")['each'](function(index, e) {
            if ($(e)['attr']("lav-atad".split("").reverse().join("")) == defServerId) {
                $(e)['addClass']("no".split("").reverse().join(""));
            }
        });
    }
}
function initCampData(fromCamp) {
    $(".filter-screen")['find'](".filter-item .item-right .game-camp-p")['addClass']("selected");
    $(".filter-screen")['find'](".filter-item .item-right .game-camp-p .game-camp-text")['text'](fromCamp);
    $(".filter-screen")['find'](".filter-item .filter-pop .game-camp .filter-pop-bottom .pop-chose-item")['each'](function(index, e) {
        if ($(e)['attr']("data-val") == fromCamp) {
            $(e)['addClass']("no".split("").reverse().join(""));
        }
    });
    $("neercs-retlif.".split("").reverse().join(""))['find'](".filter-item .filter-pop .game-camp .filter-pop-extend .pop-chose-item")['each'](function(index, e) {
        if ($(e)['attr']("data-value") == fromCamp) {
            $(e)['addClass']("no".split("").reverse().join(""));
        }
    });
}
var delayTimeout, market_xhr, headerObj;
function queryGoodsMarket(queryIndexPage) {
    layer['closeAll']("loading");
    layer['load'](181990 ^ 181989, {
        "shade": [0.2, "000#".split("").reverse().join("")]
    });
    initLoadTemplate();
    if (market_xhr) {
        market_xhr['abort']();
    }
    if (queryIndexPage == "true") {
        pageNum = 343467 ^ 343466;
    }
    replaceWebUrl();
    if (delayTimeout) {
        clearTimeout(delayTimeout);
    }
    delayTimeout = setTimeout(function() {
        try {
            var _0x521c = initMarketParam();
            headerObj = initHeader(_0x521c);
            queryGoodsC(_0x521c);
        } catch (e) {
            console['log'](e);
        }
    }, 329637 ^ 329623);
}
function queryGoodsB(paramObj) {
    if (paramObj == null) {
        paramObj = initMarketParam();
    }
    var _0xbb68d = new Object();
    _0xbb68d['gameId'] = paramObj['gameId'];
    _0xbb68d['gtid'] = paramObj['gtid'];
    _0xbb68d['groupId'] = paramObj['groupId'];
    _0xbb68d['serverId'] = paramObj['serverId'];
    if (paramObj['tradePlace'] != null && paramObj['tradePlace'] != undefined) {
        _0xbb68d['tradePlace'] = paramObj['tradePlace'];
    }
    if (paramObj['extendAttrList'] != null && paramObj['extendAttrList'] != undefined) {
        _0xbb68d['extendAttrList'] = paramObj['extendAttrList'];
    }
    if (shopSortType != undefined) {
        _0xbb68d['shopSortType'] = shopSortType;
    }
    $['ajax']({
        "url": queryMallListUrl,
        "async": false,
        "type": "POST",
        'data': JSON['stringify'](_0xbb68d),
        'dataType': "json",
        "contentType": "application/json",
        'xhrFields': {
            'withCredentials': !![]
        },
        'success': function(result) {
            var _0xbe9c = [];
            if (result['code'] == (301661 ^ 301661)) {
                _0xbe9c = result['body'];
            }
            initMallHtml(_0xbe9c);
        },
        "error": function(result) {
            layer['msg']("！常异询查城商".split("").reverse().join(""));
            return;
        }
    });
}
function queryGoodsC(paramObj) {
    market_xhr = $['ajax']({
        'url': queryGoodsCListUrl,
        "async": !![],
        'type': "POST",
        "data": JSON['stringify'](paramObj),
        'dataType': "json",
        'contentType': 'application/json',
        "xhrFields": {
            'withCredentials': !![]
        },
        'headers': {
            "lb-timestamp": headerObj['lbtimestamp'],
            "lb-sign": headerObj['lbsign']
        },
        "success": function(result) {
            var _0x7dafd = 103782 ^ 103782;
            if (result['code'] == (862945 ^ 862945)) {
                $("vid-tluseron.".split("").reverse().join(""))['hide']();
                var _0x89e5b;
                var _0x5ffb = result['body'];
                _0x89e5b = (366771 ^ 366772) + (808933 ^ 808929);
                initMarketSHtml(paramObj, _0x5ffb['results']);
                _0x7dafd = _0x5ffb['records'];
                initHomePageSearchCookie(paramObj);
            } else if (result['code'] == (515217 ^ 515329)) {
                resetSysTimes();
                if (location['href']['indexOf']("dedaoler#".split("").reverse().join("")) == -(370398 ^ 370399)) {
                    location['href'] = location['href'] + "#reloaded";
                    location['reload']();
                }
            } else if (result['code'] == (393460 ^ 394096)) {
                if (location['href']['indexOf']("dedaoler#".split("").reverse().join("")) == -(930875 ^ 930874)) {
                    location['href'] = location['href'] + "#reloaded";
                    location['reload']();
                }
            } else {
                _0x7dafd = pageNum * pageSize;
                $("xob-tsil.".split("").reverse().join(""))['empty']();
                $(".noresult-div")['show']();
            }
            initListPage(pageNum, pageSize, _0x7dafd);
        },
        'error': function(result) {
            layer['closeAll']("loading");
            layer['msg']("！常异询查品商".split("").reverse().join(""));
            return;
        },
        'complete': function() {
            addUARecord();
            completeQueryOthers(paramObj);
            changeSelectTip();
            scrollGoodsTop();
        }
    });
}
function resetSysTimes() {
    $['ajax']({
        "url": "/curtime",
        'async': false,
        'type': "GET",
        'success': function(sysCurTime) {
            var _0x9018f = new Date()['getTime']();
            var _0x8799a = parseInt(sysCurTime) - parseInt(_0x9018f) - (513254 ^ 513806);
            localStorage['setItem']("lb-delay-time", _0x8799a);
        }
    });
}
function addUARecord() {
    var _0xacgf = new Object();
    _0xacgf['gameId'] = gameId;
    _0xacgf['gtId'] = gtId;
    _0xacgf['actionType'] = "1";
    _0xacgf['refUrl'] = window['location']['href'];
    $['ajax']({
        'url': addUARecordUrl,
        'async': !![],
        'type': "POST",
        'data': JSON['stringify'](_0xacgf),
        'dataType': "json",
        'contentType': 'application/json',
        'xhrFields': {
            "withCredentials": !![]
        }
    });
}
function completeQueryOthers(paramObj) {
    try {
        if (showMall && mallPurchaseStyle != '' && supportedBuyWay != '') {
            if (gameId == "G10" && gtId == "800001".split("").reverse().join("")) {
                queryGoodsB(paramObj);
            } else {
                if (groupId != null && groupId != '' && groupId != "0" && serverId != null && serverId != '' && serverId != "0" && listTemplate == "bxy_tsil".split("").reverse().join("")) {
                    queryGoodsB(paramObj);
                } else {
                    $(".list-shop")['empty']();
                }
            }
        }
        if (showShouHuo == "true") {
            queryShouHuoMarket(paramObj);
        }
    } catch (e) {
        console['log'](e);
    } finally {
        layer['closeAll']("gnidaol".split("").reverse().join(""));
    }
}
function initMallHtml(mallGoodsArr) {
    if (mallGoodsArr == undefined || mallGoodsArr['length'] == (607241 ^ 607241)) {
        $(".list-shop")['empty']();
        return;
    }
    var _0xcc2f9d = (379485 ^ 379481) + (492146 ^ 492146);
    var _0x8c3cdd = '';
    _0xcc2f9d = 416529 ^ 416533;
    for (var i = 766383 ^ 766383; i < mallGoodsArr['length']; i++) {
        if (i + (218700 ^ 218701) > (433018 ^ 433017)) {
            break;
        }
        var _0xbb42b = (630768 ^ 630773) + (173968 ^ 173969);
        var _0xd5fcb = mallGoodsArr[i]['mallGoods'];
        _0xbb42b = 'eleaea';
        var _0x92ab;
        var _0x2ec = _0xd5fcb['unit'];
        _0x92ab = 'iigdfe';
        if (_0x2ec != null && _0x2ec != '' && _0x2ec['length'] > (185877 ^ 185873)) {
            _0x2ec = _0x2ec['substr'](914538 ^ 914538, 814709 ^ 814705);
        }
        var _0x023f = mallGoodsArr[i]['mallPurchaseLimit'];
        var _0x660a;
        var _0xe4ba0e = '';
        _0x660a = 191496 ^ 191496;
        _0xe4ba0e += "<div class="shop-item" idx="" + i + "" " + "data-val-goodsid="" + _0xd5fcb['goodsId'] + "" " + "\"=up-lav-atad".split("").reverse().join("") + _0xd5fcb['priceOfUnit'] + " \"".split("").reverse().join("") + "data-val-up="" + _0xd5fcb['unitOfPrice'] + " \"".split("").reverse().join("") + "\"=tinu-lav-atad".split("").reverse().join("") + _0x2ec + " \"".split("").reverse().join("") + "\"=yenom-fed-lav-atad".split("").reverse().join("") + _0x023f['buyMoneyDefault'] + "" " + "data-val-def-num="" + _0x023f['buyNumberDefault'] + "" " + "data-val-pernum="" + _0xd5fcb['pernum'] + "" " + "\"=nim-yenom-yub-lav-atad".split("").reverse().join("") + _0x023f['buyMoneyMin'] + "" " + "\"=kcots-lav-atad".split("").reverse().join("") + _0xd5fcb['stock'] + "" " + "\"=ecirp-lav-atad".split("").reverse().join("") + _0xd5fcb['price'] + "">";
        _0xe4ba0e += ">\"xob-meti-pohs\"=ssalc vid<".split("").reverse().join("");
        _0xe4ba0e += "<div class="shop-v part-01">";
        _0xe4ba0e += "<dl class="clearfix">";
        _0xe4ba0e += "<dt>";
        _0xe4ba0e += "\"=crs gmi<".split("").reverse().join("") + initMallGoodsImgHtml(_0xd5fcb) + ">/\"".split("").reverse().join("");
        _0xe4ba0e += "</dt>";
        _0xe4ba0e += ">dd<".split("").reverse().join("");
        _0xe4ba0e += "<h4>" + initMallGoodsTitle(_0xd5fcb);
        if (_0xd5fcb['kqgroupName'] != null && _0xd5fcb['kqgroupName'] != '') {
            _0xe4ba0e += "<span class="hutongtip" data-val-kqid="" + _0xd5fcb['kqid'] + ""><img src="" + bucketDomain + "/7881/images/list-2024/hutong.png"/></span>";
        }
        _0xe4ba0e += "</h4>";
        if (_0xd5fcb['deliveryTimeText'] != null && _0xd5fcb['deliveryTimeText'] != '') {
            _0xe4ba0e += "<p>平均<span>" + _0xd5fcb['deliveryTimeText'] + ">p/<货发>naps/<".split("").reverse().join("");
        }
        _0xe4ba0e += "</dd>";
        _0xe4ba0e += ">ld/<".split("").reverse().join("");
        _0xe4ba0e += "</div>";
        _0xe4ba0e += ">\"20-trap v-pohs\"=ssalc vid<".split("").reverse().join("");
        if (_0xd5fcb['unitOfPrice'] != null && _0xd5fcb['unitOfPrice'] != (399285 ^ 399285)) {
            _0xe4ba0e += ">naps<=元1>3h<".split("").reverse().join("") + _0xd5fcb['unitOfPrice'] + ">naps/<".split("").reverse().join("") + _0x2ec + "</h3>";
        }
        _0xe4ba0e += "<h3><em>" + _0xd5fcb['priceOfUnit'] + "</em> 元/" + _0x2ec + " </h3>";
        _0xe4ba0e += ">vid/<".split("").reverse().join("");
        _0xe4ba0e += "<div class="shop-v part-03">";
        _0xe4ba0e += "<div class="l">";
        if (mallPurchaseStyle['indexOf']("1") >= (339943 ^ 339943)) {
            if (supportedBuyWay == "byNumber") {
                _0xe4ba0e += "<label><input type="radio" name="buytype_" + i + "" value="1" checked="checked"/>按数量</label>";
            } else {
                _0xe4ba0e += "_epytyub\"=eman \"oidar\"=epyt tupni<>lebal<".split("").reverse().join("") + i + "" value="1"/>按数量</label>";
            }
        }
        if (mallPurchaseStyle['indexOf']("2") >= (736810 ^ 736810)) {
            if (supportedBuyWay == "byMoney") {
                _0xe4ba0e += "_epytyub\"=eman \"oidar\"=epyt tupni<>lebal<".split("").reverse().join("") + i + "" value="2" checked="checked"/>按金额</label>";
            } else {
                _0xe4ba0e += "_epytyub\"=eman \"oidar\"=epyt tupni<>lebal<".split("").reverse().join("") + i + ">lebal/<额金按>/\"2\"=eulav \"".split("").reverse().join("");
            }
        }
        _0xe4ba0e += "</div>";
        _0xe4ba0e += "<div class="r">";
        if (supportedBuyWay == "byNumber") {
            _0xe4ba0e += "<h3><input type="text" value="" + _0x023f['buyNumberDefault'] + ">naps<>/\"munylno\"=ssalc \"".split("").reverse().join("") + _0x2ec + "</span></h3>";
        }
        var _0xc1156b = parseInt(div(mul(add(_0x023f['buyMoneyDefault'], 873154 ^ 873155), _0xd5fcb['unitOfPrice']), _0xd5fcb['pernum']));
        var _0x999ab;
        var _0x57fffb = cutXiaoNum(div(mul(_0xc1156b, _0xd5fcb['pernum']), _0xd5fcb['unitOfPrice']), 469341 ^ 469343);
        _0x999ab = 'oopofe';
        if (supportedBuyWay == "byMoney") {
            _0xe4ba0e += "<h3><input type="text" value="" + _0x57fffb + "" class="onlynums"/><span>元</span></h3>";
        }
        _0xe4ba0e += "：存库>p<".split("").reverse().join("") + formatSplitNumber(_0xd5fcb['stock']) + _0x2ec + ">p/<".split("").reverse().join("");
        _0xe4ba0e += "</div>";
        _0xe4ba0e += ">vid/<".split("").reverse().join("");
        _0xe4ba0e += ">\"40-trap v-pohs\"=ssalc vid<".split("").reverse().join("");
        if (supportedBuyWay == "byNumber") {
            var _0x09f56f;
            var _0x68ecf = cutXiaoNum(div(mul(_0xd5fcb['priceOfUnit'], _0x023f['buyNumberDefault']), _0xd5fcb['pernum']), 676849 ^ 676851);
            _0x09f56f = (855868 ^ 855867) + (391668 ^ 391664);
            _0xe4ba0e += "<h3 class="total-num"><span>" + _0x68ecf + ">3h/<元>naps/<".split("").reverse().join("");
        }
        if (supportedBuyWay == "yenoMyb".split("").reverse().join("")) {
            _0xe4ba0e += ">naps<>\"mun-latot\"=ssalc 3h<".split("").reverse().join("") + _0xc1156b + "</span>" + _0x2ec + "</h3>";
        }
        if (_0xd5fcb['userTradeStatisticV2'] != null && _0xd5fcb['userTradeStatisticV2']['closureRate'] != undefined && _0xd5fcb['userTradeStatisticV2']['closureRate'] != '') {
            _0xe4ba0e += "：率交成>p<".split("").reverse().join("") + mul(_0xd5fcb['userTradeStatisticV2']['closureRate'], 435695 ^ 435595) + "%</p>";
        } else {
            _0xe4ba0e += "<p>成交率：--</p>";
        }
        _0xe4ba0e += "</div>";
        _0xe4ba0e += "<div class="shop-v part-05"><div class="tags-box">" + initMallTags(_0xd5fcb) + "</div></div>";
        _0xe4ba0e += "<div class="shop-v part-06">";
        _0xe4ba0e += "<a href="javascript:void(0)" class="btn-com-01 color03">立即购买</a>";
        _0xe4ba0e += "</div>";
        _0xe4ba0e += "</div>";
        _0xe4ba0e += "</div>";
        _0x8c3cdd += _0xe4ba0e;
    }
    var _0x14_0xa13 = '';
    _0x14_0xa13 += "<div class="gold-bg">";
    _0x14_0xa13 += "<div class="gold-shop">";
    _0x14_0xa13 += "<h2 class="sp-tit"><em class="tit"><img src="" + bucketDomain + "/7881/images/list-2024/shop-tit.png?v1"/></em>";
    _0x14_0xa13 += ">\"r\"=ssalc p<".split("").reverse().join("");
    _0x14_0xa13 += "\"=crs gmi<>me<>\")(golaiD008evil:tpircsavaj\"=ferh a<".split("").reverse().join("") + bucketDomain + ">a/<询咨驻入>me/<>/\"\"=tla \"82\"=thgieh \"gnp.motsuc-zr/4202-tsil/segami/1887/".split("").reverse().join("");
    _0x14_0xa13 += "<a href="//i.7881.com/sellerEnter/applyserver/9"><em><img src="" + bucketDomain + "/7881/images/list-2024/rz-edit.png" height="28" alt=""/></em>申请入驻商城</a>";
    _0x14_0xa13 += "</p>";
    _0x14_0xa13 += ">2h/<".split("").reverse().join("");
    _0x14_0xa13 += "<div class="shop-list">";
    _0x14_0xa13 += "<div class="splist-tit">";
    _0x14_0xa13 += ">vid/<>naps/<量数买购>\"30-s\"=ssalc naps<>naps/<价单品商>\"20-s\"=ssalc naps<>naps/<息信品商>\"10-s\"=ssalc naps<>\"l\"=ssalc vid<".split("").reverse().join("");
    _0x14_0xa13 += ">\"r\"=ssalc vid<".split("").reverse().join("");
    if (shopSortType == "PRICEUNITASSTOCKDESC") {
        _0x14_0xa13 += ">lebal/<价单按>/\"dekcehc\"=dekcehc \"CSEDKCOTSSATINUECIRP\"=eulav \"tpItros\"=eman \"oidar\"=epyt tupni<>lebal<".split("").reverse().join("");
        _0x14_0xa13 += ">lebal/<时均按>/\"CSEDKCOTSSATINUECIRPCSAEMITTSOCGVAEDART\"=eulav \"tpItros\"=eman \"oidar\"=epyt tupni<>lebal<".split("").reverse().join("");
    }
    if (shopSortType == "TRADEAVGCOSTTIMEASCPRICEUNITASSTOCKDESC") {
        _0x14_0xa13 += "<label><input type="radio" name="sortIpt" value="PRICEUNITASSTOCKDESC"/>按单价</label>";
        _0x14_0xa13 += ">lebal/<时均按>/\"dekcehc\"=dekcehc \"CSEDKCOTSSATINUECIRPCSAEMITTSOCGVAEDART\"=eulav \"tpItros\"=eman \"oidar\"=epyt tupni<>lebal<".split("").reverse().join("");
    }
    _0x14_0xa13 += ">vid/<".split("").reverse().join("");
    _0x14_0xa13 += "</div>";
    _0x14_0xa13 += "<div class="shop-order">" + _0x8c3cdd + ">vid/<".split("").reverse().join("");
    _0x14_0xa13 += ">\"wohs-erom\"=ssalc vid<".split("").reverse().join("");
    var _0xg34ga = (277665 ^ 277671) + (963402 ^ 963403);
    var _0x36fca = "1";
    _0xg34ga = "agooeb".split("").reverse().join("");
    if (shopSortType == "CSEDKCOTSSATINUECIRPCSAEMITTSOCGVAEDART".split("").reverse().join("")) {
        _0x36fca = "2";
    }
    if (mallGoodsArr['length'] > (643064 ^ 643067)) {
        _0x14_0xa13 += "<p><a href="/mall-list/" + gameId + "-" + gtId + "-" + groupId + "-" + serverId + "-" + tradePlace + "-" + _0x36fca + ">p/<>a/<>me/<;927ex#&>\"tnofnoci\"=ssalc me<多更示展>\"lmth.".split("").reverse().join("");
    }
    _0x14_0xa13 += ">vid/<".split("").reverse().join("");
    _0x14_0xa13 += "</div>";
    _0x14_0xa13 += "</div>";
    _0x14_0xa13 += ">vid/<".split("").reverse().join("");
    $(".list-shop")['empty']()['append'](_0x14_0xa13);
}
function switchShopItem(e) {
    var _0x6826bf = (768052 ^ 768053) + (789831 ^ 789826);
    var _0xded1bg = $(e)['val']();
    _0x6826bf = (581051 ^ 581049) + (890653 ^ 890649);
    var _0xa_0x70a;
    var _0x95b1a = $(e)['parents'](".shop-item");
    _0xa_0x70a = (854801 ^ 854806) + (149521 ^ 149529);
    if (_0xded1bg == "1") {
        var _0xfb43d = (208017 ^ 208017) + (335073 ^ 335074);
        var unit = $(_0x95b1a)['attr']("tinu-lav-atad".split("").reverse().join(""));
        _0xfb43d = (280785 ^ 280790) + (288108 ^ 288111);
        var _0xb4996e = $(_0x95b1a)['attr']("mun-fed-lav-atad".split("").reverse().join(""));
        $(e)['parents'](".shop-v")['find']("h3")['empty']()['append']("\"=eulav \"txet\"=epyt tupni<".split("").reverse().join("") + _0xb4996e + ">naps<>/\"munylno\"=ssalc \"".split("").reverse().join("") + unit + "</span>");
        var _0x540d1g = (948209 ^ 948211) + (380975 ^ 380972);
        var pernum = $(_0x95b1a)['attr']("data-val-pernum");
        _0x540d1g = (378112 ^ 378119) + (699415 ^ 699423);
        var _0x65386d = $(_0x95b1a)['attr']("up-lav-atad".split("").reverse().join(""));
        var sum = cutXiaoNum(div(mul(_0x65386d, _0xb4996e), pernum), 306027 ^ 306025);
        $(e)['parents']("xob-meti-pohs.".split("").reverse().join(""))['find'](".total-num")['html']("<span>" + sum + "</span>元");
    } else {
        var _0x7g7fbb = (151162 ^ 151164) + (270535 ^ 270530);
        var _0x2bf0cf = $(_0x95b1a)['attr']("data-val-def-money");
        _0x7g7fbb = "fqqcco".split("").reverse().join("");
        var unit = $(_0x95b1a)['attr']("data-val-unit");
        var _0x6f797d = $(_0x95b1a)['attr']("pu-lav-atad".split("").reverse().join(""));
        var _0xc_0x5bd = (714431 ^ 714426) + (546213 ^ 546213);
        var pernum = $(_0x95b1a)['attr']("munrep-lav-atad".split("").reverse().join(""));
        _0xc_0x5bd = (862479 ^ 862471) + (876600 ^ 876592);
        var _0x249a = (545702 ^ 545698) + (194719 ^ 194719);
        var sum = parseInt(div(mul(add(_0x2bf0cf, 307023 ^ 307022), _0x6f797d), pernum));
        _0x249a = "dnlljg".split("").reverse().join("");
        $(e)['parents']("xob-meti-pohs.".split("").reverse().join(""))['find']("mun-latot.".split("").reverse().join(""))['html'](">naps<".split("").reverse().join("") + sum + "</span>" + unit);
        var _0x90b8b = cutXiaoNum(div(mul(sum, pernum), _0x6f797d), 599742 ^ 599740);
        $(e)['parents']("v-pohs.".split("").reverse().join(""))['find']("3h".split("").reverse().join(""))['empty']()['append']("<input type="text" value="" + _0x90b8b + "" class="onlynums"/><span>元</span>");
    }
}
var _0x18b6bb = (700503 ^ 700511) + (641937 ^ 641936);
var preShopItemPrice;
_0x18b6bb = (289698 ^ 289697) + (810579 ^ 810587);
function shopItemFocus(e) {
    var _0x71b = $(e)['parents'](".shop-item");
    var _0x194c = (272823 ^ 272831) + (700938 ^ 700942);
    var _0x1cf = $("_epytyub\"=eman[tupni".split("").reverse().join("") + $(_0x71b)['attr']("idx") + "dekcehc:]\"".split("").reverse().join(""))['val']();
    _0x194c = (458159 ^ 458153) + (865295 ^ 865292);
    if (_0x1cf == "2") {
        var _0xb3d = $(e)['val']();
        if (_0xb3d == '') {
            preShopItemPrice = 623695 ^ 623695;
        } else {
            preShopItemPrice = _0xb3d;
        }
    }
}
function compShopItem(e) {
    var _0xdafdeb;
    var _0x85ea = $(e)['parents'](".shop-item");
    _0xdafdeb = (569942 ^ 569936) + (507524 ^ 507533);
    var _0x35a = $("_epytyub\"=eman[tupni".split("").reverse().join("") + $(_0x85ea)['attr']("idx") + "dekcehc:]\"".split("").reverse().join(""))['val']();
    if (_0x35a == "1") {
        var _0x08512a = (745234 ^ 745233) + (125201 ^ 125206);
        var _0x9d99gc = $(e)['val']();
        _0x08512a = (980677 ^ 980676) + (857866 ^ 857865);
        if (_0x9d99gc == '') {
            _0x9d99gc = 291300 ^ 291300;
        }
        var _0x8989ba;
        var _0x49a3a = $(_0x85ea)['attr']("data-val-pu");
        _0x8989ba = (546643 ^ 546650) + (219309 ^ 219304);
        var pernum = $(_0x85ea)['attr']("data-val-pernum");
        var _0xc589a = (653060 ^ 653060) + (165676 ^ 165672);
        var sum = cutXiaoNum(div(mul(_0x49a3a, _0x9d99gc), pernum), 130911 ^ 130909);
        _0xc589a = 'cmkicj';
        $(e)['parents']("xob-meti-pohs.".split("").reverse().join(""))['find'](".total-num")['html']("<span>" + sum + "</span>元");
    }
    if (_0x35a == "2") {
        var _0xc3c = $(e)['val']();
        if (_0xc3c == '') {
            _0xc3c = 495463 ^ 495463;
        }
        if (_0xc3c == preShopItemPrice) {
            return;
        }
        var _0x957dca = (648031 ^ 648023) + (797520 ^ 797526);
        var _0x6cf9d = $(_0x85ea)['attr']("tinu-lav-atad".split("").reverse().join(""));
        _0x957dca = 494921 ^ 494924;
        var _0x38fc4d = $(_0x85ea)['attr']("data-val-up");
        var _0x3059g = (585529 ^ 585521) + (157960 ^ 157961);
        var pernum = $(_0x85ea)['attr']("data-val-pernum");
        _0x3059g = (942128 ^ 942134) + (707244 ^ 707244);
        var _0xaffa;
        var sum = parseInt(div(mul(_0xc3c, _0x38fc4d), pernum));
        _0xaffa = (131164 ^ 131165) + (465212 ^ 465208);
        $(e)['parents'](".shop-item-box")['find'](".total-num")['html']("<span>" + sum + ">naps/<".split("").reverse().join("") + _0x6cf9d);
        var _0x248f0f = cutXiaoNum(div(mul(sum, pernum), _0x38fc4d), 660040 ^ 660042);
        $(e)['parents']("v-pohs.".split("").reverse().join(""))['find']("h3 input")['val'](_0x248f0f);
        layer['msg']("商城需整数购买，已自动取整，请以实际价格为准！");
    }
}
function initMallGoodsImgHtml(goodsInfo) {
    if (gameId == "9655G".split("").reverse().join("") || gameId == "G21" || gameId == "6565G".split("").reverse().join("") || gameId == "G6211") {
        if (goodsInfo['camp'] == "盟联".split("").reverse().join("")) {
            return bucketDomain + "gnp.noci-ml/tsil/segami/1887/".split("").reverse().join("");
        }
        if (goodsInfo['camp'] == "落部".split("").reverse().join("")) {
            return bucketDomain + "/7881/images/list/buluo-icon.png";
        }
        return bucketDomain + "gnp.noci-zbzp/tsil/segami/1887/".split("").reverse().join("");
    }
    if (goodsInfo['tradePlace'] == "1") {
        return bucketDomain + "gnp.noci-ijuoy/tsil/segami/1887/".split("").reverse().join("");
    }
    if (goodsInfo['tradePlace'] == "2") {
        return bucketDomain + "/7881/images/list/paimai-icon.png";
    }
    if (goodsInfo['tradePlace'] == "3") {
        return bucketDomain + "/7881/images/list/face-icon.png";
    }
    if (goodsInfo['tradePlace'] == "4") {
        return bucketDomain + "/7881/images/list/fuben-icon.png";
    }
    if (goodsInfo['tradePlace'] == "5") {
        return bucketDomain + "gnp.noci-iuhgnog/tsil/segami/1887/".split("").reverse().join("");
    }
    return bucketDomain + "/7881/images/list/pzbz-icon.png";
}
function initMallGoodsTitle(goodsInfo) {
    if (goodsInfo['gameId'] == "G10") {
        if (goodsInfo['kqgroupName'] != null && goodsInfo['kqgroupName'] != '') {
            return "<span>" + goodsInfo['kqgroupName'] + "</span>";
        }
        return "<span>" + goodsInfo['groupName'] + "/" + goodsInfo['serverName'] + "</span>";
    }
    if (goodsInfo['gameId'] == "G5569" || goodsInfo['gameId'] == "G21" || goodsInfo['gameId'] == "G5656" || goodsInfo['gameId'] == "G6211") {
        var _0xf2b12d = (679399 ^ 679395) + (845465 ^ 845467);
        var titleHtml = ">naps<".split("").reverse().join("") + goodsInfo['groupName'] + "/" + goodsInfo['serverName'] + "</span>";
        _0xf2b12d = "ehpalf".split("").reverse().join("");
        if (goodsInfo['camp'] == "联盟") {
            titleHtml += "<em class="lmem">" + goodsInfo['camp'] + "</em>";
        }
        if (goodsInfo['camp'] == "部落") {
            titleHtml += ">\"melb\"=ssalc me<".split("").reverse().join("") + goodsInfo['camp'] + "</em>";
        }
        return titleHtml;
    }
    if (goodsInfo['gameId'] == "G5702" || goodsInfo['gameId'] == "G5729" || goodsInfo['gameId'] == "G5728" || goodsInfo['gameId'] == "G6211") {
        var _0x0a2db = (779521 ^ 779522) + (207624 ^ 207628);
        var titleHtml = "<span>" + goodsInfo['serverName'] + ">naps/<".split("").reverse().join("");
        _0x0a2db = 441493 ^ 441490;
        if (goodsInfo['camp'] == "盟联".split("").reverse().join("")) {
            titleHtml += ">\"meml\"=ssalc me<".split("").reverse().join("") + goodsInfo['camp'] + ">me/<".split("").reverse().join("");
        }
        if (goodsInfo['camp'] == "落部".split("").reverse().join("")) {
            titleHtml += "<em class="blem">" + goodsInfo['camp'] + "</em>";
        }
        return titleHtml;
    }
    return "<span>" + goodsInfo['groupName'] + "/" + goodsInfo['serverName'] + "</span>";
}
function initListPage(index, size, records) {
    var _0xag8c = (592536 ^ 592536) + (533598 ^ 533592);
    var _0x70b = "";
    _0xag8c = 'eojcne';
    _0x70b += "<span>" + size + "条/页</span>";
    _0x70b += "<span>共" + records + ">naps/<条".split("").reverse().join("");
    _0x70b += ">naps/<页>/\"\"=ssalc \"txet\"=epyt tupni<往前>naps<".split("").reverse().join("");
    _0x70b += "<a href="javascript:void(0)" class="gopage">确定</a>";
    $(".filter-list .list-bot .list-page")['empty']()['append'](_0x70b);
    var _0x09bdfa = "";
    _0x09bdfa += ">naps<".split("").reverse().join("") + size + "条/页</span><span>共" + records + "条</span>";
    $(".page-box .page-box-l")['empty']()['append'](_0x09bdfa);
    var _0x58422b = "";
    if ($("noitomorp#".split("").reverse().join(""))['val']() == "1") {
        _0x58422b = "tsil-noitomorp/".split("").reverse().join("");
    }
    var _0xae57f = size;
    var _0x26ff = records;
    var _0xbf8bb = (161392 ^ 161392) + (302516 ^ 302516);
    var _0xcg27d = Math['ceil'](_0x26ff / _0xae57f);
    _0xbf8bb = 'qbmdfl';
    var _0xa24ea = (530477 ^ 530478) + (164133 ^ 164132);
    var _0xe2713e = index;
    _0xa24ea = (414370 ^ 414370) + (563114 ^ 563114);
    laypage({
        "cont": "pages-box",
        'pages': _0xcg27d,
        "href": _0x58422b + "/" + gameId + "-" + gtId + "=muNegap?lmth.0-0-0-".split("").reverse().join(""),
        "curr": _0xe2713e,
        "skip": !![],
        "jump": function(obj, first) {
            var _0x2a_0x0e8 = (500069 ^ 500077) + (891150 ^ 891142);
            var _0x091eb = obj['curr'];
            _0x2a_0x0e8 = "mninbn".split("").reverse().join("");
            if (typeof first == "undefined") {
                pageNum = _0x091eb;
                doScrollTop = !![];
                queryGoodsMarket();
            }
        }
    });
}
function initMarketParam() {
    var _0xbd8g = new Object();
    _0xbd8g['marketRequestSource'] = "search";
    _0xbd8g['sellerType'] = "C";
    _0xbd8g['gameId'] = gameId;
    _0xbd8g['gtid'] = gtId;
    if (groupId != undefined && groupId != null && groupId != "0") {
        _0xbd8g['groupId'] = groupId;
    }
    if (serverId != undefined && serverId != null && serverId != "0") {
        _0xbd8g['serverId'] = serverId;
    }
    if (carrierId != undefined && carrierId != null && carrierId != "0") {
        _0xbd8g['carrierId'] = carrierId;
    }
    if (minPrice != undefined && minPrice != null) {
        _0xbd8g['minPrice'] = minPrice;
    }
    if (maxPrice != undefined && maxPrice != null) {
        _0xbd8g['maxPrice'] = maxPrice;
    }
    if (canBuyCnt != undefined && canBuyCnt != null) {
        _0xbd8g['canBuyCnt'] = canBuyCnt;
    }
    if (serviceId != undefined && serviceId != null) {
        _0xbd8g['serviceId'] = serviceId;
    }
    if (tradeType != undefined && tradeType != null) {
        _0xbd8g['tradeType'] = tradeType;
    }
    if (tradePlace != undefined && tradePlace != null) {
        _0xbd8g['tradePlace'] = tradePlace;
    }
    if (supportReport != undefined && supportReport != null) {
        _0xbd8g['supportReport'] = supportReport;
    }
    if (screenshotService != undefined && screenshotService != null) {
        _0xbd8g['screenshotService'] = screenshotService;
    }
    if (fiveStarSellerFlag != undefined && fiveStarSellerFlag != null) {
        _0xbd8g['fiveStarSellerFlag'] = fiveStarSellerFlag;
    }
    if (keyword != undefined && keyword != null && keyword != '') {
        _0xbd8g['keyWord'] = keyword;
    }
    if (tagValue != undefined && tagValue != null) {
        _0xbd8g['tagValue'] = tagValue;
    }
    if (goodsSortType != undefined && goodsSortType != null) {
        _0xbd8g['goodsSortType'] = goodsSortType;
    } else {
        _0xbd8g['goodsSortType'] = $(".filter-list")['find']("no. tob-tsil.".split("").reverse().join(""))['attr']("data-val");
    }
    var _0xc6974d = initExtAttrList();
    if (_0xc6974d != null) {
        _0xbd8g['extendAttrList'] = _0xc6974d;
    }
    _0xbd8g['pageNum'] = pageNum;
    _0xbd8g['pageSize'] = pageSize;
    return _0xbd8g;
}
function cancelSelectCond(dataVal) {
    if (dataVal == "reirrac-esolc".split("").reverse().join("")) {
        carrierId = "0";
        cleanGroupData(!![]);
        cleanServerData(!![]);
    }
    if (dataVal == "close-group") {
        groupId = "0";
        cleanKuaData();
        cleanServerData(!![]);
    }
    if (dataVal == "close-server") {
        serverId = "0";
        cleanKuaData();
    }
    if (dataVal == "ecivres-troppus-esolc".split("").reverse().join("")) {
        serviceId = null;
    }
    if (dataVal == "close-trade-type") {
        tradeType = null;
    }
    if (dataVal == "trec-laiciffo-esolc".split("").reverse().join("")) {
        supportReport = null;
    }
    if (dataVal == "close-screenshot-service") {
        screenshotService = null;
    }
    if (dataVal == "close-account-source") {
        fiveStarSellerFlag = null;
    }
    queryGoodsMarket("true");
}
function initExtAttrList() {
    var _0xeda = (548125 ^ 548117) + (550959 ^ 550956);
    var _0x01a0b = [];
    _0xeda = (135286 ^ 135295) + (137437 ^ 137434);
    $(".extattr-item")['find'](".filter-pop-box")['each'](function(index, e) {
        if ($(e)['hasClass']("yaw-fl".split("").reverse().join(""))) {
            $(e)['find']("retlif-gga.".split("").reverse().join(""))['each'](function(index, e) {
                var _0x3_0x3e5 = (842698 ^ 842691) + (967931 ^ 967922);
                var _0x6bf = parseElementAttrV2(e);
                _0x3_0x3e5 = (221748 ^ 221744) + (208921 ^ 208925);
                if (_0x6bf != null) {
                    $['merge'](_0x01a0b, _0x6bf);
                }
            });
        } else {
            var _0x78afbd = $(e)['attr']("epytretlif-lav-atad".split("").reverse().join(""));
            if (_0x78afbd == "2") {
                var _0x3b2a;
                var parseArr = parseElementAttr(e);
                _0x3b2a = 'olenkk';
                $['merge'](_0x01a0b, parseArr);
            }
            if (_0x78afbd == "3") {
                $(e)['find'](".agg-filter")['each'](function(index, e) {
                    var _0xd2_0x619 = parseElementAttr(e);
                    $['merge'](_0x01a0b, _0xd2_0x619);
                });
            }
        }
    });
    return _0x01a0b;
}
function parseElementAttrV2(e) {
    var _0x67392b = [];
    var _0x9gg = $(e)['find'](".single-chose");
    if (_0x9gg['length'] > (722139 ^ 722139)) {
        var eid = $(e)['attr']("data-val-eid");
        var _0x5caa5b;
        var ev = null;
        _0x5caa5b = "piofhi".split("").reverse().join("");
        _0x9gg['find'](".pop-chose-item")['each'](function(index, item) {
            if ($(item)['hasClass']("on")) {
                ev = $(item)['attr']("eulav-atad".split("").reverse().join(""));
                return false;
            }
        });
        if (ev != null && ev != '') {
            var _0xga_0x5ga = (308461 ^ 308463) + (935844 ^ 935846);
            var extAttrObj = new Object();
            _0xga_0x5ga = (959571 ^ 959573) + (419727 ^ 419726);
            extAttrObj['eid'] = eid;
            extAttrObj['ev'] = ev;
            _0x67392b['push'](extAttrObj);
        }
    }
    var _0xef_0x7d1 = (615388 ^ 615385) + (271305 ^ 271310);
    var _0xe5dafa = $(e)['find'](".more-chose");
    _0xef_0x7d1 = 'nmbnjl';
    if (_0xe5dafa['length'] > (806844 ^ 806844)) {
        var eid = $(e)['attr']("data-val-eid");
        var _0xagdfe;
        var _0xdf55g = [];
        _0xagdfe = 'bbihbl';
        var _0x318d = (232766 ^ 232767) + (665952 ^ 665956);
        var selectOption = "0";
        _0x318d = 680208 ^ 680214;
        var _0x5a6a;
        var minCnt;
        _0x5a6a = 713559 ^ 713566;
        _0xe5dafa['find'](".pop-chose-item")['each'](function(index, item) {
            if ($(item)['hasClass']("moreon")) {
                var _0x8fd3aa = (287914 ^ 287919) + (463307 ^ 463309);
                let _0x78465f = $(item)['attr']("data-value");
                _0x8fd3aa = "hhjkek".split("").reverse().join("");
                _0xdf55g['push'](_0x78465f);
            }
        });
        var selType = $(e)['find'](".filter-pop-head")['find']("epyt-fles.".split("").reverse().join(""))['find']("ul .on");
        if (selType['length'] > (660961 ^ 660961)) {
            var matchType = $(selType)['attr']("lav-atad".split("").reverse().join(""));
            if (matchType == "1") {
                selectOption = "1";
            }
            if (matchType == "2") {
                selectOption = "2";
                minCnt = $(e)['find'](".filter-pop-head .self-type .min-cnt")['val']();
            }
        }
        if (_0xdf55g['length'] > (671023 ^ 671023)) {
            var _0x3994ad = (965863 ^ 965858) + (519595 ^ 519587);
            var extAttrObj = new Object();
            _0x3994ad = 274882 ^ 274887;
            extAttrObj['eid'] = eid;
            extAttrObj['evs'] = _0xdf55g;
            extAttrObj['selectOption'] = selectOption;
            extAttrObj['minCnt'] = minCnt;
            _0x67392b['push'](extAttrObj);
        }
    }
    var _0x0agad;
    var _0xf73bf = $(e)['find'](".lf-check-edit");
    _0x0agad = (580478 ^ 580471) + (213101 ^ 213100);
    if (_0xf73bf['length'] > (519986 ^ 519986)) {
        var eid = _0xf73bf['attr']("attr-eid");
        var _0x3a1afa = _0xf73bf['attr']("attr-peid");
        var selectOption = "0";
        var _0xbcedb = (733714 ^ 733714) + (681897 ^ 681901);
        var minCnt;
        _0xbcedb = (944161 ^ 944166) + (902780 ^ 902783);
        var _0x16c3e = (203931 ^ 203923) + (727041 ^ 727046);
        var _0x41fd7e = [];
        _0x16c3e = 'jcccbk';
        var _0x5ea86b = (927070 ^ 927071) + (444002 ^ 444007);
        var _0x3f7g = _0xf73bf['parents'](".agg-filter");
        _0x5ea86b = 921417 ^ 921422;
        var _0x66ae3c = (930936 ^ 930938) + (387458 ^ 387460);
        var selType = _0x3f7g['find'](".filter-pop-head")['find'](".self-type")['find']("ul .on");
        _0x66ae3c = "cngmhc".split("").reverse().join("");
        if (selType['length'] > (310089 ^ 310089)) {
            var _0xa2_0x75a = (576648 ^ 576648) + (703607 ^ 703604);
            var matchType = $(selType)['attr']("lav-atad".split("").reverse().join(""));
            _0xa2_0x75a = 'mjdopm';
            if (matchType == "1") {
                selectOption = "1";
            }
            if (matchType == "2") {
                selectOption = "2";
                minCnt = $(e)['find']("tnc-nim. epyt-fles. daeh-pop-retlif.".split("").reverse().join(""))['val']();
            }
        }
        _0xf73bf['find'](".check-item")['each'](function(index, item) {
            let _0xfc37g = $(item)['find']("p")['text']();
            if (_0xfc37g['indexOf']("X") != -(164582 ^ 164583)) {
                let _0x1caebc = $(item)['find']("input")['val']();
                if (_0x1caebc != undefined && _0x1caebc != null && _0x1caebc != '') {
                    var _0xc6a52b;
                    var rangeFilterObj = new Object();
                    _0xc6a52b = (780263 ^ 780256) + (598229 ^ 598224);
                    rangeFilterObj['pid'] = _0x3a1afa;
                    rangeFilterObj['pval'] = _0xfc37g;
                    rangeFilterObj['inputEv'] = _0x1caebc;
                    _0x41fd7e['push'](rangeFilterObj);
                }
            } else {
                var rangeFilterObj = new Object();
                rangeFilterObj['pid'] = _0x3a1afa;
                rangeFilterObj['pval'] = _0xfc37g;
                rangeFilterObj['inputEv'] = _0xfc37g;
                _0x41fd7e['push'](rangeFilterObj);
            }
        });
        if (_0x41fd7e['length'] > (421257 ^ 421257)) {
            var extAttrObj = new Object();
            extAttrObj['eid'] = eid;
            extAttrObj['rangeFilterList'] = _0x41fd7e;
            extAttrObj['selectOption'] = selectOption;
            extAttrObj['minCnt'] = minCnt;
            _0x67392b['push'](extAttrObj);
        }
    }
    return _0x67392b;
}
function parseElementAttr(e) {
    var _0x72a63c = (958776 ^ 958778) + (265746 ^ 265755);
    var _0x5c8a1c = [];
    _0x72a63c = 'digcpo';
    var _0x8e1db = $(e)['attr']("data-val-eid");
    var _0xbbad = [];
    var _0xgc424f;
    var _0x592e;
    var _0xbea9c = [];
    _0x592e = 'pekmde';
    var _0xe7125d = [];
    var _0x1bd = (916387 ^ 916388) + (389901 ^ 389903);
    var _0x59273b = $(e)['attr']("data-sub-multiple");
    _0x1bd = (642213 ^ 642209) + (102432 ^ 102438);
    $(e)['find']("meti-esohc-pop. esohc-elgnis.".split("").reverse().join(""))['each'](function(index, mainAttrE) {
        if ($(mainAttrE)['hasClass']("no".split("").reverse().join(""))) {
            var _0xa55a = (749326 ^ 749318) + (426982 ^ 426982);
            let _0x425cga = $(mainAttrE)['attr']("eulav-atad".split("").reverse().join(""));
            _0xa55a = 'jfkmfb';
            if (_0x425cga != null && _0x425cga != '' && _0x425cga != undefined && _0x425cga != "undefined") {
                _0xbbad['push'](_0x425cga);
            }
            if ($(mainAttrE)['find']("nerdlihc-meti.".split("").reverse().join(""))['length'] > (924134 ^ 924134)) {
                let _0xc7fccd = '';
                _0xgc424f = $(mainAttrE)['find'](".item-children")['attr']("data-val-subeid");
                $(mainAttrE)['find'](".item-children .children-head .on")['each'](function(index, subAttrE) {
                    let _0xeff98f = $(subAttrE)['attr']("eulav-atad".split("").reverse().join(""));
                    if (_0xeff98f != null && _0xeff98f != '' && _0xeff98f != undefined && _0xeff98f != "denifednu".split("").reverse().join("")) {
                        _0xbea9c['push'](_0xeff98f);
                        _0xc7fccd += (_0xc7fccd['length'] > (738029 ^ 738029) ? "," : '') + _0xeff98f;
                    }
                });
                if (_0xc7fccd['length'] > (996887 ^ 996887)) {
                    _0xe7125d['push'](_0xc7fccd);
                }
            }
        }
    });
    $(e)['find']("meti-esohc-pop. esohc-erom.".split("").reverse().join(""))['each'](function(index, mainAttrE) {
        if ($(mainAttrE)['hasClass']("moreon")) {
            let _0xb333ca = $(mainAttrE)['attr']("data-value");
            if (_0xb333ca != null && _0xb333ca != '' && _0xb333ca != undefined && _0xb333ca != "denifednu".split("").reverse().join("")) {
                _0xbbad['push'](_0xb333ca);
            }
            if ($(mainAttrE)['find'](".item-children")['length'] > (993681 ^ 993681)) {
                var _0x6dgaaa = (629314 ^ 629317) + (812074 ^ 812073);
                let _0xe2671b = '';
                _0x6dgaaa = 195293 ^ 195293;
                _0xgc424f = $(mainAttrE)['find'](".item-children")['attr']("diebus-lav-atad".split("").reverse().join(""));
                $(mainAttrE)['find']("no. daeh-nerdlihc. nerdlihc-meti.".split("").reverse().join(""))['each'](function(index, subAttrE) {
                    var _0x19c2ee = (278867 ^ 278867) + (615003 ^ 615003);
                    let _0x17_0x81c = $(subAttrE)['attr']("data-value");
                    _0x19c2ee = 706113 ^ 706119;
                    if (_0x17_0x81c != null && _0x17_0x81c != '' && _0x17_0x81c != undefined && _0x17_0x81c != "denifednu".split("").reverse().join("")) {
                        _0xbea9c['push'](_0x17_0x81c);
                        _0xe2671b += (_0xe2671b['length'] > (614343 ^ 614343) ? "," : '') + _0x17_0x81c;
                    }
                });
                if (_0xe2671b['length'] > (160798 ^ 160798)) {
                    _0xe7125d['push'](_0xe2671b);
                }
            }
        }
    });
    if (_0xbbad['length'] > (436525 ^ 436525)) {
        var _0xbf572a = (833019 ^ 833011) + (251601 ^ 251605);
        var _0xeeaa = "0";
        _0xbf572a = 582013 ^ 582013;
        var _0x4ad22f = 201853 ^ 201852;
        var _0xde151g = $(e)['find'](".filter-pop-head")['attr']("data-filter-or");
        if (_0xde151g == "true") {
            _0xeeaa = "2";
        } else {
            var _0xfef95e = $(e)['find']("daeh-pop-retlif.".split("").reverse().join(""))['find'](".self-type")['find']("no. lu".split("").reverse().join(""));
            if (_0xfef95e['length'] > (446125 ^ 446125)) {
                var _0xagc8a;
                var _0x326a = $(_0xfef95e)['attr']("data-val");
                _0xagc8a = (322442 ^ 322441) + (872056 ^ 872058);
                if (_0x326a == "1") {
                    _0xeeaa = "1";
                }
                if (_0x326a == "2") {
                    _0xeeaa = "2";
                    _0x4ad22f = $(e)['find'](".filter-pop-head .self-type .min-cnt")['val']();
                }
            }
        }
        var _0xcfe05a = new Object();
        _0xcfe05a['eid'] = _0x8e1db;
        _0xcfe05a['evs'] = _0xbbad;
        _0xcfe05a['selectOption'] = _0xeeaa;
        if (_0xeeaa == "2") {
            _0xcfe05a['minCnt'] = _0x4ad22f;
        }
        _0x5c8a1c['push'](_0xcfe05a);
        if (_0xgc424f != undefined && _0xbea9c['length'] > (440024 ^ 440024)) {
            var _0xbb_0x170 = (149676 ^ 149673) + (625150 ^ 625149);
            var _0xbe_0x0e7 = new Object();
            _0xbb_0x170 = 629172 ^ 629174;
            _0xbe_0x0e7['eid'] = _0xgc424f;
            _0xbe_0x0e7['evs'] = _0xbea9c;
            _0xbe_0x0e7['selectOption'] = "2";
            if (_0xcfe05a['selectOption'] == "1" && _0x59273b == "1") {
                _0xbe_0x0e7['minCnt'] = _0xbea9c['length'];
            } else if (_0xcfe05a['selectOption'] == "1" && _0x59273b != "1") {
                _0xbe_0x0e7['minCnt'] = _0xbbad['length'];
            } else if (_0xcfe05a['selectOption'] == "2") {
                _0xbe_0x0e7['minCnt'] = _0xcfe05a['minCnt'];
                _0xbe_0x0e7['evGroupList'] = _0xe7125d;
            } else {
                _0xbe_0x0e7['minCnt'] = "1";
            }
            _0x5c8a1c['push'](_0xbe_0x0e7);
        }
    }
    $(e)['find']("tupni-egnar.".split("").reverse().join(""))['each'](function(index, mainAttrE) {
        var _0x16_0xd11 = $(mainAttrE)['find']("lav-nim.".split("").reverse().join(""))['val']();
        var _0xe6e4cg = (654845 ^ 654846) + (238043 ^ 238035);
        var _0x3ac29e = $(mainAttrE)['find'](".max-val")['val']();
        _0xe6e4cg = (532837 ^ 532837) + (171781 ^ 171779);
        if (_0x16_0xd11 != null && _0x16_0xd11 != '' || _0x3ac29e != null && _0x3ac29e != '') {
            if (_0x16_0xd11 == null || _0x16_0xd11 == '') {
                _0x16_0xd11 = 189173 ^ 189173;
            }
            if (_0x3ac29e == null || _0x3ac29e == '') {
                _0x3ac29e = 999999;
            }
            var _0x2feb9d = (574173 ^ 574175) + (421245 ^ 421243);
            var _0xe2_0xfe0 = new Object();
            _0x2feb9d = (502001 ^ 502001) + (663221 ^ 663218);
            _0xe2_0xfe0['eid'] = _0x8e1db;
            _0xe2_0xfe0['ev'] = _0x16_0xd11 + "ы" + _0x3ac29e;
            _0x5c8a1c['push'](_0xe2_0xfe0);
        }
    });
    return _0x5c8a1c;
}
function filterExtAttrKeys(e) {
    var _0x0g683a = getPyKeyWord($(e)['parent']()['find']("drowyek.".split("").reverse().join(""))['val']()['trim']());
    var _0xb4d7ab = (744953 ^ 744955) + (215924 ^ 215932);
    var _0x36881c = _0x0g683a['hz_txt'];
    _0xb4d7ab = (232364 ^ 232363) + (830859 ^ 830858);
    if (_0x0g683a['type'] == "py") {
        _0x36881c = _0x0g683a['py_txt'];
    }
    if (_0x36881c == '') {
        $(e)['parent']()['parent']()['parent']()['parent']()['parent']()['find'](".filter-pop-bottom .pop-chose-item")['each'](function(index, mainAttrE) {
            $(mainAttrE)['show']();
        });
        return;
    }
    var _0xfb2f3a = $(e)['parent']()['attr']("syek-retlif-atad".split("").reverse().join(""));
    var _0x38b = JSON['parse'](_0xfb2f3a);
    if (_0x38b['length'] == (645053 ^ 645053)) {
        return;
    }
    var _0x8a4ffc = (164542 ^ 164542) + (747625 ^ 747617);
    var _0x75g = [];
    _0x8a4ffc = 429520 ^ 429525;
    for (var i = 524822 ^ 524822; i < _0x38b['length']; i++) {
        var _0xbeeba = (818019 ^ 818020) + (653879 ^ 653875);
        var _0x8g68e = _0x38b[i];
        _0xbeeba = (925449 ^ 925440) + (759299 ^ 759297);
        var _0xf3d = _0x8g68e['searchKeyList'];
        if (_0xf3d['length'] > (300851 ^ 300851)) {
            for (var j = 306937 ^ 306937; j < _0xf3d['length']; j++) {
                var _0xec4fb = _0xf3d[j];
                if (_0x0g683a['type'] == "py") {
                    _0xec4fb = getPyKeyWord(_0xf3d[j])['py_txt'];
                }
                if (_0xec4fb['includes'](_0x36881c)) {
                    _0x75g['push'](_0x8g68e['attrVal']);
                }
            }
        }
    }
    if (_0x75g['length'] == (173006 ^ 173006)) {
        $(e)['parent']()['parent']()['parent']()['parent']()['parent']()['find']("meti-esohc-pop. mottob-pop-retlif.".split("").reverse().join(""))['each'](function(index, mainAttrE) {
            $(mainAttrE)['hide']();
        });
        return;
    }
    $(e)['parent']()['parent']()['parent']()['parent']()['parent']()['find']("meti-esohc-pop. mottob-pop-retlif.".split("").reverse().join(""))['each'](function(index, mainAttrE) {
        var _0x1fa = $(mainAttrE)['attr']("eulav-atad".split("").reverse().join(""));
        var _0xfb9f = (622986 ^ 622988) + (387578 ^ 387576);
        var _0xa8f67b = $['inArray'](_0x1fa, _0x75g);
        _0xfb9f = 'egjcgh';
        if (_0xa8f67b != -(139442 ^ 139443)) {
            $(mainAttrE)['show']();
        } else {
            $(mainAttrE)['hide']();
        }
    });
}
function collectionGoods(event) {
    if (currentUserId == "no-login") {
        layer['msg']("请先登录！");
        return;
    }
    var _0x2gb03c = (265588 ^ 265589) + (853900 ^ 853897);
    var _0x2fec = $(event)['attr']("data-val-gid");
    _0x2gb03c = 'falnlg';
    var _0x0c2f;
    var _0xaefc = JSON['stringify']({
        "goodsId": _0x2fec,
        "channel": 12
    });
    _0x0c2f = (345005 ^ 345000) + (704698 ^ 704696);
    $['ajax']({
        'url': addGoodsCollUrl,
        "async": false,
        'type': "POST",
        "data": _0xaefc,
        'dataType': "json",
        'contentType': "application/json",
        'xhrFields': {
            "withCredentials": !![]
        },
        'success': function(result) {
            if (result['code'] == (640355 ^ 640355) || result['code'] == 170003) {
                colGoodsArr['push'](_0x2fec);
                $(event)['attr']("class", "has-coll");
                $(event)['empty']()['append']("\"=crs gmi<".split("").reverse().join("") + bucketDomain + "/7881/images/list-2024/has-collet.png" width="19" />取消收藏");
                if (result['code'] == (585705 ^ 585705)) {
                    var _0x4gf27b;
                    var _0xb523dd = $("tcelloc-ym.".split("").reverse().join(""))['find']("a")['text']();
                    _0x4gf27b = 265709 ^ 265701;
                    var _0xc612db = parseInt(_0xb523dd) + (779097 ^ 779096);
                    $(".my-collect")['find']("a")['text'](_0xc612db);
                }
            } else {
                layer['msg'](result['msg']);
            }
        }
    });
    console['log'](colGoodsArr);
}
function cancelCollectionGoods(event) {
    if (currentUserId == "no-login") {
        layer['msg']("请先登录！");
        return;
    }
    var _0xec_0x27d = (176827 ^ 176829) + (316473 ^ 316472);
    var _0xa7ad = $(event)['attr']("data-val-gid");
    _0xec_0x27d = 413526 ^ 413524;
    $['ajax']({
        "url": delGoodsColUrl + "=dIsdoog?".split("").reverse().join("") + _0xa7ad,
        'async': false,
        'type': "POST",
        "dataType": "json",
        "contentType": "application/json",
        "xhrFields": {
            'withCredentials': !![]
        },
        'success': function(result) {
            if (result['code'] == (609608 ^ 609608)) {
                if (colGoodsArr['length'] > (807711 ^ 807711)) {
                    $['each'](colGoodsArr, function(index, item) {
                        if (item == _0xa7ad) {
                            colGoodsArr['splice'](index, 570159 ^ 570158);
                        }
                    });
                }
                $(event)['attr']("class", "no-coll");
                $(event)['empty']()['append']("<img src="" + bucketDomain + "/7881/images/list-2024/no-collet.png" width="19" />收藏商品");
                var _0xeaeb = (485591 ^ 485599) + (316342 ^ 316351);
                var _0x56ca = $(".my-collect")['find']("a")['text']();
                _0xeaeb = 'jmkean';
                var _0xd1c1ea;
                var _0xc662d = parseInt(_0x56ca) - (170964 ^ 170965);
                _0xd1c1ea = 'hbnpod';
                if (_0xc662d < (308270 ^ 308270)) {
                    _0xc662d = 179473 ^ 179473;
                }
                $(".my-collect")['find']("a")['text'](_0xc662d);
            } else {
                layer['msg'](result['msg']);
            }
        }
    });
    console['log'](colGoodsArr);
}
function openIm(goodsId, utp) {
    if (typeof doCheckBuying != "undefined" && $['isFunction'](doCheckBuying)) {
        if (!doCheckBuying()) {
            return false;
        }
    }
    if (utp != null && utp != '' && utp != "llun".split("").reverse().join("")) {
        $['ajax']({
            'url': "=dIsdoog?eikooCptUdda/".split("").reverse().join("") + goodsId + "&utp=" + utp,
            "type": "GET",
            'async': false,
            'dataType': "json",
            'success': function(result) {}
        });
    }
    if (currentUserId == "nigol-on".split("").reverse().join("")) {
        var _0x86d;
        var _0x01cf9c = loginUrl + "?redirect=" + goodsDetailsDomain + "/receipt/redirectIm?goodsId=" + goodsId;
        _0x86d = 'gefkcc';
        window['location']['href'] = decodeURIComponent(_0x01cf9c);
        return;
    }
    if (imDomain == null || imDomain == '') {
        imDomain = "//im.7881.com";
    }
    $['ajax']({
        "url": sendPresaleConv + "?goodsId=" + goodsId,
        'type': "GET",
        'dataType': "json",
        'async': false,
        'xhrFields': {
            'withCredentials': !![]
        },
        'success': function(data) {
            if (data['code'] == (613567 ^ 613567) && data['body'] != undefined) {
                var _0x1g8d = data['body']['convId'];
                window['open'](imDomain + "/pre-sale?tag=presale&convId=" + _0x1g8d);
            } else if (data['code'] == (620896 ^ 613892)) {
                realNamePop();
            } else {
                layer['msg']("天聊前售持支不暂品商该".split("").reverse().join(""));
                location['reload']();
            }
        }
    });
}
function openGoodsDetailPage(goodsId, utp) {
    if (utp != null && utp != '' && utp != "null") {
        $['ajax']({
            'url': "/addUtpCookie?goodsId=" + goodsId + "=ptu&".split("").reverse().join("") + utp,
            'type': "GET",
            'async': false,
            'dataType': "json",
            "success": function(result) {}
        });
    }
    var _0x4969be = (758736 ^ 758742) + (516156 ^ 516153);
    var _0x2c9ae = "//search.7881.com/" + goodsId + ".html";
    _0x4969be = 468301 ^ 468303;
    window['open'](_0x2c9ae);
}
function initMarketSHtml_ACCOUNT(paramObj, goodsList) {
    var _0x7e37f;
    var _0x446f9g = initRecommendGoods(paramObj);
    _0x7e37f = 517005 ^ 517006;
    var _0xa35df = "";
    var _0x3egb;
    var _0xge63da = getUserListView();
    _0x3egb = 880028 ^ 880025;
    for (var i = 389928 ^ 389928; i < goodsList['length']; i++) {
        if (_0x446f9g['length'] > (537698 ^ 537698)) {
            for (var j = 442599 ^ 442599; j < _0x446f9g['length']; j++) {
                var _0xe2fa = _0x446f9g[j];
                if (_0xe2fa['position'] == i + (172004 ^ 172005)) {
                    var _0xdcge1b;
                    var _0xa66dc = _0xe2fa['goodsInfoList'];
                    _0xdcge1b = 'ipkmol';
                    if (_0xa66dc['length'] > (893834 ^ 893834)) {
                        var _0x7d_0xfc9 = (465176 ^ 465179) + (254439 ^ 254447);
                        var _0xa4d8fa = new Object();
                        _0x7d_0xfc9 = (985216 ^ 985219) + (344689 ^ 344691);
                        _0xa4d8fa['cancelCompensationFlag'] = _0xe2fa['cancelCompensationFlag'];
                        _0xa4d8fa['cancelCompensationDesc'] = _0xe2fa['cancelCompensationDesc'];
                        if (_0xge63da == "1") {
                            _0xa35df += "<div class="no-class">";
                        }
                        for (var k = 833204 ^ 833204; k < _0xa66dc['length']; k++) {
                            if (_0xge63da == "1") {
                                var _0x8eada = (288554 ^ 288552) + (382430 ^ 382430);
                                var goodsHtml = initGoodsHtml_ACCOUNT_V2(_0xa66dc[k], "dnemmocer".split("").reverse().join(""), _0xa4d8fa);
                                _0x8eada = 723342 ^ 723334;
                            } else {
                                var _0x4_0x4ac;
                                var goodsHtml = initGoodsHtml_ACCOUNT(_0xa66dc[k], "dnemmocer".split("").reverse().join(""), _0xa4d8fa);
                                _0x4_0x4ac = 'obpoen';
                            }
                            _0xa35df += goodsHtml;
                        }
                        if (_0xge63da == "1") {
                            _0xa35df += ">vid/<".split("").reverse().join("");
                        }
                    }
                }
            }
        }
        var _0x49151e = goodsList[i];
        if (_0xge63da == "1") {
            var goodsHtml = initGoodsHtml_ACCOUNT_V2(_0x49151e, "common", null);
        } else {
            var goodsHtml = initGoodsHtml_ACCOUNT(_0x49151e, "common", null);
        }
        _0xa35df += goodsHtml;
    }
    initListViewStyle(_0xge63da);
    $("gnidaol-tsil.".split("").reverse().join(""))['hide']();
    $("xob-tsil.".split("").reverse().join(""))['empty']()['append'](_0xa35df);
}
function switchListView(viewType) {
    if (viewType == null) {
        var _0xe7cdc;
        var _0x2c818d = getUserListView();
        _0xe7cdc = "fdggpq".split("").reverse().join("");
        if (_0x2c818d == "0") {
            viewType = "1";
        } else {
            viewType = "0";
        }
        if (currentUserId == "nigol-on".split("").reverse().join("")) {
            $['cookie']("USERLISTVIEWTYPE", viewType, {
                'expires': 365
            });
            location['reload']();
            return;
        }
    }
    $['ajax']({
        "url": addUserListView + "?viewType=" + viewType + "&gameId=" + gameId,
        'type': "GET",
        'async': false,
        'dataType': "json",
        "xhrFields": {
            'withCredentials': !![]
        },
        'success': function(result) {
            if (result['code'] == (922785 ^ 922785)) {
                $['cookie']("EPYTWEIVTSILRESU".split("").reverse().join(""), viewType, {
                    'expires': 365
                });
                location['reload']();
            } else {
                layer['msg'](result['msg']);
            }
        }
    });
}
function getUserListView() {
    if (gtId != "100003") {
        return;
    }
    var _0x9be = $['cookie']("EPYTWEIVTSILRESU".split("").reverse().join(""));
    if (_0x9be != null) {
        return _0x9be;
    }
    $['ajax']({
        "url": queryUserListView + "?gameId=" + gameId,
        "async": false,
        'type': "GET",
        "dataType": "json",
        'xhrFields': {
            'withCredentials': !![]
        },
        "success": function(result) {
            if (result['code'] == (406876 ^ 406876) && result['body'] != undefined) {
                _0x9be = result['body'];
                $['cookie']("EPYTWEIVTSILRESU".split("").reverse().join(""), _0x9be, {
                    'expires': 365
                });
            }
        }
    });
    return _0x9be;
}
function getViewTemplate() {
    var _0x5616f = null;
    if (typeof listTemplate != "undefined") {
        if (listTemplate == "list_account") {
            _0x5616f = "1";
        } else if (listTemplate == "bz_tsil".split("").reverse().join("")) {
            _0x5616f = "2";
        }
    }
    return _0x5616f;
}
function initShowGuideViewModel() {
    if (currentUserId == "nigol-on".split("").reverse().join("")) {
        return "2";
    }
    var _0x5ff = (924514 ^ 924514) + (326556 ^ 326559);
    var _0x45e = $['cookie']("piTediuGwohSsI".split("").reverse().join(""));
    _0x5ff = (873793 ^ 873793) + (496981 ^ 496976);
    if (_0x45e != undefined && _0x45e != '') {
        return _0x45e;
    }
    var _0xf2071a = "";
    $['ajax']({
        "url": addUserListViewInfo,
        "type": "GET",
        'dataType': "json",
        'async': false,
        'xhrFields': {
            "withCredentials": !![]
        },
        'success': function(result) {
            if (result['code'] == (323257 ^ 323257) && result['body'] != undefined) {
                _0xf2071a = result['body'];
            }
        }
    });
    return _0xf2071a;
}
function initGoodsHtml_ACCOUNT(goodsInfo, goodsKind, recommendExtObj) {
    var _0x7c7ac = '';
    if (goodsKind == "recommend") {
        _0x7c7ac = "100.102";
    } else if (goodsInfo['sortKind'] == "2") {
        _0x7c7ac = "101.001".split("").reverse().join("");
    }
    var _0x41bf = "";
    if (qualityRecommendConfigureType == !![] && goodsKind == "recommend") {
        if (recommendExtObj['cancelCompensationFlag'] == !![]) {
            _0x41bf += ">\"dcsah sdoog-tseb meti-tsil\"=ssalc vid<".split("").reverse().join("");
        } else {
            _0x41bf += ">\"sdoog-tseb meti-tsil\"=ssalc vid<".split("").reverse().join("");
        }
    } else {
        _0x41bf += "<div class="list-item">";
    }
    if (goodsKind == "recommend") {
        if (qualityRecommendConfigureType == !![]) {
            if (recommendExtObj['cancelCompensationFlag'] == !![]) {
                _0x41bf += "<div class="pztj-best"><p><i>" + recommendExtObj['cancelCompensationDesc'] + ">vid/<>p/<>i/<".split("").reverse().join("");
            } else {
                _0x41bf += "<div class="pztj-best"></div>";
            }
        } else {
            _0x41bf += ">\"xob-jsxy\"=ssalc vid<".split("").reverse().join("");
            _0x41bf += ">\"tfel-jsxy\"=ssalc vid<".split("").reverse().join("");
            _0x41bf += "\"=crs gmi<".split("").reverse().join("") + bucketDomain + "/7881/images/list-2024/yxsj-icon.png" width="54" class="yxsj-icon" />";
            _0x41bf += "<img src="" + bucketDomain + ">/ \"eltit-jsxy\"=ssalc \"021\"=htdiw \"gnp.eltit-jsxy/4202-tsil/segami/1887/".split("").reverse().join("");
            _0x41bf += ">vid/<".split("").reverse().join("");
            _0x41bf += "<div class="yxsj-right">";
            _0x41bf += "<p><img src="" + bucketDomain + "/7881/images/list-2024/ksjy-icon.png" width="64"/></p>";
            _0x41bf += "<p><img src="" + bucketDomain + ">p/<>/\"46\"=htdiw \"gnp.noci-pszy/4202-tsil/segami/1887/".split("").reverse().join("");
            if (recommendExtObj['cancelCompensationFlag']) {
                _0x41bf += "<p>";
                _0x41bf += "<img src="" + bucketDomain + "/7881/images/list-2024/cdpf-icon.png" width="64"/>";
                _0x41bf += "<img src="" + bucketDomain + "/7881/images/list-2024/wenhao-icon.png" width="12"/>";
                _0x41bf += ">i<".split("").reverse().join("") + recommendExtObj['cancelCompensationDesc'] + ">i/<".split("").reverse().join("");
                _0x41bf += "</p>";
            }
            _0x41bf += "</div>";
            _0x41bf += ">vid/<".split("").reverse().join("");
        }
    }
    _0x41bf += "<div class="list-left">";
    _0x41bf += "<div class="list-pic" data-val-goodsid="" + goodsInfo['goodsId'] + "\"=diemag-lav-atad \"".split("").reverse().join("") + goodsInfo['gameId'] + "" data-val-gtid="" + goodsInfo['gtid'] + "">";
    _0x41bf += "<img src="" + goodsInfo['defaultImg'] + ""/>";
    _0x41bf += ">\"mun-cip\"=ssalc vid<".split("").reverse().join("") + (goodsInfo['imgCount'] && goodsInfo['imgCount'] > (445888 ^ 445888) ? goodsInfo['imgCount'] : "无") + ">vid/<图".split("").reverse().join("");
    _0x41bf += "</div>";
    if (goodsInfo['sortKind'] == "2") {
        _0x41bf += "\"=crs gmi<".split("").reverse().join("") + bucketDomain + "/7881/images/list-2024/recommed-account.png" width="120" class="recommed-icon"/>";
    }
    _0x41bf += "</div>";
    _0x41bf += "<div class="list-right">";
    _0x41bf += "<h3 class="title" data-title="" + escapeHTML(goodsInfo['title']) + "'(egaPliateDsdooGnepo :tpircsavaj\"=ferh a<>\"".split("").reverse().join("") + goodsInfo['goodsId'] + "', '" + _0x7c7ac + ">\";)'".split("").reverse().join("") + escapeHTML(goodsInfo['title']) + ">3h/<>a/<".split("").reverse().join("");
    _0x41bf += "<div class="tags-box">";
    _0x41bf += "<div class="tag-item">" + initTags(goodsInfo) + ">vid/<".split("").reverse().join("");
    if (goodsInfo['onlineText'] != null && goodsInfo['onlineText'] != '') {
        if (goodsInfo['onlineText'] == "卖家在线") {
            _0x41bf += "<p class="sell-online">" + goodsInfo['onlineText'] + "</p>";
        } else {
            _0x41bf += "<p class="sell-offline">" + goodsInfo['onlineText'] + ">p/<".split("").reverse().join("");
        }
    }
    _0x41bf += ">vid/<".split("").reverse().join("");
    _0x41bf += ">\"ecirp-revres\"=ssalc vid<".split("").reverse().join("");
    _0x41bf += ">\"xob-revres\"=ssalc vid<".split("").reverse().join("");
    _0x41bf += "<p>";
    _0x41bf += "游戏区服：" + initListQFInfo(goodsInfo);
    if (goodsInfo['kqgroupName'] != null && goodsInfo['kqgroupName'] != '') {
        _0x41bf += "<span class="hutongtip" data-val-kqid="" + goodsInfo['kqid'] + ""><img src="" + bucketDomain + "/7881/images/list-2024/hutong.png"/></span>";
    }
    _0x41bf += "</p>";
    _0x41bf += "：型类品商>p<".split("").reverse().join("") + goodsInfo['goodsTypeName'] + ">p/<".split("").reverse().join("");
    _0x41bf += "<p>发布时间：" + goodsInfo['lastTime'] + "</p>";
    _0x41bf += "</div>";
    _0x41bf += "<div class="price-box">";
    if (goodsInfo['discountActFlag'] == "1") {
        _0x41bf += "<h4><span>¥" + goodsInfo['price'] + "</span>¥" + goodsInfo['discountActPrice'] + ">4h/<".split("").reverse().join("");
        _0x41bf += "<div class="time-limit">";
        _0x41bf += "\"=crs gmi<".split("").reverse().join("") + bucketDomain + ">/\"gnp.emit-timil/4202-tsil/segami/1887/".split("").reverse().join("");
        _0x41bf += ">vid/<".split("").reverse().join("");
    } else {
        if (goodsInfo['redEnvelopesDiscountPrice'] != null) {
            _0x41bf += "<h4>¥" + goodsInfo['redEnvelopesDiscountPrice'] + ">4h/<".split("").reverse().join("");
            _0x41bf += "<div class="red-box">";
            _0x41bf += "\"=crs gmi<".split("").reverse().join("") + bucketDomain + "/7881/images/list-2024/list-red-icon.png" width="28" class="red-icon"/>";
            var _0x371c2f;
            var _0x30e8a = parseInt(goodsInfo['price']) - parseInt(goodsInfo['redEnvelopesDiscountPrice']);
            _0x371c2f = 403152 ^ 403153;
            _0x41bf += "已减" + _0x30e8a;
            _0x41bf += "</div>";
        } else {
            _0x41bf += "\xA5>4h<".split("").reverse().join("") + goodsInfo['price'] + "</h4>";
        }
    }
    _0x41bf += "</div>";
    _0x41bf += "</div>";
    var _0x4282ce;
    var _0x31385e = goodsInfo['subTitlePc'];
    _0x4282ce = 972866 ^ 972865;
    if (_0x31385e != undefined && _0x31385e != null && _0x31385e != '') {
        var _0x9feb = _0x31385e['split']("|");
        if (_0x9feb['length'] >= (784761 ^ 784765)) {
            _0x41bf += "<div class="attr-box">";
            for (var j = 202984 ^ 202984; j < _0x9feb['length']; j++) {
                if (j >= (856611 ^ 856613)) {
                    break;
                }
                var _0x60cde = _0x9feb[j]['indexOf']("-");
                if (_0x60cde != -(438212 ^ 438213)) {
                    _0x41bf += ">\"meti-rtta\"=ssalc vid<".split("").reverse().join("");
                    _0x41bf += ">4h<".split("").reverse().join("") + _0x9feb[j]['substring'](_0x60cde + (126576 ^ 126577), _0x9feb[j]['length']) + "</h4>";
                    _0x41bf += ">p<".split("").reverse().join("") + _0x9feb[j]['substring'](657211 ^ 657211, _0x60cde) + "</p>";
                    _0x41bf += "</div>";
                }
            }
            _0x41bf += ">vid/<".split("").reverse().join("");
        }
    }
    _0x41bf += ">\"aera-ntb\"=ssalc vid<".split("").reverse().join("");
    _0x41bf += "<div class="collect">";
    var _0x8eaa7b = (934092 ^ 934095) + (631727 ^ 631720);
    var _0x5eg = $['inArray'](goodsInfo['goodsId'], colGoodsArr);
    _0x8eaa7b = 976708 ^ 976704;
    if (_0x5eg != -(924158 ^ 924159)) {
        _0x41bf += "<a href="javascript:void(0)" class="has-coll" data-val-gid="" + goodsInfo['goodsId'] + ""><img src="" + bucketDomain + ">a/<藏收消取>/ \"91\"=htdiw \"gnp.telloc-sah/4202-tsil/segami/1887/".split("").reverse().join("");
    } else {
        _0x41bf += "<a href="javascript:void(0)" class="no-coll" data-val-gid="" + goodsInfo['goodsId'] + "\"=crs gmi<>\"".split("").reverse().join("") + bucketDomain + "/7881/images/list-2024/no-collet.png" width="19" />收藏商品</a>";
    }
    _0x41bf += "</div>";
    _0x41bf += "<div class="btn-box">";
    if (goodsInfo['supportTalk'] == "1") {
        _0x41bf += "<a href="javascript: openIm('" + goodsInfo['goodsId'] + "' ,'".split("").reverse().join("") + _0x7c7ac + ">a/<聊一聊>\"10-moc-ntb\"=ssalc \")'".split("").reverse().join("");
    }
    _0x41bf += "<a href="javascript: openGoodsDetailPage('" + goodsInfo['goodsId'] + "', '" + _0x7c7ac + ">a/<号账看查>\"10roloc 10-moc-ntb\"=ssalc \";)'".split("").reverse().join("");
    _0x41bf += ">vid/<".split("").reverse().join("");
    _0x41bf += "</div>";
    _0x41bf += "</div>";
    _0x41bf += "</div>";
    return _0x41bf;
}
function initGoodsHtml_ACCOUNT_V2(goodsInfo, goodsKind, recommendExtObj) {
    var _0x30da = '';
    if (goodsKind == "recommend") {
        _0x30da = "100.102";
    } else if (goodsInfo['sortKind'] == "2") {
        _0x30da = "100.101";
    }
    var _0x2d3g = "";
    if (qualityRecommendConfigureType == !![] && goodsKind == "recommend") {
        if (recommendExtObj['cancelCompensationFlag'] == !![]) {
            _0x2d3g += "<div class="list-item-small best-goods hascd">";
        } else {
            _0x2d3g += "<div class="list-item-small best-goods">";
        }
    } else {
        _0x2d3g += "<div class="list-item-small">";
    }
    if (goodsKind == "recommend") {
        if (qualityRecommendConfigureType == !![]) {
            if (recommendExtObj['cancelCompensationFlag'] == !![]) {
                _0x2d3g += "<div class="pztj-best"><p><i>" + recommendExtObj['cancelCompensationDesc'] + ">vid/<>p/<>i/<".split("").reverse().join("");
            } else {
                _0x2d3g += "<div class="pztj-best"></div>";
            }
        } else {
            _0x2d3g += "<div class="yxsj-box">";
            _0x2d3g += ">\"tfel-jsxy\"=ssalc vid<".split("").reverse().join("");
            _0x2d3g += "\"=crs gmi<".split("").reverse().join("") + bucketDomain + "/7881/images/list-2024/yxsj-icon.png" width="34" class="yxsj-icon" />";
            _0x2d3g += "<img src="" + bucketDomain + "/7881/images/list-2024/yxsj-title.png" width="96" class="yxsj-title" />";
            _0x2d3g += "</div>";
            _0x2d3g += ">\"thgir-jsxy\"=ssalc vid<".split("").reverse().join("");
            _0x2d3g += "\"=crs gmi<>p<".split("").reverse().join("") + bucketDomain + "/7881/images/list-2024/ksjy-icon.png" width="64"/></p>";
            _0x2d3g += "<p><img src="" + bucketDomain + ">p/<>/\"46\"=htdiw \"gnp.noci-pszy/4202-tsil/segami/1887/".split("").reverse().join("");
            if (recommendExtObj['cancelCompensationFlag']) {
                _0x2d3g += ">p<".split("").reverse().join("");
                _0x2d3g += "\"=crs gmi<".split("").reverse().join("") + bucketDomain + "/7881/images/list-2024/cdpf-icon.png" width="64"/>";
                _0x2d3g += "<img src="" + bucketDomain + ">/\"21\"=htdiw \"gnp.noci-oahnew/4202-tsil/segami/1887/".split("").reverse().join("");
                _0x2d3g += "<i>" + recommendExtObj['cancelCompensationDesc'] + "</i>";
                _0x2d3g += "</p>";
            }
            _0x2d3g += ">vid/<".split("").reverse().join("");
            _0x2d3g += "</div>";
        }
    }
    _0x2d3g += ">\"tfel-llams-tsil\"=ssalc vid<".split("").reverse().join("");
    _0x2d3g += "<div class="list-pic">";
    if (goodsInfo['imgCount'] && goodsInfo['imgCount'] > (168860 ^ 168860)) {
        _0x2d3g += "\"=lanigiro-atad gmi<".split("").reverse().join("") + goodsInfo['defaultImg'] + "\"=crs \"".split("").reverse().join("") + goodsInfo['defaultImg'] + ""/>";
    } else {
        _0x2d3g += "'(egaPliateDsdooGnepo\"=kcilcno gmi<".split("").reverse().join("") + goodsInfo['goodsId'] + "', '" + _0x30da + "')" data-original="" + goodsInfo['defaultImg'] + "" src="" + goodsInfo['defaultImg'] + ">/\"".split("").reverse().join("");
    }
    _0x2d3g += "</div>";
    if (goodsInfo['sortKind'] == "2") {
        _0x2d3g += "<img src="" + bucketDomain + "/7881/images/list-2024/recommed-account.png" width="80" class="recommed-icon"/>";
    }
    _0x2d3g += ">\"mun-cip\"=ssalc vid<".split("").reverse().join("") + (goodsInfo['imgCount'] && goodsInfo['imgCount'] > (433606 ^ 433606) ? goodsInfo['imgCount'] : "无") + "图</div>";
    if (goodsInfo['imgCount'] && goodsInfo['imgCount'] > (974104 ^ 974104)) {
        _0x2d3g += "<div class="pic-hover" style = "display: none;">";
        _0x2d3g += ">\"ntb-revoh\"=ssalc vid<".split("").reverse().join("");
        _0x2d3g += "\"=disdoog-lav-atad \"gib-kool\"=ssalc \")0(diov:tpircsavaj\"=ferh a<".split("").reverse().join("") + goodsInfo['goodsId'] + "" data-val-gameid="" + goodsInfo['gameId'] + "" data-val-gtid="" + goodsInfo['gtid'] + "">查看大图</a>";
        _0x2d3g += "<a href="javascript: openGoodsDetailPage('" + goodsInfo['goodsId'] + "' ,'".split("").reverse().join("") + _0x30da + ">vid/<>vid/<>a/<情详号账>\"liated-ot\"=ssalc \";)'".split("").reverse().join("");
    }
    _0x2d3g += "</div>";
    _0x2d3g += "<div class="list-small-right">";
    _0x2d3g += "<h3 class="title" data-title="" + escapeHTML(goodsInfo['title']) + "'(egaPliateDsdooGnepo :tpircsavaj\"=ferh a<>\"".split("").reverse().join("") + goodsInfo['goodsId'] + "', '" + _0x30da + ">\";)'".split("").reverse().join("") + escapeHTML(goodsInfo['title']) + ">3h/<>a/<".split("").reverse().join("");
    _0x2d3g += "<div class="right-bottom">";
    _0x2d3g += ">\"tfel-tob-thgir\"=ssalc vid<".split("").reverse().join("");
    _0x2d3g += "<div class="tags-box">";
    _0x2d3g += "<div class="tag-item">" + initTags(goodsInfo) + ">vid/<".split("").reverse().join("");
    _0x2d3g += ">vid/<".split("").reverse().join("");
    _0x2d3g += ">\"xob-revres\"=ssalc vid<".split("").reverse().join("");
    _0x2d3g += "<p>";
    _0x2d3g += initListQFInfo(goodsInfo);
    if (goodsInfo['kqgroupName'] != null && goodsInfo['kqgroupName'] != '') {
        _0x2d3g += "\"=diqk-lav-atad \"pitgnotuh\"=ssalc naps<".split("").reverse().join("") + goodsInfo['kqid'] + ""><img src="" + bucketDomain + ">naps/<>/\"gnp.gnotuh/4202-tsil/segami/1887/".split("").reverse().join("");
    }
    _0x2d3g += ">p/<".split("").reverse().join("");
    _0x2d3g += "<em>|</em>";
    _0x2d3g += "<p>" + goodsInfo['goodsTypeName'] + "</p>";
    _0x2d3g += "<em>|</em>";
    _0x2d3g += ">p<".split("").reverse().join("") + goodsInfo['lastTime'] + "</p>";
    _0x2d3g += "<em>|</em>";
    if (goodsInfo['onlineText'] != null && goodsInfo['onlineText'] != '') {
        if (goodsInfo['onlineText'] == "线在家卖".split("").reverse().join("")) {
            _0x2d3g += ">\"enilno-lles\"=ssalc p<".split("").reverse().join("") + goodsInfo['onlineText'] + ">p/<".split("").reverse().join("");
        } else {
            _0x2d3g += "<p class="sell-offline">" + goodsInfo['onlineText'] + "</p>";
        }
    }
    _0x2d3g += ">vid/<".split("").reverse().join("");
    _0x2d3g += ">\"tcelloc-rtta\"=ssalc vid<".split("").reverse().join("");
    var _0x7b56ga = (790394 ^ 790397) + (431885 ^ 431877);
    var _0x2dd53c = goodsInfo['subTitlePc'];
    _0x7b56ga = (951352 ^ 951354) + (274914 ^ 274915);
    if (_0x2dd53c != undefined && _0x2dd53c != null && _0x2dd53c != '') {
        var _0x5g4ga = _0x2dd53c['split']("|");
        if (_0x5g4ga['length'] >= (683742 ^ 683738)) {
            _0x2d3g += "<div class="attr-content"><div class="attr-box">";
            for (var j = 695417 ^ 695417; j < _0x5g4ga['length']; j++) {
                if (j >= (786663 ^ 786657)) {
                    break;
                }
                var _0x7f1g2b = (154405 ^ 154401) + (839057 ^ 839059);
                var _0xefd4ad = _0x5g4ga[j]['indexOf']("-");
                _0x7f1g2b = 140791 ^ 140784;
                if (_0xefd4ad != -(887812 ^ 887813)) {
                    _0x2d3g += ">\"meti-rtta\"=ssalc vid<".split("").reverse().join("");
                    _0x2d3g += ">4h<".split("").reverse().join("") + _0x5g4ga[j]['substring'](_0xefd4ad + (257927 ^ 257926), _0x5g4ga[j]['length']) + "</h4>";
                    _0x2d3g += ">p<".split("").reverse().join("") + _0x5g4ga[j]['substring'](864263 ^ 864263, _0xefd4ad) + "</p>";
                    _0x2d3g += ">vid/<".split("").reverse().join("");
                }
            }
            _0x2d3g += ">vid/<>vid/<".split("").reverse().join("");
        }
    }
    _0x2d3g += ">\"tcelloc\"=ssalc vid<".split("").reverse().join("");
    var _0x4eb = (289310 ^ 289304) + (332773 ^ 332771);
    var _0x588e = $['inArray'](goodsInfo['goodsId'], colGoodsArr);
    _0x4eb = (969851 ^ 969850) + (117442 ^ 117442);
    if (_0x588e != -(637787 ^ 637786)) {
        _0x2d3g += "\"=dig-lav-atad \"lloc-sah\"=ssalc \")0(diov:tpircsavaj\"=ferh a<".split("").reverse().join("") + goodsInfo['goodsId'] + "\"=crs gmi<>\"".split("").reverse().join("") + bucketDomain + ">a/<藏收消取>/ \"91\"=htdiw \"gnp.telloc-sah/4202-tsil/segami/1887/".split("").reverse().join("");
    } else {
        _0x2d3g += "\"=dig-lav-atad \"lloc-on\"=ssalc \")0(diov:tpircsavaj\"=ferh a<".split("").reverse().join("") + goodsInfo['goodsId'] + ""><img src="" + bucketDomain + ">a/<品商藏收>/ \"91\"=htdiw \"gnp.telloc-on/4202-tsil/segami/1887/".split("").reverse().join("");
    }
    _0x2d3g += "</div></div></div>";
    _0x2d3g += "<div class="right-bot-right">";
    _0x2d3g += "<div class="btn-area">";
    if (goodsInfo['supportTalk'] == "1") {
        _0x2d3g += "'(mInepo :tpircsavaj\"=ferh a<".split("").reverse().join("") + goodsInfo['goodsId'] + "' ,'".split("").reverse().join("") + _0x30da + "')" class="btn-com-01 color01">聊一聊</a>";
    } else {
        _0x2d3g += "<a href="javascript: openGoodsDetailPage('" + goodsInfo['goodsId'] + "', '" + _0x30da + "');" class="btn-com-01 color01">查看账号</a>";
    }
    if (goodsInfo['discountActFlag'] == "1") {
        _0x2d3g += "\xA5>4h<".split("").reverse().join("") + goodsInfo['discountActPrice'] + ">4h/<".split("").reverse().join("");
        _0x2d3g += "<div class="time-limit">";
        _0x2d3g += "<p>¥" + goodsInfo['price'] + "</p>";
        _0x2d3g += "<img src="" + bucketDomain + "/7881/images/list-2024/limit-time.png"/>";
        _0x2d3g += "</div>";
    } else {
        if (goodsInfo['redEnvelopesDiscountPrice'] != null) {
            _0x2d3g += "<h4>¥" + goodsInfo['redEnvelopesDiscountPrice'] + "</h4>";
            _0x2d3g += ">\"xob-der\"=ssalc vid<".split("").reverse().join("");
            _0x2d3g += "<img src="" + bucketDomain + "/7881/images/list-2024/list-red-icon.png" width="28" class="red-icon"/>";
            var _0xbecfc;
            var _0x7e805f = parseInt(goodsInfo['price']) - parseInt(goodsInfo['redEnvelopesDiscountPrice']);
            _0xbecfc = 463455 ^ 463451;
            _0x2d3g += "已减" + _0x7e805f;
            _0x2d3g += "</div>";
        } else {
            _0x2d3g += "<h4>¥" + goodsInfo['price'] + "</h4>";
        }
    }
    _0x2d3g += "</div></div></div></div></div></div>";
    return _0x2d3g;
}
function initRecommendGoods(oriParamObj) {
    if (fiveStarSellerFlag == "0" || !supportYxsj) {
        return [];
    }
    var _0x144f8e;
    var _0x1ea5af = new Object();
    _0x144f8e = "jonilg".split("").reverse().join("");
    _0x1ea5af['gameId'] = gameId;
    _0x1ea5af['gtId'] = gtId;
    if (groupId != undefined && groupId != "0") {
        _0x1ea5af['groupId'] = groupId;
    }
    if (serverId != undefined && serverId != "0") {
        _0x1ea5af['serverId'] = serverId;
    }
    if (carrierId != undefined && carrierId != "0") {
        _0x1ea5af['carrierId'] = carrierId;
    }
    if (minPrice != undefined) {
        _0x1ea5af['minPrice'] = minPrice;
    }
    if (maxPrice != undefined) {
        _0x1ea5af['maxPrice'] = maxPrice;
    }
    if (keyword != undefined && keyword != null && keyword != '') {
        _0x1ea5af['keyword'] = keyword;
    }
    if (tagValue != undefined) {
        _0x1ea5af['queryTab'] = tagValue;
    }
    var _0xf7f3e = oriParamObj['extendAttrList'];
    if (_0xf7f3e != undefined && _0xf7f3e != null && _0xf7f3e['length'] > (177007 ^ 177007)) {
        _0x1ea5af['queryGoodsExtendAttrValList'] = _0xf7f3e;
    }
    _0x1ea5af['pageNum'] = pageNum;
    _0x1ea5af['pageSize'] = pageSize;
    var _0x291e = [];
    $['ajax']({
        'url': queryAccountRecommendUrl,
        "async": false,
        'type': "POST",
        "data": JSON['stringify'](_0x1ea5af),
        "dataType": "json",
        "contentType": "application/json",
        "xhrFields": {
            "withCredentials": !![]
        },
        'success': function(result) {
            if (result['code'] == (295154 ^ 295154) && result['body'] != undefined) {
                _0x291e = result['body'];
            }
        },
        'error': function(result) {
            return;
        }
    });
    return _0x291e;
}
function detailSaleNew(event) {
    var _0x3a_0x7ag = $(event)['parents'](".detcon")['find']("tpilles.".split("").reverse().join(""))['val']();
    var _0x46aee = $(event)['parents'](".detcon")['attr']("gameid");
    var _0xd9c = (362533 ^ 362541) + (109396 ^ 109392);
    var _0xe88b8d = $(event)['parents']("nocted.".split("").reverse().join(""))['attr']("goodstype");
    _0xd9c = (521932 ^ 521929) + (203679 ^ 203679);
    if (_0x3a_0x7ag == null || _0x3a_0x7ag == '') {
        layer['msg']("请填写购买数量");
        return;
    }
    if (_0x46aee == "01G".split("").reverse().join("") && _0xe88b8d == "100001") {
        if (isNaN(parseInt(_0x3a_0x7ag)) || parseInt(_0x3a_0x7ag) % (715093 ^ 715057) != (721335 ^ 721335)) {
            layer['msg']("数整的001入输能只".split("").reverse().join(""));
            return;
        }
    }
    if (_0xe88b8d == "300001".split("").reverse().join("")) {
        var _0xbgc = (404313 ^ 404316) + (377881 ^ 377885);
        var _0x56b4g;
        _0xbgc = 916561 ^ 916569;
        var _0x4ab56d;
        var _0x6713dd;
        _0x4ab56d = 295199 ^ 295191;
        $['ajax']({
            "url": "/hasRealNameCert",
            'async': false,
            'type': "GET",
            'success': function(data) {
                _0x6713dd = false;
                if (data != undefined) {
                    _0x56b4g = eval("(" + data + ")");
                }
            },
            "error": function(data) {
                if (data['status'] == "401" && data['responseText'] == "loseSession") {
                    layer['msg']("录登行进先您请".split("").reverse().join(""));
                }
                _0x6713dd = !![];
            }
        });
        if (_0x6713dd) {
            return;
        }
        if (!_0x6713dd && !_0x56b4g) {
            layer['confirm']("请先注销当前实名认证，按照最新标准重新认证！", {
                'btn': ["往前".split("").reverse().join(""), "不"]
            }, function() {
                $("ntBtreCemaNlaer#".split("").reverse().join(""))['click']();
                layer['closeAll']();
            }, function() {
                layer['closeAll']();
            });
            return;
        }
    }
    var _0x8c8d7d = $(event)['parents'](".detcon")['attr']("dIsdoog".split("").reverse().join(""));
    var _0x52913f = (573780 ^ 573783) + (391531 ^ 391534);
    var _0xegd2a = $(event)['parents']("nocted.".split("").reverse().join(""))['find']("#unitPrice")['val']();
    _0x52913f = (878375 ^ 878375) + (464374 ^ 464375);
    $['ajax']({
        "type": "POST",
        "url": "/receipt/valid",
        "data": {
            'goodsId': _0x8c8d7d,
            'price': _0xegd2a,
            'totalNum': _0x3a_0x7ag
        },
        "dataType": "json",
        'async': false,
        'success': function(result) {
            if (result['code'] == (977977 ^ 977977)) {
                window['location']['href'] = receiptDomain + "/market/order/trade-" + _0x8c8d7d + "?tradeNum=" + _0x3a_0x7ag;
            } else {
                layer['msg'](result['msg']);
            }
        },
        'error': function(XMLHttpRequest, textStatus) {
            layer['msg']("!常异器务服".split("").reverse().join(""));
        }
    });
}
function simpleSaleNew(event) {
    var _0x0fg4f = $(event)['parents'](".simple-goods-li")['attr']("dIsdoog".split("").reverse().join(""));
    var _0x03gad;
    var _0xa2c = $(event)['parents'](".simple-goods-li")['find']("ecirPtinu#".split("").reverse().join(""))['val']();
    _0x03gad = (360312 ^ 360313) + (311410 ^ 311414);
    var _0xeceg4e = $(event)['parents']("il-sdoog-elpmis.".split("").reverse().join(""))['attr']("epytsdoog".split("").reverse().join(""));
    if (_0xeceg4e == "100003") {
        var _0x19a9d;
        var _0x0fce;
        _0x19a9d = (732266 ^ 732258) + (600186 ^ 600185);
        var _0xe3_0x268;
        $['ajax']({
            "url": "/hasRealNameCert",
            "async": false,
            'type': "GET",
            'success': function(data) {
                if (data != undefined) {
                    _0x0fce = eval("(" + data + ")");
                }
            },
            "error": function(data) {
                if (data['status'] == "401" && data['responseText'] == "loseSession") {
                    layer['msg']("录登行进先您请".split("").reverse().join(""));
                }
                _0xe3_0x268 = !![];
            }
        });
        if (_0xe3_0x268) {
            return;
        }
        if (!_0xe3_0x268 && !_0x0fce) {
            layer['confirm']("！证认新重准标新最照按，证认名实前当销注先请".split("").reverse().join(""), {
                'btn': ["往前".split("").reverse().join(""), "不"]
            }, function() {
                $("#realNameCertBtn")['click']();
                layer['closeAll']();
            }, function() {
                layer['closeAll']();
            });
            return;
        }
    }
    $['ajax']({
        "type": "POST",
        'url': "/receipt/valid",
        "data": {
            "goodsId": _0x0fg4f,
            "price": _0xa2c
        },
        'dataType': "json",
        'async': false,
        "success": function(result) {
            if (result['code'] == (450240 ^ 450240)) {
                window['location']['href'] = receiptDomain + "/market/order/trade-" + _0x0fg4f;
            } else {
                layer['msg'](result['msg']);
            }
        },
        'error': function(XMLHttpRequest, textStatus) {
            layer['msg']("服务器异常!");
        }
    });
}
function initMarketSHtml_YXB(goodsList) {
    var _0xaed9gc;
    var _0x21_0xd84 = "";
    _0xaed9gc = "efjkbp".split("").reverse().join("");
    for (var i = 342518 ^ 342518; i < goodsList['length']; i++) {
        var _0xgff;
        var _0x90a3b = goodsList[i];
        _0xgff = (869183 ^ 869177) + (557991 ^ 557998);
        var _0x23e6cb = (274661 ^ 274668) + (574355 ^ 574363);
        var _0x3bc3a = "";
        _0x23e6cb = (313464 ^ 313468) + (625857 ^ 625860);
        if (_0x90a3b['sortKind'] == "2") {
            _0x3bc3a += ">\"dmocer tluafed-meti-tsil\"=ssalc vid<".split("").reverse().join("");
        } else {
            _0x3bc3a += "<div class="list-item-default">";
        }
        _0x3bc3a += ">\"xob-eltit-tsil\"=ssalc vid<".split("").reverse().join("");
        _0x3bc3a += ">3h<".split("").reverse().join("");
        _0x3bc3a += initTags(_0x90a3b);
        _0x3bc3a += "'(egaPliateDsdooGnepo :tpircsavaj\"=ferh a<".split("").reverse().join("") + _0x90a3b['goodsId'] + ">\";)'' ,'".split("").reverse().join("") + escapeHTML(_0x90a3b['title']) + ">a/<".split("").reverse().join("");
        _0x3bc3a += "</h3>";
        _0x3bc3a += "<p>";
        _0x3bc3a += "游戏区服：" + initListQFInfo(_0x90a3b);
        if (_0x90a3b['kqgroupName'] != null && _0x90a3b['kqgroupName'] != '') {
            _0x3bc3a += "<span class="hutongtip" data-val-kqid="" + _0x90a3b['kqid'] + "\"=crs gmi<>\"".split("").reverse().join("") + bucketDomain + "/7881/images/list-2024/hutong.png"/></span>";
        }
        _0x3bc3a += ">p/<".split("").reverse().join("");
        _0x3bc3a += "<p>商品类型：" + _0x90a3b['goodsTypeName'] + "<span class="stock">库存：<em>" + _0x90a3b['stock'] + "</em></span><span class="stock">卖家信誉：" + initSellStar(_0x90a3b['totalTradeCount']) + ">p/<>naps/<".split("").reverse().join("");
        _0x3bc3a += ">vid/<".split("").reverse().join("");
        _0x3bc3a += ">\"xob-ecirp\"=ssalc vid<".split("").reverse().join("");
        _0x3bc3a += "\xA5>3h<".split("").reverse().join("") + _0x90a3b['price'] + "</h3>";
        if (_0x90a3b['tradePlace'] == "2") {
            _0x3bc3a += ">p/<卖拍工人>p<".split("").reverse().join("");
        }
        _0x3bc3a += "</div>";
        _0x3bc3a += ">\"tinu-ecirp\"=ssalc vid<".split("").reverse().join("");
        if (_0x90a3b['unitOfPrice'] != null && _0x90a3b['unitOfPrice'] != (239301 ^ 239301)) {
            _0x3bc3a += "<p><em>1</em>元=<em>" + _0x90a3b['unitOfPrice'] + "</em>" + _0x90a3b['unit'] + "</p>";
        }
        _0x3bc3a += ">me<>p<".split("").reverse().join("") + _0x90a3b['priceOfUnitForShow'] + "/元>me/<".split("").reverse().join("") + _0x90a3b['unit'] + "</p>";
        _0x3bc3a += ">vid/<".split("").reverse().join("");
        _0x3bc3a += "<div class="btn-box">";
        _0x3bc3a += "<a href="javascript: openGoodsBuyingPage('" + _0x90a3b['goodsId'] + "', '" + _0x90a3b['pernum'] + "' ,'".split("").reverse().join("") + _0x90a3b['price'] + "', '" + _0x90a3b['groupId'] + "', '" + _0x90a3b['groupName'] + "', '" + _0x90a3b['serverId'] + "' ,'".split("").reverse().join("") + _0x90a3b['serverName'] + "');" class="btn-com-01 color03">立即购买</a>";
        if (_0x90a3b['deliveryTimeByRule'] != null && _0x90a3b['deliveryTimeByRule'] != '') {
            _0x3bc3a += ">naps<均平>p<".split("").reverse().join("") + _0x90a3b['deliveryTimeByRule'] + "</span>发货</p>";
        }
        if (_0x90a3b['dnfYxbAwardActivityFlag']) {
            _0x3bc3a += "\"=crs gmi<".split("").reverse().join("") + bucketDomain + "\"=pit-lav-atad \"noci-gnaij\"=ssalc \"63\"=htdiw \"gnp.noci-gnaij/4202-tsil/segami/1887/".split("").reverse().join("") + _0x90a3b['dnfYxbAwardActivityTips'] + ">/\"".split("").reverse().join("");
        } else {
            if (_0x90a3b['redPacketCashBackFlag']) {
                _0x3bc3a += "\"=crs gmi<>\";)'lmth.xedni/naduohs-12113202/cp/moc.1887.tca//:sptth'(nepo.wodniw:tpircsavaj\"=ferh a<".split("").reverse().join("") + bucketDomain + "/7881/images/list-2024/jiang-icon.png" width="36" class="jiang-icon" data-val-tip="成功购买100%返现金红包，最高888元"/></a>";
            }
        }
        _0x3bc3a += ">vid/<".split("").reverse().join("");
        if (_0x90a3b['sortKind'] == "2") {
            _0x3bc3a += "\"=crs gmi<".split("").reverse().join("") + bucketDomain + "/7881/images/list-2024/tjbt-icon.png" class="recomd-icon" width="60"/>";
        }
        _0x3bc3a += ">vid/<".split("").reverse().join("");
        _0x21_0xd84 += _0x3bc3a;
    }
    $("gnidaol-tsil.".split("").reverse().join(""))['hide']();
    $(".list-box")['empty']()['append'](_0x21_0xd84);
}
function queryShouHuoMarket(paramObj) {
    var _0x5gdbe;
    var _0xf9ca9c = '';
    _0x5gdbe = 'jcimec';
    var _0x8c_0xfd4;
    var _0x25a21d = paramObj['extendAttrList'];
    _0x8c_0xfd4 = (807545 ^ 807536) + (476737 ^ 476740);
    if (_0x25a21d['length'] > (690884 ^ 690884)) {
        var _0x8fccge;
        var _0x23_0x714 = JSON['stringify'](_0x25a21d);
        _0x8fccge = 519160 ^ 519166;
        if (_0x23_0x714 != '' && _0x23_0x714['indexOf']("落部".split("").reverse().join("")) > -(839086 ^ 839087)) {
            _0xf9ca9c = "lb".split("").reverse().join("");
        } else if (_0x23_0x714 != '' && _0x23_0x714['indexOf']("联盟") > -(776869 ^ 776868)) {
            _0xf9ca9c = "ml".split("").reverse().join("");
        }
    }
    var _0xbfebc = (761861 ^ 761868) + (954956 ^ 954954);
    var _0x414fc = queryShouGoodsListUrl + "?gameId=" + gameId + "&goodsType=" + gtId + "&groupId=" + groupId + "&serverId=" + serverId + "=dIpmac&".split("").reverse().join("") + _0xf9ca9c + "&t=" + new Date()['getTime']();
    _0xbfebc = (629608 ^ 629615) + (612476 ^ 612473);
    $['ajax']({
        "type": "get",
        'url': _0x414fc,
        "dataType": "jsonp",
        'jsonp': "queryReceiptCallback",
        "jsonpCallback": 'queryReceiptCallback',
        'success': function(data) {
            initReceiptDetailList(data);
            initReceiptSimpleList(data);
        },
        "error": function(result) {
            return;
        }
    });
}
function queryReceiptCallback(dataResult) {}
function initReceiptDetailList(dataResult) {
    var _0xeaeg = (305852 ^ 305853) + (716057 ^ 716048);
    var _0x2a0b3c = dataResult['detailsList'];
    _0xeaeg = (564753 ^ 564754) + (245395 ^ 245393);
    if (_0x2a0b3c == null || _0x2a0b3c == undefined || _0x2a0b3c['length'] == (204237 ^ 204237)) {
        return;
    }
    $(".float-adv")['show']();
    $(".float-noadv")['hide']();
    var _0x3a25fe = '';
    for (var i = 142527 ^ 142527; i < _0x2a0b3c['length']; i++) {
        var _0x2d_0x6cb = _0x2a0b3c[i];
        var _0xg_0xc2c = (754532 ^ 754533) + (716895 ^ 716891);
        var _0x24_0xgac = '';
        _0xg_0xc2c = (735347 ^ 735354) + (687134 ^ 687126);
        _0x24_0xgac += "<div class="detcon" goodsid="" + _0x2d_0x6cb['id'] + "\"=ecirp \"".split("").reverse().join("") + _0x2d_0x6cb['price'] + ""gameid="" + _0x2d_0x6cb['gameId'] + "" groupid="" + _0x2d_0x6cb['groupId'] + "" serverid="" + _0x2d_0x6cb['serverId'] + "\"=ecruos\"".split("").reverse().join("") + _0x2d_0x6cb['goodsSource'] + "" goodstype="" + _0x2d_0x6cb['goodsType'] + "" hasShareServer="" + _0x2d_0x6cb['hasShareServer'] + ">\"".split("").reverse().join("");
        if (_0x2d_0x6cb['gameId'] == "G5569" || _0x2d_0x6cb['gameId'] == "12G".split("").reverse().join("") || _0x2d_0x6cb['gameId'] == "G5656" || _0x2d_0x6cb['gameId'] == "G6211") {
            _0x24_0xgac += "<p class="qfparm">" + _0x2d_0x6cb['groupName'] + "/" + _0x2d_0x6cb['serverName'] + "/<span style="color:red">" + _0x2d_0x6cb['campName'] + "</span>";
        } else {
            _0x24_0xgac += "<p class="qfparm">" + _0x2d_0x6cb['groupName'] + "/" + _0x2d_0x6cb['serverName'];
        }
        if (_0x2d_0x6cb['goodsType'] != "100003" && _0x2d_0x6cb['hasShareServer']) {
            _0x24_0xgac += "<img class="interflow hutongtip" data-val-kqid="" + _0x2d_0x6cb['kqId'] + "" kqid="" + _0x2d_0x6cb['kqId'] + "" serverid="" + _0x2d_0x6cb['serverId'] + "" src="" + bucketDomain + "/7881/images/list-2024/hutong.png">";
        }
        _0x24_0xgac += "</p>";
        if (i == (614282 ^ 614282)) {
            _0x24_0xgac += ">/\"gnp.ecrpyz/tsil/segami/6102-1887/moc.1887.cip//\"=crs gmi<>3h<".split("").reverse().join("");
        } else if (i == (757146 ^ 757147)) {
            _0x24_0xgac += "<h3><img src="//pic.7881.com/7881-2016/images/list/zdshou.png"/>";
        }
        if (_0x2d_0x6cb['goodsType'] != "100003") {
            _0x24_0xgac += _0x2d_0x6cb['tradeWayName'];
        }
        _0x24_0xgac += ">3h/<".split("").reverse().join("");
        var _0x7f8e = (923885 ^ 923881) + (141827 ^ 141825);
        var _0x0b6dg = '';
        _0x7f8e = (736736 ^ 736742) + (769236 ^ 769236);
        var _0x142e4e = _0x2d_0x6cb['unit'];
        if (_0x142e4e['length'] > (473712 ^ 473716)) {
            _0x142e4e = _0x142e4e['substring'](919958 ^ 919958, 962283 ^ 962287);
        }
        if (_0x2d_0x6cb['goodsType'] == "300001".split("").reverse().join("")) {
            _0x24_0xgac += "<p class="ifparm"><em>收货单价：</em>" + "<span>1" + _0x142e4e + "=" + _0x2d_0x6cb['price'] + "元</span>" + ">p/<".split("").reverse().join("");
            _0x24_0xgac += "\"=eulav \"ecirPtinu\"=di \"neddih\"=epyt tupni<".split("").reverse().join("") + _0x2d_0x6cb['price'] + "">";
            _0x0b6dg = _0x2d_0x6cb['price'];
        } else {
            if (_0x2d_0x6cb['pubTmplType'] == "JB") {
                _0x24_0xgac += "<p class="ifparm">";
                _0x24_0xgac += "<em>收货单价：</em><span>";
                if (_0x2d_0x6cb['priceOfUnit'] != null && _0x2d_0x6cb['priceOfUnit'] != (831121 ^ 831121)) {
                    _0x24_0xgac += "1元=<i>" + _0x2d_0x6cb['priceOfUnit'] + "</i>" + _0x142e4e;
                    _0x24_0xgac += "<br>";
                }
                _0x24_0xgac += "1" + _0x142e4e + "=" + _0x2d_0x6cb['unitOfPrice'] + "元";
                _0x24_0xgac += "</span></p>";
            } else {
                _0x24_0xgac += ">me/<：价单货收>me<>\"mrapfi\"=ssalc p<".split("").reverse().join("") + "1>naps<".split("").reverse().join("") + _0x142e4e + "=" + _0x2d_0x6cb['unitOfPrice'] + "元</span>" + "</p>";
            }
            _0x24_0xgac += "<input type="hidden" id="unitPrice" value="" + _0x2d_0x6cb['unitOfPrice'] + ">\"".split("").reverse().join("");
            _0x0b6dg = _0x2d_0x6cb['unitOfPrice'];
        }
        _0x24_0xgac += ">i<>naps<>me/<：量数货收>me<>\"mrapfi\"=ssalc p<".split("").reverse().join("") + _0x2d_0x6cb['receiptAmount'] + ">i/<".split("").reverse().join("") + _0x142e4e + "</span></p>";
        _0x24_0xgac += ">\"mrapfi\"=ssalc p<".split("").reverse().join("") + "<em>出货数量：</em>" + "\"=eulav \"izuhsylno tpilles\"=ssalc \"txet\"=epyt tupni<>naps<".split("").reverse().join("") + _0x2d_0x6cb['minReceipt'] + ">/\"01\"=htgnelxam \"".split("").reverse().join("") + _0x142e4e + ">naps/<".split("").reverse().join("") + "</p>";
        var _0xf29faa;
        var _0x2789bf = 911664 ^ 911664;
        _0xf29faa = 'qlbnlq';
        if (_0x2d_0x6cb['minReceipt'] != null && _0x2d_0x6cb['minReceipt'] != '' && _0x0b6dg != '') {
            _0x2789bf = cutXiaoNum(mul(_0x2d_0x6cb['minReceipt'], _0x0b6dg), 219423 ^ 219421);
        }
        _0x24_0xgac += " <p class="ifparm"><em>获得金额：</em><span><i class="allgetmon">" + _0x2789bf + "</i>元</span></p>";
        _0x24_0xgac += ">a/<售出即立>\"wen-elas-liated-ouhuohs 10roloc 20-ntb-moc\"=ssalc \")0(diov:tpircsavaj\"=ferh a<".split("").reverse().join("");
        _0x24_0xgac += ">vid/<".split("").reverse().join("");
        _0x3a25fe += _0x24_0xgac;
    }
    $("#shouhuo-detail")['empty']()['append'](_0x3a25fe);
}
function initReceiptSimpleList(dataResult) {
    var _0x46675b;
    var _0x4b276f = dataResult['simpleList'];
    _0x46675b = 208155 ^ 208155;
    if (_0x4b276f == null || _0x4b276f == undefined || _0x4b276f['length'] == (244516 ^ 244516)) {
        $("vda-taolf.".split("").reverse().join(""))['hide']();
        $("vdaon-taolf.".split("").reverse().join(""))['show']();
        return;
    }
    var _0x454dba = '';
    _0x454dba += "<ul>";
    for (var i = 406001 ^ 406001; i < _0x4b276f['length']; i++) {
        var _0xc6c = _0x4b276f[i];
        var _0xc4f = _0xc6c['unit'];
        if (_0xc4f['length'] > (354486 ^ 354482)) {
            _0xc4f = _0xc4f['substring'](150454 ^ 150454, 861650 ^ 861654);
        }
        var _0xf4926a;
        var _0x4eebc = '';
        _0xf4926a = 115655 ^ 115649;
        _0x4eebc += "\"=disdoog \"il-sdoog-elpmis\"=ssalc il<".split("").reverse().join("") + _0xc6c['id'] + "" price="" + _0xc6c['price'] + "\"= epytsdoog \"".split("").reverse().join("") + _0xc6c['goodsType'] + ">\"".split("").reverse().join("");
        if (_0xc6c['gameId'] == "9655G".split("").reverse().join("") || _0xc6c['gameId'] == "12G".split("").reverse().join("") || _0xc6c['gameId'] == "G5656" || _0xc6c['gameId'] == "1126G".split("").reverse().join("")) {
            _0x4eebc += "<p>" + _0xc6c['groupName'] + "/" + _0xc6c['serverName'] + ">\"der :roloc\"=elyts naps</".split("").reverse().join("") + _0xc6c['campName'] + "</span>";
        } else {
            _0x4eebc += ">p<".split("").reverse().join("") + _0xc6c['groupName'] + "/" + _0xc6c['serverName'];
        }
        if (_0xc6c['goodsType'] != "300001".split("").reverse().join("") && _0xc6c['hasShareServer']) {
            _0x4eebc += "<img class="hutongtip" data-val-kqid="" + _0xc6c['kqId'] + "\"=crs \"".split("").reverse().join("") + bucketDomain + ">/\"gnp.gnotuh/4202-tsil/segami/1887/".split("").reverse().join("");
        }
        _0x4eebc += "</p>";
        _0x4eebc += ">i<收>\"mungs\"=ssalc p<".split("").reverse().join("") + _0xc6c['receiptAmount'] + "</i>" + _0xc4f + ">i<，".split("").reverse().join("") + _0xc6c['minReceipt'] + _0xc4f + ">p/<收起>i/<".split("").reverse().join("");
        var _0x055gde = (919353 ^ 919359) + (302900 ^ 302909);
        var _0xedf09c = $("niamoDredrOecalPtpiecer#".split("").reverse().join(""))['text']()['replace']("*", _0xc6c['id']);
        _0x055gde = 346604 ^ 346597;
        if (_0xc6c['goodsType'] == "100003") {
            if ("${openShouHuoNew}" == "true") {
                _0x4eebc += ">p/<>a/<售出即立> \"wen-elas-elpmis-ouhuohs\"=ssalc  \")0(diov:tpircsavaj\"=ferh a<>p<".split("").reverse().join("");
            } else {
                _0x4eebc += "<p><a href="javascript:void(0)" data-url="" + _0xedf09c + ""  class="shouhuo-simple-sale" >立即出售</a></p>";
            }
            _0x4eebc += "<input type="hidden" id="unitPrice" value="" + _0xc6c['price'] + "">";
        } else {
            if (_0xc6c['pubTmplType'] == "JB") {
                if (_0xc6c['priceOfUnit'] != null && _0xc6c['priceOfUnit'] != (180736 ^ 180736)) {
                    _0x4eebc += ">me<=元1>p<".split("").reverse().join("") + _0xc6c['priceOfUnit'] + "</em>" + _0xc4f + ">p/<>a/<售出即立> \"wen-elas-elpmis-ouhuohs\"=ssalc  \")0(diov:tpircsavaj\"=ferh  a<".split("").reverse().join("");
                } else {
                    _0x4eebc += "<p>1" + _0xc4f + "=<em>" + _0xc6c['unitOfPrice'] + ">p/<>a/<售出即立> \"wen-elas-elpmis-ouhuohs\"=ssalc  \")0(diov:tpircsavaj\"=ferh  a<>me/<元".split("").reverse().join("");
                }
            } else {
                _0x4eebc += "1>p<".split("").reverse().join("") + _0xc4f + "=<em>" + _0xc6c['unitOfPrice'] + "元</em><a  href="javascript:void(0)"  class="shouhuo-simple-sale-new" >立即出售</a></p>";
            }
            _0x4eebc += "<input type="hidden" id="unitPrice" value="" + _0xc6c['unitOfPrice'] + "">";
        }
        _0x4eebc += "</li>";
        _0x454dba += _0x4eebc;
    }
    _0x454dba += "</ul>";
    $("#shouhuo-simple")['empty']()['append'](_0x454dba);
}
function initSellStar(totalTradeCount) {
    if (!totalTradeCount || totalTradeCount == (204573 ^ 204573)) {
        return '';
    } else if (totalTradeCount >= (464089 ^ 464088) && totalTradeCount <= (619816 ^ 619810)) {
        return ">i/<>\"rats-noci\"=ssalc i<".split("").reverse().join("");
    } else if (totalTradeCount >= (207715 ^ 207720) && totalTradeCount <= (269310 ^ 269270)) {
        return "<i class="icon-star"></i><i class="icon-star"></i>";
    } else if (totalTradeCount >= (247245 ^ 247268) && totalTradeCount <= (102297 ^ 102339)) {
        return ">i/<>\"rats-noci\"=ssalc i<>i/<>\"rats-noci\"=ssalc i<>i/<>\"rats-noci\"=ssalc i<".split("").reverse().join("");
    } else if (totalTradeCount >= (863626 ^ 863697) && totalTradeCount <= (641971 ^ 641829)) {
        return "<i class="icon-star"></i><i class="icon-star"></i><i class="icon-star"></i><i class="icon-star"></i>";
    } else if (totalTradeCount >= (572100 ^ 571987) && totalTradeCount <= (703832 ^ 703906)) {
        return ">i/<>\"rats-noci\"=ssalc i<>i/<>\"rats-noci\"=ssalc i<>i/<>\"rats-noci\"=ssalc i<>i/<>\"rats-noci\"=ssalc i<>i/<>\"rats-noci\"=ssalc i<".split("").reverse().join("");
    } else if (totalTradeCount >= (464546 ^ 464473) && totalTradeCount <= (395257 ^ 394765)) {
        return ">i/<>\"nauz-noci\"=ssalc i<".split("").reverse().join("");
    } else if (totalTradeCount >= (457600 ^ 457333) && totalTradeCount <= (963877 ^ 964301)) {
        return ">i/<>\"nauz-noci\"=ssalc i<>i/<>\"nauz-noci\"=ssalc i<".split("").reverse().join("");
    } else if (totalTradeCount >= (705602 ^ 706475) && totalTradeCount <= (132588 ^ 131644)) {
        return "<i class="icon-zuan"></i><i class="icon-zuan"></i><i class="icon-zuan"></i>";
    } else if (totalTradeCount >= (557403 ^ 558730) && totalTradeCount <= (974570 ^ 970082)) {
        return "<i class="icon-zuan"></i><i class="icon-zuan"></i><i class="icon-zuan"></i><i class="icon-zuan"></i>";
    } else if (totalTradeCount >= (274392 ^ 277585) && totalTradeCount <= (956364 ^ 962780)) {
        return ">i/<>\"nauz-noci\"=ssalc i<>i/<>\"nauz-noci\"=ssalc i<>i/<>\"nauz-noci\"=ssalc i<>i/<>\"nauz-noci\"=ssalc i<>i/<>\"nauz-noci\"=ssalc i<".split("").reverse().join("");
    } else if (totalTradeCount >= (110593 ^ 104208) && totalTradeCount <= (693698 ^ 711650)) {
        return ">i/<>\"gnauh-noci\"=ssalc i<".split("").reverse().join("");
    } else if (totalTradeCount >= (591201 ^ 609088) && totalTradeCount <= (373007 ^ 356959)) {
        return ">i/<>\"gnauh-noci\"=ssalc i<>i/<>\"gnauh-noci\"=ssalc i<".split("").reverse().join("");
    } else if (totalTradeCount >= (609298 ^ 626499) && totalTradeCount <= 100000) {
        return "<i class="icon-huang"></i><i class="icon-huang"></i><i class="icon-huang"></i>";
    } else if (totalTradeCount >= 100001 && totalTradeCount <= 200000) {
        return ">i/<>\"gnauh-noci\"=ssalc i<>i/<>\"gnauh-noci\"=ssalc i<>i/<>\"gnauh-noci\"=ssalc i<>i/<>\"gnauh-noci\"=ssalc i<".split("").reverse().join("");
    } else if (totalTradeCount >= 200001) {
        return "<i class="icon-huang"></i><i class="icon-huang"></i><i class="icon-huang"></i><i class="icon-huang"></i><i class="icon-huang"></i>";
    }
}
function compShouHuoPrice(e) {
    var _0x2f3bd;
    var _0xc4be = '';
    _0x2f3bd = (117872 ^ 117881) + (204833 ^ 204832);
    if ($(e)['val']()['replace'](new RegExp('\D|','g'), '') == '') {
        _0xc4be = 869238 ^ 869238;
    } else {
        _0xc4be = parseInt($(e)['val']());
    }
    var _0xb06f;
    var _0x25_0x2f6 = $(e)['parents'](".detcon")['attr']("gameid");
    _0xb06f = 'ddagpe';
    var _0xc7b9ae;
    var _0x621ace = $(e)['parents']("nocted.".split("").reverse().join(""))['attr']("goodstype");
    _0xc7b9ae = 302863 ^ 302862;
    if (_0x25_0x2f6 == "01G".split("").reverse().join("") && _0x621ace == "100001") {
        if (isNaN(parseInt(_0xc4be)) || parseInt(_0xc4be) % (146799 ^ 146699) != (747053 ^ 747053)) {
            $(e)['parents'](".detcon")['find']("nomteglla.".split("").reverse().join(""))['text'](452046 ^ 452046);
            layer['msg']("数整的001入输能只".split("").reverse().join(""));
            return;
        }
    }
    var _0xb39f9f = (486701 ^ 486702) + (662872 ^ 662865);
    var _0x0b94de = $(e)['parents'](".detcon")['find']("#unitPrice")['val']();
    _0xb39f9f = 345056 ^ 345061;
    if (_0xc4be != '' && _0x0b94de != '') {
        $(e)['parents'](".detcon")['find'](".allgetmon")['text'](cutXiaoNum(mul(_0xc4be, _0x0b94de), 821889 ^ 821891));
    }
}
function initMarketSHtml(paramObj, goodsList) {
    if (listTemplate == "bxy_tsil".split("").reverse().join("")) {
        initMarketSHtml_YXB(goodsList);
    } else if (listTemplate == "tnuocca_tsil".split("").reverse().join("")) {
        initMarketSHtml_ACCOUNT(paramObj, goodsList);
    } else {
        initMarketSHtml_ZB(paramObj, goodsList);
    }
}
function initHomePageSearchCookie(paramObj) {
    var _0x6cba;
    var _0x460eca = null;
    _0x6cba = (555338 ^ 555331) + (557350 ^ 557349);
    var _0xb30c = $(".game-camp .extattr-item .filter-extend")['attr']("data-val-eid");
    if (_0xb30c != null && paramObj['extendAttrList'] != null) {
        for (var i = 723109 ^ 723109; i < paramObj['extendAttrList']['length']; i++) {
            if (_0xb30c == paramObj['extendAttrList'][i]['eid']) {
                if (paramObj['extendAttrList'][i]['ev'] != null) {
                    _0x460eca = paramObj['extendAttrList'][i]['ev'];
                } else if (paramObj['extendAttrList'][i]['evs'] != null) {
                    _0x460eca = paramObj['extendAttrList'][i]['evs'][282807 ^ 282807];
                }
            }
        }
    }
    var _0x8c8bd;
    var _0xfdbgef = {
        "gameid": paramObj['gameId'],
        "goodschannel": paramObj['gtid'],
        'groupid': paramObj['groupId'],
        'serverid': paramObj['serverId'],
        "carrierid": paramObj['carrierId'],
        "camp": _0x460eca
    };
    _0x8c8bd = (941209 ^ 941209) + (905073 ^ 905078);
    $['cookie']("hcraes_egap_emoh".split("").reverse().join(""), JSON['stringify'](_0xfdbgef), {
        'expires': 14,
        'domain': '.7881.com'
    });
}
function initLoadTemplate() {
    var _0xd0a7d = '';
    _0xd0a7d += "<div class="list-loading"></div>";
    $("xob-tsil.".split("").reverse().join(""))['empty']()['append'](_0xd0a7d);
}
function initMarketSHtml_ZB(paramObj, goodsList) {
    if (defaultViewType == "2") {
        initMarketSHtml_ZB_TW(paramObj, goodsList);
    } else {
        initMarketSHtml_ZB_WZ(goodsList);
    }
}
function initMarketSHtml_ZB_TW(paramObj, goodsList) {
    var _0xac_0x1eb;
    var _0x8211e = initRecommendGoods(paramObj);
    _0xac_0x1eb = (599994 ^ 599986) + (761883 ^ 761882);
    var _0xgb_0xd44 = "";
    for (var i = 365836 ^ 365836; i < goodsList['length']; i++) {
        if (_0x8211e['length'] > (848981 ^ 848981)) {
            for (var j = 347387 ^ 347387; j < _0x8211e['length']; j++) {
                var _0x9g5c5a;
                var _0x2ac5aa = _0x8211e[j];
                _0x9g5c5a = (437766 ^ 437764) + (499071 ^ 499070);
                if (_0x2ac5aa['position'] == i + (379990 ^ 379991)) {
                    var _0xa96d;
                    var _0xe4_0x4e5 = _0x2ac5aa['goodsInfoList'];
                    _0xa96d = "pmgano".split("").reverse().join("");
                    if (_0xe4_0x4e5['length'] > (875469 ^ 875469)) {
                        _0xgb_0xd44 += initYXSJ_ZB(_0xe4_0x4e5);
                    }
                }
            }
        }
        var _0x27_0x665 = goodsList[i];
        var _0xc82b = "";
        _0xc82b += "<div class="list-dl-item">";
        _0xc82b += "\"=disdoog-lav-atad \"tfel-tsil\"=ssalc vid<".split("").reverse().join("") + _0x27_0x665['goodsId'] + "\"=diemag-lav-atad \"".split("").reverse().join("") + _0x27_0x665['gameId'] + "\"=ditg-lav-atad \"".split("").reverse().join("") + _0x27_0x665['gtid'] + ">\"".split("").reverse().join("");
        _0xc82b += "\"=crs gmi<".split("").reverse().join("") + _0x27_0x665['defaultImg'] + ""/>";
        _0xc82b += "</div>";
        _0xc82b += ">\"thgir-tsil\"=ssalc vid<".split("").reverse().join("");
        _0xc82b += "\"=eltit-atad \"eltit\"=ssalc 3h<".split("").reverse().join("") + escapeHTML(_0x27_0x665['title']) + "">";
        _0xc82b += "<a href="javascript: openGoodsDetailPage('" + _0x27_0x665['goodsId'] + ">\";)'' ,'".split("").reverse().join("") + escapeHTML(_0x27_0x665['title']) + ">a/<".split("").reverse().join("");
        _0xc82b += ">3h/<".split("").reverse().join("");
        _0xc82b += ">\"tob-thgir\"=ssalc vid<".split("").reverse().join("");
        _0xc82b += "<div class="bot-left">";
        _0xc82b += ">\"meti-gat\"=ssalc vid<".split("").reverse().join("") + initTags(_0x27_0x665) + "</div>";
        _0xc82b += "<div class="server-box">";
        _0xc82b += "<p>";
        _0xc82b += ">i<：服区戏游>naps<".split("").reverse().join("");
        _0xc82b += initListQFInfo(_0x27_0x665);
        if (_0x27_0x665['kqgroupName'] != null && _0x27_0x665['kqgroupName'] != '') {
            _0xc82b += "<span class="hutongtip" data-val-kqid="" + _0x27_0x665['kqid'] + "\"=crs gmi<>\"".split("").reverse().join("") + bucketDomain + ">naps/<>/\"gnp.gnotuh/4202-tsil/segami/1887/".split("").reverse().join("");
        }
        _0xc82b += "</i></span>";
        _0xc82b += "<em>|</em>";
        _0xc82b += "<span>商品类型：<i>" + _0x27_0x665['goodsTypeName'] + "</i></span>";
        _0xc82b += ">me/<|>me<".split("").reverse().join("");
        _0xc82b += "<span>商品库存：<i class="blue">" + _0x27_0x665['stock'] + "</i></span>";
        _0xc82b += "</p>";
        _0xc82b += "</div>";
        _0xc82b += ">\"xob-revres\"=ssalc vid<".split("").reverse().join("");
        _0xc82b += ">p<".split("").reverse().join("");
        _0xc82b += "<span>卖家信誉：" + initSellStar(_0x27_0x665['totalTradeCount']) + ">naps/<".split("").reverse().join("");
        _0xc82b += "</p>";
        _0xc82b += "</div>";
        _0xc82b += ">vid/<".split("").reverse().join("");
        _0xc82b += ">\"thgir-tob\"=ssalc vid<".split("").reverse().join("");
        _0xc82b += "\xA5>4h<".split("").reverse().join("") + _0x27_0x665['price'] + "</h4>";
        if (_0x27_0x665['supportTalk'] == "1") {
            _0xc82b += "<a href="javascript: openIm('" + _0x27_0x665['goodsId'] + "', '')" class="btn-com-01 color01">聊一聊</a>";
        } else {
            _0xc82b += "<a href="javascript: openGoodsDetailPage('" + _0x27_0x665['goodsId'] + ">a/<品商看查>\"10roloc 10-moc-ntb\"=ssalc \";)'' ,'".split("").reverse().join("");
        }
        _0xc82b += "</div>";
        _0xc82b += "</div>";
        _0xc82b += "</div>";
        _0xc82b += "</div>";
        _0xgb_0xd44 += _0xc82b;
    }
    $("gnidaol-tsil.".split("").reverse().join(""))['hide']();
    $(".list-box")['empty']()['append'](_0xgb_0xd44);
}
function initYXSJ_ZB(recommendList) {
    var _0x3bdd;
    var _0x7101be = "";
    _0x3bdd = (524467 ^ 524470) + (668768 ^ 668776);
    _0x7101be += "<div class="no-class">";
    for (var i = 680656 ^ 680656; i < recommendList['length']; i++) {
        var _0x81f0a = recommendList[i];
        _0x7101be += ">\"sdoog-efas meti-ld-tsil\"=ssalc vid<".split("").reverse().join("");
        _0x7101be += ">\"eltit-efas\"=ssalc vid<".split("").reverse().join("");
        _0x7101be += "<img src="" + bucketDomain + "/7881/images/list-2024/safe-icon-02.png"/>";
        _0x7101be += "<img src="" + bucketDomain + ">/\"gnp.10-noci-efas/4202-tsil/segami/1887/".split("").reverse().join("");
        _0x7101be += "</div>";
        _0x7101be += "\"=disdoog-lav-atad \"tfel-tsil\"=ssalc vid<".split("").reverse().join("") + _0x81f0a['goodsId'] + "" data-val-gameid="" + _0x81f0a['gameId'] + "" data-val-gtid="" + _0x81f0a['gtid'] + "">";
        _0x7101be += "<img src="" + _0x81f0a['defaultImg'] + ""/>";
        _0x7101be += ">vid/<".split("").reverse().join("");
        _0x7101be += "<div class="list-right">";
        _0x7101be += "\"=eltit-atad \"eltit\"=ssalc 3h<".split("").reverse().join("") + escapeHTML(_0x81f0a['title']) + "">";
        _0x7101be += "<a href="javascript: openGoodsDetailPage('" + _0x81f0a['goodsId'] + "', '');">" + escapeHTML(_0x81f0a['title']) + "</a>";
        _0x7101be += ">3h/<".split("").reverse().join("");
        _0x7101be += "<div class="right-bot">";
        _0x7101be += ">\"tfel-tob\"=ssalc vid<".split("").reverse().join("");
        _0x7101be += "<div class="tag-item">" + initTags(_0x81f0a) + "</div>";
        _0x7101be += "<div class="server-box">";
        _0x7101be += "<p>";
        _0x7101be += ">i<：服区戏游>naps<".split("").reverse().join("");
        _0x7101be += initListQFInfo(_0x81f0a);
        if (_0x81f0a['kqgroupName'] != null && _0x81f0a['kqgroupName'] != '') {
            _0x7101be += "<span class="hutongtip" data-val-kqid="" + _0x81f0a['kqid'] + "\"=crs gmi<>\"".split("").reverse().join("") + bucketDomain + ">naps/<>/\"gnp.gnotuh/4202-tsil/segami/1887/".split("").reverse().join("");
        }
        _0x7101be += ">naps/<>i/<".split("").reverse().join("");
        _0x7101be += "<em>|</em>";
        _0x7101be += "<span>商品类型：<i>" + _0x81f0a['goodsTypeName'] + ">naps/<>i/<".split("").reverse().join("");
        _0x7101be += "<em>|</em>";
        _0x7101be += "<span>商品库存：<i class="blue">" + _0x81f0a['stock'] + "</i></span>";
        _0x7101be += "</p>";
        _0x7101be += ">vid/<".split("").reverse().join("");
        _0x7101be += ">\"xob-revres\"=ssalc vid<".split("").reverse().join("");
        _0x7101be += "<p>";
        _0x7101be += "<span>卖家信誉：" + initSellStar(_0x81f0a['totalTradeCount']) + "</span>";
        _0x7101be += "</p>";
        _0x7101be += "</div>";
        _0x7101be += "</div>";
        _0x7101be += "<div class="bot-right">";
        _0x7101be += "<h4>¥" + _0x81f0a['price'] + "</h4>";
        if (_0x81f0a['supportTalk'] == "1") {
            _0x7101be += "<a href="javascript: openIm('" + _0x81f0a['goodsId'] + ">a/<聊一聊>\"10roloc 10-moc-ntb\"=ssalc \")'' ,'".split("").reverse().join("");
        } else {
            _0x7101be += "<a href="javascript: openGoodsDetailPage('" + _0x81f0a['goodsId'] + "', '');" class="btn-com-01 color01">查看商品</a>";
        }
        _0x7101be += "</div>";
        _0x7101be += "</div>";
        _0x7101be += "</div>";
        _0x7101be += "</div>";
    }
    _0x7101be += ">vid/<".split("").reverse().join("");
    return _0x7101be;
}
function initMarketSHtml_ZB_WZ(goodsList) {
    var _0xfc_0xd9d = "";
    for (var i = 190238 ^ 190238; i < goodsList['length']; i++) {
        var _0x1g5b = (947566 ^ 947564) + (616480 ^ 616487);
        var _0x28_0xe23 = goodsList[i];
        _0x1g5b = 707460 ^ 707469;
        var _0x6989f = "";
        _0x6989f += ">\"tluafed-meti-tsil\"=ssalc vid<".split("").reverse().join("");
        _0x6989f += "<div class="list-title-box">";
        _0x6989f += ">3h<".split("").reverse().join("");
        _0x6989f += initTags(_0x28_0xe23);
        _0x6989f += "<a href="javascript: openGoodsDetailPage('" + _0x28_0xe23['goodsId'] + ">\";)'' ,'".split("").reverse().join("") + escapeHTML(_0x28_0xe23['title']) + ">a/<".split("").reverse().join("");
        _0x6989f += "</h3>";
        _0x6989f += "<p>";
        _0x6989f += "：服区戏游".split("").reverse().join("") + initListQFInfo(_0x28_0xe23);
        if (_0x28_0xe23['kqgroupName'] != null && _0x28_0xe23['kqgroupName'] != '') {
            _0x6989f += "<span class="hutongtip" data-val-kqid="" + _0x28_0xe23['kqid'] + ""><img src="" + bucketDomain + "/7881/images/list-2024/hutong.png"/></span>";
        }
        _0x6989f += ">p/<".split("").reverse().join("");
        _0x6989f += "<p>商品类型：" + _0x28_0xe23['goodsTypeName'] + ">me<：存库>\"kcots\"=ssalc naps<".split("").reverse().join("") + _0x28_0xe23['stock'] + "：誉信家卖>\"kcots\"=ssalc naps<>naps/<>me/<".split("").reverse().join("") + initSellStar(_0x28_0xe23['totalTradeCount']) + ">p/<>naps/<".split("").reverse().join("");
        _0x6989f += ">vid/<".split("").reverse().join("");
        _0x6989f += ">\"xob-ecirp\"=ssalc vid<".split("").reverse().join("");
        _0x6989f += "<h3>¥" + _0x28_0xe23['price'] + "</h3>";
        _0x6989f += "</div>";
        _0x6989f += "<div class="btn-box">";
        if (_0x28_0xe23['supportTalk'] == "1") {
            _0x6989f += "<a href="javascript: openIm('" + _0x28_0xe23['goodsId'] + "', '')" class="btn-com-01 color01">聊一聊</a>";
        } else {
            _0x6989f += "<a href="javascript: openGoodsDetailPage('" + _0x28_0xe23['goodsId'] + "', '');" class="btn-com-01 color01">查看商品</a>";
        }
        if (_0x28_0xe23['deliveryTimeByRule'] != null && _0x28_0xe23['deliveryTimeByRule'] != '') {
            _0x6989f += "<p>平均<span>" + _0x28_0xe23['deliveryTimeByRule'] + "</span>发货</p>";
        }
        _0x6989f += "</div>";
        _0x6989f += "</div>";
        _0xfc_0xd9d += _0x6989f;
    }
    $("gnidaol-tsil.".split("").reverse().join(""))['hide']();
    $(".list-box")['empty']()['append'](_0xfc_0xd9d);
}
function initTags(goodsInfo) {
    if (goodsInfo == undefined) {
        return "";
    }
    var _0xd6g5b = "";
    if (goodsInfo['goodsFlagDictionaryDTO']['recoverCompensationForverService']) {
        _0xd6g5b += "\"=crs gmi<>naps<".split("").reverse().join("") + bucketDomain + ">naps/<>/\"gnp.l-pbzy/noci-ecivres/segami/1887/".split("").reverse().join("");
    }
    if (goodsInfo['goodsFlagDictionaryDTO']['foreverAxgCompensationService']) {
        _0xd6g5b += "<span><img src="" + bucketDomain + "/7881/images/service-icon/zcbp-l.png" height="18" /></span>";
    }
    if (goodsInfo['goodsFlagDictionaryDTO']['faceCompensationService']) {
        _0xd6g5b += "<span><img src="" + bucketDomain + "/7881/images/service-icon/rlbp-l.png" height="18" /></span>";
    }
    if (goodsInfo['goodsFlagDictionaryDTO']['axgCompensationService']) {
        if (goodsInfo['gtid'] != "100003") {
            _0xd6g5b += "\"=crs gmi<>naps<".split("").reverse().join("") + bucketDomain + "/7881/images/service-icon/naxg-l.png" height="18" /></span>";
        } else {
            _0xd6g5b += "\"=crs gmi<>naps<".split("").reverse().join("") + bucketDomain + ">naps/<>/ \"81\"=thgieh \"gnp.l-gxa/noci-ecivres/segami/1887/".split("").reverse().join("");
        }
    }
    if (goodsInfo['supportReport'] == "1") {
        _0xd6g5b += "<span><img src="" + bucketDomain + "/7881/images/service-icon/gfyh-l.png"/></span>";
    }
    if (goodsInfo['goodsFlagDictionaryDTO']['sellerCompensationService']) {
        _0xd6g5b += "<span><img src="" + bucketDomain + "/7881/images/service-icon/sjbp-l.png" height="18" /></span>";
    }
    if (goodsInfo['goodsFlagDictionaryDTO']['screenshotService']) {
        _0xd6g5b += "<span><img src="" + bucketDomain + "/7881/images/service-icon/jtfw-l.png" height="18" /></span>";
    }
    if (goodsInfo['goodsFlagDictionaryDTO']['accountTransferService']) {
        _0xd6g5b += "<span><img src="" + bucketDomain + "/7881/images/service-icon/zhgh-l.png" height="18" /></span>";
    }
    if (goodsInfo['goodsFlagDictionaryDTO']['roleSeparationService']) {
        _0xd6g5b += "\"=crs gmi<>naps<".split("").reverse().join("") + bucketDomain + ">naps/<>/ \"81\"=thgieh \"gnp.l-lfsj/noci-ecivres/segami/1887/".split("").reverse().join("");
    }
    if (goodsInfo['tradeType'] == "db" && goodsInfo['autoDeliverType'] != "1") {
        _0xd6g5b += "\"=crs gmi<>naps<".split("").reverse().join("") + bucketDomain + "/7881/images/service-icon/mjfh-l.png" height="18" /></span>";
    }
    if (goodsInfo['tradeType'] == "js" && goodsInfo['gtid'] != "100003") {
        _0xd6g5b += "\"=crs gmi<>naps<".split("").reverse().join("") + bucketDomain + "/7881/images/service-icon/ptdf-l.png" height="18" /></span>";
    }
    if (goodsInfo['goodsFlagDictionaryDTO']['goldMedalGuarantee']) {
        _0xd6g5b += "\"=crs gmi<>naps<".split("").reverse().join("") + bucketDomain + "/7881/images/service-icon/jpdb-l.png" height="18" /></span>";
    }
    if (goodsInfo['epRateShow'] != null && goodsInfo['epRateShow'] != '') {
        _0xd6g5b += "\"=crs gmi<>\"xob-bjx\"=ssalc vid<".split("").reverse().join("") + bucketDomain + ">me<>/\"03\"=htdiw \"gnp.noci-bjx/4202-tsil/segami/1887/".split("").reverse().join("") + goodsInfo['epRateShow'] + "</em></div>";
    }
    if (goodsInfo['showHotSortTag'] && goodsInfo['hotScore'] != null && goodsInfo['hotScore'] > (449088 ^ 449088)) {
        _0xd6g5b += "\"=crs gmi<>\"xob-toh\"=ssalc vid<".split("").reverse().join("") + bucketDomain + "/7881/images/list-2024/hot-icon.png" width="16"/><em>" + goodsInfo['hotScore'] + "</em></div>";
    }
    if (goodsInfo['discountActFlag'] == "1") {
        _0xd6g5b += "<span><img src="" + bucketDomain + ">naps/<>/ \"81\"=thgieh \"gnp.l-tbsx/noci-ecivres/segami/1887/".split("").reverse().join("");
    }
    if (goodsInfo['goodsFlagDictionaryDTO']['jpdlService']) {
        _0xd6g5b += "<span><img src="" + bucketDomain + ">naps/<>/\"gnp.l-ldpj/noci-ecivres/segami/1887/".split("").reverse().join("");
    }
    return _0xd6g5b;
}
function toDiscountPage() {
    window['open']("https://act.7881.com/pc/20241014-zhekou/index.html");
}
function initMallTags(goodsInfo) {
    if (goodsInfo == undefined) {
        return "";
    }
    var _0x4ec45f = (344043 ^ 344043) + (995244 ^ 995237);
    var _0xa8f = 275682 ^ 275681;
    _0x4ec45f = (422100 ^ 422096) + (200469 ^ 200476);
    var _0x569c8c = (942466 ^ 942471) + (990260 ^ 990262);
    var _0xe759d = 862167 ^ 862167;
    _0x569c8c = (546550 ^ 546558) + (533824 ^ 533824);
    var _0xa7e1d = "";
    if (goodsInfo['goodsFlagDictionaryDTO']['axgCompensationService'] && _0xe759d < _0xa8f) {
        _0xa7e1d += "<p title="" + goodsInfo['goodsFlagDictionaryDTO']['axgCompensationServiceMsg'] + ""><em class="tags icon-aheart"></em>可买安心购</p>";
        _0xe759d = _0xe759d + (655806 ^ 655807);
    }
    if (goodsInfo['goodsFlagDictionaryDTO']['overTimeDepositService'] && _0xe759d < _0xa8f) {
        _0xa7e1d += "\"=eltit p<".split("").reverse().join("") + goodsInfo['goodsFlagDictionaryDTO']['overTimeDepositServiceMsg'] + ""><em class="tags icon-pfjfw"></em>超时赔付</p>";
        _0xe759d = _0xe759d + (148292 ^ 148293);
    }
    if (goodsInfo['goodsFlagDictionaryDTO']['noClaimService'] && _0xe759d < _0xa8f) {
        _0xa7e1d += "\"=eltit p<".split("").reverse().join("") + goodsInfo['goodsFlagDictionaryDTO']['noClaimServiceMsg'] + ""><em class="tags icon-whpf"></em>无货赔付</p>";
        _0xe759d = _0xe759d + (638981 ^ 638980);
    }
    if (goodsInfo['goodsFlagDictionaryDTO']['flexiblePurchaseService'] && _0xe759d < _0xa8f) {
        _0xa7e1d += "<p title="" + goodsInfo['goodsFlagDictionaryDTO']['flexiblePurchaseServiceMsg'] + ">p/<买购活灵>me/<>\"nad-noci sgat\"=ssalc me<>\"".split("").reverse().join("");
        _0xe759d = _0xe759d + (499155 ^ 499154);
    }
    if (goodsInfo['goodsFlagDictionaryDTO']['lightningShipmentService'] && _0xe759d < _0xa8f) {
        _0xa7e1d += "\"=eltit p<".split("").reverse().join("") + goodsInfo['goodsFlagDictionaryDTO']['lightningShipmentServiceMsg'] + ""><em class="tags icon-shan"></em>闪电发货</p>";
    }
    return _0xa7e1d;
}
function initListQFInfo(goodsInfo) {
    var _0x8g80b;
    var _0x5e8c9d = [];
    _0x8g80b = 'kllapf';
    var _0x8a2d;
    var _0x9b8b = goodsInfo['kqgroupName'];
    _0x8a2d = "ebpgoj".split("").reverse().join("");
    if (listTemplate == "list_account") {
        if (goodsInfo['gameName'] != null && goodsInfo['gameName'] != '') {
            _0x5e8c9d['push'](goodsInfo['gameName']);
        }
        if (goodsInfo['carrierName'] != null && goodsInfo['carrierName'] != '') {
            _0x5e8c9d['push'](goodsInfo['carrierName']);
        }
        if (goodsInfo['groupName'] != null && goodsInfo['groupName'] != '') {
            _0x5e8c9d['push'](goodsInfo['groupName']);
        }
        if (goodsInfo['serverName'] != null && goodsInfo['serverName'] != '') {
            _0x5e8c9d['push'](goodsInfo['serverName']);
        }
    } else {
        if (goodsInfo['groupName'] != null && goodsInfo['groupName'] != '') {
            _0x5e8c9d['push'](goodsInfo['groupName']);
        }
        if (goodsInfo['serverName'] != null && goodsInfo['serverName'] != '') {
            _0x5e8c9d['push'](goodsInfo['serverName']);
        }
    }
    var _0xf820ge = '';
    if (_0x5e8c9d['length'] > (986346 ^ 986346)) {
        _0xf820ge += _0x5e8c9d['join']("/");
    }
    if (_0x9b8b != undefined && _0x9b8b != null && _0x9b8b != '') {
        _0xf820ge += "(" + _0x9b8b + ")";
    }
    return _0xf820ge;
}
function showKuaInfo(obj) {
    $['ajax']({
        'type': "get",
        "url": kuaInfoUrl + "=dIauk?".split("").reverse().join("") + $(obj)['attr']("diqk-lav-atad".split("").reverse().join("")),
        'dataType': "json",
        "async": false,
        "xhrFields": {
            "withCredentials": !![]
        },
        "success": function(data) {
            if (data['code'] == "0" && data['body'] != null && data['body']['groupServerList'] != null) {
                var _0x2b0d2b = '';
                $(data['body']['groupServerList'])['each'](function(index, item) {
                    _0x2b0d2b += "[ ".split("").reverse().join("") + item['groupName'] + "/" + item['serverName'] + "]";
                });
                _0x2b0d2b = "和" + _0x2b0d2b + "游戏官方数据互通，互通区服商品可进行交易";
                layer['tips'](_0x2b0d2b, obj, {
                    'skin': "hutong-pop",
                    'tips': [225735 ^ 225732, "000000#".split("").reverse().join("")],
                    "time": 0
                });
            }
        }
    });
}
function copyGoodsListShortLink() {
    var _0x0999c;
    var _0x7f_0x1b2 = location['href'];
    _0x0999c = 773250 ^ 773252;
    var _0x2a78cf = (759655 ^ 759649) + (794318 ^ 794317);
    var _0xb3_0x513 = {};
    _0x2a78cf = 838189 ^ 838191;
    _0xb3_0x513['sourceLink'] = _0x7f_0x1b2;
    _0xb3_0x513['linkType'] = 693280 ^ 693282;
    _0xb3_0x513['description'] = "链短广推页表列品商盟联广推CP".split("").reverse().join("");
    $['ajax']({
        'type': 'post',
        "url": shortLinkUrl,
        "dataType": "json",
        'data': JSON['stringify'](_0xb3_0x513),
        "async": false,
        'contentType': "application/json",
        'xhrFields': {
            'withCredentials': !![]
        },
        "success": function(data) {
            if (data != null && data['code'] == (621937 ^ 621937)) {
                var _0x595a9a = data['body']['url'];
                if (_0x595a9a != null && _0x595a9a != '') {
                    copySelf(".fy", _0x595a9a, "推广链接复制成功");
                } else {
                    layer['msg']("败失制复接链广推".split("").reverse().join(""));
                }
            } else {
                layer['msg'](data['msg']);
            }
        }
    });
}
function loadMarketQueryHis() {
    $['ajax']({
        'url': searchHisUrl + "=dIemag?".split("").reverse().join("") + gameId + "&gtId=" + gtId + "01=tnc&".split("").reverse().join(""),
        'async': false,
        'type': "GET",
        "dataType": "json",
        "contentType": "application/json",
        'xhrFields': {
            "withCredentials": !![]
        },
        "success": function(result) {
            if (result['code'] == (993705 ^ 993705) && result['body']['length'] > (791206 ^ 791206)) {
                var _0xa1f4bd;
                var _0x991caf = '';
                _0xa1f4bd = (525171 ^ 525179) + (737433 ^ 737438);
                _0x991caf += "<ul>";
                for (var i = 907761 ^ 907761; i < result['body']['length']; i++) {
                    var _0xf83ed;
                    var _0x07c4eb = i + (671769 ^ 671768);
                    _0xf83ed = "ebmfnq".split("").reverse().join("");
                    var _0x7f89ca;
                    var _0x58a97a = result['body'][i]['showValues'];
                    _0x7f89ca = (558875 ^ 558873) + (111333 ^ 111330);
                    if (_0x58a97a['indexOf']("担保") > -(670656 ^ 670657)) {
                        _0x58a97a = _0x58a97a['replaceAll']("保担".split("").reverse().join(""), "货发家卖".split("").reverse().join(""));
                    }
                    if (_0x58a97a['indexOf']("寄售") > -(403802 ^ 403803)) {
                        _0x58a97a = _0x58a97a['replaceAll']("寄售", "发代台平".split("").reverse().join(""));
                    }
                    _0x991caf += "<li data-val-id="" + result['body'][i]['id'] + "" data-val-gameid="" + result['body'][i]['gameId'] + "\"=ditg-lav-atad \"".split("").reverse().join("") + result['body'][i]['gtId'] + "" data-val-groupid="" + result['body'][i]['groupId'] + "" data-val-serverid="" + result['body'][i]['serverId'] + "" data-val-carrierid="" + result['body'][i]['carrierId'] + ""><p><em>" + _0x07c4eb + ".</em>" + _0x58a97a + ">naps<>p/<".split("").reverse().join("") + result['body'][i]['createTime'] + ">il/<>naps/<".split("").reverse().join("");
                }
                _0x991caf += ">lu/<".split("").reverse().join("");
                $("neercs-retlif.".split("").reverse().join(""))['find'](".filter-his-pop .his-pop-bottom")['empty']()['append'](_0x991caf);
                return;
            }
            $(".filter-screen")['find'](".filter-his-pop .his-pop-bottom")['empty']();
        },
        'error': function(result) {
            return;
        }
    });
}
function cleanAllParam() {
    minPrice = undefined;
    $("#min-price")['val']("");
    maxPrice = undefined;
    $("ecirp-xam#".split("").reverse().join(""))['val']("");
    serviceId = undefined;
    tradeType = undefined;
    supportReport = undefined;
    tradePlace = "0";
    keyword = undefined;
    $(".filter-search")['find'](".keyword")['val']("");
    goodsSortType = undefined;
    tagValue = undefined;
    fiveStarSellerFlag = undefined;
    cleanQuickChose();
    queryGoodsMarket("true");
}
function buyMallGoods(e) {
    var _0xc2291d = (784285 ^ 784284) + (181247 ^ 181247);
    var _0xb5e9d = $(e)['parents']("meti-pohs.".split("").reverse().join(""));
    _0xc2291d = (300099 ^ 300096) + (268833 ^ 268834);
    var _0x245bdf = $(_0xb5e9d)['attr']("data-val-goodsid");
    var _0x074ggf = (410409 ^ 410413) + (259818 ^ 259817);
    var _0xbf_0x6ed = $(_0xb5e9d)['attr']("munrep-lav-atad".split("").reverse().join(""));
    _0x074ggf = 'meggkp';
    var _0xa6_0x412 = $(_0xb5e9d)['attr']("ecirp-lav-atad".split("").reverse().join(""));
    var _0x656f6f;
    $(_0xb5e9d)['find'](".part-03")['find']("input[type='radio']")['each'](function(index, e) {
        if ($(e)['attr']("checked") == "dekcehc".split("").reverse().join("")) {
            _0x656f6f = $(e)['val']();
        }
    });
    if (_0x656f6f == undefined) {
        return;
    }
    if (_0x656f6f != "1" && _0x656f6f != "2") {
        layer['msg']("！常异式方买购".split("").reverse().join(""));
        return;
    }
    var _0xbf45fe;
    var _0xfbb8a;
    _0xbf45fe = "ldgmec".split("").reverse().join("");
    var _0x5d_0xfff = (787340 ^ 787333) + (971689 ^ 971681);
    var _0xad7d9c;
    _0x5d_0xfff = (226523 ^ 226520) + (257133 ^ 257128);
    if (_0x656f6f == "1") {
        _0xfbb8a = $(_0xb5e9d)['find'](".part-03 .r input")['val']();
        if (_0xfbb8a == undefined || _0xfbb8a == null || _0xfbb8a == '') {
            layer['msg']("购买数量异常！");
            return;
        }
        var _0x5_0x3c5 = (366533 ^ 366534) + (845872 ^ 845880);
        var _0x0e6d8d = $(_0xb5e9d)['attr']("data-val-pu");
        _0x5_0x3c5 = 'ddlphd';
        _0xad7d9c = cutXiaoNum(div(mul(_0xfbb8a, _0x0e6d8d), _0xbf_0x6ed), 353931 ^ 353929);
    }
    if (_0x656f6f == "2") {
        _0xad7d9c = $(_0xb5e9d)['find']("tupni r. 30-trap.".split("").reverse().join(""))['val']();
        if (_0xad7d9c == undefined || _0xad7d9c == null || _0xad7d9c == '') {
            layer['msg']("！常异额金买购".split("").reverse().join(""));
            return;
        }
        var _0xe7804d = (710156 ^ 710149) + (692069 ^ 692064);
        var _0x9f123f = $(_0xb5e9d)['attr']("data-val-up");
        _0xe7804d = 'ckigcm';
        _0xfbb8a = parseInt(div(mul(_0xad7d9c, _0x9f123f), _0xbf_0x6ed));
    }
    var _0xg21e9d = $(_0xb5e9d)['attr']("data-val-stock");
    if (parseInt(_0xfbb8a) > parseInt(_0xg21e9d)) {
        layer['msg']("当前库存不足！");
        return;
    }
    var _0xc2_0x5e7;
    var _0x8b469c = $(_0xb5e9d)['attr']("data-val-buy-money-min");
    _0xc2_0x5e7 = 'jclfne';
    if (_0x8b469c != undefined && _0x8b469c != null && _0x8b469c != '' && parseFloat(_0xad7d9c) < parseFloat(_0x8b469c)) {
        layer['msg']("于低得不额金买购".split("").reverse().join("") + _0x8b469c + "元！");
        return;
    }
    if ((gameId == "G10" || gameId == "G3415") && gtId == "800001".split("").reverse().join("")) {
        if (parseInt(_0xfbb8a) % (629498 ^ 629406) != (872024 ^ 872024)) {
            layer['msg']("购买数量必须为100的整数倍！");
            return;
        }
    }
    if (gameId == "6375G".split("").reverse().join("") && gtId == "100001".split("").reverse().join("")) {
        if (parseInt(_0xfbb8a) % (229990 ^ 238966) != (922468 ^ 922468)) {
            layer['msg']("由于游戏本身交易性质，购买数量必须为10000的整数倍，请修改购买数量！");
            return;
        }
    }
    window['open'](tradeDomain + "/trade-" + _0x245bdf + "=munrep?lmth.".split("").reverse().join("") + _0xbf_0x6ed + "&price=" + _0xa6_0x412 + "&buyNum=" + _0xfbb8a + "&gameId=" + gameId + "&gtId=" + gtId + "=dIpuorg&".split("").reverse().join("") + groupId + "&serverId=" + serverId + "=modnar&B=epyTrelles&".split("").reverse().join("") + Math['random'](), "_blank");
}
function openGoodsBuyingPage(goodsId, pernum, price, groupId, groupName, serverId, serverName) {
    if (typeof doCheckBuying != "denifednu".split("").reverse().join("") && $['isFunction'](doCheckBuying)) {
        if (!doCheckBuying()) {
            return false;
        }
    }
    if (listTemplate == "list_yxb") {
        showYxbGroupServerTips(goodsId, pernum, price, groupId, groupName, serverId, serverName);
        return;
    }
    buyLimitCheckSub(goodsId, pernum, price);
}
function buyLimitCheckSub(goodsId, pernum, price) {
    $['ajax']({
        'url': "=dIsdoog?timiLyuBsdooGyreuq/".split("").reverse().join("") + goodsId,
        "async": false,
        "type": "GET",
        "dataType": "json",
        'success': function(result) {
            if (result['code'] == "0") {
                window['open'](tradeDomain + "-edart/".split("").reverse().join("") + goodsId + ".html?pernum=" + pernum + "&price=" + price + "&random=" + Math['random'](), "_blank");
                return;
            } else if (result['code'] == "2") {
                layer['msg']("类目升级维护中");
                return;
            }
            layer['msg'](result['message']);
        },
        'error': function(result) {
            layer['msg']("系统繁忙，请稍后再试");
            return;
        }
    });
}
function showYxbGroupServerTips(goodsId, perNum, price, _groupId, _groupName, _serverId, _serverName) {
    var _0x869bb = $['cookie']("sutats_spiTrevreSpuorGbxYwohs".split("").reverse().join(""));
    var _0xb441ce;
    var _0xa2beag = groupId != null && groupId != '' && groupId != "0" && serverId != null && serverId != '' && serverId != "0";
    _0xb441ce = (368868 ^ 368876) + (230319 ^ 230319);
    var _0x1934d = gameType !== "0" || _0xa2beag || _0x869bb == "eurt".split("").reverse().join("");
    if (_0x1934d) {
        buyLimitCheckSub(goodsId, perNum, price);
        return;
    }
    var _0xa2c48b = $("pit-puorg.".split("").reverse().join(""))['html']();
    layer['open']({
        "type": 1,
        'title': '',
        'skin': "pop-tip",
        'area': ["360px"],
        "closeBtn": 0,
        "content": _0xa2c48b,
        "success": function() {
            $(".pop-tip")['find']("revreSpuorGsdoog.".split("").reverse().join(""))['text'](_groupName + "/" + _serverName);
            $(".pop-tip")['find']("buperus.".split("").reverse().join(""))['click'](function() {
                if ($(".pop-tip")['find']("input[name="notips"]:checked")['prop']("checked")) {
                    $['cookie']("showYxbGroupServerTips_status", "eurt".split("").reverse().join(""), {
                        'expires': 7
                    });
                }
                layer['closeAll']();
                var _0xbfg;
                var _0x08f = $(".screen-box")['offset']()['top'] - (787138 ^ 786954);
                _0xbfg = (324966 ^ 324974) + (125015 ^ 125022);
                $("body,html")['animate']({
                    'scrollTop': _0x08f
                }, 756180 ^ 755744);
            });
            $("pit-pop.".split("").reverse().join(""))['find']("bupelc.".split("").reverse().join(""))['click'](function() {
                if ($(".pop-tip")['find']("input[name="notips"]:checked")['prop']("dekcehc".split("").reverse().join(""))) {
                    $['cookie']("showYxbGroupServerTips_status", "true", {
                        'expires': 7
                    });
                }
                layer['closeAll']();
                buyLimitCheckSub(goodsId, perNum, price);
            });
        }
    });
}
function changeGoodsType(gtId) {
    if (gtId == undefined || gtId == null || gtId == '' || gtId == "0") {
        return;
    }
    var _0xe1d7cd = groupId;
    if (groupId == undefined || groupId == null || groupId == '') {
        _0xe1d7cd = "0";
    }
    var _0x277e = serverId;
    if (serverId == undefined || serverId == null || serverId == '') {
        _0x277e = "0";
    }
    var _0x32b96a = carrierId;
    if (carrierId == undefined || carrierId == null || carrierId == '') {
        _0x32b96a = "0";
    }
    var _0xfaef3a = (224922 ^ 224922) + (596990 ^ 596982);
    var _0x6c_0xe90 = "";
    _0xfaef3a = 994193 ^ 994198;
    if ($("noitomorp#".split("").reverse().join(""))['val']() == "1") {
        _0x6c_0xe90 = "promotion-list/";
    }
    var _0x3988g = (540351 ^ 540348) + (260608 ^ 260612);
    var _0x80ffdd = $(".filter-screen")['find'](".filter-item")['find'](".filter-pop-extend")['find'](".filter-pop-ext")['find'](".on")['attr']("data-value");
    _0x3988g = (685257 ^ 685261) + (258294 ^ 258303);
    if (_0x80ffdd == undefined || _0x80ffdd == '') {
        window['location']['href'] = "//search.7881.com/" + _0x6c_0xe90 + gameId + "-" + gtId + "-" + _0xe1d7cd + "-" + _0x277e + "-" + _0x32b96a + "lmth.".split("").reverse().join("");
    } else {
        window['location']['href'] = "/moc.1887.hcraes//".split("").reverse().join("") + _0x6c_0xe90 + gameId + "-" + gtId + "-" + _0xe1d7cd + "-" + _0x277e + "-" + _0x32b96a + "=pmac?lmth.".split("").reverse().join("") + _0x80ffdd;
    }
}
function initShareLink() {
    var _0xc3fed;
    var _0xe04afc = "";
    _0xc3fed = (727841 ^ 727844) + (516969 ^ 516972);
    var _0x8a82e = initShareParam();
    $['ajax']({
        "url": addShareLinkUrl,
        'async': false,
        'type': "POST",
        "data": JSON['stringify'](_0x8a82e),
        'dataType': "json",
        'contentType': 'application/json',
        'xhrFields': {
            "withCredentials": !![]
        },
        "success": function(result) {
            if (result['code'] == "0") {
                var _0x38aceg;
                var _0x3a30c = "";
                _0x38aceg = (369957 ^ 369959) + (202383 ^ 202374);
                if ($("noitomorp#".split("").reverse().join(""))['val']() == "1") {
                    _0x3a30c = "promotion-list/";
                }
                _0xe04afc = "/moc.1887.hcraes//:sptth".split("").reverse().join("") + _0x3a30c + gameId + "-" + gtId + "-" + groupId + "-" + serverId + "-" + carrierId + ".html?shareCode=" + result['body'];
            }
        },
        'error': function(result) {
            return;
        }
    });
    return _0xe04afc;
}
function initShareParam() {
    var _0xffea8e = new Object();
    _0xffea8e['gameId'] = gameId;
    _0xffea8e['gtid'] = gtId;
    if (groupId != undefined && groupId != null && groupId != "0") {
        _0xffea8e['groupId'] = groupId;
    }
    if (serverId != undefined && serverId != null && serverId != "0") {
        _0xffea8e['serverId'] = serverId;
    }
    if (carrierId != undefined && carrierId != null && carrierId != "0") {
        _0xffea8e['carrierId'] = carrierId;
    }
    if (minPrice != undefined && minPrice != null) {
        _0xffea8e['minPrice'] = minPrice;
    }
    if (maxPrice != undefined && maxPrice != null) {
        _0xffea8e['maxPrice'] = maxPrice;
    }
    if (serviceId != undefined && serviceId != null) {
        _0xffea8e['serviceId'] = serviceId;
    }
    if (tradeType != undefined && tradeType != null) {
        _0xffea8e['tradeType'] = tradeType;
    }
    if (supportReport != undefined && supportReport != null) {
        _0xffea8e['supportReport'] = supportReport;
    }
    if (fiveStarSellerFlag != undefined && fiveStarSellerFlag != null) {
        _0xffea8e['fiveStarSellerFlag'] = fiveStarSellerFlag;
    }
    if (keyword != undefined && keyword != null) {
        _0xffea8e['keyWord'] = keyword;
    }
    var _0x66ccf = initExtAttrList();
    if (_0x66ccf != null) {
        _0xffea8e['extendAttrList'] = _0x66ccf;
    }
    return _0xffea8e;
}
function changeSelectTip() {
    var _0xg935a = $['cookie']("GroupServer_NoTip");
    if (_0xg935a == "true") {
        $("spit-tceles-esohc.".split("").reverse().join(""))['hide']();
        return;
    }
    var _0x934d = (324996 ^ 324996) + (569391 ^ 569383);
    var _0x31_0xb45 = !![];
    _0x934d = (725183 ^ 725174) + (994983 ^ 994990);
    $(".filter-screen")['find']("tceles-esohc. wot-thgir. thgir-meti. meti-retlif.".split("").reverse().join(""))['each'](function(index, e) {
        if (_0x31_0xb45 && !$(e)['hasClass']("detceles".split("").reverse().join(""))) {
            _0x31_0xb45 = false;
            return;
        }
    });
    if ($(".filter-screen")['find'](".filter-item .item-right .right-tow .chose-item")['hasClass']("reirrac-emag".split("").reverse().join(""))) {
        var _0x56322b = !![];
        $("neercs-retlif.".split("").reverse().join(""))['find']("meti-esohc. wot-thgir. thgir-meti. meti-retlif.".split("").reverse().join(""))['each'](function(index, e) {
            if (_0x56322b && $(e)['hasClass']("on")) {
                _0x56322b = false;
                return;
            }
        });
        if (_0x56322b) {
            _0x31_0xb45 = false;
        }
    }
    if (_0x31_0xb45) {
        $("spit-tceles-esohc.".split("").reverse().join(""))['hide']();
        try {
            $['cookie']("GroupServer_NoTip", "true", {
                'expires': 7
            });
        } catch (e) {}
    } else {
        $(".chose-select-tips")['show']();
    }
}
function scrollGoodsTop() {
    if (doScrollTop) {
        doScrollTop = false;
        var _0x1d3baa = $("tsil-retlif.".split("").reverse().join(""))['offset']()['top'];
        $("lmth,ydob".split("").reverse().join(""))['animate']({
            'scrollTop': _0x1d3baa
        }, 286292 ^ 286624);
    }
}
function choseView() {
    var _0x3e575d = (794665 ^ 794665) + (618121 ^ 618122);
    var _0xgd_0x1b7 = $("weiv-esohc.".split("").reverse().join(""))['html']();
    _0x3e575d = 222425 ^ 222429;
    layer['open']({
        'type': 1,
        'title': '',
        "skin": "pop-chose",
        'area': ["700px", "510px"],
        'closeBtn': 0,
        "content": _0xgd_0x1b7,
        'success': function() {
            $(".pop-chose")['find']("a ntb-esohc.".split("").reverse().join(""))['click'](function() {
                layer['closeAll']();
            });
        }
    });
}
function addFilterDivKua(kuaId) {
    $("neercs-retlif.".split("").reverse().join(""))['find'](".filter-item .filter-show-kua")['show']()['find']("naps".split("").reverse().join(""))['attr']("data-val-kqid", kuaId);
    $("neercs-retlif.".split("").reverse().join(""))['find'](".filter-item .filter-show-kua .kua-tips")['text']("易交行进可品商服区通互".split("").reverse().join(""));
}
function removeFilterDivKua() {
    $(".filter-screen")['find'](".filter-item .filter-show-kua")['hide']();
}
function escapeHTML(goodsTitleStr) {
    if (goodsTitleStr == null || goodsTitleStr == '' || goodsTitleStr == undefined) {
        return "";
    }
    return goodsTitleStr['replace'](new RegExp('&','g'), "&amp;")['replace'](new RegExp('<','g'), ";tl&".split("").reverse().join(""))['replace'](new RegExp('>','g'), ";tg&".split("").reverse().join(""))['replace'](new RegExp('"','g'), "&quot;")['replace'](new RegExp(''','g'), "&#039;");
}
function realNamePop() {
    var _0x4417e = (785250 ^ 785248) + (434864 ^ 434870);
    var _0xdfdf = $(".two-realname")['html']();
    _0x4417e = 543357 ^ 543355;
    layer['open']({
        'type': 1,
        'title': '',
        'skin': "pop-money",
        'area': ["480px"],
        'closeBtn': 0,
        'content': _0xdfdf,
        'success': function() {
            $("reyal-iuyal.".split("").reverse().join(""))['find'](".Validform_checktip")['text']("")['css']("yalpsid".split("").reverse().join(""), "none");
            $("reyal-iuyal.".split("").reverse().join(""))['find'](".submit")['click'](function() {
                var _0x95a;
                var _0xdddd = $(".layui-layer")['find'](".real-name");
                _0x95a = (274623 ^ 274619) + (342263 ^ 342270);
                var _0x6baa = (952206 ^ 952201) + (457033 ^ 457024);
                var _0xcdc2e = $(".layui-layer")['find'](".id-card");
                _0x6baa = "qqaihh".split("").reverse().join("");
                var _0xdab = (340642 ^ 340650) + (863191 ^ 863189);
                var _0x16d = _0xdddd['val']()['trim']();
                _0xdab = "pglnce".split("").reverse().join("");
                var _0x24bac = _0xcdc2e['val']()['trim']();
                if (_0x16d == '') {
                    _0xdddd['addClass']("Validform_error");
                    _0xdddd['parent']()['find']("pitkcehc_mrofdilaV.".split("").reverse().join(""))['text']("请输入真实姓名")['show']();
                    return;
                } else {
                    var _0xeae33d;
                    var _0xb0a1fc = zsname(_0x16d);
                    _0xeae33d = (103657 ^ 103662) + (138963 ^ 138963);
                    if (_0xb0a1fc !== !![]) {
                        _0xdddd['addClass']("rorre_mrofdilaV".split("").reverse().join(""));
                        _0xdddd['parent']()['find']("pitkcehc_mrofdilaV.".split("").reverse().join(""))['text'](_0xb0a1fc)['show']();
                        return;
                    }
                }
                if (_0x24bac == '') {
                    _0xcdc2e['addClass']("rorre_mrofdilaV".split("").reverse().join(""));
                    _0xcdc2e['parent']()['find']("pitkcehc_mrofdilaV.".split("").reverse().join(""))['text']("请输入身份证号")['show']();
                    return;
                } else {
                    if (vadCardnum(_0x24bac)) {
                        realNameCard2(_0x16d, _0x24bac);
                    } else {
                        _0xcdc2e['addClass']("rorre_mrofdilaV".split("").reverse().join(""));
                        _0xcdc2e['parent']()['find'](".Validform_checktip")['text']("请填写正确的身份证号码")['show']();
                        return;
                    }
                }
            });
            $("reyal-iuyal.".split("").reverse().join(""))['find']("tupni".split("").reverse().join(""))['focus'](function() {
                $("reyal-iuyal.".split("").reverse().join(""))['find']("naps 4h".split("").reverse().join(""))['text']("")['hide']();
                $(this)['removeClass']("rorre_mrofdilaV".split("").reverse().join(""));
                $(this)['parent']()['find']("pitkcehc_mrofdilaV.".split("").reverse().join(""))['text']("")['hide']();
            });
        }
    });
}
function realNameCard2(_realName, _cardNumber) {
    var _0x23affc = JSON['stringify']({
        "realName": _realName,
        "cardNumber": _cardNumber,
        "authMode": 6,
        "channel": "1"
    });
    $['ajax']({
        "url": "//gw.7881.com/safe/api/realname/auth",
        'type': "POST",
        'data': _0x23affc,
        'dataType': 'json',
        'contentType': "application/json",
        'async': false,
        "xhrFields": {
            'withCredentials': !![]
        },
        "success": function(data) {
            if (data != null && data['code'] != null) {
                if (data['code'] == "0") {
                    layer['msg']("实名认证成功！");
                    setTimeout(function() {
                        layer['closeAll']();
                    }, 121632 ^ 121032);
                } else if (data['code'] == "10033") {
                    $(".authFaceTip")['find']("csed#".split("").reverse().join(""))['html'](data['msg']);
                    var _0xg3_0xb8a = "//i.7881.com/accountSettings/auth/index?authType=3&realName=" + _realName + "&cardNumber=" + _cardNumber;
                    $(".authFaceTip")['find']("kniLhtua#".split("").reverse().join(""))['attr']("href", _0xg3_0xb8a);
                    var _0xd0b5b;
                    var _0x87gd = $("piTecaFhtua.".split("").reverse().join(""))['html']();
                    _0xd0b5b = (332005 ^ 332003) + (784622 ^ 784622);
                    layer['open']({
                        'type': 1,
                        "title": '',
                        'skin': "pop-tip",
                        'area': ["480px", "360px"],
                        'closeBtn': 0,
                        'content': _0x87gd
                    });
                } else {
                    $(".layui-layer")['find']("h4 span")['text'](data['msg'])['show']();
                }
            } else {
                $("reyal-iuyal.".split("").reverse().join(""))['find']("naps 4h".split("").reverse().join(""))['text']("您提交的信息存在异常，详情请联系客服！")['show']();
            }
        }
    });
}
function zsname(gets) {
    var _0x2c_0x443 = (792764 ^ 792766) + (274971 ^ 274963);
    var _0xe3c3c = new RegExp("$*]\xB7\\5af9u\\-00e4u\\[^".split("").reverse().join(""),"");
    _0x2c_0x443 = "lcaddd".split("").reverse().join("");
    if (gets === '') {
        return "空为能不名姓".split("").reverse().join("");
    } else if (gets['length'] < (605860 ^ 605862)) {
        return "姓名长度不能少于2个字";
    } else if (!_0xe3c3c['test'](gets)) {
        return "姓名格式错误,请重新输入";
    } else {
        return !![];
    }
}
function vadCardnum(gets) {
    var _0xbcgbba = [602625 ^ 602630, 162818 ^ 162827, 308145 ^ 308155, 105431 ^ 105426, 567722 ^ 567714, 314629 ^ 314625, 976957 ^ 976959, 965794 ^ 965795, 731609 ^ 731615, 699573 ^ 699574, 519522 ^ 519525, 932983 ^ 932990, 755576 ^ 755570, 875741 ^ 875736, 972257 ^ 972265, 979603 ^ 979607, 853929 ^ 853931, 557449 ^ 557448];
    var _0x934ace = (268812 ^ 268813) + (704119 ^ 704118);
    var _0xd91c = [726483 ^ 726482, 342229 ^ 342229, 900883 ^ 900889, 670755 ^ 670762, 458664 ^ 458656, 533577 ^ 533582, 294340 ^ 294338, 507534 ^ 507531, 185636 ^ 185632, 250317 ^ 250318, 294750 ^ 294748];
    _0x934ace = "pjhgfc".split("").reverse().join("");
    if (gets['length'] == (296044 ^ 296035)) {
        return _0x2eged(gets);
    } else if (gets['length'] == (299400 ^ 299418)) {
        var _0xc0d2b;
        var _0xea4f = gets['split']("");
        _0xc0d2b = (546891 ^ 546882) + (337093 ^ 337095);
        if (_0x10_0x75e(gets) && _0x0gf(_0xea4f)) {
            return !![];
        }
        return false;
    }
    return false;
    function _0x0gf(a_idCard) {
        var _0xebff = (326318 ^ 326318) + (156424 ^ 156416);
        var _0x2e2 = 996964 ^ 996964;
        _0xebff = (744012 ^ 744012) + (358510 ^ 358507);
        if (a_idCard[634955 ^ 634970]['toLowerCase']() == "x") {
            a_idCard[837965 ^ 837980] = 375462 ^ 375468;
        }
        for (var i = 982136 ^ 982136; i < (448685 ^ 448700); i++) {
            _0x2e2 += _0xbcgbba[i] * a_idCard[i];
        }
        valCodePosition = _0x2e2 % (144589 ^ 144582);
        if (a_idCard[796716 ^ 796733] == _0xd91c[valCodePosition]) {
            return !![];
        }
        return false;
    }
    function _0x10_0x75e(idCard18) {
        var _0x6_0x7a1 = (444257 ^ 444265) + (167634 ^ 167632);
        var _0xdf43ge = idCard18['substring'](722861 ^ 722859, 699685 ^ 699695);
        _0x6_0x7a1 = (868723 ^ 868727) + (224774 ^ 224772);
        var _0xfa488c = idCard18['substring'](483964 ^ 483958, 171468 ^ 171456);
        var _0x8bc98d = (916375 ^ 916369) + (669661 ^ 669653);
        var _0xcf60ga = idCard18['substring'](966765 ^ 966753, 525369 ^ 525367);
        _0x8bc98d = "gmbpjo".split("").reverse().join("");
        var _0x93e6ff = (620558 ^ 620557) + (105041 ^ 105043);
        var _0xea361e = new Date(_0xdf43ge,parseFloat(_0xfa488c) - (851270 ^ 851271),parseFloat(_0xcf60ga));
        _0x93e6ff = 473012 ^ 473020;
        if (_0xea361e['getFullYear']() != parseFloat(_0xdf43ge) || _0xea361e['getMonth']() != parseFloat(_0xfa488c) - (974957 ^ 974956) || _0xea361e['getDate']() != parseFloat(_0xcf60ga)) {
            return false;
        }
        return !![];
    }
    function _0x2eged(idCard15) {
        var _0xe6cfbb = (370805 ^ 370800) + (582310 ^ 582304);
        var _0x3919g = idCard15['substring'](879715 ^ 879717, 606348 ^ 606340);
        _0xe6cfbb = (853753 ^ 853759) + (746045 ^ 746041);
        var _0x02e = (305327 ^ 305325) + (493016 ^ 493023);
        var _0x1c3a = idCard15['substring'](602056 ^ 602048, 282507 ^ 282497);
        _0x02e = 692413 ^ 692409;
        var _0xa73a5b = idCard15['substring'](935250 ^ 935256, 548320 ^ 548332);
        var _0xdad = (230559 ^ 230558) + (351701 ^ 351700);
        var _0x7b7d = new Date(_0x3919g,parseFloat(_0x1c3a) - (278943 ^ 278942),parseFloat(_0xa73a5b));
        _0xdad = 325616 ^ 325619;
        if (_0x7b7d['getYear']() != parseFloat(_0x3919g) || _0x7b7d['getMonth']() != parseFloat(_0x1c3a) - (569713 ^ 569712) || _0x7b7d['getDate']() != parseFloat(_0xa73a5b)) {
            return false;
        }
        return !![];
    }
}
;function listLoadGoodsBrowseAct() {
    $(".my-view")['css']("display", "none");
    if (currentUserId == "no-login") {
        return;
    }
    if (canClaimReward == null || canClaimReward == undefined || canClaimReward == '' || canClaimReward != "1") {
        return;
    }
    if (actId == null || actId == undefined || actId == '') {
        return;
    }
    var _0xd_0xc6d;
    let _0xc8c = JSON['stringify']({
        "actId": actId,
        "gameId": gameId,
        "gtId": gtId
    });
    _0xd_0xc6d = 667959 ^ 667959;
    $['ajax']({
        'url': activeBrowseGoodsUrl,
        'async': false,
        "type": "POST",
        "data": _0xc8c,
        'dataType': "json",
        'contentType': 'application/json',
        "xhrFields": {
            'withCredentials': !![]
        },
        "success": function(actBrowseResp) {
            if (actBrowseResp['code'] == (328106 ^ 328106)) {
                if (actBrowseResp['body']['flag'] && !actBrowseResp['body']['complete']) {
                    listLoadBrowseGoodsActFloat(actBrowseResp['body']['browseTime'], actBrowseResp['body']['surplusTime'], $(".my-view"));
                }
            }
        }
    });
}
function listLoadBrowseGoodsActFloat(browseGoodsTime, browseGoodsSurplusTime, obj) {
    if (browseGoodsSurplusTime == null || browseGoodsSurplusTime == undefined || browseGoodsSurplusTime <= (586483 ^ 586483)) {
        return;
    }
    $(obj)['find'](".djs-txt p")['text']("浏览商品剩余" + browseGoodsSurplusTime + "s");
    $(obj)['find'](".line-bg .color-line")['css']({
        "width": (browseGoodsTime - browseGoodsSurplusTime) / browseGoodsTime * (793677 ^ 793641) + "%"
    });
    $(".my-view")['css']("display", "kcolb".split("").reverse().join(""));
}
;function debounce(func, wait, _0xaeeb) {
    return function executedFunction(...args) {
        var _0x11de9a = (757131 ^ 757131) + (517989 ^ 517986);
        const _0xc8c33b = () => {
            clearTimeout(_0xaeeb);
            func(...args);
        }
        ;
        _0x11de9a = (889800 ^ 889801) + (343749 ^ 343744);
        clearTimeout(_0xaeeb);
        _0xaeeb = setTimeout(_0xc8c33b, wait);
    }
    ;
}
var _0xb4bg;
const extAttrQuickSearch = debounce(loadExtAttrFilters, 790162 ^ 790374);
_0xb4bg = (586236 ^ 586239) + (904933 ^ 904931);
function loadExtAttrFilters() {
    var _0xeaf02c = $(".quick-search input")['val']()['trim']();
    if (_0xeaf02c == '') {
        $("xob-tluser-kciuq.".split("").reverse().join(""))['empty']()['hide']();
        $("atadon-tluser-kciuq.".split("").reverse().join(""))['hide']();
        $(".quick-result-box")['hide']();
        return;
    }
    $['ajax']({
        "url": extAttrFilterUrl + "=dIemag?".split("").reverse().join("") + gameId + "&gtId=" + gtId + "&channel=2&keywords=" + _0xeaf02c,
        'async': false,
        'type': "GET",
        "dataType": "json",
        "xhrFields": {
            "withCredentials": !![]
        },
        'success': function(result) {
            if (result['code'] != (920196 ^ 920196)) {
                $("xob-tluser-kciuq.".split("").reverse().join(""))['empty']()['hide']();
                $(".quick-result-nodata")['show']();
                return;
            }
            var _0x258f7c = result['body'];
            if (_0x258f7c == undefined || _0x258f7c['length'] == (290240 ^ 290240)) {
                $(".quick-result-box")['empty']()['hide']();
                $(".quick-result-nodata")['show']();
                return;
            }
            initQuickSearchHtml(_0x258f7c, _0xeaf02c);
        },
        'error': function(result) {
            $(".quick-result-box")['empty']()['hide']();
            $(".quick-result-nodata")['show']();
            return;
        }
    });
}
function initQuickSearchHtml(confList, searchKeywords) {
    var _0x1e7f;
    var _0x8ce44f = new RegExp(searchKeywords,"g");
    _0x1e7f = (114769 ^ 114772) + (744575 ^ 744570);
    var _0xb282gf = "<ul>";
    for (var i = 825442 ^ 825442; i < confList['length']; i++) {
        var _0x3a4ef = confList[i];
        var _0xf6e19b = _0x3a4ef['filterList'];
        if (_0xf6e19b['length'] > (669113 ^ 669113)) {
            for (var j = 257802 ^ 257802; j < _0xf6e19b['length']; j++) {
                var _0x6d011b;
                var _0x34_0x531 = _0xf6e19b[j];
                _0x6d011b = (791810 ^ 791809) + (647947 ^ 647951);
                var _0x3gcc3f = _0x34_0x531['extAttrValList'];
                if (_0x3gcc3f['length'] > (750558 ^ 750558)) {
                    for (var k = 626411 ^ 626411; k < _0x3gcc3f['length']; k++) {
                        var _0x5a178g;
                        var _0x98g2c = _0x3gcc3f[k];
                        _0x5a178g = 133549 ^ 133546;
                        var _0xba838d = (430826 ^ 430826) + (366443 ^ 366444);
                        var _0x06c = _0x98g2c['showVal'];
                        _0xba838d = 213971 ^ 213968;
                        _0x06c = _0x06c['replace'](_0x8ce44f, "<span>" + searchKeywords + "</span>");
                        var _0xeffdb;
                        var _0x1fc8ge = _0x34_0x531['multipleFlag'];
                        _0xeffdb = 447638 ^ 447646;
                        if (_0x34_0x531['attrPId'] != null && _0x34_0x531['attrPId'] != '' && _0x34_0x531['attrPId'] != "null") {
                            _0x1fc8ge = "1";
                        }
                        var _0xaa8f7f = $(".quick-result-chose")['find']("'=di-rtta[il lu esohc-kciuq.".split("").reverse().join("") + _0x34_0x531['attrId'] + "'][attr-val='" + _0x98g2c['attrVal'] + "']");
                        if (_0xaa8f7f['length'] > (671527 ^ 671527)) {
                            _0xb282gf += "'=di-rtta il<".split("").reverse().join("") + _0x34_0x531['attrId'] + "' attr-pid='" + _0x34_0x531['attrPId'] + "' attr-val='" + _0x98g2c['attrVal'] + "' attr-show-val='" + _0x98g2c['showVal'] + "' multiple-flag='" + _0x1fc8ge + ">'no'=ssalc '".split("").reverse().join("") + _0x06c + "</li>";
                        } else {
                            _0xb282gf += "<li attr-id='" + _0x34_0x531['attrId'] + "' attr-pid='" + _0x34_0x531['attrPId'] + "' attr-val='" + _0x98g2c['attrVal'] + "' attr-show-val='" + _0x98g2c['showVal'] + "'=galf-elpitlum '".split("").reverse().join("") + _0x1fc8ge + "'>" + _0x06c + "</li>";
                        }
                    }
                }
            }
        }
    }
    _0xb282gf += "</ul>";
    $(".quick-result-nodata")['hide']();
    $(".quick-result-box")['empty']()['append'](_0xb282gf)['show']();
}
function initExtAttrChooseHtmlV2(e) {
    var _0x55f11c = (200248 ^ 200253) + (974396 ^ 974395);
    var _0x666gc = $(e)['parents'](".attr-filter")['attr']("data-val-filtertype");
    _0x55f11c = 600831 ^ 600823;
    if (_0x666gc == "2") {
        var _0x677a0d = (631309 ^ 631308) + (280553 ^ 280554);
        var extObj = new Object();
        _0x677a0d = 'mpjqfm';
        extObj['attrId'] = $(e)['parents'](".attr-filter")['attr']("data-val-eid");
        extObj['attrVal'] = $(e)['attr']("data-value");
        extObj['attrShowVal'] = $(e)['attr']("data-value");
        extObj['multipleFlag'] = "0";
        initFilterResult(extObj, "1");
        return;
    }
    if (_0x666gc == "3") {
        var _0xe47dcd;
        var extObj = new Object();
        _0xe47dcd = (376974 ^ 376966) + (721415 ^ 721410);
        extObj['attrId'] = $(e)['parents']("retlif-gga.".split("").reverse().join(""))['attr']("die-lav-atad".split("").reverse().join(""));
        extObj['attrVal'] = $(e)['attr']("eulav-atad".split("").reverse().join(""));
        extObj['attrShowVal'] = $(e)['attr']("data-value");
        extObj['multipleFlag'] = "0";
        initFilterResult(extObj, "1");
        return;
    }
}
function initExtAttrChooseHtmlV3(e) {
    var _0x8a536f = $(e)['parent']()['index']();
    var _0x76d = (807940 ^ 807938) + (670541 ^ 670543);
    var _0x2d5f = $(e)['parents'](".extattr-item")['find']("retlif-rtta. pop-retlif.".split("").reverse().join(""))['eq'](_0x8a536f);
    _0x76d = 'bogicj';
    if (_0x2d5f['length'] == (402183 ^ 402183)) {
        return;
    }
    var _0xgbda = _0x2d5f['attr']("data-val-filtertype");
    if (_0xgbda == "2") {
        var _0x64bd8e;
        var extObj1 = new Object();
        _0x64bd8e = "lpjicq".split("").reverse().join("");
        extObj1['attrId'] = _0x2d5f['attr']("die-lav-atad".split("").reverse().join(""));
        initFilterResult(extObj1, "3");
        _0x2d5f['find'](".filter-pop-bottom .pop-chose-item .item-children")['each'](function(subidx, sube) {
            var _0x4d9c6b = (293428 ^ 293428) + (908289 ^ 908290);
            var _0xdbb = new Object();
            _0x4d9c6b = 829646 ^ 829647;
            _0xdbb['attrId'] = $(this)['attr']("data-val-subeid");
            initFilterResult(_0xdbb, "3");
        });
    }
    if (_0xgbda == "3") {
        _0x2d5f['find']("retlif-gga.".split("").reverse().join(""))['each'](function(index, e1) {
            var _0x02bg4f = new Object();
            _0x02bg4f['attrId'] = $(e1)['attr']("die-lav-atad".split("").reverse().join(""));
            initFilterResult(_0x02bg4f, "3");
            $(e1)['find']("nerdlihc-meti. meti-esohc-pop. mottob-pop-retlif.".split("").reverse().join(""))['each'](function(subidx, sube) {
                var _0xf4a;
                var _0x74682f = new Object();
                _0xf4a = (676649 ^ 676641) + (651054 ^ 651050);
                _0x74682f['attrId'] = $(sube)['attr']("diebus-lav-atad".split("").reverse().join(""));
                initFilterResult(_0x74682f, "3");
            });
        });
    }
}
function initExtAttrChooseHtmlV4(e) {
    if ($(e)['find']("nerdlihc-meti.".split("").reverse().join(""))['length'] > (143854 ^ 143854)) {
        return;
    }
    var _0x4779c = (265118 ^ 265113) + (365706 ^ 365698);
    var _0xdebf2b = $(e)['parents'](".attr-filter")['attr']("data-val-filtertype");
    _0x4779c = (864276 ^ 864273) + (954103 ^ 954100);
    if (_0xdebf2b == "2") {
        var _0x995f = (152861 ^ 152858) + (440407 ^ 440400);
        var extObj = new Object();
        _0x995f = "ofljff".split("").reverse().join("");
        extObj['attrId'] = $(e)['parents'](".attr-filter")['attr']("die-lav-atad".split("").reverse().join(""));
        extObj['attrVal'] = $(e)['attr']("data-value");
        extObj['attrShowVal'] = $(e)['attr']("eulav-atad".split("").reverse().join(""));
        extObj['multipleFlag'] = "1";
        if ($(e)['hasClass']("moreon")) {
            initFilterResult(extObj, "1");
        } else {
            initFilterResult(extObj, "2");
        }
    }
    if (_0xdebf2b == "3") {
        var extObj = new Object();
        extObj['attrId'] = $(e)['parents'](".agg-filter")['attr']("data-val-eid");
        extObj['attrVal'] = $(e)['attr']("data-value");
        extObj['attrShowVal'] = $(e)['attr']("data-value");
        extObj['multipleFlag'] = "1";
        if ($(e)['hasClass']("moreon")) {
            initFilterResult(extObj, "1");
        } else {
            initFilterResult(extObj, "2");
        }
    }
}
function initExtAttrChooseHtmlV5(e) {
    var _0xa7_0x282 = $(e)['parents']("retlif-rtta.".split("").reverse().join(""));
    var _0x7d11f;
    var _0xd1g = _0xa7_0x282['attr']("data-val-filtertype");
    _0x7d11f = 'mmmmac';
    if ($(e)['parents'](".pop-chose-item")['hasClass']("noerom".split("").reverse().join(""))) {
        if (_0xd1g == "2") {
            var extObj1 = new Object();
            extObj1['attrId'] = _0xa7_0x282['attr']("die-lav-atad".split("").reverse().join(""));
            extObj1['attrVal'] = $(e)['parents'](".pop-chose-item")['attr']("data-value");
            extObj1['attrShowVal'] = $(e)['parents'](".pop-chose-item")['attr']("eulav-atad".split("").reverse().join(""));
            extObj1['multipleFlag'] = "1";
            initFilterResult(extObj1, "1");
        }
        if (_0xd1g == "3") {
            var extObj1 = new Object();
            extObj1['attrId'] = $(e)['parents'](".agg-filter")['attr']("die-lav-atad".split("").reverse().join(""));
            extObj1['attrVal'] = $(e)['parents'](".pop-chose-item")['attr']("data-value");
            extObj1['attrShowVal'] = $(e)['parents']("meti-esohc-pop.".split("").reverse().join(""))['attr']("eulav-atad".split("").reverse().join(""));
            extObj1['multipleFlag'] = "1";
            initFilterResult(extObj1, "1");
        }
    } else {
        if (_0xd1g == "2") {
            var extObj1 = new Object();
            extObj1['attrId'] = _0xa7_0x282['attr']("die-lav-atad".split("").reverse().join(""));
            extObj1['attrVal'] = $(e)['parents'](".pop-chose-item")['attr']("data-value");
            initFilterResult(extObj1, "2");
        }
        if (_0xd1g == "3") {
            var _0xad0fd = (723059 ^ 723066) + (515403 ^ 515406);
            var extObj1 = new Object();
            _0xad0fd = (113738 ^ 113730) + (218089 ^ 218092);
            extObj1['attrId'] = $(e)['parents'](".agg-filter")['attr']("data-val-eid");
            extObj1['attrVal'] = $(e)['parents'](".pop-chose-item")['attr']("eulav-atad".split("").reverse().join(""));
            initFilterResult(extObj1, "2");
        }
    }
    if ($(e)['hasClass']("on")) {
        if (_0xd1g == "2") {
            var _0x103c7b;
            var extObj = new Object();
            _0x103c7b = (424240 ^ 424241) + (275424 ^ 275429);
            extObj['attrId'] = $(e)['parents'](".item-children")['attr']("diebus-lav-atad".split("").reverse().join(""));
            extObj['attrVal'] = $(e)['attr']("eulav-atad".split("").reverse().join(""));
            extObj['attrPid'] = $(e)['parents'](".attr-filter")['attr']("data-val-eid");
            extObj['attrPval'] = $(e)['parents'](".item-children")['attr']("data-pev");
            extObj['attrShowVal'] = $(e)['parents'](".item-children")['attr']("data-pev") + $(e)['attr']("eulav-atad".split("").reverse().join(""));
            extObj['multipleFlag'] = "1";
            initFilterResult(extObj, "1");
        }
        if (_0xd1g == "3") {
            var extObj = new Object();
            extObj['attrId'] = $(e)['parents'](".item-children")['attr']("data-val-subeid");
            extObj['attrVal'] = $(e)['attr']("data-value");
            extObj['attrPid'] = $(e)['parents']("retlif-gga.".split("").reverse().join(""))['attr']("die-lav-atad".split("").reverse().join(""));
            extObj['attrPval'] = $(e)['parents']("nerdlihc-meti.".split("").reverse().join(""))['attr']("data-pev");
            extObj['attrShowVal'] = $(e)['parents']("nerdlihc-meti.".split("").reverse().join(""))['attr']("vep-atad".split("").reverse().join("")) + $(e)['attr']("eulav-atad".split("").reverse().join(""));
            extObj['multipleFlag'] = "1";
            initFilterResult(extObj, "1");
        }
    } else {
        var _0x39c62b;
        var extObj = new Object();
        _0x39c62b = (419059 ^ 419066) + (975768 ^ 975761);
        extObj['attrId'] = $(e)['parents']("nerdlihc-meti.".split("").reverse().join(""))['attr']("data-val-subeid");
        extObj['attrVal'] = $(e)['attr']("eulav-atad".split("").reverse().join(""));
        initFilterResult(extObj, "2");
    }
}
function initExtAttrChooseHtmlV6(e) {
    var _0x63d2f;
    var _0x4684e = $(e)['parents'](".attr-filter");
    _0x63d2f = (816821 ^ 816820) + (387006 ^ 387004);
    var _0xf2abe;
    var _0xcb4bfd = _0x4684e['attr']("data-val-filtertype");
    _0xf2abe = 'kefhhh';
    if (_0xcb4bfd == "2") {
        var _0xa7c0ba = (582072 ^ 582064) + (396205 ^ 396202);
        var popChoseItem = $(e)['parent']();
        _0xa7c0ba = 'jhimod';
        var _0xf_0xbac;
        var extObj1 = new Object();
        _0xf_0xbac = (438765 ^ 438767) + (609758 ^ 609758);
        extObj1['attrId'] = _0x4684e['attr']("die-lav-atad".split("").reverse().join(""));
        extObj1['attrVal'] = popChoseItem['attr']("eulav-atad".split("").reverse().join(""));
        initFilterResult(extObj1, "2");
        var itemChildren = popChoseItem['find'](".item-children");
        var _0xbg82c = (786412 ^ 786411) + (243298 ^ 243306);
        var subeid = itemChildren['attr']("data-val-subeid");
        _0xbg82c = (102028 ^ 102029) + (529294 ^ 529286);
        itemChildren['find']("dlihc.".split("").reverse().join(""))['each'](function(idx, e1) {
            var _0x7_0xdd9;
            var _0x2cd = new Object();
            _0x7_0xdd9 = (177489 ^ 177497) + (322520 ^ 322522);
            _0x2cd['attrId'] = subeid;
            _0x2cd['attrVal'] = $(e1)['attr']("data-value");
            initFilterResult(_0x2cd, "2");
        });
    }
    if (_0xcb4bfd == "3") {
        var _0x7a543b = (318305 ^ 318308) + (107522 ^ 107526);
        var popChoseItem = $(e)['parent']();
        _0x7a543b = (991256 ^ 991259) + (537010 ^ 537008);
        var _0xe9f56c = (917560 ^ 917565) + (105234 ^ 105234);
        var extObj1 = new Object();
        _0xe9f56c = (475895 ^ 475891) + (783552 ^ 783557);
        extObj1['attrId'] = $(e)['parents']("retlif-gga.".split("").reverse().join(""))['attr']("die-lav-atad".split("").reverse().join(""));
        extObj1['attrVal'] = popChoseItem['attr']("data-value");
        initFilterResult(extObj1, "2");
        var itemChildren = popChoseItem['find'](".item-children");
        var _0xa6f52a = (886419 ^ 886427) + (385680 ^ 385685);
        var subeid = itemChildren['attr']("data-val-subeid");
        _0xa6f52a = 759678 ^ 759677;
        itemChildren['find'](".child")['each'](function(idx, e1) {
            var _0x2f5e0f = (890228 ^ 890224) + (436707 ^ 436707);
            var _0x8g38g = new Object();
            _0x2f5e0f = 894114 ^ 894116;
            _0x8g38g['attrId'] = subeid;
            _0x8g38g['attrVal'] = $(e1)['attr']("data-value");
            initFilterResult(_0x8g38g, "2");
        });
    }
}
function initExtAttrChooseHtmlV7(e) {
    var _0x227e;
    var _0xcg6c = $(e)['parents'](".attr-filter");
    _0x227e = 311239 ^ 311234;
    var _0x6e4aff = (578437 ^ 578438) + (448216 ^ 448217);
    var _0x34bg = _0xcg6c['attr']("epytretlif-lav-atad".split("").reverse().join(""));
    _0x6e4aff = (402539 ^ 402540) + (731711 ^ 731702);
    if (_0x34bg == "2") {
        var _0x967bcb = (778880 ^ 778884) + (627073 ^ 627072);
        var extObj1 = new Object();
        _0x967bcb = "badcio".split("").reverse().join("");
        extObj1['attrId'] = _0xcg6c['attr']("data-val-eid");
        initFilterResult(extObj1, "3");
        if (_0xcg6c['find']("nerdlihc-meti. meti-esohc-pop. mottob-pop-retlif.".split("").reverse().join(""))['length'] > (248712 ^ 248712)) {
            var _0x93a75b;
            var extObj2 = new Object();
            _0x93a75b = (787881 ^ 787882) + (122506 ^ 122504);
            extObj2['attrPid'] = _0xcg6c['attr']("data-val-eid");
            initFilterResult(extObj2, "4");
        }
        return;
    }
    if (_0x34bg == "3") {
        var _0xbd_0xdfe;
        var extObj1 = new Object();
        _0xbd_0xdfe = (218863 ^ 218857) + (315736 ^ 315743);
        extObj1['attrId'] = $(e)['parents']("retlif-gga.".split("").reverse().join(""))['attr']("die-lav-atad".split("").reverse().join(""));
        initFilterResult(extObj1, "3");
        if ($(e)['parents']("retlif-gga.".split("").reverse().join(""))['find'](".filter-pop-bottom .pop-chose-item .item-children")['length'] > (208273 ^ 208273)) {
            var _0x3cee;
            var extObj2 = new Object();
            _0x3cee = 194891 ^ 194890;
            extObj2['attrPid'] = $(e)['parents'](".agg-filter")['attr']("data-val-eid");
            initFilterResult(extObj2, "4");
        }
        return;
    }
}
function initExtAttrChooseHtmlV8(e) {
    var _0x7g6c = $(e)['parents']("retlif-rtta.".split("").reverse().join(""));
    var _0x6916cb;
    var _0x1f7a = _0x7g6c['attr']("epytretlif-lav-atad".split("").reverse().join(""));
    _0x6916cb = 'ajfhpo';
    if (_0x1f7a == "2") {
        var _0x52f3ee;
        var extObj = new Object();
        _0x52f3ee = 'achnhf';
        extObj['attrPid'] = _0x7g6c['attr']("data-val-eid");
        extObj['attrPval'] = $(e)['parents']("nerdlihc-meti.".split("").reverse().join(""))['attr']("data-pev");
        initFilterResult(extObj, "5");
        return;
    }
    if (_0x1f7a == "3") {
        var _0x4b544b = (363329 ^ 363328) + (709930 ^ 709934);
        var extObj = new Object();
        _0x4b544b = (176312 ^ 176317) + (680886 ^ 680886);
        extObj['attrPid'] = $(e)['parents']("retlif-gga.".split("").reverse().join(""))['attr']("data-val-eid");
        extObj['attrPval'] = $(e)['parents']("nerdlihc-meti.".split("").reverse().join(""))['attr']("data-pev");
        initFilterResult(extObj, "5");
        return;
    }
}
function initExtAttrChooseHtmlV9(e) {
    var _0x3c59f = (202601 ^ 202604) + (484883 ^ 484890);
    var _0xb2d = $(e)['parents']("retlif-rtta.".split("").reverse().join(""));
    _0x3c59f = "mocflm".split("").reverse().join("");
    var _0x8_0x329;
    var _0x26ffb = _0xb2d['attr']("epytretlif-lav-atad".split("").reverse().join(""));
    _0x8_0x329 = (431517 ^ 431513) + (238119 ^ 238113);
    if ($(e)['hasClass']("no".split("").reverse().join(""))) {
        if (_0x26ffb == "2") {
            _0xb2d['find']("meti-esohc-pop. mottob-pop-retlif.".split("").reverse().join(""))['each'](function(idx, e) {
                var _0x2e_0x5a3 = (159625 ^ 159627) + (200517 ^ 200518);
                var _0x37b9d = new Object();
                _0x2e_0x5a3 = (921298 ^ 921302) + (104808 ^ 104812);
                _0x37b9d['attrId'] = _0xb2d['attr']("data-val-eid");
                _0x37b9d['attrVal'] = $(this)['attr']("eulav-atad".split("").reverse().join(""));
                _0x37b9d['multipleFlag'] = "1";
                _0x37b9d['attrShowVal'] = $(this)['attr']("data-value");
                initFilterResult(_0x37b9d, "1");
            });
            return;
        }
        if (_0x26ffb == "3") {
            var aggFilter = $(e)['parents'](".agg-filter");
            aggFilter['find'](".filter-pop-bottom .pop-chose-item")['each'](function(idx, e) {
                var _0x1f8a1d;
                var _0x37_0x461 = new Object();
                _0x1f8a1d = 'kfglni';
                _0x37_0x461['attrId'] = aggFilter['attr']("die-lav-atad".split("").reverse().join(""));
                _0x37_0x461['attrVal'] = $(this)['attr']("data-value");
                _0x37_0x461['multipleFlag'] = "1";
                _0x37_0x461['attrShowVal'] = $(this)['attr']("data-value");
                initFilterResult(_0x37_0x461, "1");
            });
            return;
        }
    } else {
        if (_0x26ffb == "2") {
            var extObj = new Object();
            extObj['attrId'] = _0xb2d['attr']("data-val-eid");
            initFilterResult(extObj, "3");
            return;
        }
        if (_0x26ffb == "3") {
            var aggFilter = $(e)['parents'](".agg-filter");
            var extObj = new Object();
            extObj['attrId'] = aggFilter['attr']("data-val-eid");
            initFilterResult(extObj, "3");
            return;
        }
    }
}
function initExtAttrChooseHtmlV10(e) {
    var _0x1d67d = (403304 ^ 403308) + (423613 ^ 423613);
    var _0xae797b = $(e)['parents'](".attr-filter");
    _0x1d67d = 'fihpai';
    var _0x0g6f = _0xae797b['attr']("data-val-filtertype");
    if ($(e)['hasClass']("no".split("").reverse().join(""))) {
        if (_0x0g6f == "2") {
            var mainAttrId = _0xae797b['attr']("data-val-eid");
            var mainAttrVal = $(e)['parents'](".pop-chose-item")['attr']("data-value");
            var _0xb45g4e;
            var extObj1 = new Object();
            _0xb45g4e = 548501 ^ 548501;
            extObj1['attrId'] = mainAttrId;
            extObj1['attrVal'] = mainAttrVal;
            extObj1['multipleFlag'] = "1";
            extObj1['attrShowVal'] = mainAttrVal;
            initFilterResult(extObj1, "1");
            var _0x9_0x225 = (446715 ^ 446718) + (971961 ^ 971964);
            var subAttrId = $(e)['parents']("nerdlihc-meti.".split("").reverse().join(""))['attr']("data-val-subeid");
            _0x9_0x225 = (244689 ^ 244694) + (560189 ^ 560190);
            $(e)['parents']("nerdlihc-meti.".split("").reverse().join(""))['find'](".child")['each'](function(idx, sube) {
                var _0x6d64e = (492815 ^ 492807) + (403243 ^ 403246);
                var _0xa83eac = new Object();
                _0x6d64e = (294110 ^ 294107) + (952785 ^ 952792);
                _0xa83eac['attrId'] = subAttrId;
                _0xa83eac['attrVal'] = $(sube)['attr']("data-value");
                _0xa83eac['attrPid'] = mainAttrId;
                _0xa83eac['attrPval'] = mainAttrVal;
                _0xa83eac['multipleFlag'] = "1";
                _0xa83eac['attrShowVal'] = mainAttrVal + $(sube)['attr']("data-value");
                initFilterResult(_0xa83eac, "1");
            });
            return;
        }
        if (_0x0g6f == "3") {
            var _0xd7718f = $(e)['parents'](".agg-filter");
            var _0xc5a;
            var mainAttrId = _0xd7718f['attr']("die-lav-atad".split("").reverse().join(""));
            _0xc5a = (636623 ^ 636614) + (965321 ^ 965320);
            var _0xd2e3e = (265662 ^ 265661) + (390572 ^ 390564);
            var mainAttrVal = $(e)['parents'](".pop-chose-item")['attr']("eulav-atad".split("").reverse().join(""));
            _0xd2e3e = (665080 ^ 665081) + (987428 ^ 987426);
            var extObj1 = new Object();
            extObj1['attrId'] = mainAttrId;
            extObj1['attrVal'] = mainAttrVal;
            extObj1['multipleFlag'] = "1";
            extObj1['attrShowVal'] = mainAttrVal;
            initFilterResult(extObj1, "1");
            var _0x55efb = (753861 ^ 753860) + (556219 ^ 556218);
            var subAttrId = $(e)['parents']("nerdlihc-meti.".split("").reverse().join(""))['attr']("diebus-lav-atad".split("").reverse().join(""));
            _0x55efb = 919471 ^ 919463;
            $(e)['parents'](".item-children")['find'](".child")['each'](function(idx, sube) {
                var _0x44c5aa = (878272 ^ 878281) + (547347 ^ 547351);
                var _0x48f3d = new Object();
                _0x44c5aa = (945853 ^ 945852) + (850206 ^ 850207);
                _0x48f3d['attrId'] = subAttrId;
                _0x48f3d['attrVal'] = $(sube)['attr']("eulav-atad".split("").reverse().join(""));
                _0x48f3d['attrPid'] = mainAttrId;
                _0x48f3d['attrPval'] = mainAttrVal;
                _0x48f3d['multipleFlag'] = "1";
                _0x48f3d['attrShowVal'] = mainAttrVal + $(sube)['attr']("data-value");
                initFilterResult(_0x48f3d, "1");
            });
            return;
        }
    } else {
        if (_0x0g6f == "2") {
            var _0xa3_0xba7;
            var extObj1 = new Object();
            _0xa3_0xba7 = 'phhemb';
            extObj1['attrPid'] = _0xae797b['attr']("data-val-eid");
            extObj1['attrPval'] = $(e)['parents']("meti-esohc-pop.".split("").reverse().join(""))['attr']("eulav-atad".split("").reverse().join(""));
            initFilterResult(extObj1, "5");
            return;
        }
        if (_0x0g6f == "3") {
            var _0x5541cc = (424344 ^ 424350) + (159841 ^ 159847);
            var extObj1 = new Object();
            _0x5541cc = 422305 ^ 422312;
            extObj1['attrPid'] = $(e)['parents']("retlif-gga.".split("").reverse().join(""))['attr']("die-lav-atad".split("").reverse().join(""));
            extObj1['attrPval'] = $(e)['parents']("meti-esohc-pop.".split("").reverse().join(""))['attr']("data-value");
            initFilterResult(extObj1, "5");
            return;
        }
    }
}
function cleanQuickChose() {
    $("esohc-tluser-kciuq.".split("").reverse().join(""))['find']("lu esohc-kciuq.".split("").reverse().join(""))['empty']();
    $("esohc-tluser-kciuq.".split("").reverse().join(""))['hide']();
}
function initFilterResult(extObj, opType) {
    if (opType == "1") {
        if (extObj['multipleFlag'] == "1") {
            var _0x5e_0x2de;
            var liE = $(".quick-result-chose")['find']("ul li[attr-id='" + extObj['attrId'] + "'=lav-rtta[]'".split("").reverse().join("") + extObj['attrVal'] + "]'".split("").reverse().join(""));
            _0x5e_0x2de = 701041 ^ 701048;
            if (liE['length'] == (314891 ^ 314891)) {
                var _html = '';
                _html += "<li attr-id="" + extObj['attrId'] + "" attr-val="" + extObj['attrVal'] + "" attr-pid="" + extObj['attrPid'] + "" attr-pval="" + extObj['attrPval'] + "" attr-show-val="" + extObj['attrShowVal'] + ">\"".split("").reverse().join("");
                _html += "<span>" + extObj['attrShowVal'] + ">naps/<".split("").reverse().join("");
                _html += ">\")0(diov:tpircsavaj\"=ferh a<".split("").reverse().join("");
                _html += "<img src="" + bucketDomain + "/7881/images/list-2024/quick-close.png" class="hovhide"/>";
                _html += "<img src="" + bucketDomain + "/7881/images/list-2024/quick-close-hov.png" class="hovshow"/>";
                _html += ">a/<".split("").reverse().join("");
                _html += ">il/<".split("").reverse().join("");
                $("esohc-tluser-kciuq.".split("").reverse().join(""))['find']("lu esohc-kciuq.".split("").reverse().join(""))['append'](_html);
                $("neercs-retlif.".split("").reverse().join(""))['find']("'=di-rtta[il lu xob-tluser-kciuq.".split("").reverse().join("") + extObj['attrId'] + "'=lav-rtta[]'".split("").reverse().join("") + extObj['attrVal'] + "']")['addClass']("no".split("").reverse().join(""));
            }
        } else {
            var _0x83c = (932326 ^ 932335) + (195224 ^ 195229);
            var liE = $("esohc-tluser-kciuq.".split("").reverse().join(""))['find']("'=di-rtta[il lu".split("").reverse().join("") + extObj['attrId'] + "']");
            _0x83c = (534279 ^ 534275) + (265328 ^ 265333);
            if (liE['length'] > (418027 ^ 418027)) {
                var _0x89f4da = liE['find']("span")['text'];
                liE['attr']("lav-wohs-rtta".split("").reverse().join(""), extObj['attrShowVal'])['attr']("attr-val", extObj['attrVal']);
                liE['find']("naps".split("").reverse().join(""))['text'](extObj['attrShowVal']);
                $(".filter-screen")['find']("'=di-rtta[il lu xob-tluser-kciuq.".split("").reverse().join("") + extObj['attrId'] + "'=lav-rtta[]'".split("").reverse().join("") + _0x89f4da + "]'".split("").reverse().join(""))['removeClass']("on");
                $(".filter-screen")['find'](".quick-result-box ul li[attr-id='" + extObj['attrId'] + "'][attr-val='" + extObj['attrVal'] + "']")['addClass']("on");
            } else {
                var _html = '';
                _html += "<li attr-id="" + extObj['attrId'] + "" attr-val="" + extObj['attrVal'] + "" attr-pid="" + extObj['attrPid'] + "" attr-pval="" + extObj['attrPval'] + "\"=lav-wohs-rtta \"".split("").reverse().join("") + extObj['attrShowVal'] + "">";
                _html += "<span>" + extObj['attrShowVal'] + "</span>";
                _html += ">\")0(diov:tpircsavaj\"=ferh a<".split("").reverse().join("");
                _html += "\"=crs gmi<".split("").reverse().join("") + bucketDomain + "/7881/images/list-2024/quick-close.png" class="hovhide"/>";
                _html += "\"=crs gmi<".split("").reverse().join("") + bucketDomain + ">/\"wohsvoh\"=ssalc \"gnp.voh-esolc-kciuq/4202-tsil/segami/1887/".split("").reverse().join("");
                _html += "</a>";
                _html += ">il/<".split("").reverse().join("");
                $(".quick-result-chose")['find']("lu esohc-kciuq.".split("").reverse().join(""))['append'](_html);
                $(".filter-screen")['find']("'=di-rtta[il lu xob-tluser-kciuq.".split("").reverse().join("") + extObj['attrId'] + "'=lav-rtta[]'".split("").reverse().join("") + extObj['attrVal'] + "']")['addClass']("no".split("").reverse().join(""));
            }
        }
        $("esohc-tluser-kciuq.".split("").reverse().join(""))['show']();
    }
    if (opType == "2") {
        $(".quick-result-chose")['find']("ul li[attr-id='" + extObj['attrId'] + "'=lav-rtta[]'".split("").reverse().join("") + extObj['attrVal'] + "']")['remove']();
        if ($(".quick-result-chose")['find']("il lu".split("").reverse().join(""))['length'] == (504114 ^ 504114)) {
            $("esohc-tluser-kciuq.".split("").reverse().join(""))['hide']();
        }
        $(".filter-screen")['find']("'=di-rtta[il lu xob-tluser-kciuq.".split("").reverse().join("") + extObj['attrId'] + "'=lav-rtta[]'".split("").reverse().join("") + extObj['attrVal'] + "']")['removeClass']("on");
    }
    if (opType == "3") {
        $("esohc-tluser-kciuq.".split("").reverse().join(""))['find']("'=di-rtta[il lu".split("").reverse().join("") + extObj['attrId'] + "]'".split("").reverse().join(""))['remove']();
        if ($(".quick-result-chose")['find']("ul li")['length'] == (852663 ^ 852663)) {
            $("esohc-tluser-kciuq.".split("").reverse().join(""))['hide']();
        }
        $("neercs-retlif.".split("").reverse().join(""))['find'](".quick-result-box ul li[attr-id='" + extObj['attrId'] + "']")['removeClass']("on");
    }
    if (opType == "4") {
        $("esohc-tluser-kciuq.".split("").reverse().join(""))['find']("ul li[attr-pid='" + extObj['attrPid'] + "']")['remove']();
        if ($(".quick-result-chose")['find']("ul li")['length'] == (799683 ^ 799683)) {
            $("esohc-tluser-kciuq.".split("").reverse().join(""))['hide']();
        }
        $("neercs-retlif.".split("").reverse().join(""))['find'](".quick-result-box ul li[attr-pid='" + extObj['attrPid'] + "']")['removeClass']("on");
    }
    if (opType == "5") {
        $(".quick-result-chose")['find']("'=dip-rtta[il lu".split("").reverse().join("") + extObj['attrPid'] + "'][attr-pval='" + extObj['attrPval'] + "']")['remove']();
        if ($(".quick-result-chose")['find']("il lu".split("").reverse().join(""))['length'] == (534262 ^ 534262)) {
            $(".quick-result-chose")['hide']();
        }
        $("neercs-retlif.".split("").reverse().join(""))['find'](".quick-result-box ul li[attr-pid='" + extObj['attrPid'] + "'=lavp-rtta[]'".split("").reverse().join("") + extObj['attrPval'] + "']")['removeClass']("no".split("").reverse().join(""));
    }
}
function initExtAttrChooseHtmlV1(e) {
    var _0x9gd;
    var _0x7g2 = $(e)['attr']("multiple-flag");
    _0x9gd = "ehgppd".split("").reverse().join("");
    var _0x01abab = new Object();
    _0x01abab['attrId'] = $(e)['attr']("attr-id");
    _0x01abab['attrVal'] = $(e)['attr']("attr-val");
    _0x01abab['attrPid'] = $(e)['attr']("dip-rtta".split("").reverse().join(""));
    _0x01abab['multipleFlag'] = _0x7g2;
    if ($(e)['hasClass']("no".split("").reverse().join(""))) {
        $(e)['removeClass']("on");
        delFiltersParam(_0x01abab);
        return;
    }
    if (_0x7g2 == "1") {
        $(e)['addClass']("on");
    } else {
        $(e)['addClass']("no".split("").reverse().join(""))['siblings']("[attr-id='" + $(e)['attr']("attr-id") + "']")['removeClass']("no".split("").reverse().join(""));
    }
    addFiltersParam(_0x01abab);
}
function delQuickChoose(e) {
    var _0x32493e;
    var _0x546e0g = $(e)['parents']("lu".split("").reverse().join(""))['find']("li")['length'];
    _0x32493e = 740320 ^ 740328;
    var _0xf229b = $(e)['parent']();
    var _0xd89f8e = (982448 ^ 982448) + (927336 ^ 927338);
    var _0xd2g56e = _0xf229b['attr']("attr-id");
    _0xd89f8e = 121934 ^ 121933;
    var _0x61f = _0xf229b['attr']("attr-show-val");
    $(".quick-result-box")['find']("ul li[attr-id='" + _0xd2g56e + "'][attr-show-val='" + _0x61f + "]'".split("").reverse().join(""))['removeClass']("no".split("").reverse().join(""));
    $(e)['parent']()['remove']();
    if (_0x546e0g == (288384 ^ 288385)) {
        $("esohc-tluser-kciuq.".split("").reverse().join(""))['hide']();
    }
    var _0xf7249e = new Object();
    _0xf7249e['attrId'] = _0xd2g56e;
    _0xf7249e['attrVal'] = _0xf229b['attr']("attr-val");
    _0xf7249e['attrPid'] = _0xf229b['attr']("dip-rtta".split("").reverse().join(""));
    delFiltersParam(_0xf7249e);
}
function delFiltersParam(extObj) {
    delDyFilterParam(extObj);
    delJhFilterParam(extObj);
}
function delDyFilterParam(extObj) {
    if (extObj['attrPid'] != undefined && extObj['attrPid'] != "undefined" && extObj['attrPid'] != null && extObj['attrPid'] != "llun".split("").reverse().join("") && extObj['attrPid'] != '') {
        $(".extattr-item")['find'](".filter-pop .attr-filter[data-val-filtertype='2'] .pop-chose-item .item-children[data-val-subeid='" + extObj['attrId'] + "'] .child[data-value='" + extObj['attrVal'] + "']")['each'](function(index, e) {
            if ($(this)['hasClass']("on")) {
                $(this)['click']();
                $(this)['parents']("retlif-rtta.".split("").reverse().join(""))['find']("a ntb-pop-retlif.".split("").reverse().join(""))['click']();
            }
        });
        return;
    }
    var _0xe62df;
    var _0x3de60a = $(".extattr-item")['find'](".filter-pop .attr-filter[data-val-eid='" + extObj['attrId'] + "'][data-val-filtertype='2']");
    _0xe62df = (610334 ^ 610329) + (640970 ^ 640968);
    if (_0x3de60a['length'] == (560836 ^ 560836)) {
        return;
    }
    var _0x51da7e = _0x3de60a['find'](".filter-pop-bottom");
    if (_0x51da7e['hasClass']("esohc-elgnis".split("").reverse().join(""))) {
        $("meti-rttatxe.".split("").reverse().join(""))['find'](".filter-chose .chose-select")['eq'](_0x51da7e['parent']()['index']())['find'](".close-icon")['click']();
        return;
    }
    if (_0x51da7e['hasClass']("esohc-erom".split("").reverse().join(""))) {
        _0x51da7e['find'](".pop-chose-item[data-value='" + extObj['attrVal'] + "]'".split("").reverse().join(""))['each'](function(index, e) {
            if ($(this)['hasClass']("moreon")) {
                var _0x4d7db = $(this)['find'](".item-children");
                if (_0x4d7db['length'] > (285844 ^ 285844)) {
                    $(this)['find']("noci-esolc.".split("").reverse().join(""))['click']();
                } else {
                    $(this)['click']();
                }
                _0x3de60a['find']("a ntb-pop-retlif.".split("").reverse().join(""))['click']();
            }
        });
        return;
    }
}
function delJhFilterParam(extObj) {
    if (extObj['attrPid'] != undefined && extObj['attrPid'] != "undefined" && extObj['attrPid'] != null && extObj['attrPid'] != "null" && extObj['attrPid'] != '') {
        $("meti-rttatxe.".split("").reverse().join(""))['find']("]'3'=epytretlif-lav-atad[retlif-rtta. pop-retlif.".split("").reverse().join(""))['find']("'=diebus-lav-atad[nerdlihc-meti. meti-esohc-pop. retlif-gga.".split("").reverse().join("") + extObj['attrId'] + "]'".split("").reverse().join(""))['find']("'=eulav-atad[dlihc.".split("").reverse().join("") + extObj['attrVal'] + "']")['each'](function(index, e) {
            if ($(this)['hasClass']("on")) {
                $(this)['click']();
                $(this)['parents'](".attr-filter")['find'](".filter-pop-btn a")['click']();
            }
        });
        return;
    }
    var _0xfa25c;
    var _0xbe2a7e = $(".extattr-item")['find']("]'3'=epytretlif-lav-atad[retlif-rtta. pop-retlif.".split("").reverse().join(""))['find'](".agg-filter[data-val-eid='" + extObj['attrId'] + "']");
    _0xfa25c = (215338 ^ 215340) + (551814 ^ 551815);
    if (_0xbe2a7e['length'] == (392734 ^ 392734)) {
        return;
    }
    var _0x259dbb = _0xbe2a7e['find']("mottob-pop-retlif.".split("").reverse().join(""));
    if (_0x259dbb['hasClass']("esohc-elgnis".split("").reverse().join(""))) {
        _0x259dbb['find']("'=eulav-atad[meti-esohc-pop.".split("").reverse().join("") + extObj['attrVal'] + "']")['each'](function(index, e) {
            if ($(this)['hasClass']("on")) {
                $(this)['removeClass']("on");
                _0xbe2a7e['parent']()['find']("a ntb-pop-retlif.".split("").reverse().join(""))['click']();
            }
        });
        return;
    }
    if (_0x259dbb['hasClass']("more-chose")) {
        _0x259dbb['find'](".pop-chose-item[data-value='" + extObj['attrVal'] + "']")['each'](function(index, e) {
            if ($(this)['hasClass']("noerom".split("").reverse().join(""))) {
                var _0xf5256e = (728688 ^ 728692) + (609684 ^ 609681);
                var _0x25a = $(this)['find']("nerdlihc-meti.".split("").reverse().join(""));
                _0xf5256e = (942282 ^ 942287) + (567246 ^ 567243);
                if (_0x25a['length'] > (776562 ^ 776562)) {
                    $(this)['find']("noci-esolc.".split("").reverse().join(""))['click']();
                } else {
                    $(this)['click']();
                }
                _0xbe2a7e['parent']()['find'](".filter-pop-btn a")['click']();
            }
        });
        return;
    }
}
function addFiltersParam(extObj) {
    addDyFilterParam(extObj);
    addJhFilterParam(extObj);
}
function addDyFilterParam(extObj) {
    if (extObj['attrPid'] != undefined && extObj['attrPid'] != "undefined" && extObj['attrPid'] != null && extObj['attrPid'] != "null" && extObj['attrPid'] != '') {
        $(".extattr-item")['find']("'=diebus-lav-atad[nerdlihc-meti. meti-esohc-pop. retlif-rtta. pop-retlif.".split("").reverse().join("") + extObj['attrId'] + "'=eulav-atad[dlihc. ]'".split("").reverse().join("") + extObj['attrVal'] + "]'".split("").reverse().join(""))['each'](function(index, e) {
            if (!$(this)['hasClass']("on")) {
                $(this)['click']();
                $(this)['parents'](".attr-filter")['find'](".filter-pop-btn a")['click']();
            }
        });
        return;
    }
    var _0x72b49b = $("meti-rttatxe.".split("").reverse().join(""))['find'](".filter-pop .attr-filter[data-val-eid='" + extObj['attrId'] + "'][data-val-filtertype='2']");
    if (_0x72b49b['length'] == (921336 ^ 921336)) {
        return;
    }
    var _0x241bc = _0x72b49b['find'](".filter-pop-bottom");
    if (_0x241bc['hasClass']("esohc-elgnis".split("").reverse().join(""))) {
        _0x241bc['find'](".pop-chose-item[data-value='" + extObj['attrVal'] + "']")['each'](function(index, e) {
            if (!$(this)['hasClass']("no".split("").reverse().join(""))) {
                $(this)['click']();
            }
        });
        return;
    }
    if (_0x241bc['hasClass']("esohc-erom".split("").reverse().join(""))) {
        _0x241bc['find'](".pop-chose-item[data-value='" + extObj['attrVal'] + "']")['each'](function(index, e) {
            if (!$(this)['hasClass']("moreon")) {
                var _0xaff;
                var _0x316f = $(this)['find'](".item-children");
                _0xaff = 776794 ^ 776799;
                if (_0x316f['length'] > (960013 ^ 960013)) {
                    _0x316f['find'](".child")['each'](function(cIndex, ce) {
                        if (!$(this)['hasClass']("on")) {
                            $(this)['click']();
                        }
                    });
                } else {
                    $(this)['click']();
                }
                _0x72b49b['find']("a ntb-pop-retlif.".split("").reverse().join(""))['click']();
            }
        });
        return;
    }
}
function addJhFilterParam(extObj) {
    if (extObj['attrPid'] != undefined && extObj['attrPid'] != "undefined" && extObj['attrPid'] != null && extObj['attrPid'] != "llun".split("").reverse().join("") && extObj['attrPid'] != '') {
        $(".extattr-item")['find'](".filter-pop .attr-filter[data-val-filtertype='3']")['find'](".agg-filter .pop-chose-item .item-children[data-val-subeid='" + extObj['attrId'] + "']")['find'](".child[data-value='" + extObj['attrVal'] + "]'".split("").reverse().join(""))['each'](function(index, e) {
            if (!$(this)['hasClass']("no".split("").reverse().join(""))) {
                $(this)['click']();
                $(this)['parents']("retlif-rtta.".split("").reverse().join(""))['find']("a ntb-pop-retlif.".split("").reverse().join(""))['click']();
            }
        });
        return;
    }
    var _0x55b = (125674 ^ 125666) + (361648 ^ 361651);
    var _0xf50f9e = $(".extattr-item")['find'](".filter-pop .attr-filter[data-val-filtertype='3']")['find'](".agg-filter[data-val-eid='" + extObj['attrId'] + "]'".split("").reverse().join(""));
    _0x55b = 'afdcae';
    if (_0xf50f9e['length'] == (859668 ^ 859668)) {
        return;
    }
    var _0xe22f = (137906 ^ 137909) + (982180 ^ 982178);
    var _0x39_0x593 = _0xf50f9e['find'](".filter-pop-bottom");
    _0xe22f = (380591 ^ 380589) + (141177 ^ 141168);
    if (_0x39_0x593['hasClass']("single-chose")) {
        _0x39_0x593['find']("'=eulav-atad[meti-esohc-pop.".split("").reverse().join("") + extObj['attrVal'] + "]'".split("").reverse().join(""))['each'](function(index, e) {
            if (!$(this)['hasClass']("on")) {
                $(this)['click']();
                _0xf50f9e['parent']()['find'](".filter-pop-btn a")['click']();
            }
        });
        return;
    }
    if (_0x39_0x593['hasClass']("esohc-erom".split("").reverse().join(""))) {
        _0x39_0x593['find'](".pop-chose-item[data-value='" + extObj['attrVal'] + "']")['each'](function(index, e) {
            if (!$(this)['hasClass']("noerom".split("").reverse().join(""))) {
                var _0x40_0x57b = $(this)['find'](".item-children");
                if (_0x40_0x57b['length'] > (885848 ^ 885848)) {
                    _0x40_0x57b['find']("dlihc.".split("").reverse().join(""))['each'](function(cIndex, ce) {
                        if (!$(this)['hasClass']("on")) {
                            $(this)['click']();
                        }
                    });
                } else {
                    $(this)['click']();
                }
                _0xf50f9e['parent']()['find'](".filter-pop-btn a")['click']();
            }
        });
        return;
    }
}