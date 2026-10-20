class BCM:
    def CAN_Message_Generator(self):
        yield "0x120", "01 02 03"
        yield "0x150", "01 03 03"
        yield "0x120", "01 02 03"
        yield "0x160", "01 04 03" 
        yield "0x120", "01 02 03"
        yield "0x120", "01 06 03"
        yield "0x120", "07 02 03"
        yield "0x140", "01 02 03"
        yield "0x120", "08 02 03"
        yield "0x120", "09 02 09"
bcm1 = BCM()
expected_CAN_ID = "0x120"
for CAN_ID, CAN_Data in bcm1.CAN_Message_Generator():
   
    print("_______________Test started_____________________________________________________")
    print(f"CAN ID ={CAN_ID}")
    print(f"CAN Data = {CAN_Data}")
    if expected_CAN_ID == CAN_ID:
        print("Expected CAN Message received")
    else:
        print("Unexpected CAN message")
print("________________________Test completed_______________________________________")