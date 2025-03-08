import serial.tools.list_ports
import time
import os

# Function to list all available COM ports and USB descriptors
def list_com_ports():
    """Lists all available COM ports and their USB descriptors, letting the user select one."""
    ports = list(serial.tools.list_ports.comports())
    print("Available COM Ports:")
    for i, port in enumerate(ports):
        # Print the port device, description, and manufacturer information
        print(f"{i}: {port.device} - {port.description} (Manufacturer: {port.manufacturer or 'Unknown'})")
    
    while True:
        try:
            selection = int(input("Select the COM port by entering its number: "))
            if 0 <= selection < len(ports):
                return ports[selection].device  # Return the selected COM port
            else:
                print("Invalid selection. Please choose a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to calculate an 8-bit checksum of a given string
def checksum(buf):
    return sum(buf.encode('utf-8')) & 0xFF  # Ensures the result fits within 8 bits

# Function to decode error codes
def err_code(err_code):
    msg = '                                '
    if err_code[0:8] == '80000001':
        msg = 'Failed to access thermal sensor '
    elif err_code[0:8] == '80000004':
        msg = 'AC/DC Power Fail                '
    elif err_code[0:8] == '80000005':
        msg = 'Main SoC CPU Power Fail         '
    elif err_code[0:8] == '80000006':
        msg = 'Main SoC GFX Power Fail         '
    elif err_code[0:8] == '80000007':
        msg = 'Main SoC Thrm Hi Tempr Abnormal '
    elif err_code[0:8] == '80000008':
        msg = 'Drive Dead Notify Timeout       '
    elif err_code[0:8] == '80000009':
        msg = 'AC In Detect                    '
    elif err_code[0:8] == '8000000A':
        msg = 'VRM HOT Fatal                   '
    elif err_code[0:8] == '8000000B':
        msg = 'Unexpected Thermal Shutdown     '
    elif err_code[0:8] == '8000000C':
        msg = 'MSoC Tempr Alert                '
    elif err_code[0:8] == '80050000':
        msg = 'SoC VRM Power Fail (CPU)        '
    elif err_code[0:4] == '8005':
        msg = 'SoC VRM Power Fail (CPU)        '
    elif err_code[0:8] == '80060000':
        msg = 'SoC VRM Power Fail (GFX)        '
    elif err_code[0:4] == '8006':
        msg = 'SoC VRM Power Fail (GFX)        '
    elif err_code[0:4] == '8080':
        msg = 'Fatal Shutdown by OS request    '
    elif err_code[0:8] == '80810001':
        msg = 'Power Seq Error                 '
    elif err_code[0:8] == '80810002':
        msg = 'Power Seq: NVS Access Error     '
    elif err_code[0:8] == '80810013':
        msg = 'Power Seq: ScCmd DRAM Init Error'
    elif err_code[0:8] == '80810014':
        msg = 'Power Seq: ScCmd Link Up Failure'
    elif err_code[0:8] == '80830000':
        msg = 'Main SoC Sync Flood             '
    elif err_code[0:8] == '80840000':
        msg = 'PCIe Link Down                  '
    elif err_code[0:8] == '80870001':
        msg = 'Flash Cont:RAM Protect Error    '
    elif err_code[0:8] == '80870002':
        msg = 'Flash Cont:RAM Parity Error     '
    elif err_code[0:8] == '80870003':
        msg = 'Flash Cont:Boot Failed          '
    elif err_code[0:8] == '80870004':
        msg = 'Flash Cont:Boot Failed NoRecord '
    elif err_code[0:8] == '80870005':
        msg = 'Flash Cont:Boot Failed State Err'
    elif err_code[0:6] == '808710':
        msg = 'Flash Cont:ScCmd Response Error '
    elif err_code[0:4] == '8088':
        msg = 'Flash Cont:Boot EAP Error       '
    elif err_code[0:4] == '8089':
        msg = 'Flash Cont:Boot EFC Error       '
    elif err_code[0:4] == '808A':
        msg = 'Flash Cont:Temper Error         '
    elif err_code[0:4] == '808B':
        msg = 'Flash Cont:Watch Dog Timer      '
    elif err_code[0:4] == '808C':
        msg = 'USB Type-C Errror               '
    elif err_code[0:8] == '808D0000':
        msg = 'Thermal Shutdown: Main SoC      '
    elif err_code[0:8] == '808D0001':
        msg = 'Thermal Shutdown: Local Sensor 1'
    elif err_code[0:8] == '808D0002':
        msg = 'Thermal Shutdown: Local Sensor 2'
    elif err_code[0:8] == '808D0003':
        msg = 'Thermal Shutdown: Local Sensor 3'
    elif err_code[0:8] == '808E0000':
        msg = 'COM Err:Close Error             '
    elif err_code[0:8] == '808E0001':
        msg = 'COM Err:Open Error              '
    elif err_code[0:8] == '808E0002':
        msg = 'COM Err:Host Write Flag Error   '
    elif err_code[0:8] == '808E0003':
        msg = 'COM Err:EMC Read Flag Error     '
    elif err_code[0:8] == '808E0004':
        msg = 'COM Err:Write Flag Error        '
    elif err_code[0:8] == '808E0005':
        msg = 'COM Err:Wait SIG1 Error         '
    elif err_code[0:8] == '808E0006':
        msg = 'COM Err:Reset request from Host '
    elif err_code[0:8] == '808E0007':
        msg = 'COM Err:Checksum Error          '
    elif err_code[0:8] == '808F0001':
        msg = 'SMCU Com Err:Timeout            '
    elif err_code[0:8] == '808F0002':
        msg = 'SMCU Com Err:Reset              '
    elif err_code[0:8] == '808F0003':
        msg = 'SMCU Com Err:TIS Error          '
    elif err_code[0:8] == '808F00FF':
        msg = 'SMCU Com Err:Undefined          '
    elif err_code[0:4] == '8090':
        msg = 'Fatal Shutdown by Error Add Code'
    elif err_code[0:4] == '8091':
        msg = 'SSD PMIC Error                  '
    elif err_code[0:8] == '80C00114':
        msg = 'Watch Dog For SoC               '
    elif err_code[0:8] == '80C00115':
        msg = 'Watch Dog For EAP               '
    elif err_code[0:8] == '80C0012C':
        msg = 'BD Drive Detached               '
    elif err_code[0:8] == '80C0012D':
        msg = 'EMC Watch Dog Timer Error       '
    elif err_code[0:8] == '80C0012E':
        msg = 'ADC Error (Button)              '
    elif err_code[0:8] == '80C0012F':
        msg = 'ADC Error (BD Drive)            '
    elif err_code[0:8] == '80C00130':
        msg = 'ADC Error (AC In Det)           '
    elif err_code[0:8] == '80C00131':
        msg = 'USB Over Current                '
    elif err_code[0:8] == '80C00132':
        msg = 'FAN Storage Access Failed       '
    elif err_code[0:8] == '80C00133':
        msg = 'USB-BT FW Header Invalid        '
    elif err_code[0:8] == '80C00134':
        msg = 'USB-BT BT Command Error         '
    elif err_code[0:8] == '80C00135':
        msg = 'USB-BT Memory Malloc Failed     '
    elif err_code[0:8] == '80C00136':
        msg = 'USB-BT Device Not Found         '
    elif err_code[0:8] == '80C00137':
        msg = 'USB-BT MISC Error               '
    elif err_code[0:8] == '80C00138':
        msg = 'Flash Cont Interrupt HW Error   '
    elif err_code[0:8] == '80C00139':
        msg = 'BD Drive Eject Assert Delayed   '
    elif err_code[0:6] == '80D001':
        msg = 'USB-BT Error (Bulk Out)         '
    elif err_code[0:6] == '80D002':
        msg = 'USB-BT Error (Bulk In)          '
    elif err_code[0:6] == '80D003':
        msg = 'USB-BT Error (Bt Init)          '
    elif err_code[0:6] == '80D004':
        msg = 'USB-BT Error (Download Firmware)'
    elif err_code[0:6] == '80D005':
        msg = 'USB-BT Error (Release Device)   '
    elif err_code[0:6] == '80D006':
        msg = 'USB-BT Error (Exec Cmd0)        '
    elif err_code[0:6] == '80D007':
        msg = 'USB-BT Error (Exec Cmd1)        '
    elif err_code[0:2] == 'B0':
        msg = 'Sonics Bus Error                '
    elif err_code[0:4] == 'C001':
        msg = 'Main SoC Access Error (I2C)     '
    elif err_code[0:4] == 'C002':
        msg = 'Main SoC Access Err (SB-TSI I2C)'
    elif err_code[0:4] == 'C003':
        msg = 'Main SoC Access Error (SB-RMI)  '
    elif err_code[0:4] == 'C00B':
        msg = 'Serial Flash Access Error       '
    elif err_code[0:4] == 'C00C':
        msg = 'VRM Controller Access Error     '
    elif err_code[0:4] == 'C00D':
        msg = 'PMIC (Subsystem) Access Error   '
    elif err_code[0:4] == 'C010':
        msg = 'Flash Controller Access Error   '
    elif err_code[0:4] == 'C011':
        msg = 'Potentiometer Access Error      '
    elif err_code[0:4] == 'C015':
        msg = 'PCIe Redriver Access Errror     '
    elif err_code[0:4] == 'C016':
        msg = 'PMIC (SSD) Access Error         '
    elif err_code[0:4] == 'C081':
        msg = 'HDMI Tx Access Error            '
    elif err_code[0:4] == 'C090':
        msg = 'USB Type-C PD Cont Access Error '
    elif err_code[0:4] == 'C091':
        msg = 'USB Type-C USB/DP Mux Accss Err '
    elif err_code[0:4] == 'C092':
        msg = 'USB Type-C Redriver Access Error'
    elif err_code[0:4] == 'C0FE':
        msg = 'Dummy                           '
    return msg

# Function to decode power states
def pw_state(pw_state):
    msg1 = '         '
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

# Function to decode wake-up causes
def upcause(BT_TRG):
    msg = '___'
    if BT_TRG[0:8] == '40000000':
        msg = 'UUART Wake'
    elif BT_TRG[0:8] == '00080000':
        msg = 'BT Wake '
    elif BT_TRG[0:8] == '00040000':
        msg = 'HDMI CEC Wake'
    elif BT_TRG[0:8] == '00020000':
        msg = 'EAP Wake'
    elif BT_TRG[0:8] == '00010000':
        msg = 'Main SoC Wake'
    elif BT_TRG[0:8] == '00000400':
        msg = 'Eject Switch'
    elif BT_TRG[0:8] == '00000200':
        msg = 'Download_WOL_WOW'
    elif BT_TRG[0:8] == '00000100':
        msg = 'Power Button'
    elif BT_TRG[0:8] == '00000001':
        msg = 'BPW'
    return msg

# Function to decode device power
def devpower(devpower_hex):
    value = int(devpower_hex, 16)
    result = ""
    result += f"HDMI 5V: {'ON' if (value & 0x10) != 0 else 'OFF'}, "
    result += f"BDD: {'ON' if (value & 0x08) != 0 else 'OFF'}, "
    result += f"HDMI-CEC: {'ON' if (value & 0x04) != 0 else 'OFF'}, "
    result += f"USB-VBUS: {'ON' if (value & 0x02) != 0 else 'OFF'}, "
    result += f"WIFI: {'ON' if (value & 0x01) != 0 else 'OFF'}"
    return result

# Function to calculate temperature from hexadecimal value
def calculate_temp(hex_value):
    temp_value = int(hex_value, 16)
    temp_celsius = temp_value / 256.0
    return f"{temp_celsius:.2f}°C"

# Function to send a command via UART and wait for a response
def send_command(uart, command, echo_timeout=3, reply_timeout=3):
    cmd_checksum = checksum(command)
    full_command = f'{command}:{cmd_checksum:02X}\n'  # Append checksum to command
    uart.write(full_command.encode('utf-8'))  # Send the command

    # Wait for Echo Reply
    start_time = time.time()
    echo_reply = ""
    while (time.time() - start_time) < echo_timeout:
        if uart.in_waiting:
            echo_reply += uart.read(uart.in_waiting).decode('utf-8', errors='ignore')
            if '\n' in echo_reply:
                break

    # Wait for Full Reply Data
    start_time = time.time()
    reply_data = ""
    while (time.time() - start_time) < reply_timeout:
        if uart.in_waiting:
            reply_data += uart.read(uart.in_waiting).decode('utf-8', errors='ignore')
            if '\n' in reply_data:
                break

    return reply_data.strip()

import datetime

TIME_ZERO = 1325376000  # Reference point for timestamp calculation

def format_rtc_field(rtc_field):
    """Format the RTC/TIME field to a human-readable timestamp or calculated value."""
    try:
        # Assuming the RTC field is in 'YYYY/MM/DD HH:MM:SS' format
        time = datetime.datetime.strptime(rtc_field + '+00:00', '%Y/%m/%d %H:%M:%S%z')
        unix_timestamp = int(time.timestamp() - TIME_ZERO)
        return f"{unix_timestamp} ({rtc_field})"  # Show both the timestamp and original field
    except ValueError:
        return "Invalid RTC Field (FF:FF:FF)"
        

def send_and_display_responses(uart, increments):
    print("\n==== EMC LOG DATA UART  ====")
    print("version ==", send_command(uart, 'version'))
    print("\nPOWER STATS")
    print("===========")
    
    # Define helper to process powcount responses
    def process_powcount_response(label, response):
        # Split response into fields and decode the last hex value
        if response.startswith("OK"):
            fields = response.split()
            hex_value = fields[-1].split(":")[0]  # Extract hex portion before ":"
            decimal_value = int(hex_value, 16)  # Convert to decimal
            print(f"{label:<7}: (Count: {decimal_value}) {response} ")
        else:
            print(f"{label:<7}: {response} (Invalid Response)")

    # Display power stats
    #process_powcount_response("EAP", send_command(uart, 'powcount eap'))
    #process_powcount_response("SOC", send_command(uart, 'powcount soc'))
    process_powcount_response("FATAL CRASH", send_command(uart, 'powcount fatal'))
    process_powcount_response("ACINDET", send_command(uart, 'powcount acindet'))

    print("\nLOG DATA")
    print("=========")
    # Continue handling the log data (errlog) as before
    for i in range(increments + 1):  # Loop through errlog increments
        command = f"errlog {i}"
        reply_data = send_command(uart, command)

        if reply_data and reply_data.startswith("OK"):
            reply_data = reply_data[3:].strip()  # Strip "OK"
            meaningful_data = reply_data.split(" ", 1)[1] if " " in reply_data else reply_data

        # Decode fields
        if reply_data:
            fields = meaningful_data.split()
            error = err_code(fields[0]) if len(fields) > 0 else "Unknown"
            rtc = format_rtc_field(fields[1]) if len(fields) > 1 else "Unknown"
            power_state = pw_state(fields[2]) if len(fields) > 2 else "Unknown"
            wake_cause = upcause(fields[3]) if len(fields) > 3 else "Unknown"
            dev_pwr = devpower(fields[4]) if len(fields) > 4 else "Unknown"
            tsoc = calculate_temp(fields[5]) if len(fields) > 5 else "Unknown"
            tenv = calculate_temp(fields[6]) if len(fields) > 6 else "Unknown"


            # Print formatted row
            # Print formatted row
            print(f"  {i:02}")  # Line for entry number
            print(f"          {fields[0]:<13}")  # Code
            print(f"          {error:<17}")  # Decoded error message
            print(f"     Time            =       {rtc:<12}")  # RTC value
            print(f"     Power State     =       {power_state:<16}")  # Power state
            print(f"     Wake Cause      =       {wake_cause:<8}")  # Wake-up cause
            print(f"     DevPower        =       {dev_pwr:<40}")  # Device power status
            print(f"     Thermal         =       SOC: {tsoc:<7}  Env: {tenv}")  # Thermal values
            print()  # Add a blank line for separation
        else:
            print(f"{i:02}  No Reply Data (Timeout)")

            #print(f"{i:02}  {fields[0]:<13} {error:<17} {rtc:<12} {power_state:<16} {wake_cause:<8} {dev_pwr:<40} {tsoc:<7} {tenv}")
        #else:
           # print(f"{i:02}  No Reply Data (Timeout)")

# Main loop
try:
    # Step 1: List COM ports and let the user select one
    com_port = list_com_ports()

    # Step 2: Ask the user how many errlog increments to request
    while True:
        try:
            increments = int(input("Enter the number of errlog increments to request (0-50): "))
            if 0 <= increments <= 50:
                break
            else:
                print("Please enter a number between 0 and 50.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Step 3: Open the selected COM port
    BAUD_RATE = 115200
    uart = serial.Serial(com_port, 115200, timeout=1)
    print(f"Connected to {com_port} at {BAUD_RATE} baud.")

    # Step 4: Send and display responses
    send_and_display_responses(uart, increments)

except KeyboardInterrupt:
    print("Program interrupted by user.")

finally:
    if 'uart' in locals() and uart.is_open:
        uart.close()
        print("Connection closed.")

# os.system("pause")
