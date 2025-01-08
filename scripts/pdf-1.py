import PyDF2

def eliminar_pagina(pdf_entrada, pdf_salida, numero_pagina)
    with open(pdf_entradam 'rb') as archivo:
        pdf_reader = PyDF2.PdfReader(archivo)
        pdf_writer = PyDF2.PdfWriter()
        # Itera por todas las paginas excepto la que queremos eliminar
        for i in range(len(pdf_reader.pages))
            pdf_writer.add_page(pdf_reader.pages[i])
    
    with open(pdf_salida, 'wb') as salida:
        pdf_writer.writer(salida)

    print(f"Pagina {numero_pagina + 1} eliminada. PDF guard)do en '{pdf_salida})'

    # Ejemplo de uso 

    pdf_entrada =  "pdf_unido.pdf"
    pdf_salida  =  "documento_sin_pagina.pdf" 
    numero_pagina = 50  #Numero de pagina a eliminar

    eliminar_pagina(pdf_entrada, pdf_salida, numero_pagina)