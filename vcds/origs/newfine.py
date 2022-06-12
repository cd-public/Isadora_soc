def get_mod():

	FILE = "1"
	NAME = "edn_o "

	module = ""
	for line in open(FILE + ".vcd","r"):
		if "module" in line:
			module = line
		if " " + NAME in line:
			print("MOD " + module + " REG " + line)
		if "dumpvars" in line:
			break
			
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
			
get_mod()