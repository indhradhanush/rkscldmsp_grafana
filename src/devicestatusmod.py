# Ruckus Cloud MSP - Python program to extract from API and update influx database.

# devicestatusmod.py - Modifying Device status to be stored in series.
# - Modify device status.
# - Modify device severity.

def devicestatus_grafana(device_status):
    match device_status:
        case "1_01_NeverContactedCloud":
            return "Never Contacted Cloud"
        case "1_07_Initializing":
            return "Initializing"
        case "1_09_Offline":
            return "Offline"
        case "2_00_Operational":
            return "Operational"
        case "2_01_ApplyingFirmware":
            return "Applying Firmware"
        case "2_02_ApplyingConfiguration":
            return "Applying Configuration"
        case "3_02_FirmwareUpdateFailed":
            return "Firmware Update Failed"
        case "3_03_ConfigurationUpdateFailed":
            return "Configuration Update Failed"
        case "3_04_DisconnectedFromCloud":
            return "Disconnected From Cloud"
        case "4_01_Rebooting":
            return "Rebooting"
        case "4_04_HeartbeatLost":
            return "Heartbeat Lost"
        case "OFFLINE":
            return "Offline"
        case default:
            return device_status

def deviceseverity_grafana(device_severity):
    match device_severity:
        case "1_InSetupPhase":
            return "In Setup Phase"
        case "1_InSetupPhase_Offline":
            return "Offline"
        case "2_Operational":
            return "Operational"
        case "3_RequiresAttention":
            return "Requires Attention"
        case "4_TransientIssue":
            return "Transient Issue"
        case default:
            return "NaN"

#EOL