import libraries.action as lib_action
def action_list_init(act_lst):
    act_lst.add("BREAKPOINT", lib_action.BreakpointAction, categories=["FPGA"])
    act_lst.add("NOP", lib_action.NopAction, categories=["FPGA"])
