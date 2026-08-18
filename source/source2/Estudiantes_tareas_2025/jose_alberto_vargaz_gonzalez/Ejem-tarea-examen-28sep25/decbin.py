def conversiones():
    # Conversión directa
    decimal = 1024
    binario = "110101"
    
    # Decimal a Binario
    bin_result = bin(decimal)[2:]  # [2:] para quitar el '0b' prefix
    print(f"Decimal {decimal} → Binario: {bin_result}")
    
    # Binario a Decimal
    dec_result = int(binario, 2)
    print(f"Binario {binario} → Decimal: {dec_result}")

# Ejecutar
conversiones()

