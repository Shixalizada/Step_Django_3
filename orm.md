# Dərs 9 — ORM sorğuları

Aşağıdakı nümunələr Django shell-də (`python manage.py shell`) işlədilən əsas ORM sorğularıdır.

```python
from blog.models import Post, Category
```

## 1. Bütün postlar
```python
Post.objects.all()
```
Nəticə: bazadakı bütün `Post` obyektləri.

## 2. Yalnız dərc olunmuş postlar
```python
Post.objects.filter(is_published=True)
```
Nəticə: yalnız `is_published=True` olan postlar.

## 3. Ən yeni 3 post
```python
Post.objects.filter(is_published=True).order_by("-created_at")[:3]
```
Nəticə: dərc olunmuş postlardan ən yeni 3-ü, yenidən köhnəyə.

## 4. Post və kateqoriya sayı
```python
Post.objects.filter(is_published=True).count()
Category.objects.count()
```
Nəticə: uyğun olaraq dərc olunmuş postların və kateqoriyaların sayı.

## 5. Ən çox oxunan post
```python
Post.objects.filter(is_published=True).order_by("-views").first()
```
Nəticə: ən çox baxışı olan dərc olunmuş post; post yoxdursa `None`.

> Qeyd: konkret nəticələr repoda `db.sqlite3` saxlanmadığı üçün hər istifadəçinin lokal bazasındakı məlumatlara görə dəyişir.
