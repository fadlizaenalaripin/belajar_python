# Inisialisasi skor
programmer = 0
desainer = 0
marketer = 0
mekanik = 0

# Pertanyaan 1
answer1 = int(input(
    'Apa kegiatan favoritmu di waktu luang?\n'
    '1. Main game dan otak-atik komputer\n'
    '2. Menggambar atau desain di HP\n'
    '3. Nonton video bisnis/motivasi\n'
    '4. Bongkar pasang motor atau alat rumah\n'
))
if answer1 == 1:
    programmer += 1
elif answer1 == 2:
    desainer += 1
elif answer1 == 3:
    marketer += 1
elif answer1 == 4:
    mekanik += 1
else:
    print('Jawablah sesuai dengan pertanyaan yang ada!')

# Pertanyaan 2
answer2 = int(input(
    'Apa yang paling kamu hargai?\n'
    '1. Logika dan efisiensi\n'
    '2. Kreativitas dan estetika\n'
    '3. Komunikasi dan pengaruh\n'
    '4. Keahlian teknis dan praktik langsung\n'
))
if answer2 == 1:
    programmer += 1
elif answer2 == 2:
    desainer += 1
elif answer2 == 3:
    marketer += 1
elif answer2 == 4:
    mekanik += 1
else:
    print('Jawablah sesuai dengan pertanyaan yang ada!')

# Pertanyaan 3
answer3 = int(input(
    'Alat mana yang paling kamu suka gunakan?\n'
    '1. Laptop dan keyboard\n'
    '2. Kertas dan pensil digital\n'
    '3. Mic dan kamera\n'
    '4. Obeng dan kunci inggris\n'
))
if answer3 == 1:
    programmer += 1
elif answer3 == 2:
    desainer += 1
elif answer3 == 3:
    marketer += 1
elif answer3 == 4:
    mekanik += 1
else:
    print('Jawablah sesuai dengan pertanyaan yang ada!')

# Pertanyaan 4
answer4 = int(input(
    'Jika kamu dapat proyek kelompok, kamu lebih suka menjadi…\n'
    '1. Programmer sistem atau logika\n'
    '2. Desainer presentasi atau poster\n'
    '3. Pembicara atau koordinator\n'
    '4. Orang lapangan yang menyelesaikan hal teknis\n'
))
if answer4 == 1:
    programmer += 1
elif answer4 == 2:
    desainer += 1
elif answer4 == 3:
    marketer += 1
elif answer4 == 4:
    mekanik += 1
else:
    print('Jawablah sesuai dengan pertanyaan yang ada!')

# Menampilkan skor akhir
print('\nSkor akhir jawaban kamu:')
print('Programmer:', programmer)
print('Desainer:', desainer)
print('Marketing:', marketer)
print('Mekanik:', mekanik)

# Menentukan profesi yang cocok
skor_max = max(programmer, desainer, marketer, mekanik)

if programmer == skor_max:
    print('Anda sangat cocok menjadi seorang programmer 👨‍💻')
if desainer == skor_max:
    print('Anda sangat cocok menjadi seorang desainer 🎨')
if marketer == skor_max:
    print('Anda sangat cocok menjadi seorang marketing 📢')
if mekanik == skor_max:
    print('Anda sangat cocok menjadi seorang mekanik 🔧')
