def get_mod(name):

	FILE = "1"
	NAME = name

	module = ""
	mods = []
	for line in open(FILE + ".vcd","r"):
		if "module" in line:
			module = line.split()[2]
		if " " + NAME + " " in line:
			mods.append(module)
		if "dumpvars" in line:
			return set([m for m in mods if "[" not in m])
			
def lines():
	
	FILE = "2"
	CODE = "+07"
	
	in_vars = False
	cycles = 0
	
	for line in open(FILE + ".vcd","r"):
		if "dumpvars" in line:
			in_vars = True
		if in_vars and line[0] == "#":
			cycles = int(line[1:])
		if in_vars:
			if line[0] == "#":
				cycles = int(line[1:])
			if " " + CODE in line.strip()[-4:]:
				print(str(cycles) + " " + line)
# build reg struct
def make_regs():
	#regs = [["seed", 1, ["data_q", "edn_i", "core_tl_i", "prim_tl_i", "alert_rx_i", "alert_tx_o", "obs_ctrl_i", "otp_ast_pwr_seq_o", "pwr_otp_o", "lc_otp_vendor_test_i", "lc_otp_vendor_test_o", "lc_otp_program_o", "lc_seed_hw_rd_en_i", "lc_dft_en_i", "lc_escalate_en_i", "lc_check_byp_en_i", "flash_otp_key_i", "sram_otp_key_i", "otbn_otp_key_i", "otbn_otp_key_o", "scanmode_i", "cio_test_o", "cio_test_en_o", "rst_edn_ni", "intr_otp_operation_done_o", "intr_otp_error_o", "scan_rst_ni"]]]
	#regs += [["key", 1, ["data_q", "edn_i", "core_tl_i", "prim_tl_i", "alert_rx_i", "alert_tx_o", "obs_ctrl_i", "otp_ast_pwr_seq_o", "pwr_otp_o", "lc_otp_vendor_test_i", "lc_otp_vendor_test_o", "lc_otp_program_o", "lc_seed_hw_rd_en_i", "lc_dft_en_i", "lc_escalate_en_i", "lc_check_byp_en_i", "flash_otp_key_i", "sram_otp_key_i", "otbn_otp_key_o", "scanmode_i", "cio_test_o", "cio_test_en_o", "scan_rst_ni"]]]
	regs = [["all", 12, ["data_copy"]]]
	regs += [["all", 5, ["data_load"]]]
	regs += [["all", 2, ["edn_o"]]]
	regs += [["seed", 52, ["core_tl_o"]]]
	regs += [["all", 14, ["prim_tl_o"]]]
	regs += [["all", 3, ["otp_obs_o"]]]
	regs += [["all", 70, ["otp_ast_pwr_seq_h_i"]]]
	regs += [["all", 69, ["pwr_otp_i"]]]
	regs += [["all", 1, ["otp_alert_o","otp_ext_voltage_h_io","scan_en_i"]]]
	regs += [["seed", 2, ["rst_ni"]]]
	regs += [["key", 52, ["core_tl_o"]]]
	regs += [["key", 2, ["otbn_otp_key_i", "rst_ni", "rst_edn_ni", "intr_otp_operation_done_o", "intr_otp_error_o"]]]
	return regs

def make_heat():
	# find unique modules
	regs = make_regs()
	setr = set()
	for flow in regs:
		flow[2] = [reg for reg in flow[2] if {"u_otp_ctrl"} == get_mod(reg)]
		setr.update(set(flow[2]))
	lstr = list(setr)
	heat = [[0,0] for r in lstr]
	for flow in regs:
		for reg in flow[2]:
			if "seed" or "all" in flow[0]:
				heat[lstr.index(reg)][0] += flow[1]
			if "key" or "all" in flow[0]:
				heat[lstr.index(reg)][1] += flow[1]
	print(lstr)
	print(heat)
	
make_heat()

