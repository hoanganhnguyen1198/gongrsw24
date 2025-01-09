#Script generated on: 11:04:20
 if [ $# -eq 0 ]
  then
    echo "[*] Please add vm name!"
    echo "[*] Available vms:"
    VBoxManage list vms | awk -F'"' {' print $2 '} | sed 's/"//g'
    exit
fi 
# VBoxManage setextradata "$1" VBoxInternal/Devices/pcbios/0/Config/DmiBIOSFirmwareMajor	** No value to retrieve **
# VBoxManage setextradata "$1" VBoxInternal/Devices/pcbios/0/Config/DmiBIOSFirmwareMinor	** No value to retrieve **
VBoxManage setextradata "$1" VBoxInternal/Devices/pcbios/0/Config/DmiBIOSReleaseDate	'string:07/14/2022'
VBoxManage setextradata "$1" VBoxInternal/Devices/pcbios/0/Config/DmiBIOSReleaseMajor	'1'
VBoxManage setextradata "$1" VBoxInternal/Devices/pcbios/0/Config/DmiBIOSReleaseMinor	'24'
VBoxManage setextradata "$1" VBoxInternal/Devices/pcbios/0/Config/DmiBIOSVendor	'string:Dell Inc.'
VBoxManage setextradata "$1" VBoxInternal/Devices/pcbios/0/Config/DmiBIOSVersion	'string:1.24.0'
VBoxManage setextradata "$1" VBoxInternal/Devices/pcbios/0/Config/DmiBoardAssetTag	'string:Not Specified'
VBoxManage setextradata "$1" VBoxInternal/Devices/pcbios/0/Config/DmiBoardBoardType	'10'
VBoxManage setextradata "$1" VBoxInternal/Devices/pcbios/0/Config/DmiBoardLocInChass	'string:NotSpecified'
VBoxManage setextradata "$1" VBoxInternal/Devices/pcbios/0/Config/DmiBoardProduct	'string:0Y7WYT'
VBoxManage setextradata "$1" VBoxInternal/Devices/pcbios/0/Config/DmiBoardSerial	'/22EA2B6/768074B63B3991/'
VBoxManage setextradata "$1" VBoxInternal/Devices/pcbios/0/Config/DmiBoardVendor	'string:DellInc.'
VBoxManage setextradata "$1" VBoxInternal/Devices/pcbios/0/Config/DmiBoardVersion	'string:A00'
VBoxManage setextradata "$1" VBoxInternal/Devices/pcbios/0/Config/DmiChassisAssetTag	'string:Not Specified'
VBoxManage setextradata "$1" VBoxInternal/Devices/pcbios/0/Config/DmiChassisSerial	'string:DFA9702'
VBoxManage setextradata "$1" VBoxInternal/Devices/pcbios/0/Config/DmiChassisType	'3'
VBoxManage setextradata "$1" VBoxInternal/Devices/pcbios/0/Config/DmiChassisVendor	'string:DellInc.'
VBoxManage setextradata "$1" VBoxInternal/Devices/pcbios/0/Config/DmiChassisVersion	'string:NotSpecified'
# VBoxManage setextradata "$1" VBoxInternal/Devices/pcbios/0/Config/DmiOEMVBoxRev	** No value to retrieve **
# VBoxManage setextradata "$1" VBoxInternal/Devices/pcbios/0/Config/DmiOEMVBoxVer	** No value to retrieve **
VBoxManage setextradata "$1" VBoxInternal/Devices/pcbios/0/Config/DmiProcManufacturer	'string:Intel(R)Corporation'
VBoxManage setextradata "$1" VBoxInternal/Devices/pcbios/0/Config/DmiProcVersion	'string:Intel(R)Core(TM)i7-6700CPU@3.40GHz'
VBoxManage setextradata "$1" VBoxInternal/Devices/pcbios/0/Config/DmiSystemFamily	'string:OptiPlex'
VBoxManage setextradata "$1" VBoxInternal/Devices/pcbios/0/Config/DmiSystemProduct	'string:OptiPlex7040'
VBoxManage setextradata "$1" VBoxInternal/Devices/pcbios/0/Config/DmiSystemSKU	'06B9'
VBoxManage setextradata "$1" VBoxInternal/Devices/pcbios/0/Config/DmiSystemSerial	'string:6565AF5'
VBoxManage setextradata "$1" VBoxInternal/Devices/pcbios/0/Config/DmiSystemUuid	'9EA857A5-DF14-4109-A5B3-675BA8DDAEC4'
VBoxManage setextradata "$1" VBoxInternal/Devices/pcbios/0/Config/DmiSystemVendor	'string:DellInc.'
VBoxManage setextradata "$1" VBoxInternal/Devices/pcbios/0/Config/DmiSystemVersion	'string:NotSpecified'
controller=`VBoxManage showvminfo "$1" --machinereadable | grep SATA`
if [[ -z "$controller" ]]; then
VBoxManage setextradata "$1" VBoxInternal/Devices/piix3ide/0/Config/PrimaryMaster/SerialNumber	'3BDF0AF0DC89'
VBoxManage setextradata "$1" VBoxInternal/Devices/piix3ide/0/Config/PrimaryMaster/FirmwareRevision	'401000WD'
VBoxManage setextradata "$1" VBoxInternal/Devices/piix3ide/0/Config/PrimaryMaster/ModelNumber	'WD'
else
VBoxManage setextradata "$1" VBoxInternal/Devices/ahci/0/Config/Port0/SerialNumber	'3BDF0AF0DC89'
VBoxManage setextradata "$1" VBoxInternal/Devices/ahci/0/Config/Port0/FirmwareRevision	'401000WD'
VBoxManage setextradata "$1" VBoxInternal/Devices/ahci/0/Config/Port0/ModelNumber	'WD'
fi
if [[ -z "$controller" ]]; then
VBoxManage setextradata "$1" VBoxInternal/Devices/piix3ide/0/Config/PrimarySlave/ATAPISerialNumber	'2C62CF03B71'
VBoxManage setextradata "$1" VBoxInternal/Devices/piix3ide/0/Config/PrimarySlave/ATAPIRevision	'A1C0'
VBoxManage setextradata "$1" VBoxInternal/Devices/piix3ide/0/Config/PrimarySlave/ATAPIProductId	'DVD+-RW GU90N'
VBoxManage setextradata "$1" VBoxInternal/Devices/piix3ide/0/Config/PrimarySlave/ATAPIVendorId	'HL-DT-ST'
else
VBoxManage setextradata "$1" VBoxInternal/Devices/ahci/0/Config/Port1/ATAPISerialNumber	'2C62CF03B71'
VBoxManage setextradata "$1" VBoxInternal/Devices/ahci/0/Config/Port1/ATAPIRevision	'A1C0'
VBoxManage setextradata "$1" VBoxInternal/Devices/ahci/0/Config/Port1/ATAPIProductId	'DVD+-RW GU90N'
VBoxManage setextradata "$1" VBoxInternal/Devices/ahci/0/Config/Port1/ATAPIVendorId	'HL-DT-ST'
fi
if [ ! -f "DSDT_OptiPlex7040.bin" ]; then echo "[WARNING] Unable to find the DSDT file!"; fi	
VBoxManage setextradata "$1" "VBoxInternal/Devices/acpi/0/Config/CustomTable"	 "$PWD"/DSDT_OptiPlex7040.bin
VBoxManage setextradata "$1" VBoxInternal/Devices/acpi/0/Config/AcpiOemId	'DELL'
VBoxManage setextradata "$1" VBoxInternal/Devices/acpi/0/Config/AcpiCreatorId	'INTL'
VBoxManage setextradata "$1" VBoxInternal/Devices/acpi/0/Config/AcpiCreatorRev	'20120913'
VBoxManage modifyvm "$1" --macaddress1	64006a07697f
VBoxManage setextradata "$1" VBoxInternal/CPUM/HostCPUID/80000002/eax  0x65746e49	
VBoxManage setextradata "$1" VBoxInternal/CPUM/HostCPUID/80000002/ebx  0x2952286c	
VBoxManage setextradata "$1" VBoxInternal/CPUM/HostCPUID/80000002/ecx  0x726f4320	
VBoxManage setextradata "$1" VBoxInternal/CPUM/HostCPUID/80000002/edx  0x4d542865	
VBoxManage setextradata "$1" VBoxInternal/CPUM/HostCPUID/80000003/eax  0x37692029	
VBoxManage setextradata "$1" VBoxInternal/CPUM/HostCPUID/80000003/ebx  0x3037362d	
VBoxManage setextradata "$1" VBoxInternal/CPUM/HostCPUID/80000003/ecx  0x50432030	
VBoxManage setextradata "$1" VBoxInternal/CPUM/HostCPUID/80000003/edx  0x20402055	
VBoxManage setextradata "$1" VBoxInternal/CPUM/HostCPUID/80000004/eax  0x30342e33	
VBoxManage setextradata "$1" VBoxInternal/CPUM/HostCPUID/80000004/ebx  0x207a4847	
VBoxManage setextradata "$1" VBoxInternal/CPUM/HostCPUID/80000004/ecx  0x20202020	
VBoxManage setextradata "$1" VBoxInternal/CPUM/HostCPUID/80000004/edx  0x00202020	
cpu_count=$(VBoxManage showvminfo --machinereadable "$1" | grep cpus=[0-9]* | sed "s/cpus=//")	
if [ $cpu_count -lt "2" ]; then echo "[WARNING] CPU count is less than 2. Consider adding more!"; fi	
memory_size=$(VBoxManage showvminfo --machinereadable "$1" | grep memory=[0-9]* | sed "s/memory=//")	
if [ $memory_size -lt "2048" ]; then echo "[WARNING] Memory size is 2GB or less. Consider adding more memory!"; fi	
net_used=$(VBoxManage showvminfo "$1" | grep NIC | grep -v disabled | grep -o "vboxnet.")	
hostint_ip=$(VBoxManage list hostonlyifs | grep "$net_used\|IPAddress:" | sed -n '2p' | awk {' print $2 '} | grep '192.168.56.1')	
if [ "$hostint_ip" == '192.168.56.1' ]; then echo "[WARNING] You are using the default IP/IP-range. Consider changing the IP and the range used!"; fi	
virtualization_type=$(VBoxManage showvminfo --machinereadable "$1" | grep -i ^paravirtprovider | cut -d "=" -f2 | sed 's/"//g')	
if [ ! $virtualization_type == 'none' ]; then echo "[WARNING] Please switch paravirtualization interface to: None!"; fi	
audio=$(VBoxManage showvminfo --machinereadable "$1" | grep audio | cut -d "=" -f2 | sed 's/"//g' | head -1)	
if [ $audio == 'none' ]; then echo "[WARNING] Please consider adding an audio device!"; fi	
arc_devman=64	
devman_arc=$(VBoxManage showvminfo --machinereadable "$1" | grep ostype | cut -d "=" -f2 | grep -o "(.*)" | sed 's/(//;s/)//;s/-bit//')	
if [ $devman_arc != $arc_devman ]; then echo "[WARNING] Please use the DevManView version that coresponds to the guest architecture: $devman_arc "; fi	
