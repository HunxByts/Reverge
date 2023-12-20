#===========================#
#  W  A  T  E  R  M  A  K   #
#############################
#   CODE BY FAISS | HUNX    #
#############################
#  PROJECT CTF TOOL SIMPLE  #
#===========================#
#======================================================
# R E C O D E  T A N P A  I Z I N  S I A L  7 TURUNAN #
#======================================================

import time
import sys
import argparse
import binascii
from hexdump import hexdump 

#==============VARIABLE BUAT WARNA CUYY========
Bl='\033[30m'
Re='\033[1;31m'
Gr='\033[1;32m'
Ye='\033[1;33m'
Blu='\033[1;34m'
Mage='\033[1;35m'
Cy='\033[1;36m'
Wh='\033[1;37m'

#===============BANER============
print(f"""{Ye}
__________                                        
\______   \ _______  __ ___________  ____   ____  
 |       _// __ \  \/ // __ \_  __ \/ ___\_/ __ \ 
 |    |   \  ___/\   /\  ___/|  | \/ /_/  >  ___/ 
 |____|_  /\___  >\_/  \___  >__|  \___  / \___  >
        \/     \/          \/     /_____/      \/\n 
                      {Wh}TOOL REV & FORW {Ye}| {Wh}BY HUNX\n
""")

def main():
    parser = argparse.ArgumentParser(description="Tool ini digunakan untuk extract dan convert hex pada suatu file.")
    
    parser.add_argument('-i', '--INPUT', help='Masukan file nya')
    parser.add_argument('-r', '--REVERSE', action='store_true', help='Unlstuk meng extract file ke hex')
    parser.add_argument('-f', '--FORWARD', action='store_true', help='Untuk meng convert hex ke bentuk file')
    parser.add_argument('-o', '--OUTPUT', help='Simpan file output')
    args = parser.parse_args()
#=================KONDISI====================    
    if args.REVERSE:
        with open(args.INPUT, 'rb') as file:
            file_to_hex = file.read()
            print(f"{Wh}[{Ye} + {Wh}] {Ye}Sedang meng extract file {Wh}\n")
            hexdump(file_to_hex)
#==================ANIMASI====================
        print("\n")
        def animasi():    
            for i in range(5):
                sys.stdout.write(f'\r{Wh}[{Ye} + {Wh}] {Ye}Sedang mengambil hexadesiaml 00%')
                time.sleep(0.3)
                sys.stdout.write(f'\r{Wh}[{Ye} + {Wh}] {Ye}Sedang mengambil hexadesiaml 20%')
                time.sleep(0.3)
                sys.stdout.write(f'\r{Wh}[{Ye} + {Wh}] {Ye}Sedang mengambil hexadesiaml 60%')
                time.sleep(0.3)
                sys.stdout.write(f'\r{Wh}[{Ye} + {Wh}] {Ye}Sedang mengambil hexadesiaml 80%')
                time.sleep(0.3)
                sys.stdout.write(f'\r{Wh}[{Ye} + {Wh}] {Ye}Sedang mengambil hexadesiaml 100%{Wh}')
                time.sleep(0.3)
        animasi()
#=================KONDISI====================   
        print("\n")
        command = binascii.hexlify(file_to_hex).decode('utf-8')
        print(command)
        with open(f"{args.OUTPUT}", 'w') as file_out_hex:
            file_out_hex.write(command)
        file_out_hex = args.OUTPUT if args.OUTPUT else "file_out_hex.txt"
        print(f"{Wh}[{Ye} + {Wh}] {Ye}File telah disimpan di [ {Wh}{file_out_hex} {Ye}] {Wh}...")
        
#=================KONDISI====================   
    elif args.FORWARD:
        ext = input(f"{Wh}[{Ye} + {Wh}] {Ye}Masukan extensi file mu {Wh}: ")
        if not ext:
            print(f"{Wh}Extensinya mana kaks!")
            sys.exit()
        with open(args.INPUT, 'r') as file_out:
            file_convert = file_out.read().strip()
            hex_dump = binascii.unhexlify(file_convert)
            
            with open(f"{args.OUTPUT}.{ext}", 'wb') as file_dump:
                file_dump.write(hex_dump)
            file_out_hex2 = args.OUTPUT if args.OUTPUT else f"out_file_hex.{ext}"
            print(f"\n{Wh}[{Ye} + {Wh}] {Ye}File output forward telah berhasil dibuat [ {file_out_hex2}.{ext} ]")
    else:
        print('Pilih opsi --REVERSE/--FORWARD')
        sys.exit()
        
if __name__ == '__main__':
    main()


