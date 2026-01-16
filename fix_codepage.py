def fix_track_tag(text):
    """ fix decode tags problems """
    if not text:
        return ""

    specific_cases = {
        'Þòà': 'Юта',
        'Ïàäàòü': 'Падать',
    }

    for wrong, right in specific_cases.items():
        if wrong in text:
            return text.replace(wrong, right)

    if any('А' <= c <= 'я' for c in text):
        return text

    try:
        fixed = text.encode('latin-1').decode('cp1251')
        # Проверяем результат
        russian_count = sum(1 for c in fixed if 'А' <= c <= 'я')
        if russian_count > 0:
            return fixed
    except:
        pass

    return text
