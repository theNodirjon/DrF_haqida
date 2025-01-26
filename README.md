# Student Management API

**Student Management API** — bu Django REST Framework (DRF) yordamida yaratilgan talaba va kurslarni boshqarish tizimi. Ushbu API yordamida talaba va kurslar bilan bog'liq CRUD amallarini bajarishingiz mumkin.

---

## 🧩 Funksional Imkoniyatlar

- Talabalar ma'lumotlarini qo'shish, ko'rish, tahrirlash va o'chirish.
- Kurslarni qo'shish, ko'rish, tahrirlash va o'chirish.
- Kursga talabalarni qo'shish yoki olib tashlash.
- Talabalarni yosh, daraja yoki ism bo'yicha filtrlash/qidirish.
- Kurslarni talaba soniga qarab tartiblash yoki filtrlash.

---

## 🛠 O'rnatish va Ishga Tushirish

Loyihani sozlash uchun quyidagi buyruqlarni ketma-ket bajaring:

**1. Repositoryni Klonlash**
```bash
    git clone <repository-url>
    cd student_management
```
**2. Virtual muhitni yaratish va ishga tushirish**
```bash
   python -m venv .venv
   .venv\Scripts\activate # Windows uchun: 
   source .venv/bin/activate  # linux uchun
```
**3. Kutubxonalarni o'rnatish**
```bash
    pip install -r requirements.txt
```
**4. Ma'lumotlar bazasini sozlash**
```bash
    python manage.py makemigrations
    python manage.py migrate
```
**5. Superuser yaratish**
```bash
    python manage.py createsuperuser
 ```
**6. Serverni ishga tushirish**
```bash
    python manage.py runserver
```
**Admin panelga kirish**
```bash
    http://127.0.0.1:8000/admin/
```
---
# 📋 API Endpointlar
### Talabalar (students/)
- GET ```/students/ ```
  - Barcha talabalarni ko'rish.

- POST ```/students/```
  - Yangi talaba qo'shish.

- GET ```/students/<id>/ ```
  - Talabaning ma'lumotlarini ko'rish.

- PUT ```/students/<id>/```
  - Talabaning ma'lumotlarini yangilash.

- DELETE ```/students/<id>/```
  - Talabani o'chirish.

### Kurslar (courses/)
- GET``` /courses/```
  - Barcha kurslarni ko'rish.

- POST ```/courses/```
  - Yangi kurs qo'shish.

- GET```/courses/<id>/```
  - Kurs ma'lumotlarini ko'rish.

- PUT ```/courses/<id>/```
  - Kurs ma'lumotlarini yangilash.

- DELETE ```/courses/<id>/```
  - Kursni o'chirish.

- POST ```/courses/<id>/add_student/```
  - Kursga talaba qo'shish.

---

# 🔍 Filtrlash va Qidiruv
**Talabalar uchun qidiruv va filtrlash:**
- Yosh (```age```), daraja (```grade```), va ism (```first_name```) bo'yicha qidiruv:
 ```bash
    /students/?age=18
    /students/?grade=A
    /students/?search=John
```

**Kurslar uchun qidiruv va tartiblash:**
- Talaba soniga qarab kurslarni tartiblash:
 ```bash
    /courses/?ordering=students_count
```
---

# 🚀 Texnologiyalar
**Loyihada ishlatilgan asosiy texnologiyalar:**
- Python 3.13
- Django 5.1 
- Django REST Framework 
- django-filter (Filtrlash uchun)

---

# 📝 Muallif
- Muallif: [ **Nodirjon**  ]
- Aloqa:

`
https://github.com/theNodirjon  
`
`
testabsd2@gmail.com
 `

---

# 🌟 Litsenziya
**Ushbu loyiha MIT Litsenziyasi ostida taqdim etilgan.**

---

### **Tartib haqida izoh**

1. Har bir qadam boshida aniq maqsad yozilgan.
2. Har bir qadamda terminalda ishlatish kerak bo'lgan **buyruqlar** keltirilgan.
3. Filtrlash va qidiruv uchun misollar berilgan.
4. `Muallif`, `Texnologiyalar`, va `Litsenziya` bo'limlari umumiy tushuncha yaratadi.

---
# Agar qo'shimcha talablaringiz bo'lsa, yozing! 😊

