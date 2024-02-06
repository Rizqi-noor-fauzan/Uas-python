from . import Operasi


#Delete
def delete_console():
  read_console()
  while(True):
    print("Silahkan Pilih Nomor Buku yang akan di delete")
    no_buku = int(input("Nomor Buku: "))
    data_buku = Operasi.read(index=no_buku)
    
    if data_buku:
      data_break = data_buku.split(',')
      pk = data_break[0]
      date_add = data_break [1]
      penulis = data_break [2]
      judul = data_break[3]
      tahun = data_break[4] [:-1]
    
      
      print("Input Data Yang Akan di hapus")
      print(f"1. Judul\t: {judul:.40}")
      print(f"2. Penulis\t: {penulis:.40}")
      print(f"3. Tahun\t: {tahun:4}")
           
      is_done = input("Apakah Anda Yakin?(y/n) ? ")
      if is_done == "y" or is_done == "Y":
        Operasi.delete(no_buku)   
        break
    else:
      print("Nomor Tidak Valid,Silahkan Coba Kembali")
      
  print("Data Berhasil Dihapus")
 
  #Delete end
  

# Update
def update_console():
  read_console()
  while(True):
    print("Silahkan Pilih Nomor Buku yang akan di Update")
    no_buku = int(input("Nomor Buku: "))
    data_buku = Operasi.read(index=no_buku)
    
    if data_buku:
      break
    else:
      print("Nomor Tidak Valid,Silahkan Coba Kembali")
      
  data_break = data_buku.split(',')
  pk = data_break[0]
  date_add = data_break [1]
  penulis = data_break [2]
  judul = data_break[3]
  tahun = data_break[4] [:-1]
  
  while(True):
    # Data Yang ingin di Update
    print("\n"+"="*100)
    print("Silahkan Pilih data apa yang akan di update")
    print(f"1. Judul\t: {judul:.40}")
    print(f"2. Penulis\t: {penulis:.40}")
    print(f"3. Tahun\t: {tahun:4}")
    
    # Memilih mode untuk update
    user_option = input("Pilih data {1,2,3}: ")
    print("\n"+"="*100)
    match user_option:
      case "1": Judul = input("judul\t: ")
      case "2": Penulis = input("penulis\t: ")
      case "3": 
        while(True):
          try:
              tahun = int(input("Tahun\t: "))
              if len(str(tahun)) == 4:
                break
              else:
                print("Input Harus 4 digit Angka!")
          except:
              print("Input Harus Angka!")
    case_: print("Index Tidak Cocok")
    
    print("Data Baru Anda")
    print(f"1. Judul\t: {judul:.40}")
    print(f"2. Penulis\t: {penulis:.40}")
    print(f"3. Tahun\t: {tahun:4}")
    
    is_done = input("Apakah Datanya Sudah Sesuai(y/n) ? ")
    if is_done == "y" or is_done == "Y":
        break
  # Update
# Create
def create_console():
  print("\n\n"+"="*100)
  print("Silahkan tambah data buku \n")
  penulis = input("Penulis\t: ")
  judul = input("Judul\t: ")
  while(True):
    try:
        tahun = int(input("Tahun\t: "))
        if len(str(tahun)) == 4:
          break
        else:
           print("Input Harus 4 digit Angka!")
    except:
      print("Input Harus Angka!")
      
  Operasi.create(tahun,judul,penulis)
  print("\nBerikut adalah data baru anda")
  read_console()
  #Create End


# Read
def read_console():
  data_file = Operasi.read()
  index = "No"
  judul = "Judul"
  penulis = "Penulis"
  tahun = "Tahun"
  
  
  # header
  print("\n" + "=" * 100)
  print(f"{index:4} | {judul:40} | {penulis:40} | {tahun:5}")
  print("-"*100)
  
  # Data
  for index,data in enumerate(data_file):
    data_break = data.split(",")
    pk = data_break[0]
    date_add = data_break[1]
    penulis = data_break[2]
    judul = data_break[3]
    tahun = data_break[4]
    print(f"{index+1:4} | {judul:.40} | {penulis:.40} | {tahun:4}", end="")
     
  
  # footer
  print( "=" * 100 + "\n" )