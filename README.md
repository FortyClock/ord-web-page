# Блог на Pelican + GitHub Pages

## Быстрый старт

1. В `pelicanconf.py` поменяй:
   - `AUTHOR`
   - `SITENAME`
   - `PELICAN_COMMENT_SYSTEM_EMAIL_USER`
   - `PELICAN_COMMENT_SYSTEM_EMAIL_DOMAIN`
2. В GitHub открой `Settings -> Pages` и выбери `Source: GitHub Actions`.
3. Запушь изменения в `main`.
4. GitHub Actions соберет сайт и опубликует его на:

```text
https://fortyclock.github.io/ord-web-page
```

## Как добавить статью

Создай Markdown-файл в `content/articles/`:

```markdown
Title: Заголовок статьи
Date: 2026-07-22 18:00
Slug: zagolovok-stati
Category: Блог
Tags: tag1, tag2
Summary: Короткое описание.

Текст статьи.
```

После `git push` статья появится на сайте.

## Как добавить одобренный комментарий

Форма под статьей отправляет комментарий на почту. После проверки создай файл:

```text
content/comments/zagolovok-stati/001-comment.md
```

Пример:

```markdown
email: reader@example.com
date: 2026-07-22T18:10:00+03:00
author: Имя читателя

Текст комментария.
```

Подробности: `docs/comments.md`.

## Локальная проверка

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/pelican content -s publishconf.py
```
