from os import system
from os import path
import os
import sys

# done, returns a string
def iflow_to_dout(src,snk):
	con = open("conditions.txt","r")
	case = ""
	for line in con:
		if "case: " in line:
			case = line.replace("case: ","").strip()
		else:
			splits = line.replace("[","").replace("]","").replace(",","").split()
			if src == splits[0]:
				if snk in splits[1:]:
					con.close()
					return case
	return ""

def check_zs(case, reg, is_zero):
	cd_orig = os.getcwd()
	# --- ENTER ZS DIR --- #
	os.chdir(os.getcwd().replace("utils","outs/zs"))
	zin = open(case + ".zs.txt","r")
	# --- RETURN TO DIR --- #
	os.chdir(cd_orig)
	line = zin.readline() # only need zs - can be nz without being = to a constant
	ret = reg + "," in line or reg + "}" in line
	if is_zero:
		return ret
	else:
		return not ret
	return # could be last

def check_cwe(cwe):
	check_zs(iflow_to_dout(cwe[0],cwe[1]), cwe[2], not bool(cwe[3]))

# use: python main.py src snk reg {0/n}	
if __name__ == "__main__":	
	# total arguments
	n = len(sys.argv)
	if (n < 3):
		exit()
	# get vcd name
	src = sys.argv[1]
	snk = sys.argv[2]
	if (n == 5): # cond case
		reg = sys.argv[3]
		isz = sys.argv[4]
		print(check_zs(iflow_to_dout(src,snk), reg, not bool(int(isz))))
	if (n == 3): # test case
		print(iflow_to_dout(src,snk))
		
#cwes = [['M_AXI_WREADY', 'M_AXI_WREADY_wire', 'ARESETN', 1], ['M_AXI_BID', 'M_AXI_BID_wire', 'ARESETN', 1], ['M_AXI_BRESP', 'M_AXI_BRESP_wire', 'ARESETN', 1], ['M_AXI_BUSER', 'M_AXI_BUSER_wire', 'ARESETN', 1], ['M_AXI_BVALID', 'M_AXI_BVALID_wire', 'ARESETN', 1], ['M_AXI_RID', 'M_AXI_RID_wire', 'ARESETN', 1], ['M_AXI_RDATA', 'M_AXI_RDATA_wire', 'ARESETN', 1], ['M_AXI_RRESP', 'M_AXI_RRESP_wire', 'ARESETN', 1], ['M_AXI_RLAST', 'M_AXI_RLAST_wire', 'ARESETN', 1], ['M_AXI_RUSER', 'M_AXI_RUSER_wire', 'ARESETN', 1], ['M_AXI_RVALID', 'M_AXI_RVALID_wire', 'ARESETN', 1], ['M_AXI_AWID_wire', 'M_AXI_AWID_INT', 'ARESETN', 1], ['M_AXI_AWADDR_wire', 'M_AXI_AWADDR_INT', 'ARESETN', 1], ['M_AXI_AWLEN_wire', 'M_AXI_AWLEN_INT', 'ARESETN', 1], ['M_AXI_AWSIZE_wire', 'M_AXI_AWSIZE_INT', 'ARESETN', 1], ['M_AXI_AWBURST_wire', 'M_AXI_AWBURST_INT', 'ARESETN', 1], ['M_AXI_AWLOCK_wire', 'M_AXI_AWLOCK_INT', 'ARESETN', 1], ['M_AXI_AWCACHE_wire', 'M_AXI_AWCACHE_INT', 'ARESETN', 1], ['M_AXI_AWPROT_wire', 'M_AXI_AWPROT_INT', 'ARESETN', 1], ['M_AXI_AWQOS_wire', 'M_AXI_AWQOS_INT', 'ARESETN', 1], ['M_AXI_AWUSER_wire', 'M_AXI_AWUSER_INT', 'ARESETN', 1], ['M_AXI_WDATA_wire', 'M_AXI_WDATA', 'ARESETN', 1], ['M_AXI_WSTRB_wire', 'M_AXI_WSTRB', 'ARESETN', 1], ['M_AXI_WLAST_wire', 'M_AXI_WLAST', 'ARESETN', 1], ['M_AXI_WUSER_wire', 'M_AXI_WUSER', 'ARESETN', 1], ['M_AXI_WVALID_wire', 'M_AXI_WVALID', 'ARESETN', 1], ['M_AXI_BREADY_wire', 'M_AXI_BREADY', 'ARESETN', 1], ['M_AXI_RREADY_wire', 'M_AXI_RREADY', 'ARESETN', 1], ['M_AXI_ARID_wire', 'M_AXI_ARID_INT', 'ARESETN', 1], ['M_AXI_ARADDR_wire', 'M_AXI_ARADDR_INT', 'ARESETN', 1], ['M_AXI_ARLEN_wire', 'M_AXI_ARLEN_INT', 'ARESETN', 1], ['M_AXI_ARSIZE_wire', 'M_AXI_ARSIZE_INT', 'ARESETN', 1], ['M_AXI_ARBURST_wire', 'M_AXI_ARBURST_INT', 'ARESETN', 1], ['M_AXI_ARLOCK_wire', 'M_AXI_ARLOCK_INT', 'ARESETN', 1], ['M_AXI_ARCACHE_wire', 'M_AXI_ARCACHE_INT', 'ARESETN', 1], ['M_AXI_ARPROT_wire', 'M_AXI_ARPROT_INT', 'ARESETN', 1], ['M_AXI_ARQOS_wire', 'M_AXI_ARQOS_INT', 'ARESETN', 1], ['M_AXI_ARUSER_wire', 'M_AXI_ARUSER_INT', 'ARESETN', 1], ['M_AXI_WREADY', 'M_AXI_WREADY_wire', 'reg00_config', 1], ['M_AXI_BID', 'M_AXI_BID_wire', 'reg00_config', 1], ['M_AXI_BRESP', 'M_AXI_BRESP_wire', 'reg00_config', 1], ['M_AXI_BUSER', 'M_AXI_BUSER_wire', 'reg00_config', 1], ['M_AXI_BVALID', 'M_AXI_BVALID_wire', 'reg00_config', 1], ['M_AXI_RID', 'M_AXI_RID_wire', 'reg00_config', 1], ['M_AXI_RDATA', 'M_AXI_RDATA_wire', 'reg00_config', 1], ['M_AXI_RRESP', 'M_AXI_RRESP_wire', 'reg00_config', 1], ['M_AXI_RLAST', 'M_AXI_RLAST_wire', 'reg00_config', 1], ['M_AXI_RUSER', 'M_AXI_RUSER_wire', 'reg00_config', 1], ['M_AXI_RVALID', 'M_AXI_RVALID_wire', 'reg00_config', 1], ['M_AXI_AWID_wire', 'M_AXI_AWID_INT', 'reg00_config', 1], ['M_AXI_AWADDR_wire', 'M_AXI_AWADDR_INT', 'reg00_config', 1], ['M_AXI_AWLEN_wire', 'M_AXI_AWLEN_INT', 'reg00_config', 1], ['M_AXI_AWSIZE_wire', 'M_AXI_AWSIZE_INT', 'reg00_config', 1], ['M_AXI_AWBURST_wire', 'M_AXI_AWBURST_INT', 'reg00_config', 1], ['M_AXI_AWLOCK_wire', 'M_AXI_AWLOCK_INT', 'reg00_config', 1], ['M_AXI_AWCACHE_wire', 'M_AXI_AWCACHE_INT', 'reg00_config', 1], ['M_AXI_AWPROT_wire', 'M_AXI_AWPROT_INT', 'reg00_config', 1], ['M_AXI_AWQOS_wire', 'M_AXI_AWQOS_INT', 'reg00_config', 1], ['M_AXI_AWUSER_wire', 'M_AXI_AWUSER_INT', 'reg00_config', 1], ['M_AXI_WDATA_wire', 'M_AXI_WDATA', 'reg00_config', 1], ['M_AXI_WSTRB_wire', 'M_AXI_WSTRB', 'reg00_config', 1], ['M_AXI_WLAST_wire', 'M_AXI_WLAST', 'reg00_config', 1], ['M_AXI_WUSER_wire', 'M_AXI_WUSER', 'reg00_config', 1], ['M_AXI_WVALID_wire', 'M_AXI_WVALID', 'reg00_config', 1], ['M_AXI_BREADY_wire', 'M_AXI_BREADY', 'reg00_config', 1], ['M_AXI_RREADY_wire', 'M_AXI_RREADY', 'reg00_config', 1], ['M_AXI_ARID_wire', 'M_AXI_ARID_INT', 'reg00_config', 1], ['M_AXI_ARADDR_wire', 'M_AXI_ARADDR_INT', 'reg00_config', 1], ['M_AXI_ARLEN_wire', 'M_AXI_ARLEN_INT', 'reg00_config', 1], ['M_AXI_ARSIZE_wire', 'M_AXI_ARSIZE_INT', 'reg00_config', 1], ['M_AXI_ARBURST_wire', 'M_AXI_ARBURST_INT', 'reg00_config', 1], ['M_AXI_ARLOCK_wire', 'M_AXI_ARLOCK_INT', 'reg00_config', 1], ['M_AXI_ARCACHE_wire', 'M_AXI_ARCACHE_INT', 'reg00_config', 1], ['M_AXI_ARPROT_wire', 'M_AXI_ARPROT_INT', 'reg00_config', 1], ['M_AXI_ARQOS_wire', 'M_AXI_ARQOS_INT', 'reg00_config', 1], ['M_AXI_ARUSER_wire', 'M_AXI_ARUSER_INT', 'reg00_config', 1]]

#for cwe in cwes:
#	print(cwe, check_cwe(cwe))