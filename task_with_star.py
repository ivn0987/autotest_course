# Есть маркер @pytest.mark.id_check(1, 2, 3), нужно вывести на печать, то что в него передано
#
# >>> 1, 2, 3

import pytest


@pytest.mark.id_check(1, 2, 3)
def test(request):
    """
    Тестовая функция которая выыводит параметры id_check
    :param request: object Объект, через который мы вытащим данные
    """
    print(request.node.get_closest_marker('id_check').args)
    # Здесь пишем код
    pass
