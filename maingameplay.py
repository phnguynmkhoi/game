import pygame, sys
import function
from pygame.locals import *
from pygame.constants import KEYDOWN, MOUSEBUTTONDOWN, QUIT
import ioexcel, try_nam
from pygame import mixer

def tongket(rank, manvcuoc, tongtien, tiencuoc):
    global luotdau
    tiengiaodong = 0
    checkwin = 0
    checkdoan = 0
    #if manvcuoc == rank[0][0]:
    if rank == 1:
        tiengiaodong += tiencuoc
        checkwin = 1
    else:
        tiengiaodong -= tiencuoc
    luotdau = (checkwin, tiengiaodong, manvcuoc)
    tongtien += tiengiaodong
    thongtin = tuple(str(rank)) + (checkwin, checkdoan, tongtien, tiengiaodong)
    return thongtin

def gameplaymain(screen, username,selection_track, nvcuoc, tennv, tiencuoc, tile, modedua):
    tongtien = ioexcel.layTongtien(username)
    # trave = try_nam.play(screen,selection_track,nvcuoc/10,nvcuoc%10,modedua,username,tennv)
    #trave = gameplay.game(screen, nvcuoc,tile,modedua,0,tennv)
    # thongtin = tongket(trave,nvcuoc,tongtien,tiencuoc)
    # ioexcel.writefile(username, luotdau)
    # ioexcel.cout(username)
    # function.score(screen, username, thongtin,tennv,nvcuoc,tile)
    # game_over_situation(thongtin,tennv,nvcuoc,tile)