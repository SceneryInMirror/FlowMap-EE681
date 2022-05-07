/////////////////////////////////////////////////////////////
// Created by: Synopsys DC Expert(TM) in wire load mode
// Version   : P-2019.03-SP1-1
// Date      : Fri May  6 01:20:55 2022
/////////////////////////////////////////////////////////////


module c1355 ( G1, G8, G15, G22, G29, G36, G43, G50, G57, G64, G71, G78, G85, 
        G92, G99, G106, G113, G120, G127, G134, G141, G148, G155, G162, G169, 
        G176, G183, G190, G197, G204, G211, G218, G225, G226, G227, G228, G229, 
        G230, G231, G232, G233, G1324, G1325, G1326, G1327, G1328, G1329, 
        G1330, G1331, G1332, G1333, G1334, G1335, G1336, G1337, G1338, G1339, 
        G1340, G1341, G1342, G1343, G1344, G1345, G1346, G1347, G1348, G1349, 
        G1350, G1351, G1352, G1353, G1354, G1355 );
  input G1, G8, G15, G22, G29, G36, G43, G50, G57, G64, G71, G78, G85, G92,
         G99, G106, G113, G120, G127, G134, G141, G148, G155, G162, G169, G176,
         G183, G190, G197, G204, G211, G218, G225, G226, G227, G228, G229,
         G230, G231, G232, G233;
  output G1324, G1325, G1326, G1327, G1328, G1329, G1330, G1331, G1332, G1333,
         G1334, G1335, G1336, G1337, G1338, G1339, G1340, G1341, G1342, G1343,
         G1344, G1345, G1346, G1347, G1348, G1349, G1350, G1351, G1352, G1353,
         G1354, G1355;
  wire   n158, n159, n160, n161, n162, n163, n164, n165, n166, n167, n168,
         n169, n170, n171, n172, n173, n174, n175, n176, n177, n178, n179,
         n180, n181, n182, n183, n184, n185, n186, n187, n188, n189, n190,
         n191, n192, n193, n194, n195, n196, n197, n198, n199, n200, n201,
         n202, n203, n204, n205, n206, n207, n208, n209, n210, n211, n212,
         n213, n214, n215, n216, n217, n218, n219, n220, n221, n222, n223,
         n224, n225, n226, n227, n228, n229, n230, n231, n232, n233, n234,
         n235, n236, n237, n238, n239, n240, n241, n242, n243, n244, n245,
         n246, n247, n248, n249, n250, n251, n252, n253, n254, n255, n256,
         n257, n258, n259, n260, n261, n262, n263, n264, n265, n266, n267,
         n268, n269, n270, n271, n272, n273, n274, n275, n276, n277, n278,
         n279, n280, n281, n282, n283, n284, n285, n286, n287, n288, n289,
         n290, n291, n292, n293, n294, n295, n296, n297, n298, n299, n300,
         n301, n302, n303, n304, n305, n306, n307, n308, n309, n310, n311,
         n312, n313, n314, n315, n316, n317, n318, n319, n320;

  XNOR2 U190 ( .a(G218), .b(n158), .O(G1355) );
  NAND2 U191 ( .a(n159), .b(n160), .O(n158) );
  XNOR2 U192 ( .a(G211), .b(n161), .O(G1354) );
  NAND2 U193 ( .a(n159), .b(n162), .O(n161) );
  XNOR2 U194 ( .a(G204), .b(n163), .O(G1353) );
  NAND2 U195 ( .a(n159), .b(n164), .O(n163) );
  XNOR2 U196 ( .a(G197), .b(n165), .O(G1352) );
  NAND2 U197 ( .a(n159), .b(n166), .O(n165) );
  AND2 U198 ( .a(n167), .b(n168), .O(n159) );
  NOR2 U199 ( .a(n169), .b(n170), .O(n168) );
  OR2 U200 ( .a(n171), .b(n172), .O(n170) );
  AND2 U201 ( .a(n173), .b(n174), .O(n167) );
  XNOR2 U202 ( .a(G190), .b(n175), .O(G1351) );
  NAND2 U203 ( .a(n176), .b(n160), .O(n175) );
  XNOR2 U204 ( .a(G183), .b(n177), .O(G1350) );
  NAND2 U205 ( .a(n176), .b(n162), .O(n177) );
  XNOR2 U206 ( .a(G176), .b(n178), .O(G1349) );
  NAND2 U207 ( .a(n176), .b(n164), .O(n178) );
  XNOR2 U208 ( .a(G169), .b(n179), .O(G1348) );
  NAND2 U209 ( .a(n176), .b(n166), .O(n179) );
  NOR2 U210 ( .a(n180), .b(n181), .O(n176) );
  NAND2 U211 ( .a(n182), .b(n173), .O(n180) );
  XOR2 U212 ( .a(G162), .b(n183), .O(G1347) );
  NOR2 U213 ( .a(n184), .b(n185), .O(n183) );
  XOR2 U214 ( .a(G155), .b(n186), .O(G1346) );
  NOR2 U215 ( .a(n187), .b(n185), .O(n186) );
  XOR2 U216 ( .a(G148), .b(n188), .O(G1345) );
  NOR2 U217 ( .a(n189), .b(n185), .O(n188) );
  XOR2 U218 ( .a(G141), .b(n190), .O(G1344) );
  NOR2 U219 ( .a(n191), .b(n185), .O(n190) );
  NAND2 U220 ( .a(n192), .b(n193), .O(n185) );
  NOR2 U221 ( .a(n172), .b(n171), .O(n193) );
  NOR2 U222 ( .a(n173), .b(n194), .O(n192) );
  XOR2 U223 ( .a(G134), .b(n195), .O(G1343) );
  NOR2 U224 ( .a(n184), .b(n196), .O(n195) );
  XOR2 U225 ( .a(G127), .b(n197), .O(G1342) );
  NOR2 U226 ( .a(n187), .b(n196), .O(n197) );
  XOR2 U227 ( .a(G120), .b(n198), .O(G1341) );
  NOR2 U228 ( .a(n189), .b(n196), .O(n198) );
  XOR2 U229 ( .a(G113), .b(n199), .O(G1340) );
  NOR2 U230 ( .a(n191), .b(n196), .O(n199) );
  NAND2 U231 ( .a(n200), .b(n169), .O(n196) );
  NOR2 U232 ( .a(n173), .b(n181), .O(n200) );
  NAND2 U233 ( .a(n201), .b(n171), .O(n181) );
  NOR2 U234 ( .a(n172), .b(n174), .O(n201) );
  AND2 U235 ( .a(n202), .b(n203), .O(n172) );
  NAND2 U236 ( .a(n204), .b(n184), .O(n203) );
  NOR2 U237 ( .a(n205), .b(n206), .O(n204) );
  NOR2 U238 ( .a(n187), .b(n189), .O(n206) );
  NOR2 U239 ( .a(n207), .b(n191), .O(n205) );
  NAND2 U240 ( .a(n207), .b(n191), .O(n202) );
  XNOR2 U241 ( .a(n208), .b(n209), .O(G1339) );
  NOR2 U242 ( .a(n171), .b(n210), .O(n209) );
  XOR2 U243 ( .a(G99), .b(n211), .O(G1338) );
  NOR2 U244 ( .a(n174), .b(n210), .O(n211) );
  XOR2 U245 ( .a(G92), .b(n212), .O(G1337) );
  NOR2 U246 ( .a(n169), .b(n210), .O(n212) );
  XOR2 U247 ( .a(G85), .b(n213), .O(G1336) );
  NOR2 U248 ( .a(n173), .b(n210), .O(n213) );
  NAND2 U249 ( .a(n214), .b(n215), .O(n210) );
  NOR2 U250 ( .a(n216), .b(n217), .O(n215) );
  NAND2 U251 ( .a(n164), .b(n160), .O(n217) );
  NOR2 U252 ( .a(n162), .b(n166), .O(n214) );
  XOR2 U253 ( .a(G78), .b(n218), .O(G1335) );
  NOR2 U254 ( .a(n171), .b(n219), .O(n218) );
  XOR2 U255 ( .a(G71), .b(n220), .O(G1334) );
  NOR2 U256 ( .a(n174), .b(n219), .O(n220) );
  XOR2 U257 ( .a(G64), .b(n221), .O(G1333) );
  NOR2 U258 ( .a(n169), .b(n219), .O(n221) );
  XNOR2 U259 ( .a(n222), .b(n223), .O(G1332) );
  NOR2 U260 ( .a(n173), .b(n219), .O(n223) );
  NAND2 U261 ( .a(n224), .b(n225), .O(n219) );
  NOR2 U262 ( .a(n189), .b(n166), .O(n224) );
  INV U263 ( .a(n164), .O(n189) );
  XOR2 U264 ( .a(G50), .b(n226), .O(G1331) );
  NOR2 U265 ( .a(n171), .b(n227), .O(n226) );
  XOR2 U266 ( .a(G43), .b(n228), .O(G1330) );
  NOR2 U267 ( .a(n174), .b(n227), .O(n228) );
  XOR2 U268 ( .a(G36), .b(n229), .O(G1329) );
  NOR2 U269 ( .a(n169), .b(n227), .O(n229) );
  XNOR2 U270 ( .a(n230), .b(n231), .O(G1328) );
  NOR2 U271 ( .a(n173), .b(n227), .O(n231) );
  NAND2 U272 ( .a(n232), .b(n233), .O(n227) );
  NOR2 U273 ( .a(n184), .b(n191), .O(n233) );
  NOR2 U274 ( .a(n216), .b(n234), .O(n232) );
  INV U275 ( .a(n207), .O(n234) );
  NOR2 U276 ( .a(n162), .b(n164), .O(n207) );
  XOR2 U277 ( .a(G22), .b(n235), .O(G1327) );
  NOR2 U278 ( .a(n171), .b(n236), .O(n235) );
  XOR2 U279 ( .a(G15), .b(n237), .O(G1326) );
  NOR2 U280 ( .a(n174), .b(n236), .O(n237) );
  XOR2 U281 ( .a(G8), .b(n238), .O(G1325) );
  NOR2 U282 ( .a(n169), .b(n236), .O(n238) );
  XOR2 U283 ( .a(G1), .b(n239), .O(G1324) );
  NOR2 U284 ( .a(n173), .b(n236), .O(n239) );
  NAND2 U285 ( .a(n240), .b(n225), .O(n236) );
  AND2 U286 ( .a(n241), .b(n184), .O(n225) );
  INV U287 ( .a(n160), .O(n184) );
  XNOR2 U288 ( .a(n242), .b(n243), .O(n160) );
  XOR2 U289 ( .a(n244), .b(n245), .O(n243) );
  XOR2 U290 ( .a(G162), .b(G134), .O(n245) );
  XOR2 U291 ( .a(G218), .b(G190), .O(n244) );
  XOR2 U292 ( .a(n246), .b(n247), .O(n242) );
  XOR2 U293 ( .a(n248), .b(n249), .O(n246) );
  NAND2 U294 ( .a(G232), .b(G233), .O(n248) );
  NOR2 U295 ( .a(n187), .b(n216), .O(n241) );
  AND2 U296 ( .a(n250), .b(n251), .O(n216) );
  NAND2 U297 ( .a(n252), .b(n171), .O(n251) );
  NAND2 U298 ( .a(n253), .b(n173), .O(n250) );
  NOR2 U299 ( .a(n254), .b(n255), .O(n253) );
  NOR2 U300 ( .a(n174), .b(n169), .O(n255) );
  NOR2 U301 ( .a(n252), .b(n171), .O(n254) );
  XOR2 U302 ( .a(n256), .b(n257), .O(n171) );
  XOR2 U303 ( .a(n258), .b(n259), .O(n257) );
  XNOR2 U304 ( .a(G22), .b(n208), .O(n259) );
  INV U305 ( .a(G106), .O(n208) );
  XOR2 U306 ( .a(G78), .b(G50), .O(n258) );
  XOR2 U307 ( .a(n260), .b(n261), .O(n256) );
  XOR2 U308 ( .a(n262), .b(n263), .O(n260) );
  NAND2 U309 ( .a(G228), .b(G233), .O(n262) );
  INV U310 ( .a(n194), .O(n252) );
  NAND2 U311 ( .a(n169), .b(n174), .O(n194) );
  XOR2 U312 ( .a(n264), .b(n265), .O(n174) );
  XOR2 U313 ( .a(n266), .b(n267), .O(n265) );
  XOR2 U314 ( .a(G43), .b(G15), .O(n267) );
  XOR2 U315 ( .a(G99), .b(G71), .O(n266) );
  XOR2 U316 ( .a(n268), .b(n269), .O(n264) );
  XOR2 U317 ( .a(n270), .b(n271), .O(n268) );
  NAND2 U318 ( .a(G227), .b(G233), .O(n270) );
  INV U319 ( .a(n182), .O(n169) );
  XNOR2 U320 ( .a(n272), .b(n273), .O(n182) );
  XOR2 U321 ( .a(n274), .b(n275), .O(n273) );
  XOR2 U322 ( .a(G64), .b(G36), .O(n275) );
  XOR2 U323 ( .a(G92), .b(G8), .O(n274) );
  XOR2 U324 ( .a(n276), .b(n271), .O(n272) );
  XNOR2 U325 ( .a(n277), .b(n278), .O(n271) );
  XOR2 U326 ( .a(G190), .b(G183), .O(n278) );
  XNOR2 U327 ( .a(G169), .b(G176), .O(n277) );
  XOR2 U328 ( .a(n279), .b(n261), .O(n276) );
  XNOR2 U329 ( .a(n280), .b(n281), .O(n261) );
  XOR2 U330 ( .a(G218), .b(G211), .O(n281) );
  XNOR2 U331 ( .a(G197), .b(G204), .O(n280) );
  NAND2 U332 ( .a(G226), .b(G233), .O(n279) );
  INV U333 ( .a(n162), .O(n187) );
  XNOR2 U334 ( .a(n282), .b(n283), .O(n162) );
  XOR2 U335 ( .a(n284), .b(n285), .O(n283) );
  XOR2 U336 ( .a(G155), .b(G127), .O(n285) );
  XOR2 U337 ( .a(G211), .b(G183), .O(n284) );
  XOR2 U338 ( .a(n286), .b(n287), .O(n282) );
  XOR2 U339 ( .a(n288), .b(n289), .O(n286) );
  NAND2 U340 ( .a(G233), .b(G231), .O(n288) );
  NOR2 U341 ( .a(n191), .b(n164), .O(n240) );
  XNOR2 U342 ( .a(n290), .b(n291), .O(n164) );
  XOR2 U343 ( .a(n292), .b(n293), .O(n291) );
  XOR2 U344 ( .a(G148), .b(G120), .O(n293) );
  XOR2 U345 ( .a(G204), .b(G176), .O(n292) );
  XOR2 U346 ( .a(n294), .b(n289), .O(n290) );
  XNOR2 U347 ( .a(n295), .b(n296), .O(n289) );
  XOR2 U348 ( .a(G78), .b(G71), .O(n296) );
  XNOR2 U349 ( .a(G57), .b(G64), .O(n295) );
  XOR2 U350 ( .a(n297), .b(n249), .O(n294) );
  XNOR2 U351 ( .a(n298), .b(n299), .O(n249) );
  XOR2 U352 ( .a(G99), .b(G92), .O(n299) );
  XNOR2 U353 ( .a(G106), .b(G85), .O(n298) );
  NAND2 U354 ( .a(G230), .b(G233), .O(n297) );
  INV U355 ( .a(n166), .O(n191) );
  XNOR2 U356 ( .a(n300), .b(n301), .O(n166) );
  XOR2 U357 ( .a(n302), .b(n303), .O(n301) );
  XOR2 U358 ( .a(G141), .b(G113), .O(n303) );
  XNOR2 U359 ( .a(n304), .b(G169), .O(n302) );
  INV U360 ( .a(G197), .O(n304) );
  XOR2 U361 ( .a(n305), .b(n287), .O(n300) );
  XNOR2 U362 ( .a(n306), .b(n307), .O(n287) );
  XOR2 U363 ( .a(G8), .b(G22), .O(n307) );
  XNOR2 U364 ( .a(G1), .b(G15), .O(n306) );
  XOR2 U365 ( .a(n308), .b(n247), .O(n305) );
  XNOR2 U366 ( .a(n309), .b(n310), .O(n247) );
  XOR2 U367 ( .a(G50), .b(G43), .O(n310) );
  XNOR2 U368 ( .a(G29), .b(G36), .O(n309) );
  NAND2 U369 ( .a(G229), .b(G233), .O(n308) );
  XOR2 U370 ( .a(n311), .b(n312), .O(n173) );
  XOR2 U371 ( .a(n313), .b(n314), .O(n312) );
  XNOR2 U372 ( .a(n230), .b(G1), .O(n314) );
  INV U373 ( .a(G29), .O(n230) );
  XNOR2 U374 ( .a(G85), .b(n222), .O(n313) );
  INV U375 ( .a(G57), .O(n222) );
  XOR2 U376 ( .a(n315), .b(n269), .O(n311) );
  XNOR2 U377 ( .a(n316), .b(n317), .O(n269) );
  XOR2 U378 ( .a(G134), .b(G127), .O(n317) );
  XNOR2 U379 ( .a(G113), .b(G120), .O(n316) );
  XOR2 U380 ( .a(n318), .b(n263), .O(n315) );
  XNOR2 U381 ( .a(n319), .b(n320), .O(n263) );
  XOR2 U382 ( .a(G162), .b(G155), .O(n320) );
  XNOR2 U383 ( .a(G141), .b(G148), .O(n319) );
  NAND2 U384 ( .a(G225), .b(G233), .O(n318) );
endmodule
