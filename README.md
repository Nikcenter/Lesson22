# Lesson22
Щоб встановити python-docx, відкриємо Паур шел з правами адміністратора. Щоб не створювати нове віртуальне середовище, скористаємось тим, що ми створили на попередніх уроках.
За допомогою команди  cd перейдемо між папками. 
cd Documents\MyProject
Тут venv - це ім'я папки, де буде зберігатися віртуальне середовище. Ви можете назвати її як завгодно. Щоб активувати віртуальне середовище, виконайте наступну команду:
.\venv\Scripts\activate
Або якщо ви користуєтесь Лінукс або Мак:
source venv/bin/activate
  Після активації ви побачите ім'я вашого віртуального середовища у командному рядку, наприклад (venv)
pip install python-docx
Отже бібліотека встановлено успішно.

wget "https://public.docs.openprocurement.org/get/b479910f2d3c43cc86186f86f694d605?KeyID=52462340&Signature=Ny1vudcpgOGqpqdZqFtniV3rpoHI9sDY3J8vUFfKDZDOzIBZOzQypOBODQjfjtFYe2b5AKiQiE5f02FfAw0LAQ%3D%3D" -O poekt_dogovoru.doc
