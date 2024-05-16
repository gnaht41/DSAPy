from abc import ABC, abstractmethod


class GiaoDich(ABC):
    def __init__(self, salseID, orderDate, unitPrice, orderQty):
        self.salseID = salseID
        self.orderDate = orderDate
        self.unitPrice = unitPrice
        self.orderQty = orderQty

    @abstractmethod
    def totalMoney(self):
        pass


class GiaoDichvang(GiaoDich):
    def __init__(self, salseID, orderDate, unitPrice, orderQty, typeGold):
        super().__init__(salseID, orderDate, unitPrice, orderQty)
        self.typeGold = typeGold

    def totalMoney(self):
        return self.unitPrice * self.orderQty


class GiaoDichTienTe(GiaoDich):
    def __init__(
        self, salseID, orderDate, unitPrice, orderQty, typeMoney, typeTransaction
    ):
        super().__init__(salseID, orderDate, unitPrice, orderQty)
        self.typeMoney = typeMoney
        self.typeTransaction = typeTransaction

    def totalMoney(self):
        if self.typeTransaction.strip().lower() == "mua":
            return self.unitPrice * self.orderQty
        elif self.typeTransaction.strip().lower() == "ban":
            return self.unitPrice * self.orderQty * 1.05
        else:
            raise ValueError("Khong co loai giao dich nao")
        return 0


#
def main():
    def nhap_giao_dich():
        loai_giao_dich = input("Nhập loại giao dịch (vang/tiente): ")
        salseID = input("Nhập salseID: ")
        orderDate = input("Nhập orderDate: ")
        unitPrice = float(input("Nhập unitPrice: "))
        orderQty = int(input("Nhập orderQty: "))

        if loai_giao_dich.lower() == "vang":
            typeGold = input("Nhập typeGold: ")
            return GiaoDichvang(salseID, orderDate, unitPrice, orderQty, typeGold)
        elif loai_giao_dich.lower() == "tiente":
            typeMoney = input("Nhập typeMoney: ")
            typeTransaction = input("Nhập typeTransaction: ")
            return GiaoDichTienTe(
                salseID, orderDate, unitPrice, orderQty, typeMoney, typeTransaction
            )
        else:
            raise ValueError("Loại giao dịch không hợp lệ.")

    def xuat_giao_dich(giao_dich):
        print("SalseID:", giao_dich.salseID)
        print("OrderDate:", giao_dich.orderDate)
        print("UnitPrice:", giao_dich.unitPrice)
        print("OrderQty:", giao_dich.orderQty)
        print("TotalMoney:", giao_dich.totalMoney())

    def tinh_tong_giao_dich(giao_dich_list):
        tong = 0
        for giao_dich in giao_dich_list:
            tong += giao_dich.totalMoney()
        return tong

    # Ví dụ sử dụng
    giao_dich_list = []
    so_luong_giao_dich = int(input("Nhập số lượng giao dịch: "))

    for i in range(so_luong_giao_dich):
        print("Nhập thông tin giao dịch thứ", i + 1)
        giao_dich = nhap_giao_dich()
        giao_dich_list.append(giao_dich)
        print()

    print("Thông tin các giao dịch:")
    for giao_dich in giao_dich_list:
        xuat_giao_dich(giao_dich)
        print()

    tong_tien = tinh_tong_giao_dich(giao_dich_list)
    print("Tổng tiền của các giao dịch:", tong_tien)


if __name__ == "__main__":
    main()
