import csv
import re


class Employee:
    def __init__(self, id, name, gender, birth_year, phone):
        self.id = id
        self.name = name
        self.gender = gender
        self.birth_year = birth_year
        self.phone = phone
        self.next = None


class EmployeeLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_Dulication(self, id):
        current = self.head
        while current:
            if current.id == id:
                return False
            else:
                return True

    def append(self, id, name, gender, birth_year, phone):
        if not all([id, name, gender, birth_year, phone]):
            print("No data!!!")
            return 0
        if gender not in ["Nam", "Nữ"]:
            raise ValueError("Gender is Nam or Nữ")
        if birth_year < 1990:
            raise ValueError("Born >= 1990")
        if not id.startswith("NV"):
            raise ValueError("Name is start NV")
        if self.is_Dulication(id) == False:
            raise ValueError("Id is duplication in data")
        if not phone.startswith("0909"):
            raise ValueError("Phone is start  [0909xxx]")

        nv = Employee(id, name, gender, birth_year, phone)
        if self.head == None:
            self.head = nv
            self.tail = nv
        else:
            self.tail.next = nv
            self.tail = nv

    def display(self):
        current = self.head
        while current != None:
            print(
                f"Id: {current.id}, name: {current.name}, gender: {current.gender}, birth_year: {current.birth_year}, phone: {current.phone}"
            )
            current = current.next

    def search_1994(self):
        current = self.head
        found_1994 = False
        while current is not None:
            if current.birth_year == 1994:
                found_1994 = True
                print(
                    f"Id: {current.id}, name: {current.name}, gender: {current.gender}, birth_year: {current.birth_year}, phone: {current.phone}"
                )
            current = current.next
        if not found_1994:
            print("No employee born in 1994 in the data!")

    def update_0909(self):
        current = self.head
        while current is not None:
            if current.phone.startswith("0909"):
                current.phone = "0380" + current.phone[4:]
            current = current.next

    def sort_by_id_desc(self):
        if self.head is None:
            return
        # Tạo danh sách phụ chứa các đối tượng nhân viên
        employees = []
        current = self.head
        while current is not None:
            employees.append(current)
            current = current.next

        # Sắp xếp danh sách phụ theo ID giảm dần
        employees.sort(key=lambda x: x.id, reverse=True)

        # Cập nhật liên kết trong danh sách liên kết
        self.head = employees[0]
        current = self.head
        for i in range(1, len(employees)):
            current.next = employees[i]
            current = current.next
        current.next = None

    def remove(self):
        previous = None
        current = self.head
        while current is not None:
            if current.gender == "Nam":
                if current == self.head and current == self.tail:
                    self.head = self.tail = None
                    del current
                    break
                elif current == self.head:
                    self.head = self.head.next
                    del current
                    current = self.head
                elif current == self.tail:
                    previous.next = None
                    self.tail = previous
                    del current
                    break
                else:
                    next_node = current.next
                    previous.next = next_node
                    del current
                    current = next_node
            else:
                previous = current
                current = current.next

    def save_to_csv(self, filename):
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Gender", "Birth Year", "Phone"])
            current = self.head
            while current:
                writer.writerow(
                    [
                        current.id,
                        current.name,
                        current.gender,
                        current.birth_year,
                        current.phone,
                    ]
                )
                current = current.next

    def load_from_csv(self, filename):
        # Xóa tất cả các nhân viên hiện có trong danh sách
        self.head = None
        self.tail = None

        with open(filename, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    self.append(
                        row["ID"],
                        row["Name"],
                        row["Gender"],
                        int(row["Birth Year"]),
                        row["Phone"],
                    )
                except ValueError as e:
                    print(f"Error loading employee data: {e}")


def main():
    ds = EmployeeLinkedList()
    ds.append("NV001", "Nguyen Van A", "Nam", 1990, "0909123456")
    ds.append("NV002", "Bui Thi B", "Nữ", 1994, "0909123456")
    ds.append("NV003", "Banh Văn C", "Nam", 2000, "0909123456")
    ds.display()
    print("---remove----")
    ds.remove()
    ds.display()
    print()
    print("Srearch born 1994 in data: ")
    ds.search_1994()
    print("Transfer phone 0909 to 0380: ")
    ds.update_0909()
    ds.display()
    print("Sort with id")
    ds.sort_by_id_desc()
    ds.display()

    # Lưu vào file CSV
    ds.save_to_csv("NhanVien.csv")

    # Đọc từ file CSV
    ds.load_from_csv("NhanVien.csv")

    ds.display()


if __name__ == "__main__":
    main()
