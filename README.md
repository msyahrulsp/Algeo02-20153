## Tugas Besar 2 IF2123 - Kelompok 31 "Algeough"
Sebuah *Image Compressor* yang bisa meng-*compress* foto menggunakan metode *Singular Value Decomposition*. Pada *compressor* ini juga, bisa menerima input berapa persen pixel yang ingin di *compress*. Dan hasil peng-*compress*-annya, bisa didownload oleh user. Tech Stack yang digunakan untuk tugas ini ialah React untuk Front-End dan Flask untuk Back-End

## Struktur Folder
```sh
Algeo02-20153                   # Berisi java byte code (*.class)
├── src                         # Berisi source code dari program (frontend dan  backend)
│   ├── backend                 # Berisi program backend
│   │   └── static              # Berisi data yang perlu diambil ketika web dijalankan
│   └── frontend                # Berisi program frontend
│       ├── public              # Berisi file template index.html
|       └── src                 # Berisi program-program frontend web
|           ├── components      # Berisi program component untuk frontend
|           ├── images          # Berisi gambar untuk frontend
|           ├── page            # Berisi program halaman untuk frontend
|           └── styles          # Berisi template untuk styling
├── test                        # Berisi gambar uji dan hasilnya
└── doc                         # Berisi laporan
```

## Cara pakai
- Pastikan ada [NodeJS](https://nodejs.org/en/)
- Pastikan ada [Git](https://git-scm.com/)
- Pastikan ada [Flask](https://flask.palletsprojects.com/en/2.0.x/installation/)
- Clone repo ini
```
git clone https://github.com/msyahrulsp/Algeo02-20153.git Algeo02-20153
cd Algeo02-20153/src/backend
pip install -r requirements.txt

cd ../frontend
npm install
```

## How to Run
```
cd backend
main.py

cd ../frontend
npm start
```

## Anggota Kelompok:
| NIM      | NAMA                   |
|----------|------------------------|
| 13520153 | Vito Ghifari           | 
| 13520161 | M Syahrul Surya Putra  | 
| 13520165 | Ghazian Tsabit Alkamil |