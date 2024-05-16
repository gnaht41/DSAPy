from a import *
def main():
    ds = DSLK()
    # Them
    print("1.---Them cac so")
    ds.them(1)
    ds.them(2)
    ds.them(3)
    
    ds.inds()
    # Chen
    print("2.---Chen cac so")
    ds.chen(2,6)
    ds.inds()
    # Tim
    print("3.--Tim cac so")
    ds.inds()
    so = 2
    vt = ds.tim_ds(so)
    print(f'Vi tri cua so {so} can tim la {vt}')
    # Xoa
    so = 6
    print(f'Sau khi xoa gia tri {so}')
    ds.xoa(so)
    ds.inds()
    # Cap nhat
    so = 1
    vt = 2
    print(f'Sau khi cap nhap {so} vao vi tri {vt}')
    ds.cap_nhat(vt, so)
    ds.inds()
    # Xoa het
    print(f'Xoa het')
    ds.xoa_het()
    
if __name__ == '__main__':
    main()