import generar_correo

def test_generar_correo():
    ingreso = "Luis Soto"
    esperado = "luis.soto@miumg.edu.gt"
    assert generar_correo.generar_correo(ingreso) == esperado