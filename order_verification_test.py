import sender_stend_request

def test_check_order_get_success():

    # В переменную get_order_response сохраняется результат запроса на проверку заказа
    get_order_response = sender_stend_request.get_take_an_order()

    # Проверяется, что код ответа равен 200
    assert get_order_response.status_code == 200
