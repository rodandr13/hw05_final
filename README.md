# Yatube

Блог с возможностью публикации постов, подпиской на группы и авторов, а также комментированием постов.

**Используемые технологии:**
- Python 3.9
- Django framework 2.2.16
- Djangorestframework-simplejwt 4.7.2
- Pillow 8.3.1
- HTML
- CSS (Bootstrap 3)
- sorl-thumbnail 12.7.0

**Авторизованные пользователи могут:**
- Просматривать, публиковать, удалять и редактировать свои публикации;
- Просматривать информацию о сообществах;
- Просматривать и публиковать комментарии от своего имени к публикациям других пользователей (включая самого себя), удалять и редактировать свои комментарии;
- Подписываться на других пользователей и просматривать свои подписки.
- Примечание: Доступ ко всем операциям записи, обновления и удаления доступны только после аутентификации и получения токена.

**Анонимные пользователи могут:**
- Просматривать публикации;
- Просматривать информацию о сообществах;
- Просматривать комментарии;
