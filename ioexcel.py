import openpyxl
import xlwings
maUser = 0 #biến toàn cục mã User
Tongtien = 2000 #biến toàn cục tổng tiền
lichsu = ()#biến toàn cục lịch sử
mabua = str()
def laythongtin(name):
    global lichsu, Tongtien, maUser, mabua
    file = openpyxl.load_workbook('data/userhistory.xlsx')
    sheet = file['Sheet1']
    g_all = sheet.values
    thongtin = tuple(g_all)
    maxrow = sheet.max_row
    maUser = maxrow + 1
    def checkname(name):#kiểm tra tên mới hay cũ, nếu tên cũ trả về lịch sử , mới thì trả rỗng
        global maUser
        if maxrow != 1:
            for i in range(maxrow):
                if(thongtin[i][0]==name):
                    maUser = i + 1
                    return thongtin[i]
            return ()
        else:
            return()
    lichsu = checkname(name) 
    def lichsumoi():# tạo lịch sử mới
        return (name,Tongtien,0,0,0,"","","","")
    if (lichsu != ()):#kiểm tra nếu tên mới thì tạo lịch sử mới, cũ thì lấy tổng tiền trong lịch sử
        Tongtien = lichsu [1]
        if lichsu[2] == 0:
            lichsu = lichsu[:5] +('','','','')
    else:
        lichsu += lichsumoi()
    mabua = lichsu[8]
    return lichsu
def layTongtien(name):
    return lichsu[1]
def lichsudau (index):# lấy lịch sử lượt thứ index kể từ lúc bắt đầu chơi trả về các chuỗi
    thangthua = lichsu [5].split(';')
    nhanvat = lichsu [6].split(';')
    tanggiam = lichsu [7].split(';')
    return (thangthua[index], tanggiam[index], nhanvat[index])
def trangthai ():# lấy trạng thái của tài khoản chả về các con số
    tongtien = lichsu[1]
    soluot = lichsu[2]
    solanthang = lichsu[3]
    solanthua = lichsu [4]
    return (tongtien, soluot, solanthang, solanthua)
def laymabua():
    global mabua
    return mabua
def updatemabua(mathaydoi):
    global mabua, lichsu
    mabua = mathaydoi
    lichsu = lichsu[:8]+(mabua,)

def updatelichsu (name, luotdau): # trả về lịch sử được update sau khi chơi 1 lượt
    tongtien = lichsu[1]
    soluot = lichsu[2]
    solanthang = lichsu[3]
    solanthua = lichsu [4]
    thangthua = lichsu [5]
    nhanvat = lichsu [6]
    tanggiam = lichsu [7]
    tongtien += luotdau[1]
    soluot += 1
    if (luotdau[0]==1):
        solanthang += 1
        thangthua+=";1"
        tanggiam += ";+" + str(luotdau[1])
    else:
        solanthua += 1
        thangthua = thangthua + ";0"
        tanggiam += ";" + str(luotdau[1])
    nhanvat += ";"+str(luotdau[2])
    return (name, tongtien, soluot, solanthang, solanthua, thangthua, nhanvat, tanggiam)
def writefile(name, luotdau):#ghi vào file userhistory sau 1 lượt, luotdau là thông tin sau khi chơi, update biến lichsu
    global lichsu
    lichsu = updatelichsu(name, luotdau) + (mabua,)   
def writeExcel():
    global lichsu
    excel_app = xlwings.App(visible=False)
    wb = xlwings.Book('data/userhistory.xlsx')
    sheetw = wb.sheets[0]
    for i in range(9):
        sheetw.range(maUser, i+1).value = lichsu[i]
    wb.save()
    wb.close()
    excel_app.quit()
def cout(name):############################################ bỏ đi
    if(lichsu == ()): pass
    else:
        trthai = trangthai()
        for i in range(trthai[1] , 0, -1):
            lsd = lichsudau(i)
            mix = "kết quả : "
            if(lsd[0]=='1'):
                mix += "WIN "
            else:
                mix += "LOSE "
            mix += " Tiền " + lsd [1] + " nhân vật: " + lsd[2]

def laythongtinhienthi(username):
    tt = trangthai()
    if(tt[1]==0):
        return (username,)+tt+( [''] , [''] ,[''])
    thangthua = lichsu[5][1:]+";"
    nhanvat = lichsu[6][1:]+";"
    tanggiam = lichsu[7][1:]+";"
    
    thangthualist = thangthua.split(';')
    nvlist = nhanvat.split(';')
    tglist = tanggiam.split(';')
    
    thangthualist.reverse()
    nvlist.reverse()
    tglist.reverse()
   
    return (username,)+tt+( thangthualist , nvlist, tglist)
def tong_tien(username, tiencongthem):
    global lichsu
    tongtien = tiencongthem + layTongtien(username)
    lichsu = (username,tongtien)+lichsu[2:]