from DSLK import *

def main():
    ds = DSLienKet()
    ds.in_ds()
    
    # a - them
    print('a: them------------------------')
    so = 12
    print(f'them {so}')
    ds.them(so)
    ds.in_ds()
    
    so = 10
    print(f'them {so}')
    ds.them(so)
    ds.in_ds()
    # b -chen
    print('b: chen----------------------')
    so = 8
    vt = 0
    print(f'chen {so} vao vi tri {vt}')
    ds.chen(vt, so)
    ds.in_ds()
    
    so = 17
    vt = 3
    print(f'chen {so} vao vi tri {vt}')
    ds.chen(vt, so)
    ds.in_ds()
    
    
    # c - tim
    print('c: tim-----------------')
    ds.in_ds()
    so =99
    print(f'Tim {so}')
    vt = ds.tim(so)
    print(f'so {so} tai vi tri {vt}')
    
    ds.in_ds()
    so =10
    print(f'Tim {so}')
    vt = ds.tim(so)
    print(f'so {so} tai vi tri {vt}')
    
    
    # d - xoa
    print('d - xoa-----------------')
    so =19
    print(f'xoa {so}')
    ds.xoa(so)
    ds.in_ds()
    
    so =15
    print(f'xoa {so}')
    ds.xoa(so)
    ds.in_ds()
    
    # e - cap nhat
    print('e- cap nhat-----------------------')
    vt =6
    gia_tri= 23
    print(f'cap nhat vi tri {vt} voi gia tri {gia_tri}')
    ds.cap_nhat(vt, gia_tri)
    ds.in_ds()
    
    vt =2
    gia_tri= 9
    print(f'cap nhat vi tri {vt} voi gia tri {gia_tri}')
    ds.cap_nhat(vt, gia_tri)
    ds.in_ds()
    # f - xoa het
    print('f: xoa het-----------------------')
    print('xoa het')
    ds.xoa_het()
    ds.in_ds()

if __name__ == '__main__':
    main()
