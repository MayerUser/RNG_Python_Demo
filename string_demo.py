Num =  127
Num_String = str(127)
Num_Byte_Array = Num_String.encode('ascii')
print(Num)          #Serial.println(Num) : int -> string -> print;
print(Num_String)   #Serial.println(Num_String): string -> print;
print(Num_Byte_Array)

for item in Num_Byte_Array:
    print("Num_Byte:","0x%0x"%item)

print("Num:","0x%0x"%Num)
