/////////////////////////////////////////////////////////////
// Created by: Synopsys DC Expert(TM) in wire load mode
// Version   : P-2019.03-SP1-1
// Date      : Fri May  6 00:57:22 2022
/////////////////////////////////////////////////////////////


module c17 ( G1, G2, G3, G6, G7, G22, G23 );
  input G1, G2, G3, G6, G7;
  output G22, G23;
  wire   n6, n7, n8, n9, n10;

  NOR2 U8 ( .a(n6), .b(n7), .O(G23) );
  NOR2 U9 ( .a(G2), .b(G7), .O(n7) );
  INV U10 ( .a(n8), .O(n6) );
  NAND2 U11 ( .a(n9), .b(n10), .O(G22) );
  NAND2 U12 ( .a(G2), .b(n8), .O(n10) );
  NAND2 U13 ( .a(G6), .b(G3), .O(n8) );
  NAND2 U14 ( .a(G1), .b(G3), .O(n9) );
endmodule

