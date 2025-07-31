#Este código serve para transformar unidades de medidas diversas.

valor_em_texto = input("Digite um valor em quilometros (km): ")

quilometros = float(valor_em_texto)
metros = quilometros * 1000
print(f"{quilometros} km  equivalem a{metros}m")
# Conversão de quilometros para metros

centimetros = quilometros * 100000
milimetros = quilometros * 1000000


