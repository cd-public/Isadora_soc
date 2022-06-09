## 3,591,492,600 cycles

CYCLES = 10000
MODULE = "u_otp_ctrl"

def refine(name):

	def key_to_dump():
		step0 = True 						# tracks location in the VCD
		step1 = False	
		orig_design_regs = set()			# tracks verilog names of origianl design
		refined_vars = []
		active = False
		for line in vcd_key:
		
			if step0:
			
				if "scope" in line:
					step0 = False
					step1 = True
				else:
					vcd_out.write(line)

			## assume all state in "u0" module

			if step1:
				
				if "module " in line and "module " + MODULE not in line and active:
					step1 = False
					active = False
				elif "module " + MODULE  in line:
					active = True
				elif active and "var reg" in line or "var wire" in line:
					vcd_out.write(line)
					orig_design_regs.add(line.split()[4])
					refined_vars = refined_vars + [line.split()[3]]
					
			if "dumpvars" in line:
				# vcd_out.write("$enddefinitions $end\n$dumpvars\n#0\n")
				return orig_design_regs, refined_vars
				
	def in_to_dump(orig_design_regs, refined_vars):
		active = False
		for line in vcd_in:

			if "module " in line and active:
				step1 = False
				active = False
			elif "module " + MODULE in line:
				active = True
			elif active:
				for reg in orig_design_regs:
					if "shadow_" + reg + " " in line:
						vcd_out.write(line)
						refined_vars = refined_vars + [line.split()[3]]
				
			if "dumpvars" in line:
				vcd_out.write("$enddefinitions $end\n$dumpvars\n#0\n")
				return
		
	def tick(fp):
		first = True
		for line in fp:
			if "#" in line[0]:
				return int(line[1:])
			else:
				if first:
					first = False
				splits = line.strip().split()
				if len(splits) == 1:
					tag = line[1:].strip()
				else:
					tag = splits[1]
				if tag in refined_vars:
					vcd_out.write(line)

## refine vcd

	vcd_key = open("key.vcd","r")
	vcd_in = open(name + ".vcd","r")
	vcd_out = open("r_" + name + ".vcd","w")
	
	## inits
	cache = ""							# tracks timing info
	cache_live = False
	tag = ""							# internal line read variable for vcd encoding
	active = False						# tracks if copying is active
	fps = [vcd_key, vcd_in]
	
	# first get the orig regs + do the header
	
	orig_design_regs, refined_vars = key_to_dump()
	in_to_dump(orig_design_regs, refined_vars)
	
	# now advance key and in together with time synchronization
	
	# run once to get a tick value
	prevs = [0,0]
	delta = [0,0]
	
	while max(prevs) < CYCLES:
		if prevs[0] <= prevs[1]:
			vcd_out.write("#" + str(prevs[0]) + "\n")
			print("Delta advanced to " + str(prevs[0]))
			prevs[0] = delta[0]
			delta[0] = tick(fps[0])
		else:
			prevs[1] = delta[1]
			delta[1] = tick(fps[1])

refine("1")