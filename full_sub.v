`timescale 1ns / 1ps
module or_gate(x0, y0, c0);

    input x0, y0;

    output c0;

    assign c0 = x0 | y0;

endmodule


module xor_gate(x1, y1, c1);

    input x1, y1;

    output c1;

    assign c1 = x1 ^ y1;

endmodule


module and_gate(x2, y2, c2);

    input x2, y2;

    output c2;

    assign c2 = x2 & y2;

endmodule


module not_gate(x3, y3);

    input x3;

    output y3;

    assign y3 = ~ x3;

endmodule


module half_subtractor(x4, y4, c4, d4);

    input x4, y4;

    output c4, d4;

    wire x;

    xor_gate u1(x4, y4, c4);

    and_gate u2(x, y4, d4);

    not_gate u3(x4, x);

endmodule


module full_subtractor(A, B, Bin,Res, Bout);

    input A, B, Bin;

    output Res, Bout;

    wire p, q, r;

    half_subtractor u4(A, B, p, q);

    half_subtractor u5(p, Bin, Res, r);

    or_gate u6(q, r, Bout);

endmodule

module test;

 reg a, bin, b;

 wire bout, R; 


 full_subtractor wew(.A(a),.B(b),.Bin(bin),.Res(R),.Bout(bout));
 initial begin
 //test1
 a=1'd1;
 b=1'd1;
 bin=1'd1;
 #100;
 //test2
 a=1'd0;
 b=1'd1;
 bin=1'd1;
 #100;
 //test3
 a=1'd1;
 b=1'd0;
 bin=1'd0;
 #100;
   end

endmodule