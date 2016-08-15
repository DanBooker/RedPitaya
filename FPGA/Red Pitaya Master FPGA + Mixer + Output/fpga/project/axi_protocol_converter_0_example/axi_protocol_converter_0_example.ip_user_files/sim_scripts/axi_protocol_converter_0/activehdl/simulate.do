onbreak {quit -force}
onerror {quit -force}

asim -t 1ps +access +r +m+axi_protocol_converter_0 -L unisims_ver -L unimacro_ver -L secureip -L xil_defaultlib -L xpm -L generic_baseblocks_v2_1_0 -L fifo_generator_v13_1_1 -L axi_data_fifo_v2_1_8 -L axi_infrastructure_v1_1_0 -L axi_register_slice_v2_1_9 -L axi_protocol_converter_v2_1_9 -O5 xil_defaultlib.axi_protocol_converter_0 xil_defaultlib.glbl

do {wave.do}

view wave
view structure
view signals

do {axi_protocol_converter_0.udo}

run -all

endsim

quit -force
