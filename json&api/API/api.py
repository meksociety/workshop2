# reg -> ResourceWarningร้านอาหารตามสั่ง
# อยากกินกระเพรา ไปสั่งร้านข้าวที่ถัตตาคาร -> req(website)
# สั่งงานบ๋อยว่าจะกินข้าวผัด -> respond (server api)
# โอเคฉันจะรอกิน -> req(website)

# --------------------------------------

# mysql (relation)

# table account

# id/Name
# 6130260555/Thanakorn

# table รายชื่อที่ลงทะเบยนเรียน
# student_id / sec_id
# 6130260555/10112538

# table รายวิชา
# secid   /Name
# 10112538/ python basic & API


# mongodb
# {
#     "student_id":6130260555
#     "student_name":"Thanakorn",
#     "3/02":[
#         {
#             sec_id:"1011258",
#             sec_name:"python&API"

#         },
#         {
#             sec_id:"1011257",
#             sec_name:"Java"

#         },
#     ]
# }