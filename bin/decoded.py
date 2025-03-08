def err_code(err_code):
    msg = '                                    '
    if err_code[0:8] == '80000001':
        msg = 'Failed to access thermal sensor '
    elif err_code[0:8] == '80000004':
        msg = 'AC/DC Power Fail                     '
    elif err_code[0:8] == '80000005':
        msg = 'Main SoC CPU Power Fail             '
    elif err_code[0:8] == '80000006':
        msg = 'Main SoC GFX Power Fail             '
    elif err_code[0:8] == '80000007':
        msg = 'Main SoC Thrm Hi Tempr Abnormal '
    elif err_code[0:8] == '80000008':
        msg = 'Drive Dead Notify Timeout             '
    elif err_code[0:8] == '80000009':
        msg = 'AC In Detect                         '
    elif err_code[0:8] == '8000000A':
        msg = 'VRM HOT Fatal                         '
    elif err_code[0:8] == '8000000B':
        msg = 'Unexpected Thermal Shutdown         '
    elif err_code[0:8] == '8000000C':
        msg = 'MSoC Tempr Alert                     '
    elif err_code[0:8] == '80050000':
        msg = 'SoC VRM Power Fail (CPU)            '
    elif err_code[0:4] == '8005':
        msg = 'SoC VRM Power Fail (CPU)            '
    elif err_code[0:8] == '80060000':
        msg = 'SoC VRM Power Fail (GFX)            '
    elif err_code[0:4] == '8006':
        msg = 'SoC VRM Power Fail (GFX)            '
    elif err_code[0:4] == '8080':
        msg = 'Fatal Shutdown by OS request         '
    elif err_code[0:8] == '80810001':
        msg = 'Power Seq Error                     '
    elif err_code[0:8] == '80810002':
        msg = 'Power Seq: NVS Access Error         '
    elif err_code[0:8] == '80810013':
        msg = 'Power Seq: ScCmd DRAM Init Error'
    elif err_code[0:8] == '80810014':
        msg = 'Power Seq: ScCmd Link Up Failure'
    elif err_code[0:8] == '80830000':
        msg = 'Main SoC Sync Flood                 '
    elif err_code[0:8] == '80840000':
        msg = 'PCIe Link Down                         '
    elif err_code[0:8] == '80870001':
        msg = 'Flash Cont:RAM Protect Error         '
    elif err_code[0:8] == '80870002':
        msg = 'Flash Cont:RAM Parity Error         '
    elif err_code[0:8] == '80870003':
        msg = 'Flash Cont:Boot Failed                 '
    elif err_code[0:8] == '80870004':
        msg = 'Flash Cont:Boot Failed NoRecord '
    elif err_code[0:8] == '80870005':
        msg = 'Flash Cont:Boot Failed State Err'
    elif err_code[0:6] == '808710':
        msg = 'Flash Cont:ScCmd Response Error     '
    elif err_code[0:4] == '8088':
        msg = 'Flash Cont:Boot EAP Error             '
    elif err_code[0:4] == '8089':
        msg = 'Flash Cont:Boot EFC Error             '
    elif err_code[0:4] == '808A':
        msg = 'Flash Cont:Temper Error             '
    elif err_code[0:4] == '808B':
        msg = 'Flash Cont:Watch Dog Timer            '
    elif err_code[0:4] == '808C':
        msg = 'USB Type-C Errror                     '
    elif err_code[0:8] == '808D0000':
        msg = 'Thermal Shutdown: Main SoC         '
    elif err_code[0:8] == '808D0001':
        msg = 'Thermal Shutdown: Local Sensor 1'
    elif err_code[0:8] == '808D0002':
        msg = 'Thermal Shutdown: Local Sensor 2'
    elif err_code[0:8] == '808D0003':
        msg = 'Thermal Shutdown: Local Sensor 3'
    elif err_code[0:8] == '808E0000':
        msg = 'COM Err:Close Error                 '
    elif err_code[0:8] == '808E0001':
        msg = 'COM Err:Open Error                     '
    elif err_code[0:8] == '808E0002':
        msg = 'COM Err:Host Write Flag Error     '
    elif err_code[0:8] == '808E0003':
        msg = 'COM Err:EMC Read Flag Error         '
    elif err_code[0:8] == '808E0004':
        msg = 'COM Err:Write Flag Error             '
    elif err_code[0:8] == '808E0005':
        msg = 'COM Err:Wait SIG1 Error             '
    elif err_code[0:8] == '808E0006':
        msg = 'COM Err:Reset request from Host     '
    elif err_code[0:8] == '808E0007':
        msg = 'COM Err:Checksum Error             '
    elif err_code[0:8] == '808F0001':
        msg = 'SMCU Com Err:Timeout                 '
    elif err_code[0:8] == '808F0002':
        msg = 'SMCU Com Err:Reset                     '
    elif err_code[0:8] == '808F0003':
        msg = 'SMCU Com Err:TIS Error             '
    elif err_code[0:8] == '808F00FF':
        msg = 'SMCU Com Err:Undefined             '
    elif err_code[0:4] == '8090':
        msg = 'Fatal Shutdown by Error Add Code'
    elif err_code[0:4] == '8091':
        msg = 'SSD PMIC Error                         '
    elif err_code[0:8] == '80C00114':
        msg = 'Watch Dog For SoC                     '
    elif err_code[0:8] == '80C00115':
        msg = 'Watch Dog For EAP                     '
    elif err_code[0:8] == '80C0012C':
        msg = 'BD Drive Detached                     '
    elif err_code[0:8] == '80C0012D':
        msg = 'EMC Watch Dog Timer Error             '
    elif err_code[0:8] == '80C0012E':
        msg = 'ADC Error (Button)                     '
    elif err_code[0:8] == '80C0012F':
        msg = 'ADC Error (BD Drive)                 '
    elif err_code[0:8] == '80C00130':
        msg = 'ADC Error (AC In Det)                 '
    elif err_code[0:8] == '80C00131':
        msg = 'USB Over Current                     '
    elif err_code[0:8] == '80C00132':
        msg = 'FAN Storage Access Failed             '
    elif err_code[0:8] == '80C00133':
        msg = 'USB-BT FW Header Invalid             '
    elif err_code[0:8] == '80C00134':
        msg = 'USB-BT BT Command Error             '
    elif err_code[0:8] == '80C00135':
        msg = 'USB-BT Memory Malloc Failed         '
    elif err_code[0:8] == '80C00136':
        msg = 'USB-BT Device Not Found             '
    elif err_code[0:8] == '80C00137':
        msg = 'USB-BT MISC Error                     '
    elif err_code[0:8] == '80C00138':
        msg = 'Flash Cont Interrupt HW Error     '
    elif err_code[0:8] == '80C00139':
        msg = 'BD Drive Eject Assert Delayed         '
    elif err_code[0:6] == '80D001':
        msg = 'USB-BT Error (Bulk Out)             '
    elif err_code[0:6] == '80D002':
        msg = 'USB-BT Error (Bulk In)             '
    elif err_code[0:6] == '80D003':
        msg = 'USB-BT Error (Bt Init)             '
    elif err_code[0:6] == '80D004':
        msg = 'USB-BT Error (Download Firmware)'
    elif err_code[0:6] == '80D005':
        msg = 'USB-BT Error (Release Device)         '
    elif err_code[0:6] == '80D006':
        msg = 'USB-BT Error (Exec Cmd0)             '
    elif err_code[0:6] == '80D007':
        msg = 'USB-BT Error (Exec Cmd1)             '
    elif err_code[0:2] == 'B0':
        msg = 'Sonics Bus Error                     '
    elif err_code[0:4] == 'C001':
        msg = 'Main SoC Access Error (I2C)         '
    elif err_code[0:4] == 'C002':
        msg = 'Main SoC Access Err (SB-TSI I2C)'
    elif err_code[0:4] == 'C003':
        msg = 'Main SoC Access Error (SB-RMI)     '
    elif err_code[0:4] == 'C00B':
        msg = 'Serial Flash Access Error             '
    elif err_code[0:4] == 'C00C':
        msg = 'VRM Controller Access Error         '
    elif err_code[0:4] == 'C00D':
        msg = 'PMIC (Subsystem) Access Error         '
    elif err_code[0:4] == 'C010':
        msg = 'Flash Controller Access Error     '
    elif err_code[0:4] == 'C011':
        msg = 'Potentiometer Access Error         '
    elif err_code[0:4] == 'C015':
        msg = 'PCIe Redriver Access Errror         '
    elif err_code[0:4] == 'C016':
        msg = 'PMIC (SSD) Access Error             '
    elif err_code[0:4] == 'C081':
        msg = 'HDMI Tx Access Error                 '
    elif err_code[0:4] == 'C090':
        msg = 'USB Type-C PD Cont Access Error '
    elif err_code[0:4] == 'C091':
        msg = 'USB Type-C USB/DP Mux Accss Err '
    elif err_code[0:4] == 'C092':
        msg = 'USB Type-C Redriver Access Error'
    elif err_code[0:4] == 'C0FE':
        msg = 'Dummy                                 '
    return msg

def pw_state(pw_state):
    msg1 = '        '
    if pw_state[2:4] == '00':
        msg1 = 'SysReady:'
    elif pw_state[2:4] == '01':
        msg1 = 'MaOnStby:'
    elif pw_state[2:3] == '0':
        msg1 = 'Reserved:'
    elif pw_state[2:3] == '1':
        msg1 = 'PSP_____:'
    elif pw_state[2:4] == '20':
        msg1 = 'BIOS____:'
    elif pw_state[2:4] == '30':
        msg1 = 'BIOS____:'
    elif pw_state[2:4] == '40':
        msg1 = 'EAP_Redy:'
    elif pw_state[2:3] == '4':
        msg1 = 'EAP_____:'
    elif pw_state[2:3] == '5':
        msg1 = 'Kernel__:'
    elif pw_state[2:3] == '6':
        msg1 = 'Kernel__:'
    elif pw_state[2:3] == '7':
        msg1 = 'Kernel__:'
    elif pw_state[2:3] == '8':
        msg1 = 'Kernel__:'
    elif pw_state[2:3] == '9':
        msg1 = 'Kernel__:'
    elif pw_state[2:3] == 'A':
        msg1 = 'Kernel__:'
    elif pw_state[2:3] == 'B':
        msg1 = 'Kernel__:'
    elif pw_state[2:3] == 'C':
        msg1 = 'IntPrcss:'
    elif pw_state[2:3] == 'D':
        msg1 = 'IntPrcss:'
    elif pw_state[2:3] == 'E':
        msg1 = 'IntPrcss:'
    elif pw_state[2:4] == 'FF':
        msg1 = 'HstOsOFF:'
    elif pw_state[2:3] == 'F':
        msg1 = 'IntPrcss:'
    msg2 = '______'
    if pw_state[6:8] == '00':
        msg2 = 'ACIN_L'
    elif pw_state[6:8] == '01':
        msg2 = 'Stanby'
    elif pw_state[6:8] == '02':
        msg2 = 'PG2_ON'
    elif pw_state[6:8] == '03':
        msg2 = 'EFC_ON'
    elif pw_state[6:8] == '04':
        msg2 = 'EAP_ON'
    elif pw_state[6:8] == '05':
        msg2 = 'SOC_ON'
    elif pw_state[6:8] == '06':
        msg2 = 'ErrDET'
    elif pw_state[6:8] == '07':
        msg2 = 'FtlErr'
    elif pw_state[6:8] == '08':
        msg2 = 'NvrBot'
    elif pw_state[6:8] == '09':
        msg2 = 'FrcOFF'
    elif pw_state[6:8] == '0A':
        msg2 = 'FofBTd'
    return msg1 + msg2

def upcause(BT_TRG):
    msg = '___'
    if BT_TRG[0:8] == '40000000':
        msg = 'URT'
    elif BT_TRG[0:8] == '00080000':
        msg = 'BT '
    elif BT_TRG[0:8] == '00040000':
        msg = 'CEC'
    elif BT_TRG[0:8] == '00020000':
        msg = 'EAP'
    elif BT_TRG[0:8] == '00010000':
        msg = 'SoC'
    elif BT_TRG[0:8] == '00000400':
        msg = 'Ejc'
    elif BT_TRG[0:8] == '00000200':
        msg = 'DLd'
    elif BT_TRG[0:8] == '00000100':
        msg = 'PBt'
    elif BT_TRG[0:8] == '00000001':
        msg = 'BPW'
    return msg

def devpower(devpower_hex):
    value = int(devpower_hex, 16)
    result = ""

    h_on = (value & 0x10) != 0
    b_on = (value & 0x08) != 0
    c_on = (value & 0x04) != 0
    u_on = (value & 0x02) != 0
    w_on = (value & 0x01) != 0

    result += f"HDMI 5V: {'ON' if h_on else 'OFF'}, "
    result += f"BDD: {'ON' if b_on else 'OFF'}, "
    result += f"HDMI-CEC: {'ON' if c_on else 'OFF'}, "
    result += f"USB-VBUS: {'ON' if u_on else 'OFF'}, "
    result += f"WIFI: {'ON' if w_on else 'OFF'}"

    return result