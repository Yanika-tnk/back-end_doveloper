print('กรอกข้อมูลส่วนตัว')
name = input("กรอกชื่อ :\n")
nickname = input("กรอกชื่อเล่น :\n")
age = input("กรอกอายุ :\n")
id = input("กรอกรหัสประจำตัวนักเรียน :\n")
no = input("กรอกชั้นปี :\n")
height = float(input("กรอกส่วนสูง :\n"))
weight = float(input("กรอกน้ำหนัก :\n"))
hw = height+weight
print('ประวัติโดยย่อ')
print("ชื่อ :"+ name + "อายุ :" + age )
print("รหัสประจำตัวนักเรียน :" + id, "ระดับชั้น :" + no )
print("ชื่อเล่น : " + nickname)
print("ส่วนสูง :" + str(height) + "เซนติเมตร" "น้ำหนัก :" + str(weight) + "กิโลกรัม")
print("ส่วนสูง + น้ำหนัก :" + str(hw))