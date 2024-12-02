budget = 1000
products = {
    "หมูสับกิโล": 150,
    "เนื้ออกไก่": 105,
    "ไก่บ้าน(ตัว)": 120,
    "มาม่าต้มยำ": 6.50,
    "ข้าวสาร": 150,
    "น้ำตาล": 20,
    "ปลากระป๋อง": 10,
    "ซอสน้ำมันหอย": 18,
    "ผงชูรส": 10.25,
    "ไข่แยกดละเบอร์": 120.25,
    "ชาเขียว": 21.50,
    "Pepsi": 29.50,
    "กาแฟ": 15.75,
    "ขนมปังอบเนย": 19,
    "ชาไทย": 11.50,
    "น้ำเปล่า": 15.15,
    "น้ำแข็ง": 10
}
selected = [
    "หมูสับกิโล",
    "เนื้ออกไก่",
    "ไก่บ้าน(ตัว)",
    "มาม่าต้มยำ",
    "ข้าวสาร",
    "น้ำตาล",
    "ปลากระป๋อง",
    "ซอสน้ำมันหอย",
    "ผงชูรส",
    "ไข่แยกดละเบอร์",
    "ชาเขียว",
    "Pepsi",
    "กาแฟ",
    "ขนมปังอบเนย",
    "น้ำแข็ง"
]
total = sum(products[item] for item in selected)

change = budget - total

print("ยอดรวมค่าใช้จ่าย: {:.2f} บาท".format(total))
print("เงินทอนที่เหลือ: {:.2f} บาท".format(change))
