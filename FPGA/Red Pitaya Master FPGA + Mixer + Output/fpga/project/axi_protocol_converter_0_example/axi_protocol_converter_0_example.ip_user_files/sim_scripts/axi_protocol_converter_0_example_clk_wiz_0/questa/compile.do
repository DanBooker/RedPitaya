vlib work
vlib msim

vlib msim/xil_defaultlib
vlib msim/xpm

vmap xil_defaultlib msim/xil_defaultlib
vmap xpm msim/xpm

vlog -work xil_defaultlib -64 -sv "+incdir+../../../ipstatic/clk_wiz_v5_3_1" "+incdir+../../../ipstatic/clk_wiz_v5_3_1" \
"C:/Xilinx/Vivado/2016.2/data/ip/xpm/xpm_cdc/hdl/xpm_cdc.sv" \

vcom -work xpm -64 \
"C:/Xilinx/Vivado/2016.2/data/ip/xpm/xpm_VCOMP.vhd" \

vlog -work xil_defaultlib -64 "+incdir+../../../ipstatic/clk_wiz_v5_3_1" "+incdir+../../../ipstatic/clk_wiz_v5_3_1" \
"../../../../axi_protocol_converter_0_example.srcs/sources_1/ip/axi_protocol_converter_0_example_clk_wiz_0/axi_protocol_converter_0_example_clk_wiz_0_clk_wiz.v" \
"../../../../axi_protocol_converter_0_example.srcs/sources_1/ip/axi_protocol_converter_0_example_clk_wiz_0/axi_protocol_converter_0_example_clk_wiz_0.v" \

vlog -work xil_defaultlib "glbl.v"

