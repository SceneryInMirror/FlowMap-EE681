module O17 (N1,N2,N3,N6,N7,N22,N23);

input N1,N2,N3,N6,N7;

output N22,N23;

wire N10,N11,N16,N19;

NAND NAND2_1 (.O(N10), .a(N1), .b(N3));
NAND NAND2_2 (.O(N11), .a(N3), .b(N6));
NAND NAND2_3 (.O(N16), .a(N2), .b(N11));
NAND NAND2_4 (.O(N19), .a(N11), .b(N7));
NAND NAND2_5 (.O(N22), .a(N10), .b(N16));
NAND NAND2_6 (.O(N23), .a(N16), .b(N19));

endmodule
