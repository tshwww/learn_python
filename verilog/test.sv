module chardet(
    input  loigc clk,
    input       a,

    output  ss,
    output bb
);

assign ss=a;
assign bb=a;


aa aa(
    .clk(clk),
    .rst_n(rst_n)
);

bb #(
    .NSPI (8),
    .NCPI (2)
)bb_1(
    .clk(clk),
    .rst_n(rst_n),

    .sig(sig)

);

endmodule