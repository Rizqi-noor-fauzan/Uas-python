import os 
import CRUD as CRUD

# Declare fungsi dasar python
if __name__ == "__main__":
  sistem_operasi = os.name

    # Mencocokan os untuk meng clear console/terminal
  match sistem_operasi:
        case "posix": os.system("clear")
        case "nt": os.system("cls")
       
  print("SELAMAT DATANG DI PROGRAM")
  print("DATABASE PERPUSTAKAAN")
  print("===========================")
  # Check database ada atau tidak
  CRUD.init_console()

  # Perulangan
  while(True):
    # Mencocokan os untuk meng clear console/terminal
      match sistem_operasi:
        case "posix": os.system("clear")
        case "nt": os.system("cls")
    
      print("SELAMAT DATANG DI PROGRAM")
      print("DATABASE PERPUSTAKAAN")
      print("===========================")

      print(f"1. Read Data")
      print(f"2. Create Data")
      print(f"3. Update Data")
      print(f"4. Delete Data\n")

      print("Apakah ada yang bisa saya bantu?: ")
      user_option = input("Masukkan opsi: ")

  
      # User Option
      match user_option:
          case "1": CRUD.read_console()
          case "2": CRUD.create_console()
          case "3": CRUD.update_console()
          case "4": CRUD.delete_console()

      
    # pengecekan pilihan
      is_done = input("Apakah Sudah Selesai(y/n) ? ")
      if is_done == "y" or is_done == "Y":
        break

  print("Terimakasih telah berkunjung✌️")