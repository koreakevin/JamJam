
const element = document.querySelectorAll(".region-name");
var s1 = document.getElementById("seoul");
var s2 = document.getElementById("gyeonggi");
var s3 = document.getElementById("incheon");
var s4 = document.getElementById("gangwon");
var s5 = document.getElementById("chungbuk");
var s6 = document.getElementById("sejong");
var s7 = document.getElementById("chungnam");
var s8 = document.getElementById("gyeongbuk");
var s9 = document.getElementById("daejeon");
var s10 = document.getElementById("daegu");
var s11 = document.getElementById("jeonbuk");
var s12 = document.getElementById("gwangju");
var s13 = document.getElementById("jeonnam");
var s14 = document.getElementById("gyeongnam");
var s15 = document.getElementById("busan");
var s16 = document.getElementById("ulsan");
var s17 = document.getElementById("jeju");

function deleteText() {
  const element = document.querySelectorAll(".region-name");
  console.log(element);
  s1.innerHTML = "";
  s2.innerHTML = "";
  s3.innerHTML = "";
  s4.innerHTML = "";
  s5.innerHTML = "";
  s6.innerHTML = "";
  s7.innerHTML = "";
  s8.innerHTML = "";
  s9.innerHTML = "";
  s10.innerHTML = "";
  s11.innerHTML = "";
  s12.innerHTML = "";
  s13.innerHTML = "";
  s14.innerHTML = "";
  s15.innerHTML = "";
  s16.innerHTML = "";
  s17.innerHTML = "";
} 

function showseoul() {
    s1.innerHTML = "<li><input type='checkbox' id='jongnogu'>종로구</li><li><input type='checkbox' id='junggu_s'>중구</li><li><input type='checkbox' id='yongsangu'>용산구</li><li><input type='checkbox' id='gwangjingu'>광진구</li><li><input type='checkbox' id='dongdaemungu'>동대문구</li><li><input type='checkbox' id='jungnanggu'>중랑구</li><li><input type='checkbox' id='seongbukgu'>성북구</li><li><input type='checkbox' id='gangbukgu'>강북구</li><li><input type='checkbox' id='dobonggu'>도봉구</li><li><input type='checkbox' id='nowongu'>노원구</li><li><input type='checkbox' id='eunpyeonggu'>은평구</li><li><input type='checkbox' id='seodaemungu'>서대문구</li><li><input type='checkbox' id='mapogu'>마포구</li><li><input type='checkbox' id='yangcheongu'>양천구</li><li><input type='checkbox' id='gangseogu'>강서구</li><li><input type='checkbox' id='gurogu'>구로구</li><li><input type='checkbox' id='geumcheongu'>금천구</li><li><input type='checkbox' id='yeongdeungpogu'>영등포구</li><li><input type='checkbox' id='dongjakgu'>동작구</li><li><input type='checkbox' id='gwanakgu'>관악구</li><li><input type='checkbox' id='seochogu'>서초구</li><li><input type='checkbox' id='gangnamgu'>강남구</li><li><input type='checkbox' id='songpagu'>송파구</li><li><input type='checkbox' id='gangdonggu'>강동구</li>";

    var jongnogu = document.getElementById(jongnogu);

    var junggu_s = document.getElementById(junggu_s);
    
    var yongsangu = document.getElementById(yongsangu);

    var gwangjingu = document.getElementById(gwangjingu);

    var dongdaemungu = document.getElementById(dongdaemungu);

    var jungnanggu = document.getElementById(jungnanggu);
    
    var seongbukgu = document.getElementById(seongbukgu);

    var gangbukgu = document.getElementById(gangbukgu);

    var dobonggu = document.getElementById(dobonggu);

    var nowongu = document.getElementById(nowongu);

    var eunpyeonggu = document.getElementById(eunpyeonggu);

    var mapogu = document.getElementById(mapogu);

    var yangcheongu = document.getElementById(yangcheongu);

    var gangseogu = document.getElementById(gangseogu);

    var gurogu = document.getElementById(gurogu);

    var geumcheongu = document.getElementById(geumcheongu);

    var yeongdeungpogu = document.getElementById(yeongdeungpogu);

    var dongjakgu = document.getElementById(dongjakgu);

    var gwanakgu = document.getElementById(gwanakgu);

    var seochogu = document.getElementById(seochogu);

    var gangnamgu = document.getElementById(gangnamgu);

    var songpagu = document.getElementById(songpagu);

    var gangdonggu = document.getElementById(gangdonggu);
  }

function showgyeonggi() {
    s2.innerHTML = "<li><input type='checkbox' id='gapyeonggun'>가평군</li><li><input type='checkbox' id='gapyeonggun'>가평군</li><li><input type='checkbox' id='yangpyeonggun'>양평군</li><li><input type='checkbox' id='yeoncheongun'>연천군</li><li><input type='checkbox' id='goyangsi'>고양시</li><li><input type='checkbox' id='gwacheonsi'>과천시</li><li><input type='checkbox' id='gwangmyeongsi'>광명시</li><li><input type='checkbox' id='gwangjusi'>광주시</li><li><input type='checkbox' id='gurisi'>구리시</li><li><input type='checkbox' id='gunposi'>군포시</li><li><input type='checkbox' id='gimposi'>김포시</li><li><input type='checkbox' id='namyangjusi'>남양주시</li><li><input type='checkbox' id='dongducheongsi'>동두천시</li><li><input type='checkbox' id='bucheonsi'>부천시</li><li><input type='checkbox' id='seongnamsi'>성남시</li><li><input type='checkbox' id='suwonsi'>수원시</li><li><input type='checkbox' id='siheungsi'>시흥시</li><li><input type='checkbox' id='ansansi'>안산시</li><li><input type='checkbox' id='anseongsi'>안성시</li><li><input type='checkbox' id='anyangsi'>안양시</li><li><input type='checkbox' id='yangjusi'>양주시</li><li><input type='checkbox' id='yeojusi'>여주시</li><li><input type='checkbox' id='osansi'>오산시</li><li><input type='checkbox' id='yonginsi'>용인시</li><li><input type='checkbox' id='uiwangsi'>의왕시</li><li><input type='checkbox' id='uijeongbusi'>의정부시</li><li><input type='checkbox' id='icheonsi'>이천시</li><li><input type='checkbox' id='pajusi'>파주시</li><li><input type='checkbox' id='pyeongtaeksi'>평택시</li><li><input type='checkbox' id='pocheonsi'>포천시</li><li><input type='checkbox' id='hanamsi'>하남시</li><li><input type='checkbox' id='hwaseongsi'>화성시</li>";

    var gapyeonggun = document.getElementById(gapyeonggun);

    var yangpyeonggun = document.getElementById(yangpyeonggun);

    var yeoncheongun = document.getElementById(yeoncheongun);

    var goyangsi = document.getElementById(goyangsi);

    var gwacheonsi = document.getElementById(gwacheonsi);

    var gwangmyeongsi = document.getElementById(gwangmyeongsi);

    var gwangjusi = document.getElementById(gwangjusi);

    var gurisi = document.getElementById(gurisi);

    var gunposi = document.getElementById(gunposi);

    var gimposi = document.getElementById(gimposi);

    var namyangjusi = document.getElementById(namyangjusi);

    var dongducheongsi = document.getElementById(dongducheongsi);

    var bucheonsi = document.getElementById(bucheonsi);

    var seongnamsi = document.getElementById(seongnamsi);

    var suwonsi = document.getElementById(suwonsi);

    var siheungsi = document.getElementById(siheungsi);

    var ansansi = document.getElementById(ansansi);

    var anseongsi = document.getElementById(anseongsi);

    var anyangsi = document.getElementById(anyangsi);

    var yangjusi = document.getElementById(yangjusi);

    var yeojusi = document.getElementById(yeojusi);

    var osansi = document.getElementById(osansi);

    var yonginsi = document.getElementById(yonginsi);

    var uiwangsi = document.getElementById(uiwangsi);

    var uijeongbusi = document.getElementById(uijeongbusi);

    var icheonsi = document.getElementById(icheonsi);

    var pajusi = document.getElementById(pajusi);

    var pyeongtaeksi = document.getElementById(pyeongtaeksi);

    var pocheonsi = document.getElementById(pocheonsi);

    var hanamsi = document.getElementById(hanamsi);

    var hwaseongsi = document.getElementById(hwaseongsi);
  }

function showincheon() {
    s3.innerHTML = "<li><input type='checkbox' id='junggu_i'>중구</li><li><input type='checkbox' id='donggu_i'>동구</li><li><input type='checkbox' id='michuholgu'>미추홀구</li><li><input type='checkbox' id='yeonsugu'>연수구</li><li><input type='checkbox' id='namdonggu'>남동구</li><li><input type='checkbox' id='bupyeonggu'>부평구</li><li><input type='checkbox' id='gyeuanggu'>계양구</li><li><input type='checkbox' id='seoyanggu'>서양구</li><li><input type='checkbox' id='seogu_i'>서구</li><li><input type='checkbox' id='ganghwagun'>강화군</li><li><input type='checkbox' id='ongjingun'>옹진군</li>";

    var junggu_i = document.getElementById(junggu_i);

    var donggu_i = document.getElementById(donggu_i);

    var michuholgu = document.getElementById(michuholgu);

    var yeonsugu = document.getElementById(yeonsugu);

    var namdonggu = document.getElementById(namdonggu);

    var bupyeonggu = document.getElementById(bupyeonggu);

    var gyeonggi = document.getElementById(gyeonggi);

    var seoyanggu = document.getElementById(seoyanggu);

    var seogu_i = document.getElementById(seogu_i);

    var ganghwagun = document.getElementById(ganghwagun);

    var ongjingun = document.getElementById(ongjingun);
}

function showgangwon() {
    s4.innerHTML = "<li><input type='checkbox' id='wonjusi'>원주시</li><li><input type='checkbox' id='chuncheonsi'>춘천시</li><li><input type='checkbox' id='gangneungsi'>강릉시</li><li><input type='checkbox' id='donghaesi'>동해시</li><li><input type='checkbox' id='sokchosi'>속초시</li><li><input type='checkbox' id='samcheoksi'>삼척시</li><li><input type='checkbox' id='taebaeksi'>태백시</li><li><input type='checkbox' id='hongcheongun'>홍천군</li><li><input type='checkbox' id='cheorwon'>철원군</li><li><input type='checkbox' id='hoengseonggun'>횡성군</li><li><input type='checkbox' id='pyeongchanggun'>평창군</li><li><input type='checkbox' id='jeongseongun'>정선군</li><li><input type='checkbox' id='yeongwolgun'>영월군</li><li><input type='checkbox' id='injegun'>인제군</li><li><input type='checkbox' id='goseonggun'>고성군</li><li><input type='checkbox' id='yangyanggun'>양양군</li><li><input type='checkbox' id='hwacheongun'>화천군</li><li><input type='checkbox' id='yanggugun'>양구군</li>";

    var wonjusi = document.getElementById(wonjusi);

    var chuncheonsi = document.getElementById(chuncheonsi);

    var gangneungsi = document.getElementById(gangneungsi);

    var donghaesi = document.getElementById(donghaesi);

    var sokchosi = document.getElementById(sokchosi);

    var samcheoksi = document.getElementById(samcheoksi);

    var taebaeksi = document.getElementById(taebaeksi);

    var hongcheongun = document.getElementById(hongcheongun);

    var cheorwon = document.getElementById(cheorwon);

    var hoengseonggun = document.getElementById(hoengseonggun);

    var pyeongchanggun = document.getElementById(pyeongchanggun);

    var jeongseongun = document.getElementById(jeongseongun);

    var yeongwolgun = document.getElementById(yeongwolgun);

    var injegun = document.getElementById(injegun);

    var goseonggun = document.getElementById(goseonggun);

    var yangyanggun = document.getElementById(yangyanggun);

    var hwacheongun = document.getElementById(hwacheongun);

    var yanggugun = document.getElementById(yanggugun);
}

function showchungbuk() {
  s5.innerHTML = "<li><input type='checkbox' id='cheongjusi'>청주시</li><li><input type='checkbox' id='seowongu'>서원구</li><li><input type='checkbox' id='heungdeokgu'>흥덕구</li><li><input type='checkbox' id='chengwongu'>청원구</li><li><input type='checkbox' id='chungjusi'>충주시</li><li><input type='checkbox' id='jecheonsi'>제천시</li><li><input type='checkbox' id='boeungun'>보은군</li><li><input type='checkbox' id='okcheongun'>옥천군</li><li><input type='checkbox' id='yeongdonggun'>영동군</li><li><input type='checkbox' id='jeungpyeonggun'>증평군</li><li><input type='checkbox' id='jincheongun'>진천군</li><li><input type='checkbox' id='geosangun'>괴산군</li><li><input type='checkbox' id='eumseonggun'>음성군</li><li><input type='checkbox' id='danyanggun'>단양군</li>";

  var cheongjusi = document.getElementById(cheongjusi);

  var seowongu = document.getElementById(seowongu);

  var heungdeokgu = document.getElementById(heungdeokgu);

  var cheongwongu = document.getElementById(cheongwongu);

  var chungjusi = document.getElementById(chungjusi);

  var jecheonsi = document.getElementById(jecheonsi);

  var boeungun = document.getElementById(boeungun);

  var okcheongun = document.getElementById(okcheongun);

  var yeongdonggun = document.getElementById(yeongdonggun);

  var jeungpyeonggun = document.getElementById(jeungpyeonggun);

  var jincheongun = document.getElementById(jincheongun);

  var geosangun = document.getElementById(geosangun);

  var eumseonggun = document.getElementById(eumseonggun);

  var danyanggun = document.getElementById(danyanggun);
}

function showsejong() {
  s6.innerHTML = "<li><input type='checkbox' id='sojeongmeon'>소정면</li><li><input type='checkbox' id='jeonuimeon'>전의면</li><li><input type='checkbox' id='jeondongmeon'>전동면</li><li><input type='checkbox' id='jochiwonmeon'>조치원읍</li><li><input type='checkbox' id='yeonseomeon'>연서면</li><li><input type='checkbox' id='yeondongmeon'>연동면</li><li><input type='checkbox' id='yeongimeon'>연기면</li><li><input type='checkbox' id='bugangmeonmeon'>부강면</li><li><input type='checkbox' id='janggunmeon'>장군면</li><li><input type='checkbox' id='geumnammeon'>금남면</li>";

  var sojeongmeon = document.getElementById(sojeongmeon);

  var jeonuimeon = document.getElementById(jeonuimeon);

  var jeondongmeon = document.getElementById(jeondongmeon);

  var jochiwonmeon = document.getElementById(jochiwonmeon);

  var yeonseomeon = document.getElementById(yeonseomeon);

  var yeondongmeon= document.getElementById(yeondongmeon);

  var yeongimeon = document.getElementById(yeongimeon);

  var bugangmeonmeon = document.getElementById(bugangmeonmeon);

  var janggunmeon = document.getElementById(janggunmeon);

  var geumnammeon = document.getElementById(geumnammeon);
}

function showchungnam() {
  s7.innerHTML = "<li><input type='checkbox' id='cheonansi'>천안시</li><li><input type='checkbox' id='gongjusi'>공주시</li><li><input type='checkbox' id='boryeongsi'>보령시</li><li><input type='checkbox' id='asansi'>아산시</li><li><input type='checkbox' id='seosansi'>서산시</li><li><input type='checkbox' id='nonsansi'>논산시</li><li><input type='checkbox' id='gyeryongsi'>계룡시</li><li><input type='checkbox' id='dangjinsi'>당진시</li><li><input type='checkbox' id='geumsangun'>금산군</li><li><input type='checkbox' id='buyeogun'>부여군</li><li><input type='checkbox' id='seocheongun'>서천군</li><li><input type='checkbox' id='cheongyanggun'>청양군</li><li><input type='checkbox' id='hongseonggun'>홍성군</li><li><input type='checkbox' id='yesangun'>예산군</li><li><input type='checkbox' id='taeangun'>태안군</li>";

  var cheonansi = document.getElementById(cheonansi);

  var gongjusi = document.getElementById(gongjusi);

  var boryeongsi = document.getElementById(boryeongsi);

  var asansi = document.getElementById(asansi);

  var seosansi = document.getElementById(seosansi);

  var nonsansi = document.getElementById(nonsansi);

  var gyeryongsi = document.getElementById(gyeryongsi);

  var dangjinsi = document.getElementById(dangjinsi);

  var geumsangun = document.getElementById(geumsangun);

  var buyeogun = document.getElementById(buyeogun);

  var seocheongun = document.getElementById(seocheongun);

  var cheongyanggun = document.getElementById(cheongyanggun);

  var hongseonggun = document.getElementById(hongseonggun);

  var yesangun = document.getElementById(yesangun);

  var taeangun = document.getElementById(taeangun);
}

function showgyeongbuk() {
  s8.innerHTML = "<li><input type='checkbox' id='pohangsi'>포항시</li><li><input type='checkbox' id='gyeongjusi'>경주시</li><li><input type='checkbox' id='gimcheonsi'>김천시</li><li><input type='checkbox' id='andongsi'>안동시</li><li><input type='checkbox' id='gumisi'>구미시</li><li><input type='checkbox' id='yeongjusi'>영주시</li><li><input type='checkbox' id='yeongcheonsi'>영천시</li><li><input type='checkbox' id='sangjusi'>상주시</li><li><input type='checkbox' id='mungyeongsi'>문경시</li><li><input type='checkbox' id='gyeongsansi'>경산시</li><li><input type='checkbox' id='gunwigun'>군위군</li><li><input type='checkbox' id='uiseonggun'>의성군</li><li><input type='checkbox' id='cheongsonggun'>청송군</li><li><input type='checkbox' id='yeongyanggun'>영양군</li><li><input type='checkbox' id='yeongdeokgun'>영덕군</li><li><input type='checkbox' id='cheongdogun'>청도군</li><li><input type='checkbox' id='goryeonggun'>고령군</li><li><input type='checkbox' id='seongjugun'>성주군</li><li><input type='checkbox' id='chilgokgun'>칠곡군</li><li><input type='checkbox' id='yecheongun'>예천군</li><li><input type='checkbox' id='bonghwagun'>봉화군</li><li><input type='checkbox' id='uljingun'>울진군</li><li><input type='checkbox' id='ulleunggun'>울릉군</li>";
  
  var pohangsi = document.getElementById(pohangsi);
  
  var gyeongjusi = document.getElementById(gyeongjusi);
  
  var gimcheonsi = document.getElementById(gimcheonsi);

  var andongsi = document.getElementById(andongsi);

  var gumisi = document.getElementById(gumisi);

  var yeongjusi = document.getElementById(yeongjusi);

  var yeongcheonsi = document.getElementById(yeongcheonsi);

  var sangjusi = document.getElementById(sangjusi);

  var mungyeongsi = document.getElementById(mungyeongsi);

  var gyeongsansi = document.getElementById(gyeongsansi);

  var gunwigun = document.getElementById(gunwigun);

  var uiseonggun = document.getElementById(uiseonggun);

  var cheongsonggun = document.getElementById(cheongsonggun);

  var yeongyanggun = document.getElementById(yeongyanggun);

  var yeongdeokgun = document.getElementById(yeongdeokgun);

  var cheongdogun = document.getElementById(cheongdogun);

  var goryeonggun = document.getElementById(goryeonggun);

  var seongjugun = document.getElementById(seongjugun);

  var chilgokgun = document.getElementById(chilgokgun);

  var yecheongun = document.getElementById(yecheongun);
  
  var bonghwagun = document.getElementById(bonghwagun);

  var uljingun = document.getElementById(uljingun);

  var ulleunggun = document.getElementById(ulleunggun);
}

function showdaejeon() {
  s9.innerHTML = "<li><input type='checkbox' id='donggu_dj'>동구</li><li><input type='checkbox' id='junggu_dj'>중구</li><li><input type='checkbox' id='seogu_dj'>서구</li><li><input type='checkbox' id='yooseonggu'>유성구</li><li><input type='checkbox' id='daedeokgu'>대덕구</li>";

  var donggu_dj = document.getElementById(donggu_dj);

  var junggu_dj = document.getElementById(junggu_dj);

  var seogu_dj = document.getElementById(seogu_dj);

  var yooseonggu = document.getElementById(yooseonggu);

  var daedeokgu = document.getElementById(daedeokgu);
}

function showdaegu() {
  s10.innerHTML = "<li><input type='checkbox' id='junggu-dg'>중구</li><li><input type='checkbox' id='donggu-dg'>동구</li><li><input type='checkbox' id='seogu-dg'>서구</li><li><input type='checkbox' id='namgu-dg'>남구</li><li><input type='checkbox' id='bukgu-dg'>북구</li><li><input type='checkbox' id='suseonggu'>수성구</li><li><input type='checkbox' id='dalseogu'>달서구</li><li><input type='checkbox' id='dalseonggun'>달성군</li>";

  var junggu_dg = document.getElementById(junggu_dg);

  var donggu_dg = document.getElementById(donggu_dg);

  var seogu_dg = document.getElementById(seogu_dg);

  var namgu_dg = document.getElementById(namgu_dg);

  var bukgu_dg = document.getElementById(bukgu_dg);

  var suseonggu = document.getElementById(suseonggu);

  var dalseogu = document.getElementById(dalseogu);

  var dalseonggun = document.getElementById(dalseonggun);
}

function showjeonbuk() {
  s11.innerHTML = "<li><input type='checkbox' id='jeonjusi'>전주시</li><li><input type='checkbox' id='gunsansi'>군산시</li><li><input type='checkbox' id='iksansi'>익산시</li><li><input type='checkbox' id='jeongeupsi'>정읍시</li><li><input type='checkbox' id='namwonsi'>남원시</li><li><input type='checkbox' id='gimjesi'>김제시</li><li><input type='checkbox' id='wanjugun'>완주군</li><li><input type='checkbox' id='jinangun'>진안군</li><li><input type='checkbox' id='mujugun'>무주군</li><li><input type='checkbox' id='jangsugun'>장수군</li><li><input type='checkbox' id='imsilgun'>임실군</li><li><input type='checkbox' id='sunchanggun'>순창군</li><li><input type='checkbox' id='gochanggun'>고창군</li><li><input type='checkbox' id='buangun'>부안군</li>";

  var jeonjusi = document.getElementById(jeonjusi);
  
  var gunsansi = document.getElementById(gunsansi);

  var iksansi = document.getElementById(iksansi);

  var jeongeupsi = document.getElementById(jeongeupsi);

  var namwonsi = document.getElementById(namwonsi);

  var gimjesi = document.getElementById(gimjesi);

  var wanjusi = document.getElementById(wanjusi);

  var jinangun = document.getElementById(jinangun);

  var mujugun = document.getElementById(mujugun);

  var jangsugun = document.getElementById(jangsugun);

  var imsilgun = document.getElementById(imsilgun);

  var sunchanggun = document.getElementById(sunchanggun);

  var gochanggun = document.getElementById(gochanggun);

  var buangun = document.getElementById(buangun);
}

function showgwangju() {
  s12.innerHTML = "<li><input type='checkbox' id='gwangsangu'>광산구</li><li><input type='checkbox' id='donggu_j'>동구</li><li><input type='checkbox' id='seogu_j'>서구</li><li><input type='checkbox' id='namgu_j'>남구</li><li><input type='checkbox' id='bukgu_j'>북구</li>";

  var gwangsangu = document.getElementById(gwangsangu);

  var donggu_j = document.getElementById(donggu_j);

  var seogu_j = document.getElementById(seogu_j);

  var namgu_j = document.getElementById(namgu_j);

  var bukgu_j = document.getElementById(bukgu_j);
}

function showjeonnam() {
  s13.innerHTML = "<li><input type='checkbox' id='mokposi'>목포시</li><li><input type='checkbox' id='yeosusi'>여수시</li><li><input type='checkbox' id='suncheonsi'>순천시</li><li><input type='checkbox' id='najusi'>나주시</li><li><input type='checkbox' id='gwangyangsi'>광양시</li><li><input type='checkbox' id='damyanggun'>담양군</li><li><input type='checkbox' id='gokseonggun'>곡성군</li><li><input type='checkbox' id='guryegun'>구례군</li><li><input type='checkbox' id='goheunggun'>고흥군</li><li><input type='checkbox' id='boseonggun'>보성군</li><li><input type='checkbox' id='hwasungun'>화순군</li><li><input type='checkbox' id='jangheunggun'>장흥군</li><li><input type='checkbox' id='gangjingun'>강진군</li><li><input type='checkbox' id='haenamgun'>해남군</li><li><input type='checkbox' id='yeongamgun'>영암군</li><li><input type='checkbox' id='muangun'>무안군</li><li><input type='checkbox' id='hampyeonggun'>함평군</li><li><input type='checkbox' id='yeonggwanggun'>영광군</li><li><input type='checkbox' id='jangseonggun'>장성군</li><li><input type='checkbox' id='wandogun'>완도군</li><li><input type='checkbox' id='jindogun'>진도군</li><li><input type='checkbox' id='sinangun'>신안군</li>";

  var mokposi = document.getElementById(mokposi);

  var yeosusi = document.getElementById(yeosusi);

  var suncheonsi = document.getElementById(suncheonsi);

  var najusi = document.getElementById(najusi);

  var gwangyangsi = document.getElementById(gwangyangsi);

  var damyanggun = document.getElementById(damyanggun);

  var gokseonggun = document.getElementById(gokseonggun);

  var guryegun = document.getElementById(guryegun);

  var goheunggun = document.getElementById(goheunggun);

  var boseonggun = document.getElementById(boseonggun);

  var hwasungun = document.getElementById(hwasungun);

  var jangheunggun = document.getElementById(jangheunggun);

  var gangjingun = document.getElementById(gangjingun);
  
  var haenamgun = document.getElementById(haenamgun);

  var yeongamgun = document.getElementById(yeongamgun);

  var muangun = document.getElementById(muangun);

  var hampyeonggun = document.getElementById(hampyeonggun);

  var yeonggwanggun = document.getElementById(yeonggwanggun);

  var jangseonggun = document.getElementById(jangseonggun);

  var wandogun = document.getElementById(wandogun);

  var jindogun = document.getElementById(jindogun);

  var sinangun = document.getElementById(sinangun);
}

function showgyeongnam() {
  s14.innerHTML = "<li><input type='checkbox' id='changwonsi'>창원시</li><li><input type='checkbox' id='gimhaesi'>김해시</li><li><input type='checkbox' id='yangsansi'>양산시</li><li><input type='checkbox' id='jinjusi'>진주시</li><li><input type='checkbox' id='geojesi'>거제시</li><li><input type='checkbox' id='tongyeongsi'>통영시</li><li><input type='checkbox' id='sacheonsi'>사천시</li><li><input type='checkbox' id='miryangsi'>밀양시</li><li><input type='checkbox' id='hamangun'>함안군</li><li><input type='checkbox' id='geochanggun'>거창군</li><li><input type='checkbox' id='changnyeonggun'>창녕군</li><li><input type='checkbox' id='goseonggun'>고성군</li><li><input type='checkbox' id='hadonggun'>하동군</li><li><input type='checkbox' id='hapcheongun'>합천군</li><li><input type='checkbox' id='namhaegun'>남해군</li><li><input type='checkbox' id='hamyanggun'>함양군</li><li><input type='checkbox' id='sancheonggun'>산청군</li><li><input type='checkbox' id='uiryeonggun'>의령군</li>";

  var changwonsi = document.getElementById(changwonsi);

  var gimhaesi = document.getElementById(gimhaesi);

  var yangsansi = document.getElementById(yangsansi);

  var jinjusi = document.getElementById(jinjusi);

  var geojesi = document.getElementById(geojesi);

  var tongyeongsi = document.getElementById(tongyeongsi);

  var sacheonsi = document.getElementById(sacheonsi);

  var miryangsi = document.getElementById(miryangsi);

  var hamangun = document.getElementById(hamangun);

  var geochanggun = document.getElementById(geochanggun);

  var changnyeonggun = document.getElementById(changnyeonggun);

  var goseonggun = document.getElementById(goseonggun);

  var hadonggun = document.getElementById(hadonggun);

  var hapcheongun = document.getElementById(hapcheongun);

  var namhaegun = document.getElementById(namhaegun);

  var hamyanggun = document.getElementById(hamyanggun);

  var sancheonggun = document.getElementById(sancheonggun);

  var uiryeonggun = document.getElementById(uiryeonggun);
}

function showbusan() {
  s15.innerHTML = "<li><input type='checkbox' id='junggu_b'>중구</li><li><input type='checkbox' id='seogu_b'>서구</li><li><input type='checkbox' id='donggu_b'>동구</li><li><input type='checkbox' id='yeongdogu'>영도구</li><li><input type='checkbox' id='jingu'>진구</li><li><input type='checkbox' id='dongnaegu'>동래구</li><li><input type='checkbox' id='namgu_b'>남구</li><li><input type='checkbox' id='bukgu_b'>북구</li><li><input type='checkbox' id='haeundaegu'>해운대구</li><li><input type='checkbox' id='sahagu'>사하구</li><li><input type='checkbox' id='geumjeonggu'>금정구</li><li><input type='checkbox' id='gangseo_bu'>강서구</li><li><input type='checkbox' id='yeonjegu'>연제구</li><li><input type='checkbox' id='suyeonggu'>수영구</li><li><input type='checkbox' id='sasanggu'>사상구</li><li><input type='checkbox' id='gijang'>기장군</li>";

  var junggu_b = document.getElementById(junggu_b);

  var seogu_b = document.getElementById(seogu_b);

  var donggu_b = document.getElementById(donggu_b);

  var yeongdogu= document.getElementById(yeongdogu);

  var jingu = document.getElementById(jingu);

  var dongnaegu = document.getElementById(dongnaegu);

  var namgu_b = document.getElementById(namgu_b);

  var bukgu_b = document.getElementById(bukgu_b);

  var haeundaegu = document.getElementById(haeundaegu);

  var sahagu = document.getElementById(sahagu);

  var geumjeonggu = document.getElementById(geumjeonggu);

  var gangseo_b = document.getElementById(gangseo_b);

  var yeonjegu = document.getElementById(yeonjegu);

  var suyeonggu = document.getElementById(suyeonggu);

  var sasanggu = document.getElementById(sasanggu);

  var gijang = document.getElementById(gijang);
}

function showulsan() {
  s16.innerHTML = "<li><input type='checkbox' id='junggu_u'>중구</li><li><input type='checkbox' id='namgu_u'>남구</li><li><input type='checkbox' id='donggu_u'>동구</li><li><input type='checkbox' id='bukgu_u'>북구</li><li><input type='checkbox' id='uljugun'>울주군</li>";

  var junggu_u = document.getElementById(junggu_u);

  var namgu_u = document.getElementById(namgu_u);

  var donggu_u = document.getElementById(donggu_u);

  var bukgu_u = document.getElementById(bukgu_u);

  var uljugun = document.getElementById(uljugun);
}


function showjeju() {
  s17.innerHTML = "<li><input type='checkbox' id='jejusi'>제주시</li><li><input type='checkbox' id='seogwiposi'>서귀포시</li>";

  var jejusi = document.getElementById(jejusi);

  var seogwiposi = document.getElementById(seogwiposi);
}