'''
Deskripsi file teks: 
Diberikan sebuah file teks yang berisi beberapa baris data nilai mahasiswa. Data terdiri dari lima kolom yang menyatakan NIM mahasiswa, 
dan Nilai CLO 1, CLO 2, CLO 3, dan CLO 4. Range nilai adalah dari 0 hingga 100 dan masing-masing kolom dipisahkan oleh tab.

File teks:
|     NIM    | CLO1 | CLO2 | CLO3 | CLO4 |
| 130121322X | 90   |  50  |  40  |  60  |
| 130121323Y | 80   |  70  |  60  |  60  |
| 130121325X | 100  |  90  |  75  |  50  |
| 130121334Y | 90   |  90  |  80  |  85  |
| 130121337Z | 95   |  60  |  70  |  80  |
| 130121338X | 50   |  50  |  40  |  60  |

Contoh pembacaan file:
130121322X 90 50 40 60 artinya mahasiswa dengan NIM 130121322X memperoleh nilai CLO 1 sampai dengan CLO 4 sebesar 
90, 50, 40, 60.

Tugas:
a. Buatlah sebuah sebuah dictionary daftar_CLO dengan key adalah nama CLO dan value berupa list yang berisi empat elemen. 
Elemen pertama adalah rerata CLO semua mahasiswa, elemen kedua adalah nilai CLO tertinggi, elemen ketiga adalah nilai CLO 
terendah, dan elemen keempat adalah jumlah mahasiswa di bawah standar kelulusan (kurang atau sama dengan 50) CLO 
tertentu. Gunakan tipe data terstruktur ini untuk proses pada fungsi yang diminta di bawah ini. 
b. Buatlah fungsi report untuk menampilkan data setiap CLO sesuai dengan dictionary yang telah di buat.
c. Buatlah main program yang digunakan untuk menampilkan dictionary dan memanggil fungsi yang dibuat.
'''

#Membuat Fungsi
def data(namafile): #membuat fungsi dengan nama data untuk membuat dictionary dan listnya
    list_clo = [[], [], [], []] #membuat list perclo
    daftar_CLO = {"CLO1" : [],"CLO2" : [],"CLO3" : [],"CLO4" : []} #dictionary dari list untuk valuenya
    nilai_mahasiswa = open(namafile, "r") #untuk membuka file txtnya
    nilai = nilai_mahasiswa.readline() #untuk membaca file txtnya dalam 1 baris
    #print (nilai) #untuk mengecek apakah sudah terpotong dengan readlinenya
    
    while  nilai != "": # pengulangan untuk memasukan nilai
        list_nilai = list(map(int, nilai.split("\t")[1:])) 
        """
        merubah list string menjadi integer agar bisa di hitung
        dan memotong dengan menggunakan split dimana pemotongannya pertab
        dan diambil index nilainya menggunakan slicing dari index 1 sampai akhir
        sebab yang dibutuhkan adalah nilainya
        """
        #print (list_nilai)  #untuk mengecek list nilainya (masih perNIM mahasiswa)
        nilai = nilai_mahasiswa.readline().replace("\n", "")
        """
        readline untuk membaca file satu persatu baris dan 
        replace untuk mengganti newline jadi tanpa newline
        """
        list_clo[0].append(list_nilai[0]) #memasukan nilai kedalam list_clo1 index ke 0 dengan menambahkan list_nilai dari perNIM mahasiswa 
        list_clo[1].append(list_nilai[1]) #memasukan nilai kedalam list_clo2 index ke 1 dengan menambahkan list_nilai dari perNIM mahasiswa 
        list_clo[2].append(list_nilai[2]) #memasukan nilai kedalam list_clo3 index ke 2 dengan menambahkan list_nilai dari perNIM mahasiswa 
        list_clo[3].append(list_nilai[3]) #memasukan nilai kedalam list_clo4 index ke 3 dengan menambahkan list_nilai dari perNIM mahasiswa 
    print (list_clo) # untuk melihat hasil list perclonya
    """ 
    Buat dictionary daftar_CLO dengan key adalah nama CLO dan value berupa list yang berisi empat elemen. 
    Elemen pertama adalah rerata CLO semua mahasiswa, elemen kedua adalah nilai CLO tertinggi, elemen ketiga adalah nilai CLO 
    terendah, dan elemen keempat adalah jumlah mahasiswa di bawah standar kelulusan (kurang atau sama dengan 50) CLO tertentu.
    """
    #Membuat Dictionary CLO 1
    daftar_CLO["CLO1"].append(sum(list_clo[0]) / len(list_clo[0])) #elemen 1 rerata CLO 1
    daftar_CLO["CLO1"].append(max(list_clo[0])) #elemen 2 maks CLO 1
    daftar_CLO["CLO1"].append(min(list_clo[0])) #elemen 3 min CLO 1
    daftar_CLO["CLO1"].append(len([x for x in list_clo[0] if x <= 50 ])) #elemen 4 untuk menghitung jumlah nilai <= 50 dalam CLO 1
    #print (dict_clo) #untuk pengecekan dictionary daftar_CLO, key = CLO1

    #Membuat Dictionary CLO 2
    daftar_CLO["CLO2"].append(sum(list_clo[1]) / len(list_clo[1])) #elemen 1 rerata CLO 2
    daftar_CLO["CLO2"].append(max(list_clo[1])) #elemen 2 maks CLO 2
    daftar_CLO["CLO2"].append(min(list_clo[1])) #elemen 3 min CLO 2
    daftar_CLO["CLO2"].append(len([x for x in list_clo[1] if x <= 50 ])) #elemen 4 untuk menghitung jumlah nilai <= 50 dalam CLO 2
    #print (dict_clo) #untuk pengecekan dictionary daftar_CLO, key = CLO2

    #Membuat Dictionary CLO 3
    daftar_CLO["CLO3"].append(sum(list_clo[2]) / len(list_clo[2])) #elemen 1 rerata CLO 3
    daftar_CLO["CLO3"].append(max(list_clo[2])) #elemen 2 maks CLO 3
    daftar_CLO["CLO3"].append(min(list_clo[2])) #elemen 3 min CLO 4
    daftar_CLO["CLO3"].append(len([x for x in list_clo[2] if x <= 50 ])) #elemen 4 untuk menghitung jumlah nilai <= 50 dalam CLO 3
    #print (dict_clo) #untuk pengecekan dictionary daftar_CLO, key = CLO3

    #Membuat Dictionary CLO 4
    daftar_CLO["CLO4"].append(sum(list_clo[3]) / len(list_clo[3])) #elemen 1 rerata CLO 4
    daftar_CLO["CLO4"].append(max(list_clo[3])) #elemen 2 maks CLO 4
    daftar_CLO["CLO4"].append(min(list_clo[3])) #elemen 3 min CLO 4
    daftar_CLO["CLO4"].append(len([x for x in list_clo[3] if x <= 50 ])) #elemen 4 untuk menghitung jumlah nilai <= 50 dalam CLO 2
    #print (dict_clo) #untuk pengecekan dictiomary daftar_CLO key = CLO4

    #Print Hasil Dictionarynya
    print("Isi Dictionary:", daftar_CLO) # hasil dictionary akhir (rerata, maks, min, jumlah nilai (<= 50))
    return daftar_CLO #mengembalikan nilai ke daftar_CLO
    
def report(data):
    """ buat fungsi report untuk menampilkan hasil CLO mulai dari rerata nilai maks,
        nilai min, dan jumlah nilai <= 50 dan dibuat dari CLO 1 sampai CLO 4"""
    #CLO 1
    rerata_CLO1 = data["CLO1"][0] #memasukan value list index ke [0] dari key "CLO1" kedalam variabel rerata_CLO1
    maks_CLO1 = data["CLO1"][1] #memasukan value list index ke [1] dari key "CLO1" kedalam variabel maks_CLO1
    min_CLO1 = data["CLO1"][2] #memasukan value list index ke [2] dari key "CLO1" kedalam variabel min_CLO1
    dibawah_standart1 = data["CLO1"][3] #memasukan value list index ke [4] dari key "CLO1" kedalam variabel dibawah_Standart1

    print("CLO 1")
    print ("Nilai Rerata :", rerata_CLO1) #untuk print nilai rerata dalam CLO1
    print ("Nilai Tertinggi :", maks_CLO1) #untuk print nilai maks dalam CLO1
    print ("Nilai Terendah :", min_CLO1) #untuk print nilai min dalam CLO1
    print ("Jumlah Mahasiswa (Nilai <= 50) :", dibawah_standart1) #untuk print jumlah nilai dibawah standart dalam CLO1

    #CLO 2
    rerata_CLO2 = data["CLO2"][0] #memasukan value list index ke [0] dari key "CLO2" kedalam variabel rerata_CLO2
    maks_CLO2 = data["CLO2"][1] #memasukan value list index ke [1] dari key "CLO2" kedalam variabel maks_CLO2
    min_CLO2 = data["CLO2"][2] #memasukan value list index ke [2] dari key "CLO2" kedalam variabel min_CLO2
    dibawah_standart2 = data["CLO2"][3] #memasukan value list index ke [4] dari key "CLO2" kedalam variabel dibawah_Standart2

    print("CLO 2")
    print ("Nilai Rerata :", rerata_CLO2) #untuk print nilai rerata dalam CLO2
    print ("Nilai Tertinggi :", maks_CLO2) #untuk print nilai maks dalam CLO2
    print ("Nilai Terendah :", min_CLO2) #untuk print nilai min dalam CLO2
    print ("Jumlah Mahasiswa (Nilai <= 50) :", dibawah_standart2) #untuk print jumlah nilai dibawah standart dalam CLO2

    #CLO 3
    rerata_CLO3 = data["CLO3"][0] #memasukan value list index ke [0] dari key "CLO3" kedalam variabel rerata_CLO3
    maks_CLO3 = data["CLO3"][1] #memasukan value list index ke [1] dari key "CLO3" kedalam variabel maks_CLO3
    min_CLO3 = data["CLO3"][2] #memasukan value list index ke [2] dari key "CLO3" kedalam variabel min_CLO3
    dibawah_standart3 = data["CLO3"][3] #memasukan value list index ke [4] dari key "CLO3" kedalam variabel dibawah_Standart3

    print("CLO 3")
    print ("Nilai Rerata :", rerata_CLO3) #untuk print nilai rerata dalam CLO3
    print ("Nilai Tertinggi :", maks_CLO3) #untuk print nilai maks dalam CLO3
    print ("Nilai Terendah :", min_CLO3) #untuk print nilai min dalam CLO3
    print ("Jumlah Mahasiswa (Nilai <= 50) :", dibawah_standart3) #untuk print jumlah nilai dibawah standart dalam CLO3

    #CLO 4
    rerata_CLO4 = data["CLO4"][0] #memasukan value list index ke [0] dari key "CLO4" kedalam variabel rerata_CLO4
    maks_CLO4 = data["CLO4"][1] #memasukan value list index ke [1] dari key "CLO4" kedalam variabel maks_CLO4
    min_CLO4 = data["CLO4"][2] #memasukan value list index ke [2] dari key "CLO4" kedalam variabel min_CLO4
    dibawah_standart4 = data["CLO4"][3] #memasukan value list index ke [4] dari key "CLO4" kedalam variabel dibawah_Standart4

    print("CLO 4")
    print ("Nilai Rerata :", rerata_CLO4) #untuk print nilai rerata dalam CLO4
    print ("Nilai Tertinggi :", maks_CLO4) #untuk print nilai maks dalam CLO4
    print ("Nilai Terendah :", min_CLO4) #untuk print nilai min dalam CLO4
    print ("Jumlah Mahasiswa (Nilai <= 50) :", dibawah_standart4) #untuk print jumlah nilai dibawah standart dalam CLO4


#Main Program

nama_file = "Tubes_1301213256_ArdhianRizkyAyatollahNurIsmail.txt" #buat variabel untuk file txtnya
hasil_CLO = data(nama_file) #buat variabel untuk fungsi data
report(hasil_CLO) #variabel yang diatas dimasukan kedalam fungsi report