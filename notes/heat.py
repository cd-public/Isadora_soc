import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def graph():
	sns.set()
	#mods = ['u_scrmbl_mtx', 'u_prim_lc_sync_check_byp_en', 'u_prim_lc_sync_seed_hw_rd_en', 'u_intr_operation_done', 'u_otp_arb', 'u_reg_core', 'u_otp_ctrl_kdi', 'u_otp', 'u_prim_lc_sync_dft_en', 'u_prim_lc_sender_rma_token_valid', 'u_prim_lc_sync_escalate_en', 'u_otp_ctrl_scrmbl', 'u_tlul_adapter_sram', 'u_part_sel_idx', 'u_prim_lc_sync_creator_seed_sw_rw_en', 'u_otp_ctrl_lci', 'u_intr_error', 'u_prim_lc_sender_test_tokens_valid', 'u_prim_edn_req', 'u_otp_ctrl_dai', 'u_prim_lc_sender_secrets_valid', 'u_otp_init_sync', 'u_otp_ctrl_lfsr_timer', 'u_edn_arb', 'u_tlul_lc_gate', 'u_otp_rsp_fifo']
	#cnts = [[2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [7, 7, 6, 6, 6], [9, 9, 9, 9, 9], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [7, 7, 6, 6, 6], [3, 3, 3, 3, 3], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2]]
	mods = ['pwr_otp_i', 'otp_ext_voltage_h_io', 'intr_otp_error_o', 'otp_ast_pwr_seq_h_i', 'otp_alert_o', 'prim_tl_o', 'core_tl_o', 'intr_otp_operation_done_o']
	cnts = [[69, 69], [1, 1], [2, 2], [70, 70], [1, 1], [14, 14], [104, 104], [2, 2]]
	cnts = [[cnts[i][0] for i in range(len(cnts))] for j in range(5)]
	#plt.figure(figsize=(15,5))
	ax = sns.heatmap(cnts, cmap='Blues', annot=True, fmt='d')
	labels = ['RndCnstKey', 'UserKeys', 'sram_data_key_seed', 'flash_data_key_seed', 'flash_addr_key_seed']
	#ax.set_xticks(len(labels))
	ax.set_yticklabels(labels)
	#ax.set_yticks(len(mods))
	ax.set_xticklabels(mods)  
	plt.xlabel("Sink Signal in u_otp_ctrl")
	plt.ylabel("Source Signal")
	plt.yticks(rotation=0)
	plt.xticks(rotation=90)
	plt.tight_layout()
	plt.savefig('heat.png')
	
graph()

